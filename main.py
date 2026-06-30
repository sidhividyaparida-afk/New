import time, asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    await asyncio.sleep(3)
    return{
        "message":"Async API"
    }
# def fun():
#     time.sleep(3)
#     return "Function executed after 3 seconds"
# 
# print(fun())

# async def fun():
#     await asyncio.sleep(3)
#     return "Function executed after 3 seconds"

# print(asyncio.run(fun()))