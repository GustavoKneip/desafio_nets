import json
from processors.baseProcessor import BaseProcessor
from unittest.mock import MagicMock

def make_kafka_message(payload: dict):
    msg = MagicMock()
    msg.error.return_value = None
    msg.value.return_value = json.dumps(payload).encode("utf-8")
    return msg

def test_processor_produces_for_each_schema():
    # Arrange
    event = {
        "order_id": "ORD-1",
        "customer_id": "C1"
    }

    msg = make_kafka_message(event)

    consumer = MagicMock()
    consumer.poll.return_value = msg

    producer = MagicMock()

    schema1 = MagicMock()
    schema1.topic = "order"
    schema1.build.return_value = [
        ("ORD-1", {"order_id": "ORD-1"})
    ]

    schema2 = MagicMock()
    schema2.topic = "audit"
    schema2.build.return_value = [
        ("ORD-1", {"event": "created"})
    ]

    processor = BaseProcessor(
        consumer=consumer,
        producer=producer,
        schemas=[schema1, schema2]
    )

    # Act
    processor.process_once()

    # Assert
    schema1.build.assert_called_once_with(event)
    schema2.build.assert_called_once_with(event)

    producer.produce.assert_any_call(
        topic="order",
        key="ORD-1",
        value={"order_id": "ORD-1"},
    )

    producer.produce.assert_any_call(
        topic="audit",
        key="ORD-1",
        value={"event": "created"},
    )

    producer.poll.assert_called_once()


def test_process_once_no_message_does_nothing():
    consumer = MagicMock()
    consumer.poll.return_value = None

    producer = MagicMock()
    schema = MagicMock()

    processor = BaseProcessor(
        consumer=consumer,
        producer=producer,
        schemas=[schema],
    )

    processor.process_once()

    schema.build.assert_not_called()
    producer.produce.assert_not_called()
    producer.poll.assert_not_called()

def test_process_once_consumer_error_skips():
    msg = MagicMock()
    msg.error.return_value = "boom"

    consumer = MagicMock()
    consumer.poll.return_value = msg

    producer = MagicMock()
    schema = MagicMock()

    processor = BaseProcessor(
        consumer=consumer,
        producer=producer,
        schemas=[schema],
    )

    processor.process_once()

    schema.build.assert_not_called()
    producer.produce.assert_not_called()
    producer.poll.assert_not_called()


def test_process_once_invalid_json():
    msg = MagicMock()
    msg.error.return_value = None
    msg.value.return_value = b"not-json"

    consumer = MagicMock()
    consumer.poll.return_value = msg

    producer = MagicMock()
    schema = MagicMock()

    processor = BaseProcessor(
        consumer=consumer,
        producer=producer,
        schemas=[schema],
    )

    processor.process_once()

    schema.build.assert_not_called()
    producer.produce.assert_not_called()
    producer.poll.assert_not_called()





