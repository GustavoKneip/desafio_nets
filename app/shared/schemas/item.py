from shared.schemas.base import EventSchema
from shared.config.kafka import GroupIDs, Topics

class ItemSchema(EventSchema):
    topic = Topics.ITEM
    group = GroupIDs.ITEM_CONSUMER_GROUP

    def build(self, event):
        for idx, item in enumerate(event["items"]):
            yield (
                f"{event['order_id']}",
                {
                    **item,
                    "order_id": event["order_id"],
                    "item_index": idx,
                    "timestamp": event["timestamp"],
                }
            )
