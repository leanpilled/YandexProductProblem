from datetime import date
from fastapi import APIRouter, Request
from app.couriers.dao import CouriersDAO

from app.couriers.schemas import SCouriers

router = APIRouter(
    prefix="/couriers",
    tags=["Couriers"]
)

_incomeC = {
    'FOOT': 2,
    'BIKE': 3,
    'AUTO': 4
}

_raitingC = {
    'FOOT': 3,
    'BIKE': 2,
    'AUTO': 1
}

@router.post("")
async def add_couriers(request: Request, couriers_data: list[SCouriers]):
    for courier in couriers_data:
        await CouriersDAO.add(type=courier.type, regions=courier.regions , working_hours=courier.working_hours)
        
@router.get("/{courier_id}")
async def get_courier_by_id(request: Request, courier_id: int) -> SCouriers:
    return await CouriersDAO.find_by_id(courier_id)

@router.get("")
async def get_couriers(request: Request, offset: int = 0, limit: int = 1) -> list[SCouriers]:
    couriers = await CouriersDAO.find_all()
    return couriers[offset:][:limit]

@router.get("/meta-info/{courier_id}")
async def get_raiting(request: Request, courier_id: int, start_date: date, end_date: date):
    hours = (end_date - start_date).total_seconds() / 3600
    type = await CouriersDAO.get_courier_type(courier_id)
    incomeC = _incomeC[type]
    raitingC = _raitingC[type]
    _income, _orders_count = await CouriersDAO.get_raiting_info(courier_id, start_date, end_date)
    if _income == 0:
        return None
    income = _income * incomeC
    raiting = (_orders_count / hours) * raitingC
    return income, raiting

@router.get("/assignments")
async def get_assignments(request: Request):
    pass
