KAFKA_CONFIG = {
    "bootstrap.servers": "localhost:9092"
}

class Topics:
    MAIN = "main"
    ORDER = "order"
    PAYMENT_INFO = "payment_info"
    ITEM = "item"


class GroupIDs:
    ORDER_CONSUMER_GROUP = "group-order-consumer-group"
    PAYMENT_INFO_CONSUMER_GROUP = "group-payment-info-consumer-group"
    ITEM_CONSUMER_GROUP = "group-item-consumer-group"
    MAIN_PROCESSOR_GROUP = "main-processor-group"


