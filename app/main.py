from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
    expose_headers=["*"], 
)

class ToDo(BaseModel):
    id:int
    task : str
    status : bool = False
    
#response model to control return data
class ReturnToDo(BaseModel):
    task : str
    
todos = []

@app.post("/todos",response_model = ReturnToDo)
async def add_todo_items(item:ToDo):
    item.id = len(todos) + 1
    todos.append(item)
    return item
    
@app.get("/todos")
async def get_todo_items(completed:Optional[bool]=None):
    if completed is None:
        return todos
    else:
        return [item for item in todos if item.status == completed]

#Path Parameters
@app.get("/todos/{id}")
async def get_specific_todo_item(id:int):
    for item in todos:
        if item.id == id:
            return item
    raise HTTPException(status_code=404,details="No Specific item with {id} found retrival !!!")

@app.delete("/todos/{id}")
async def remove_todo_item(id:int):

    action = False
    for inx, todo in enumerate(todos):
        if todo.id == id:
            del todos[inx]
            action = True
    if action:
        raise HTTPException(status_code=200)
    else:
        raise HTTPException(status_code=404,details="No Specific item with {id} found for deletion !!!")

@app.put("/todos/update/{id}")
async def update_todo_items(id:int, new:ToDo):
    updated = False
    for inx, item in enumerate(todos):
        if item.id == id:
            todos[inx]= new
            todos[inx].id = id
            updated = True
    
    if not updated:
        raise HTTPException(status_code=404,details="Item updation failed !!!")