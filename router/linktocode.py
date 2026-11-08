from fastapi import APIRouter ,Depends,HTTPException,status
from db import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from schema import CodeResponse,CreateCode
from model import LinkToCode
from sqlalchemy.exc import IntegrityError
import secrets


#پرفیکس یه پیشوند به همه آدرس های روتر اضاف میکنه /=/linktocode
router = APIRouter(prefix="/linktocode",tags=["linktocode"])

@router.get("/ping")
def get_ping():
    return {"ok":True}


@router.post("/InputLink",response_model=CodeResponse,status_code=status.HTTP_201_CREATED)
def input_link(link:CreateCode,db:Session=Depends(get_db)):
    while True:
        short_code = secrets.token_urlsafe(6)

        existing_link = db.scalar(select(LinkToCode).where(LinkToCode.short_code==short_code))     
        if existing_link is None:
            break

    new_link = LinkToCode(long_link=str(link.long_link),
                          short_code = short_code)
    try:
        db.add(new_link)
        db.commit()
        db.refresh(new_link)
    except IntegrityError as e :
        db.rollback()
        print(e.orig)
        print("Database constraint violation")

        raise HTTPException(status_code=409,detail="link already exsits")
    return new_link     


@router.get("/getshortcode",response_model=CodeResponse)
def show_codes(db:Session=Depends(get_db)):
    return {"soper":True}     

#kos