#example 1 - basic hello world
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"world"}

#example 2 - returning a course id and validating its an integer
@app.get("/course/{course_id}")
def my_course(course_id: int):
    return {"course_id" : course_id}

#example 3 - basic query parameters and returning a set of results
dummy_data = [i for i in range(100)]

@app.get("/my/page/items/")
async def read_item(page: int = 0, limit: int = 0, skip: int=1):
    return dummy_data[page*10: page*10 + limit: skip]

#example 4-  used for creating posts from json requests
from pydantic import BaseModel

class MyItem(BaseModel):
    name: str
    info: str = None
    price: float
    qty: int

@app.post("/purchase/item/")
async def create_item(item: MyItem):
    return {"amount": item.qty*100, "success": True}


#example 5 -used for creating posts from HTML forms
from fastapi import Form

@app.post("/accounts/form")
async def login_view(username: str = Form(...), password: str = Form(...)):
    return {"success": True}
