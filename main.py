# main.py

from config.kafka import GroupIDs, Topics
from consumers.baseConsumer import BaseConsumer
from processors.baseProcessor import BaseProcessor
from producers.baseProducer import BaseProducer
from schemas.registry import ORDER_SCHEMAS


from fastapi import FastAPI, HTTPException
from producers.baseProducer import BaseProducer
from config.kafka import Topics

app = FastAPI(title="Kafka Producer API")

producer = BaseProducer()

@app.post("/events/main")
def produce_main_event(payload: dict):
    try:
        producer.produce(
            topic=Topics.MAIN,
            value=payload,
        )
        producer.poll()
        return {
            "status": "ok",
            "topic": Topics.MAIN,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


consumer = BaseConsumer(Topics.MAIN, GroupIDs.MAIN_PROCESSOR_GROUP)
producer = BaseProducer()

processor = BaseProcessor(
    consumer=consumer,
    producer=producer,
    schemas=ORDER_SCHEMAS
)

processor.process()
