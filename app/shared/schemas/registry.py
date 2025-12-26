# schemas/registry.py

from shared.schemas.order import OrderSchema
from shared.schemas.payment import PaymentSchema
from shared.schemas.item import ItemSchema

ORDER_SCHEMAS = [
    OrderSchema(),
    PaymentSchema(),
    ItemSchema(),
]
