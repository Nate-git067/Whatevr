#File for the contractors registration SQL model 
from server.config.config import Base
from sqlalchemy import (
    String,
    DateTime
)
from sqlalchemy.orm import mapped_column

from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from datetime import datetime


"""Maps the contractor registration -> Postgres"""
class ContractorRegistration(Base):
    __tablename__ = 'contractor_registration' #name of the table in Postgres 

    #personal info of the table 
    first_name:str = mapped_column(String(length=50), nullable=False)
    last_name:str = mapped_column(String(length=50), nullable=False)

    #contact information for the table 
    email:EmailStr = mapped_column(String(length=50), nullable=False)
    phonenumber:PhoneNumber = mapped_column(String(length=15), nullable=False)

    #audit info 
    created_at:datetime = mapped_column(DateTime(timezone=True))