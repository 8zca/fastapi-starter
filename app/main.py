from fastapi import FastAPI
from app.route import router


app = FastAPI()

app.include_router(router, prefix="/v1", responses={404: {"message": "Not Found"}})
