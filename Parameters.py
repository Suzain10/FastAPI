from fastapi import FastAPI
from typing import Optional
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/greet/{name}")
def greet(name: str, age: Optional[int] = None):
    greeting = f"Hello, {name}!"

    if age is not None:
        greeting += f" You are {age} years old."

    return {"message": greeting}