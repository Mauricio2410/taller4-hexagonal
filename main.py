from fastapi import FastAPI
from app.infrastructure.api.user_controller import router as user_router

app = FastAPI(title="Microservicio Usuarios - Puerto 8001")
app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)