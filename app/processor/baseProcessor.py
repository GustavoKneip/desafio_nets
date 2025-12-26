import json


class BaseProcessor:
    def __init__(self, consumer, producer, schemas):
        self.consumer = consumer
        self.producer = producer
        self.schemas = schemas

    def process_once(self):
        msg = self.consumer.poll()

        if msg is None:
            return

        if msg.error():
            print(f"❌ Consumer error: {msg.error()}")
            return

        try:
            event = json.loads(msg.value().decode("utf-8"))
        except Exception as e:
            print("⚠️ Failed to read message:", e)
            return

        for schema in self.schemas:
            print(f"Processing with schema for topic: {schema.topic}")
            for key, payload in schema.build(event):
                self.producer.produce(
                    topic=schema.topic,
                    key=key,
                    value=payload,
                )

        self.producer.poll()

    def process(self):
        while True:
            self.process_once()