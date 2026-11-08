from pydantic import BaseModel ,AnyUrl ,Field,HttpUrl
from datetime import datetime
#پایدنتیک و انواع ساده  رشته و عدد رو میفهمه
#هر چیزی که از پایدنتیک میاد لازم نیست ساده باسه 
#هرچیزی که به دیتابیس میره باید ساده باشه

class CodeResponse(BaseModel):
    id:int
    long_link:str 
    short_code:str
    Number_of_views :int = Field(default=0)
    created_at : datetime



class CreateCode (BaseModel):
    long_link:HttpUrl
    short_code:str
    
    

