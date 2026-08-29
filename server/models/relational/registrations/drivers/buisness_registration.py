#File for the SQL model for the buisnesses registration 
from server.config.config import Base
from sqlalchemy import (
    String,
    DateTime
)
from sqlalchemy.orm import mapped_column
from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from datetime import datetime


"""Maps the buisness registration object -> Postgres """
class BuisnessRegistration(Base):
    __tablename__ = 'buisness_registration' #name of the table 

    #personal attributes of the table 
    first_name:str = mapped_column(String(length=50), nullable=False)
    last_name:str = mapped_column(String(length=50), nullable=False)
    buisness_name:str = mapped_column(String(length=100), nullable=False)

    #contact info of the table 
    email:EmailStr = mapped_column(String(length=50), nullable=False, index=True)
    phonenumber:PhoneNumber = mapped_column(String(length=15), nullable=False, index=True)

    #audit info 
    created_at:datetime = mapped_column(DateTime(timezone=True))