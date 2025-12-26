import json

from shared.config.kafka import Topics
from producers.baseProducer import BaseProducer

with open('./data/payload.json', 'r') as f:
    payload = json.load(f)

producer = BaseProducer()

producer.produce(
    topic=Topics.MAIN,
    value=payload)

producer.poll()

producer.flush()
