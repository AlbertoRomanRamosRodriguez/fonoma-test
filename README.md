# Total price endpoint

The endpoint receives a string ```criterion``` to filter the orders defined by a Pydantic Model as 

```py

class Order(BaseModel):
    id: int
    item: str
    quantity: int
    price: float
    status: str
```

Parameters are validated such that:
 - the status should be one of the valid statuses
 - the criterion must be one of the valid statuses or ```'all'```
 - the price must not be negative

It then uses a numpy array to efficiently filter and calculate the total amount according to the ```criterion```.

