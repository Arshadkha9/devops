from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to devops"}


@app.get("/ok")
def health_check():
    return {"status": "all ok"}

@app.get("/chec")
def health_check():
    return {"status": "checking"}
