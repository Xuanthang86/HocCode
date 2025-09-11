# API CRUD cơ bản


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

users = [
    {"id": 1, "name": "Thang", "age": 25},
    {"id": 2, "name": "Hoa", "age": 20},
]

# GET all
@app.get("/users")
def get_users():
    return {"users": users}

# POST thêm user
@app.post("/users")
def add_user(user: User):
    new_id = max([u["id"] for u in users], default=0) + 1
    new_user = {"id": new_id, **user.dict()}
    users.append(new_user)
    return {"msg": "User added", "user": new_user}

# PUT update
@app.put("/users/{id}")
def update_user(id: int, user: User):
    for u in users:
        if u["id"] == id:
            u["name"] = user.name
            u["age"] = user.age
            return {"msg": "User updated", "user": u}
    return {"error": "User not found"}

# DELETE
@app.delete("/users/{id}")
def delete_user(id: int):
    for u in users:
        if u["id"] == id:
            users.remove(u)
            return {"msg": f"User {id} deleted"}
    return {"error": "User not found"}
