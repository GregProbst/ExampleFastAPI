from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"Message": "This is Greg Probst's example project. Visit localhost:/8000/docs to see the documentation"}
