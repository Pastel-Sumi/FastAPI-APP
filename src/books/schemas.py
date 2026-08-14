#Pydantic enables us to establish the structure of the data being sent.
#It also aids in validating data types using type hints.
from pydantic import BaseModel

class BookSchema(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

class BookUpdateSchema(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str
