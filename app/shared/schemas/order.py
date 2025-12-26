from shared.schemas.base import EventSchema
from shared.config.kafka import GroupIDs, Topics

class OrderSchema(EventSchema):
    topic = Topics.ORDER
    group = GroupIDs.ORDER_CONSUMER_GROUP

    def build(self, event):
        yield (
            event["order_id"],
            {
                "order_id": event["order_id"],
                "customer_id": event["customer_id"],
                "timestamp": event["timestamp"],
                "metadata": event.get("metadata"),
            }
        )
