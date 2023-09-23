
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, Response, status

import numpy as np

app = FastAPI()

VALID_CRITERIONS = ['completed', 'pending', 'canceled', 'all']

class Order(BaseModel):
    id: int
    item: str
    quantity: int
    price: float
    status: str

class OrderData(BaseModel):
    orders : List[Order]
    criterion: str

@app.post("/solution", status_code=status.HTTP_200_OK)
def process_orders(order_data:OrderData, response:Response) -> float:
    
    orders = order_data.orders
    criterion = order_data.criterion

    total = 0

    if not criterion in VALID_CRITERIONS:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE

        return -1

    if criterion == 'all':
        prices = np.array([order.price for order in orders])
    else:
        prices = np.array([order.price for order in orders if order.status == criterion])
        
    total = np.sum(prices, where=(prices>=0))

    return total