from fastapi import FastAPI
from fastapi.testclient import TestClient
import sys
import os
from app.main import app


client = TestClient(app)

#Tested in sequence 

def test_add_todo_items():
    response = client.post("/todos",json={"id":1,"task":"Learn Fast API","status":False})
    assert response.status_code == 200
    
def test_get_todo_items():
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == [{"id":1,"task":"Learn Fast API","status":False}]
    
def test_get_specific_todo_item():
    response = client.get("/todos/1")
    assert response.status_code == 200
    

