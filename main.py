from fastapi import FastAPI, Header, status
from fastapi.exceptions import HTTPException
#To make path parameters optional
from typing import Optional
#Pydantic enables us to establish the structure of the data being sent.
#It also aids in validating data types using type hints.
from pydantic import BaseModel

#The FastAPI class serves as the primary entry point for all FastAPI applications.
#We create an instance of the FastAPI class
app = FastAPI()

#Our book model
class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str

"""
This route responds to GET requests made to /books, providing a list of all books available in the application. It ensures
that the response adheres to the List[Book] model, guaranteeing consistency with the structure defined by the Book model.
"""
@app.get("/books", response_model=list[Book])
async def get_all_books():
    return books


@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()

    books.append(new_book)
    return new_book

@app.get("/book/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.patch("/book/{book_id}")
async def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language

            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

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

books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The web socket handbook",
        "author": "Alex Diaconu",
        "publisher": "Xinyu Wang",
        "published_date": "2021-01-01",
        "page_count": 3677,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Head first Javascript",
        "author": "Hellen Smith",
        "publisher": "Oreilly Media",
        "published_date": "2021-01-01",
        "page_count": 540,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Algorithms and Data Structures In Python",
        "author": "Kent Lee",
        "publisher": "Springer, Inc",
        "published_date": "2021-01-01",
        "page_count": 9282,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Head First HTML5 Programming",
        "author": "Eric T Freeman",
        "publisher": "O'Reilly Media",
        "published_date": "2011-21-01",
        "page_count": 3006,
        "language": "English",
    },
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