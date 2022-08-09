import json
import random
import sys

from kafka import KafkaProducer

topic = "page_views3"
num_part = 3

if len(sys.argv) >= 2:
    topic = sys.argv[1]

bootstrap_servers = "localhost:9092"
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
)

for _ in range(100):
    rand_id = random.randint(1, 100)
    page_view = {"id": f"foo{rand_id}", "user": f"bar", "x": "100"}
    page_view = {"id": rand_id, "user": f"bar", "x": "100"}
    page_view_json = json.dumps(page_view)
    page_view_bytes = page_view_json.encode("utf-8")
    producer.send(topic, value=page_view_bytes)

print(producer.metrics())
producer.flush()
print(producer.metrics())
