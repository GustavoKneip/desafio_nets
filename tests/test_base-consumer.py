from unittest.mock import MagicMock, patch
from consumers.baseConsumer import BaseConsumer


@patch("consumers.baseConsumer.Consumer")
def test_consumer_initialization(mock_kafka_consumer):
    BaseConsumer("test_topic", "test_group")
    mock_kafka_consumer.assert_called_once()
    
@patch("consumers.baseConsumer.Consumer")
def test_consumer_subscribe_called(mock_kafka_consumer):
    mock_instance = MagicMock()
    mock_kafka_consumer.return_value = mock_instance

    consumer = BaseConsumer("test_topic", "test_group")

    mock_instance.subscribe.assert_called_once_with(["test_topic"])

@patch("consumers.baseConsumer.Consumer")
def test_poll_returns_message(mock_kafka_consumer):
    mock_instance = MagicMock()
    mock_kafka_consumer.return_value = mock_instance

    mock_message = MagicMock()
    mock_message.error.return_value = None
    mock_instance.poll.return_value = mock_message

    consumer = BaseConsumer("test_topic", "test_group")
    msg = consumer.poll()
    print(msg)

    assert msg == mock_message

@patch("consumers.baseConsumer.Consumer")
def test_poll_handles_no_message(mock_kafka_consumer):
    mock_instance = MagicMock()
    mock_kafka_consumer.return_value = mock_instance

    mock_instance.poll.return_value = None

    consumer = BaseConsumer("test_topic", "test_group")
    msg = consumer.poll()

    assert msg is None

@patch("consumers.baseConsumer.Consumer")
def test_poll_handles_error_message(mock_kafka_consumer):
    mock_instance = MagicMock()
    mock_kafka_consumer.return_value = mock_instance

    mock_error = MagicMock()
    mock_error.error.return_value = "Some error"

    mock_instance.poll.return_value = mock_error

    consumer = BaseConsumer("test_topic", "test_group")
    msg = consumer.poll()

    assert msg is None

@patch("consumers.baseConsumer.Consumer")
def test_shutdown_closes_consumer_and_exits(mock_kafka_consumer):
    mock_instance = MagicMock()
    mock_kafka_consumer.return_value = mock_instance

    consumer = BaseConsumer("test_topic", "test_group")

    with patch("sys.exit") as mock_sys_exit:
        consumer.shutdown(None, None)

        mock_instance.close.assert_called_once()
        mock_sys_exit.assert_called_once()


@patch("consumers.baseConsumer.Consumer")
def test_run_calls_poll(mock_kafka_consumer):
    mock_instance = MagicMock()
    mock_kafka_consumer.return_value = mock_instance

    consumer = BaseConsumer("test_topic", "test_group")

    consumer.poll = MagicMock(side_effect=[None, KeyboardInterrupt])

    try:
        consumer.run()
    except KeyboardInterrupt:
        pass

    consumer.poll.assert_called()

