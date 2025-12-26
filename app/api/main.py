from fastapi import FastAPI, HTTPException
from shared.producers.baseProducer import BaseProducer
from shared.config.kafka import Topics

app = FastAPI(title="Kafka Producer API")

producer = BaseProducer()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/events/main")
def produce_main_event(payload: dict):
    try:
        producer.produce(
            topic=Topics.MAIN,
            value=payload,
        )
        producer.poll()
        return {"status": "ok", "topic": Topics.MAIN}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
