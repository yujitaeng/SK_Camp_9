from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_docker():
    return "YOOZI's First Docker, HELLO!"