# schemas/registry.py

from schemas.order import OrderSchema
from schemas.payment import PaymentSchema
from schemas.item import ItemSchema

ORDER_SCHEMAS = [
    OrderSchema(),
    PaymentSchema(),
    ItemSchema(),
]
