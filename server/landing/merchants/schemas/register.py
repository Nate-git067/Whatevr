#Schema file for the merchants registration 
from pydantic import (
    BaseModel,
    EmailStr,
    field_validator,
    model_validator,
)
from pydantic_extra_types.phone_numbers import PhoneNumber

