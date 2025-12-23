import redis

r = redis.from_url("redis://red-d48agnruibrs7394rujg:6379")

#r.set('switch1', 'ON')
#r.delete('key')



from fastapi import FastAPI
app = FastAPI()


from typing import Optional, Annotated

from fastapi import FastAPI,Header

app = FastAPI()


@app.get("/")
async def root(name: str, age: int,token: Annotated[str | None, Header()] = None):
    return {"name": name,"age":age,"token":token}

@app.get("/items/{item_id}")
def read_item(item_id: str, q: Optional[str] = None):
    value = r.get(item_id).decode()
    return {item_id: value}
