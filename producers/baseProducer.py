from confluent_kafka import Producer
import json
from config.kafka import KAFKA_CONFIG

class BaseProducer:
    def __init__(self):
        self.producer = Producer(KAFKA_CONFIG)

    def produce(self, topic: str, value: dict, key: str | None = None):
        print(f"Producing to topic {topic}: {value}")
        self.producer.produce(
            topic=topic,
            key=key,
            value=json.dumps(value).encode("utf-8"),
            on_delivery=self.delivery_report
        )


    def poll(self):
        self.producer.poll(0)

    def flush(self):
        self.producer.flush()

    def delivery_report(self, err, msg):
        if err:
            print(f"❌ Delivery failed: {err}")
        else:
            print(
                f"✅ Delivered to {msg.topic()} "
                f"[{msg.partition()}] @ offset {msg.offset()}"
            )
