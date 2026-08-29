#File for the contractor to register on the landing page 
from fastapi.exceptions import HTTPException
from fastapi import Depends
from server.landing.merchants.routes.register import landing_router
from server.models.relational.registrations.drivers.contractors_registration import ContractorRegistration
from server.landing.drivers.contractors.schemas.register import (
    ContractorRegister,
    ContractorRegisterResponse
)
from server.config.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from typing import Annotated
from datetime import datetime, UTC


"""Route for the contractor to register"""
@landing_router.post('/contractor/register', response_model=ContractorRegisterResponse)
async def register_contractor(contractor_info:ContractorRegister, session_db:Annotated[AsyncSession, Depends(get_db)]):
    #database query for the contractor
    try:
        contractor_query = await session_db.execute(select(ContractorRegistration).where(or_(
            ContractorRegistration.email == contractor_info.email,
            ContractorRegistration.phonenumber == contractor_info.phonenumber
        )))
        contractor_registration = contractor_query.scalar_one_or_none()
    except Exception:
        raise HTTPException(
            status_code=500,
            detail='Database lookup failed during registration verification.'
        )

    #check if contractor already registered 
    if contractor_registration:
        raise HTTPException(
            status_code=400,
            detail='A contractor with this email or phone number already exists.'
        )

    #if no contractor registration -> create one 
    new_contractor_registration = ContractorRegistration(
        first_name=contractor_info.first_name,
        last_name=contractor_info.last_name,
        email=contractor_info.email,
        phonenumber=contractor_info.phonenumber,
        created_at=datetime.now(UTC)
    )

    #database transaction -> add registered contractor to Postgres 
    try:
        session_db.add(new_contractor_registration)
        await session_db.commit()
    except Exception:
        await session_db.rollback()
        raise HTTPException(
            status_code=500,
            detail='Failed to commit new contractor registration record to the database.'
        )

    #response to the client 
    return ContractorRegisterResponse(
        response='Registration successful! We will contact you directly with any important updates regarding Whatevr.'
    )