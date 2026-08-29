#Schema file for the contractors registration
from pydantic import (
    BaseModel,
    EmailStr,
    field_validator,
    model_validator
)
from pydantic_extra_types.phone_numbers import PhoneNumber
import re 


#Schema for the contractors registration
class ContractorRegister(BaseModel):
    #personal attributes 
    first_name:str = None 
    last_name:str = None

    #contact attributes 
    email:EmailStr = None 
    phonenumber:PhoneNumber = None 

    #validating the users fields 
    @field_validator('first_name')
    @classmethod
    def firstname_check(cls, name:str) -> str:
        name = name.strip() #stripping leading/ending whitespace 
        if not name:
            raise ValueError('First name cannot be empty.')

        #checking the length of the name 
        if len(name) > 50:
            raise ValueError('First name is too long.')

        #checking the contents of the name 
        pattern = r'[^A-Za-z]'
        if re.search(pattern, name):
            raise ValueError('First name must contain only alphabetic characters.')

        return name.title() #returns all sections of the name capitalized 

    #last name field 
    @field_validator('last_name')
    @classmethod
    def lastname_check(cls, name:str) -> str:
        name = name.strip() #stripping leading/ending whitespace 
        if not name:
            raise ValueError('First name cannot be empty.')

        #checking the length of the name 
        if len(name) > 50:
            raise ValueError('First name is too long.')

        #checking the contents of the name 
        pattern = r'[^A-Za-z]'
        if re.search(pattern, name):
            raise ValueError('First name must contain only alphabetic characters.')

        return name.title() #returns all sections of the name capitalized

    #validating the contractor schema model 
    @model_validator(mode='after')
    def model_check(self):
        if not all([self.first_name, self.last_name,
                    self.email, self.phonenumber]):
            raise ValueError('')

        return self #-> returns the instance of the schema 


#Schema for the response to client 
class ContractorRegisterResponse(BaseModel):
    response:str = None 