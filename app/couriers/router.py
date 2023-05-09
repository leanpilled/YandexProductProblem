from fastapi import APIRouter
from app.couriers.dao import CouriersDAO

from app.couriers.schemas import SCouriers

router = APIRouter(
    prefix="/couriers",
    tags=["Couriers"]
)

@router.post("")
async def add_couriers(couriers_data: list[SCouriers]):
    for courier in couriers_data:
        await CouriersDAO.add(courier)
        
@router.get("/{courier_id}")
async def get_courier_by_id(courier_id: int) -> SCouriers:
    return await CouriersDAO.find_by_id(courier_id)

@router.get("")
async def get_couriers(offset: int = 0, limit: int = 1) -> list[SCouriers]:
    return await CouriersDAO.find_all[offset:][:limit]