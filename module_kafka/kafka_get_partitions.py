from kafka import KafkaConsumer
from kafka.structs import TopicPartition

topic = "request"
bootstrap_servers = "test:9092"
consumer = KafkaConsumer(
    topic, bootstrap_servers=bootstrap_servers, auto_offset_reset="earliest"
)
partitions = consumer.partitions_for_topic(topic)
for partition in partitions:
    p = TopicPartition(topic, partition)
    print(p)
