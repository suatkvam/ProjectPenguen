from fastapi import FastAPI

app = FastAPI(title="Zemin360 API")


@app.get("/health")
def health():
    return {"status": "ok"}
