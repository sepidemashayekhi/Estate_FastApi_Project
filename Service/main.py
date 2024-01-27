
from Api.User import router
from Api.files import file_router

from  fastapi import FastAPI,status,responses





app=FastAPI()

app.include_router(router)
app.include_router(file_router)

