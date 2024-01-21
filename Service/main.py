
from Api.User import router

from  fastapi import FastAPI,status,responses





app=FastAPI()

app.include_router(router)
