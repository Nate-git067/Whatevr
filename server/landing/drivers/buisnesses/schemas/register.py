#Schema file for the buisness to register 
from pydantic import (
    BaseModel,
    EmailStr,
    field_validator,
    model_validator
)
from pydantic_extra_types.phone_numbers import PhoneNumber
import re


"""Schema for the business to register"""
class BuisnessRegister(BaseModel):
    first_name:str = None 
    last_name:str = None 
    buisness_name:str = None 

    #contact attributes 
    email:EmailStr = None
    phonenumber:PhoneNumber = None 

    #validating the fields 
    @field_validator('first_name')
    @classmethod
    def firstname_check(cls, name:str) -> str:
        name = name.strip()
        if not name:
            raise ValueError('First name cannot be empty')

        #checking length of name 
        if len(name) > 50:
            raise ValueError('First name cannot exceed 50 characters')

        #checking contents of the name 
        pattern = r"^[A-Za-z\s\-]+$"
        if re.search(pattern, name):
            raise ValueError('First name can only contain letters, spaces, or hyphens')

        return name.title()

    #last name field 
    @field_validator('last_name')
    @classmethod
    def firstname_check(cls, name:str) -> str:
        name = name.strip()
        if not name:
            raise ValueError('Last name cannot be empty')

        #checking length of name 
        if len(name) > 50:
            raise ValueError('Last name cannot exceed 50 characters')

        #checking contents of the name 
        pattern = r'[^A-Za-z]'
        if re.search(pattern, name):
            raise ValueError('Last name can only contain letters, spaces, or hyphens')

        return name.title()

    #validating the buisness name 
    @field_validator('buisness_name')
    @classmethod
    def buisness_name_check(cls, buisness:str) -> str:
        buisness = buisness.strip()
        if not buisness:
            raise ValueError('Business name cannot be empty')

        #checking the length of the buisness
        if len(buisness) > 100:
            raise ValueError('Business name cannot exceed 100 characters')

        return buisness.title()

    #validating the schemas model instance
    @model_validator(mode='after')
    def model_check(self):
        if not all([self.first_name, self.last_name,
                    self.buisness_name, self.email, self.phonenumber]):
            raise ValueError('All fields are required to register.')

        return self #returns instance of the model 


#Schema for the response returned to the client 
class BuisnessRegisterResponse(BaseModel):
    response:str = None 