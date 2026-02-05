from fastapi import FastAPI

app = FastAPI(title="Carbon Fibre")

@app.get("/health")
def health_check():
    return {"status": "healthy"}