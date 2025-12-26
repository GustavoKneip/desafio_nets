from shared.config.kafka import GroupIDs, Topics
from consumers.baseConsumer import BaseConsumer

class PaymentInfoConsumer(BaseConsumer):
    def __init__(self):
        super().__init__(Topics.PAYMENT_INFO,GroupIDs.PAYMENT_INFO_CONSUMER_GROUP)