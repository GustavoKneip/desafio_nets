import json
import pytest
from unittest.mock import MagicMock, patch

from shared.config.kafka import KAFKA_CONFIG
from shared.producers.baseProducer import BaseProducer


@patch("shared.producers.baseProducer.Producer")
def test_producer_initialization(mock_kafka_producer):
    BaseProducer()

    mock_kafka_producer.assert_called_once_with(KAFKA_CONFIG)


@patch("shared.producers.baseProducer.Producer")
def test_produce_calls_kafka_produce(mock_kafka_producer):
    mock_instance = MagicMock()
    mock_kafka_producer.return_value = mock_instance

    producer = BaseProducer()

    payload = {"order_id": "ORD-1"}
    producer.produce(
        topic="order",
        key="ORD-1",
        value=payload
    )

    mock_instance.produce.assert_called_once()

    args, kwargs = mock_instance.produce.call_args

    assert kwargs["topic"] == "order"
    assert kwargs["key"] == "ORD-1"
    assert json.loads(kwargs["value"].decode()) == payload
    assert "on_delivery" in kwargs

@patch("shared.producers.baseProducer.Producer")
def test_poll_calls_kafka_poll(mock_kafka_producer):
    mock_instance = MagicMock()
    mock_kafka_producer.return_value = mock_instance

    producer = BaseProducer()
    producer.poll()

    mock_instance.poll.assert_called_once_with(0)

@patch("shared.producers.baseProducer.Producer")
def test_flush_calls_kafka_flush(mock_kafka_producer):
    mock_instance = MagicMock()
    mock_kafka_producer.return_value = mock_instance

    producer = BaseProducer()
    producer.flush()

    mock_instance.flush.assert_called_once()

@patch("shared.producers.baseProducer.Producer")
def test_delivery_report_success(mock_kafka_producer):
    mock_instance = MagicMock()
    mock_kafka_producer.return_value = mock_instance

    producer = BaseProducer()

    mock_msg = MagicMock()
    mock_msg.topic.return_value = "order"
    mock_msg.partition.return_value = 0
    mock_msg.offset.return_value = 123

    with patch("builtins.print") as mock_print:
        producer.delivery_report(None, mock_msg)

        mock_print.assert_called_once_with(
            "✅ Delivered to order [0] @ offset 123"
        )

@patch("shared.producers.baseProducer.Producer")
def test_delivery_report_failure(mock_kafka_producer):
    mock_instance = MagicMock()
    mock_kafka_producer.return_value = mock_instance

    producer = BaseProducer()

    error_message = "Some error occurred"

    with patch("builtins.print") as mock_print:
        producer.delivery_report(error_message, None)

        mock_print.assert_called_once_with(
            f"❌ Delivery failed: {error_message}"
        )

