from shared.consumers.baseConsumer import BaseConsumer
from baseProcessor import BaseProcessor
from shared.producers.baseProducer import BaseProducer
from shared.schemas.registry import ORDER_SCHEMAS
from shared.config.kafka import Topics, GroupIDs


def main():
    consumer = BaseConsumer(
        topic=Topics.MAIN,
        group_id=GroupIDs.MAIN_PROCESSOR_GROUP,
    )

    producer = BaseProducer()

    processor = BaseProcessor(
        consumer=consumer,
        producer=producer,
        schemas=ORDER_SCHEMAS,
    )

    processor.process()


if __name__ == "__main__":
    main()
