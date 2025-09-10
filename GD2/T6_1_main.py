
# Endpoint với Query và Path Parameter


from fastapi import FastAPI

app = FastAPI()

# Mock data
users = [
    {"id": 1, "name": "Thang", "age": 25},
    {"id": 2, "name": "Hoa", "age": 20},
    {"id": 3, "name": "Nam", "age": 30},
]

# 1. GET /users → trả danh sách user
@app.get("/users")
def get_users(age: int | None = None):
    if age:
        filtered = [u for u in users if u["age"] == age]
        return {"users": filtered}
    return {"users": users}

# 2. GET /users/{id} → trả về user theo id
@app.get("/users/{id}")
def get_user_by_id(id: int):
    for u in users:
        if u["id"] == id:
            return u
    return {"error": "User not found"}
