from __future__ import print_function

import random
import logging
import grpc

import route_guide_pb2
import route_guide_pb2_grpc
import route_guide_resources


def make_route_note(message, latitude, longitude):
    return route_guide_pb2.RouteNote(
        message=message,
        location=route_guide_pb2.Point(latitude=latitude, longitude=longitude)
    )


def guide_get_one_feature(stub, point):
    feature = stub.GetFeature(point)
    if not feature.location:
        print('server returned incomplete feature')
        return

    if feature.name:
        print('feature called %s at %s' % (feature.name, feature.location))
    else:
        print('found no feature at %s' % feature.location)


def guide_get_feature(stub):
    guide_get_one_feature(stub, route_guide_pb2.Point(latitude=409146138, longitude=-746188906))
    guide_get_one_feature(stub, route_guide_pb2.Point(latitude=0, longitude=0))


def guide_list_features(stub):
    rectangle = route_guide_pb2.Rectangle(
        lo=route_guide_pb2.Point(latitude=400000000, longitude=-750000000),
        hi=route_guide_pb2.Point(latitude=420000000, longitude=-730000000)
    )
    print('looking for features between 40, -75 and 42, -73')

    features = stub.ListFeatures(rectangle)
    for feature in features:
        print('feature called %s at %s' % (feature.name, feature.location))


def generate_route(feature_list):
    for _ in range(0, 10):
        random_feature = feature_list[random.randint(0, len(feature_list) - 1)]
        print('visiting point %s' % random_feature.location)
        yield random_feature.location


def guide_record_route(stub):
    feature_list = route_guide_resources.read_route_guide_database()
    route_iterator = generate_route(feature_list)
    route_summary = stub.RecordRoute(route_iterator)
    print('finished trip with %s points' % route_summary.point_count)
    print('passed %s features' % route_summary.feature_count)
    print('travelled %s meters' % route_summary.distance)
    print('it took %s seconds' % route_summary.elapsed_time)


def generate_messages():
    messages = [
        make_route_note('first message', 0, 0),
        make_route_note('second message', 0, 1),
        make_route_note('third message', 1, 0),
        make_route_note('fourth message', 0, 0),
        make_route_note('fifth message', 1, 0),
    ]

    for msg in messages:
        print('sending %s at %s' % (msg.message, msg.location))
        yield msg


def guide_route_chat(stub):
    responses = stub.RouteChat(generate_messages())
    for response in responses:
        print('received message %s at (%s, %s)' % (
            response.message,
            response.location.latitude,
            response.location.longitude,
        ))


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = route_guide_pb2_grpc.RouteGuideStub(channel)
        print('-- GetFeature --')
        guide_get_feature(stub)

        print('-- ListFeatures --')
        guide_list_features(stub)

        print('-- RecordRoute --')
        guide_record_route(stub)

        print('-- RouteChat --')
        guide_route_chat(stub)


if __name__ == '__main__':
    run()

