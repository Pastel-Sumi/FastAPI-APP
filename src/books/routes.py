from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from src.books.book_data import books
from src.books.schemas import BookSchema, BookUpdateSchema

book_router =  APIRouter()

"""
This route responds to GET requests made to /books, providing a list of all books available in the application. It ensures
that the response adheres to the List[Book] model, guaranteeing consistency with the structure defined by the Book model.
"""
@book_router.get("/books", response_model=list[BookSchema])
async def get_all_books():
    return books

@book_router.post("/books", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: BookSchema) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@book_router.get("/book/{book_id}")
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.patch("/book/{book_id}")
async def update_book(book_id: int, book_update_data: BookUpdateSchema) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language

            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)

            return {}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")