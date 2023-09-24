
from pydantic import BaseModel
from typing import List, Annotated
from fastapi import FastAPI, Body, status

import numpy as np

app = FastAPI()

VALID_STATUSES = ['completed', 'pending', 'canceled']
VALID_CRITERIONS = VALID_STATUSES
VALID_CRITERIONS.append('all')

class Order(BaseModel):
    id: int
    item: str
    quantity: int
    price: float
    status: str

@app.post("/solution", status_code=status.HTTP_200_OK)
def process_orders(orders:List[Order], criterion:Annotated[str, Body()]) -> float:

    total = 0

    negative_prices = [o.price < 0 for o in orders] # check for negative prices
    invalid_statuses = [o.status not in VALID_STATUSES for o in orders] # check for invalid statuses

    if any(negative_prices) or any(invalid_statuses) or not criterion in VALID_CRITERIONS:
        return -1

    if criterion == 'all':
        amounts = np.array([o.price * o.quantity for o in orders])
    else:
        amounts = np.array([o.price * o.quantity for o in orders if o.status == criterion])
        
    total = np.sum(amounts)

    return total