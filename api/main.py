from fastapi import FastAPI

app = FastAPI(title = "This is my Task Management Application")

@app.get("/")
def read_root():
    return {"message": "FastAPI server running"}