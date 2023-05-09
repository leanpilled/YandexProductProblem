from datetime import date
from fastapi import APIRouter

from app.orders.dao import OrdersDAO
from app.orders.schemas import SOrders, FOrders

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("")
async def add_orders(orders_data: list[SOrders]):
    for order in orders_data:
        await OrdersDAO.add(order)
        
@router.get("/{order_id}")
async def get_order_by_id(order_id: int) -> FOrders:
    return await OrdersDAO.find_by_id(order_id)

@router.get("")
async def get_orders(offset: int = 0, limit: int = 1) -> list[FOrders]:
    return await OrdersDAO.find_all[offset:][:limit]

@router.post("/complete")
async def order_complited(order_info: list):
    complition_date = date.today()
    complition_time = order_info[2]
    order_id = order_info[1]
    courier_id = order_info[0]
    return await OrdersDAO.update_completed_order(order_id, courier_id, complition_date, complition_time)
    
    
    