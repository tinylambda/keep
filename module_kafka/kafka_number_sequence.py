import sys

from kafka import KafkaProducer

topic = "greetings"
num_part = 3

if len(sys.argv) >= 2:
    topic = sys.argv[1]

bootstrap_servers = "localhost:30001,localhost:30002,localhost:30003"
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
)

for i in range(100):
    part_num = i % num_part
    part = f"{part_num}".encode("utf-8")
    data = f"{i * 10}".encode("utf-8")
    print("sending", data)
    producer.send(topic, value=data, key=part)

print(producer.metrics())
producer.flush()
