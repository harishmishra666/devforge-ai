from fastapi import FastAPI

app = FastAPI(
    title="DevForge AI",
    description="Agentic AI Software Engineering & Autonomous Development Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "DevForge AI is running!",
        "status": "success",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }