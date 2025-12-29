from shared.consumers.baseConsumer import BaseConsumer
from shared.config.kafka import GroupIDs, Topics

class ItemConsumer(BaseConsumer):
    def __init__(self):
        super().__init__(Topics.ITEM,GroupIDs.ITEM_CONSUMER_GROUP)