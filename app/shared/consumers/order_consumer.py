from shared.config.kafka import GroupIDs, Topics
from consumers.baseConsumer import BaseConsumer

class OrderConsumer(BaseConsumer):
    def __init__(self):
        super().__init__(Topics.ORDER,GroupIDs.ORDER_CONSUMER_GROUP)