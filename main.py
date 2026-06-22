from fastapi import FastAPI, Request
import time
app = FastAPI()

@app.middleware("http")
async def log_request(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    print(f"Path: {request.url.path} | Method: {request.method} | Status Code: {response.status_code} | Process Time: {process_time} seconds")

    return response

@app.middleware("http")
async def add_custom_header(request: Request, call_next):
    print("Request recieved")
    response = await call_next(request)
    response.headers["X-Custom-Header"] = "Custom Value"
    print("Response sent with custom header")
    return response