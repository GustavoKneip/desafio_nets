from datetime import datetime
import os
from confluent_kafka import Consumer
import json
import signal
import sys
from shared.config.kafka import KAFKA_CONFIG   

class BaseConsumer():
     
    def __init__(self, topic,group_id):
        self.consumer = Consumer({
            **KAFKA_CONFIG,
            "group.id": group_id,
            "auto.offset.reset": "earliest"
        })

        self.consumer.subscribe([topic])
        
    def shutdown(self, sig, frame):
        self.consumer.close()
        sys.exit(0)

    def run(self):
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)

        while True:
            msg = self.poll()
            if msg:
                print("#################### New message received ####################")
                print("Topic:", msg.topic())
                print("Timestamp:", datetime.now())
                data = json.loads(msg.value().decode())
                print(json.dumps(data, indent=2, ensure_ascii=False))

    def poll(self):
        msg = self.consumer.poll(1.0)

        if msg is None:
            return None
        if msg.error():
            print(msg.error())
            return None

        return msg