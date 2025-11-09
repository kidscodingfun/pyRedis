import redis

r = redis.from_url("redis://red-d489ot4hg0os73857el0:6379")

#r.set('switch1', 'ON')
#r.delete('key')
print(r.get('switch1').decode())


from fastapi import FastAPI
app = FastAPI()


from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}