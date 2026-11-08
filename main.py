from fastapi import FastAPI
from sqlalchemy.orm import Session
from schema import CreateCode
from router import linktocode

app =FastAPI()

app.include_router(linktocode.router)


