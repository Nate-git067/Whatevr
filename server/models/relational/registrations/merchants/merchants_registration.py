#File for the SQL model for the merchant registration
from server.config.config import Base
from sqlalchemy import (
    String,
    DateTime
)
from sqlalchemy.orm import mapped_column
from pydantic import EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from datetime import datetime


"""Map the table for merchant registration -> Postgres"""
class MerchantRegistration(Base):
    __tablename__ = 'merchant_registration'

    #personal info of the table 
    first_name:str = mapped_column(String(length=50), nullable=False)
    last_name:str = mapped_column(String(length=50), nullable=False)
    store_name:str = mapped_column(String(length=100), nullable=False)

    #contact info in the table 
    email:str = mapped_column(String(length=50), nullable=False, index=True)
    phonenumber:str = mapped_column(String(length=15), nullable=False, index=True)

    #audit info 
    created_at:datetime = mapped_column(DateTime(timezone=True))