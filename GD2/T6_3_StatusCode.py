# Trả Status Code


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

users = []

@app.post("/users", status_code=201)
def add_user(user: User):
    new_id = len(users) + 1
    new_user = {"id": new_id, **user.dict()}
    users.append(new_user)
    return new_user

@app.get("/users/{id}")
def get_user(id: int):
    for u in users:
        if u["id"] == id:
            return u
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/check_age")
def check_age(user: User):
    if user.age <= 0:
        raise HTTPException(status_code=400, detail="Age must be positive")
    return {"msg": "Valid age"}
