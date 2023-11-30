from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()

class Employee(Base):
    __table__name = "employee"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    email = Column(String, index=True)
    departement = Column(String, index=True)
    hire_date = Column(String, index=True)

DATABASE_URL = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_HOST']}:{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_DB']}"
app = FastAPI()
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app.add_middleware(
    CORSMiddleware,
    allows_origins=["*"],
    allows_methods=["*"],
    allows_headers=["*"]
)

@app.get("/")
async def hello ():
    return {"hello Clement"}