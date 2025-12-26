from schemas.base import EventSchema
from config.kafka import GroupIDs, Topics

class PaymentSchema(EventSchema):
    topic = Topics.PAYMENT_INFO
    group = GroupIDs.PAYMENT_INFO_CONSUMER_GROUP

    def build(self, event):
        payment = event["payment_info"]

        yield (
            payment["payment_id"],
            {
                **payment,
                "order_id": event["order_id"],
                "timestamp": event["timestamp"],
            }
        )
