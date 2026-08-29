#Schema file for the merchants registration 
from pydantic import (
    BaseModel,
    EmailStr,
    field_validator,
    model_validator,
)
from pydantic_extra_types.phone_numbers import PhoneNumber
import re


#Schema for the merchants registration
class MerchantRegister(BaseModel):
    #personal attributes 
    first_name:str = None 
    last_name:str = None 
    store_name:str = None

    #contact attributes 
    email:EmailStr = None 
    phonenumber:PhoneNumber = None 

    #validating fields user entered 
    @field_validator('first_name')
    @classmethod
    def firstname_check(cls, name:str) -> str:
        name = name.strip() #stripping leading/ending whitespace
        if not name:
            raise ValueError('Please enter your first name to continue.')

        #checking the length of the name 
        if len(name) > 50:
            raise ValueError('First name is too long. Please shorten your entry.')

        #checking the contents of the name 
        pattern = r'[^a-zA-Z]'
        if re.search(pattern, name):
            raise ValueError('First name cannot contain numbers or special characters.')

        #checking if any spaces in name 
        if any(char.isspace() for char in name):
            raise ValueError('First name cannot contain spaces.')

        return name.title() 

    #last name field 
    @field_validator('last_name')
    @classmethod
    def lastname_check(cls, name:str) -> str:
        name = name.strip() #stripping leading/ending whitespace
        if not name:
            raise ValueError('Please enter your first name to continue.')
    
        #checking the length of the name 
        if len(name) > 50:
            raise ValueError('First name is too long. Please shorten your entry.')
    
        #checking the contents of the name 
        pattern = r'[^a-zA-Z]'
        if re.search(pattern, name):
            raise ValueError('First name cannot contain numbers or special characters.')
    
        #checking if any spaces in name 
        if any(char.isspace() for char in name):
            raise ValueError('First name cannot contain spaces.')
    
        return name.title()

    #merchant store field 
    @field_validator('store_name')
    @classmethod
    def store_name_check(cls, store:str) -> str:
        store = store.strip() #stripping leading and ending whitespace 
        if not store:
            raise ValueError('')

        #checking length of the store name 
        if len(store) > 100:
            raise ValueError('')

        return store #returning the store field 

    #validating the model 
    @model_validator(mode='after')
    def model_check(self):
        if not all([self.first_name, self.last_name,
                    self.store_name, self.email, self.phonenumber]):
            raise ValueError('')

        return self #returning the schema instance 