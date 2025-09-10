# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Xin chào API"}





from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # đường dẫn gốc
def read_root():
    return {"message": "Xin chào API"}

@app.get("/hello")  # đường dẫn /hello
def say_hello():
    return {"message": "Hello từ FastAPI"}

@app.get("/test")  # đường dẫn /test
def test_api():
    return {"status": "success", "data": "Đây là API test"}




# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"message": "Xin chào API", "version": 1.0}




















# 1. Kiến thức cần nắm

# HTTP protocol:

# Request = yêu cầu từ client (trình duyệt, mobile app, Postman).

# Response = phản hồi từ server.

# Method thường dùng:

# GET: lấy dữ liệu

# POST: gửi dữ liệu

# PUT/PATCH: cập nhật dữ liệu

# DELETE: xóa dữ liệu

# Status code (quan trọng):

# 200 OK: thành công

# 201 Created: tạo mới thành công

# 400 Bad Request: request sai

# 404 Not Found: không tìm thấy

# 500 Internal Server Error: lỗi server