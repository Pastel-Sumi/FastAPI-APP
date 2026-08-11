# FastAPI-APP
Back-end application made with FastAPI using the tutorials from [***FastAPI Beyond CRUD***](https://jod35.github.io/fastapi-beyond-crud-docs/site/)

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
