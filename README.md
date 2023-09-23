# Total price endpoint

The endpoint receives a Pydantic Model defined as 

```py

class Order(BaseModel):
    id: int
    item: str
    quantity: int
    price: float
    status: str

class OrderData(BaseModel):
    orders : List[Order]
    criterion: str
```

This temporarily solves the issue of the application mistaking the ```criterion``` as a url query parameter.

