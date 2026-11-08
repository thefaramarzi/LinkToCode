from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base , sessionmaker


db_url = "sqlite:///database.db"
engine = create_engine(db_url,)
Base = declarative_base()
sessionlocal = sessionmaker(bind=engine)

def get_db():
    print("baz shod")
    db =sessionlocal()
    try:
        yield db #سشن رو به اندپوینت تخویل میدهبرای انجام کار رو دیتابیس و همون جا میایسته
        print("tamam shod")
    finally:
        db.close()    #بعد از تموم شدن کار دیتابیس را میبندد
