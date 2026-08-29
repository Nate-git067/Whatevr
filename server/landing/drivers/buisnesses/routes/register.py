#File for the route for the buisness registation
from fastapi.exceptions import HTTPException
from fastapi import Depends
from server.landing.merchants.routes.register import landing_router
from server.models.relational.registrations.drivers.buisness_registration import BuisnessRegistration
from server.landing.drivers.buisnesses.schemas.register import (
    BuisnessRegister,
    BuisnessRegisterResponse
)
from server.config.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from typing import Annotated
from datetime import datetime, UTC


"""Route for the buisness to register"""
@landing_router.post('/buisness/register', response_model=BuisnessRegisterResponse)
async def register_buisnes(buisness_info:BuisnessRegister, session_db:Annotated[AsyncSession, Depends(get_db)]):
    try:
        buisness_query = await session_db.execute(select(BuisnessRegistration).where(or_(
            BuisnessRegistration.email == buisness_info.email,
            BuisnessRegistration.phonenumber == buisness_info.phonenumber
        )))
        buisness_registration = buisness_query.scalar_one_or_none()
    except Exception:
        raise HTTPException(
            status_code=500,
            detail='Internal server error occurred while checking for existing buisness registrations.'
        )

    #check if the buisness already registered 
    if buisness_registration:
        raise HTTPException(
            status_code=400,
            detail='An email or phone number is already registered with us.'
        )

    #if buisness not registered -> create registration
    new_buisness_registration = BuisnessRegistration(
        first_name=buisness_info.first_name,
        last_name=buisness_info.last_name,
        buisness_name=buisness_info.buisness_name,
        email=buisness_info.email,
        phonenumber=buisness_info.phonenumber,
        created_at=datetime.now(UTC)
    )

    #session transaction -> adding new buisness registration
    try:
        session_db.add(new_buisness_registration)
        await session_db.commit()
    except Exception:
        await session_db.rollback()
        raise HTTPException(
            status_code=500,
            detail='Failed to save buisness registration to the database.'
        )

    #response back to client 
    return BuisnessRegisterResponse(
        response='Registration successful! We will contact you directly with any important updates regarding Whatevr.'
    )