# FastAPI-APP
Back-end application made with FastAPI for personal practice.

## Documentation
### Setup
Created a virtual environment (on windows) using:
```shell
    python -m venv env
```

And ran the following command to activate the virtual environment:
```shell
    env\Scripts\activate
```

And installed FastAPI within our virtual environment.
```shell
    pip install "fastapi[standard]"
```

We freeze our dependencies into a `requirements.txt` file to track the exact versions of our dependencies so that we can easily reproduce them in the future.
```shell
    pip freeze > requirements.txt
```

To run the application we use the command:
```shell
    fastapi dev main.py
```

### Request Headers
During a request-response transaction, the client not only sends parameters to the server but also provides information about the context of the request's origin. This contextual information is crucial as it enables the server to customize the type of response it returns to the client.
Common request headers include:

- User-Agent: This string allows network protocol peers to identify the application responsible for the request, the operating system it's running on, or the version of the software being used.

- Host: This specifies the domain name of the server, and (optionally) the TCP port number on which the server is listening.

- Accept: Informs the server about the types of data that can be sent back.

- Accept-Language: This header informs the server about the preferred human language for the response.

- Accept-Encoding: The encoding algorithm, usually a compression algorithm, that can be used on the resource sent back.

- Referer: This specifies the address of the previous web page from which a link to the currently requested page was followed.

- Connection: This header controls whether the network connection stays open after the current transaction finishes.

`routes.py` will contain all the book routes.

`schemas.py` will contain the schemas that are currently in our root directory.

FastAPI routers allow easy modularization of our API by grouping related API routes together.

Using our FastAPI instance, we include all endpoints created with it by calling the `include_router` method.
Furthermore, we added the following arguments to the include_router method:

* `prefix`: The path through which all related endpoints can be accessed. In our case, it's named the /{version}/books prefix, resulting in /v1/books or /v2/books based on the application version. This implies that all book-related endpoints can be accessed using http://localhost:8000/api/v1/books.

* `tags`: The list of tags associated with the endpoints that fall within a given router.

The current organization of our API endpoints is as follows:

| Endpoint | Method | Description |
| --- | --- | --- |
| /api/v1/books | GET	| Read all books |
/api/v1/books | POST | Create a book
/api/v1/books/{book_id} | GET | Get a book by ID
/api/v1/books/{book_id} | PATCH | Update a book by ID
/api/v1/books/{book_id} | DELETE | Delete a book by ID


### Explaining an Object-Relational Mapper (ORM)
An Object-Relational Mapper (ORM) serves as a translator between a programming language, such as Python, and a database, like PostgreSQL or MySQL.

1. **Mapping Objects to Tables:** You create Python classes to represent tables in the database. Each object of these classes corresponds to a row in the database table.
2. **Interacting with Data:** You can then interact with these Python objects as if they were regular objects in your code, like setting attributes and calling methods.
3. **Behind the Scenes:** When you perform operations on these objects, like saving or deleting, the ORM translates these actions into the appropriate SQL queries that the database understands.
4. **Data Conversion:** The ORM handles converting Python data types into database-specific types and vice versa, ensuring compatibility between the two.

An ORM simplifies the process of working with databases by allowing you to focus on your application's logic in Python, rather than getting bogged down in SQL queries and database management details. It acts as a bridge between the object-oriented world of programming and the relational world of databases.
