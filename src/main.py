from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def root():
    return {}


@app.get("/files")
async def files():
    return {"files": []}
