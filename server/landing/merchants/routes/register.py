#File for the route for the route for the user to register 
from fastapi.routing import APIRouter
from fastapi.exceptions import HTTPException
from fastapi import Depends
from server.models.relational.registrations.merchants.merchants_registration import MerchantRegistration
from server.landing.merchants.schemas.register import (
    MerchantRegister
)
from server.config.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from typing import Annotated
from datetime import datetime, UTC


"""global router instance for the landing page router"""
landing_router = APIRouter(prefix='/landing', tags=['Router for the landing page routes'])


"""Route for the merchant to register"""
@landing_router.post('/merchant', response_model=GeneratorExit)
async def register_merchant(merchant_info:MerchantRegister, session_db:Annotated[AsyncSession, Depends(get_db)]):
    #database query for the merchant 
    try:
        merchant_query = await session_db.execute(select(MerchantRegistration).where(or_(
            MerchantRegistration.email == merchant_info.email,
            MerchantRegistration.phonenumber == merchant_info.phonenumber
        )))
        merchant_registration = merchant_query.scalar_one_or_none() #returns first row found or -> None
    except Exception:
        raise HTTPException(
            status_code=500,
            detail='Internal server error occurred while checking for existing merchant registrations.'
        )
    
    if merchant_registration:
        raise HTTPException(
            status_code=400,
            detail='An email or phone number is already registered with us.'
        )

    #if no merchant -> create one 
    new_merchant_registration = MerchantRegistration(
        first_name=merchant_info.first_name,
        last_name=merchant_info.last_name,
        store_name=merchant_info.store_name,
        email=merchant_info.email,
        phonenumber=merchant_info.phonenumber,
        created_at=datetime.now(UTC)
    )

    #session transaction -> map merchant to Postgres
    try:
        session_db.add(new_merchant_registration)
        await session_db.commit()
    except Exception:
        await session_db.rollback()
        raise HTTPException(
            status_code=500,
            detail='Failed to save merchant registration to the database.'
        )