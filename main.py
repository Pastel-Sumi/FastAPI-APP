from fastapi import FastAPI, Header
#To make path parameters optional
from typing import Optional
#Pydantic enables us to establish the structure of the data being sent.
#It also aids in validating data types using type hints.
from pydantic import BaseModel

#The FastAPI class serves as the primary entry point for all FastAPI applications.
#We create an instance of the FastAPI class
app = FastAPI()

#the User model
class UserSchema(BaseModel):
    username:str
    email:str

users = []
user_list = [
    "Jerry",
    "Joey",
    "Phil"
]

#Definition of an API Route
#The @app decorator associates the function with the HTTP GET method via the `get` method
@app.get('/')
async def read_root():
    return {"message": "Hello World!"}

@app.get('/greet/')
async def greet(username:Optional[str]="User"):
    return {"message": f"Hello {username}!"}

@app.get('/search')
async def search_for_user(username:str):
    for user in user_list:
        if username in user_list:
            return {"message": f"details for user {username}"}

        else:
            return {"message":"User not found"}

@app.post("/create_user")
async def create_user(user_data:UserSchema):
    new_user = {
        "username": user_data.username,
        "email": user_data.email
    }
    users.append(new_user)

    return {"message": "User Created succesfully", "user": new_user}

@app.get('/get_headers')
async def get_all_request_headers(
    user_agent: Optional[str] = Header(None),
    accept_encoding: Optional[str] = Header(None),
    referer: Optional[str] = Header(None),
    connection: Optional[str] = Header(None),
    accept_language: Optional[str] = Header(None),
    host: Optional[str] = Header(None)
):
    request_headers = {}
    request_headers["User-Agent"] = user_agent
    request_headers["Accept-Encoding"] = accept_encoding
    request_headers["Referer"] = referer
    request_headers["Connection"] = connection
    request_headers["Accept-Language"] = accept_language
    request_headers["Host"] = host

    return request_headers