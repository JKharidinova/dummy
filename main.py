from fastapi import FastAPI

from project.settings import settings

app = FastAPI(title=settings.PROJECT_NAME,)


@app.get("/")
async def root():
    return {"message": "Hello World"}
