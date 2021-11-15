from typing import Optional
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from starlette.responses import FileResponse

app = FastAPI()
app.mount("/public", StaticFiles(directory="public"), name="public")


@app.get("/")
def read_index():
    return FileResponse('public/index.html')


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    if q:
        return "hi"
    else:
        return "bye"
    return {"item_id": item_id, "q": q}
@app.get("/50968")
@app.get("/25280")
@app.post("/login")
def login(id :Optional[str] , password: Optional[str]):
    return "login success"

# REST API -> GET , POST , PUT, DELETE 