from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Example REST API",
    description="A simple REST API built with FastAPI",
    version="1.0.0"
)

@app.get("/hello-world")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 
