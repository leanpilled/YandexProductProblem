from fastapi import APIRouter, Request

from app.orders.dao import OrdersDAO
from app.orders.schemas import SOrders, FOrders

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("")
async def add_orders(request: Request, orders_data: list[SOrders]):
    for order in orders_data:
        await OrdersDAO.add(weight=order.weight, region=order.region, time=order.time, price=order.price)
        
@router.get("/{order_id}")
async def get_order_by_id(request: Request, order_id: int) -> FOrders:
    return await OrdersDAO.find_by_id(order_id)

@router.get("")
async def get_orders(request: Request, offset: int = 0, limit: int = 1) -> list[FOrders]:
    orders = await OrdersDAO.find_all()
    return orders[offset:][:limit]

@router.post("/complete")
async def order_complited(request: Request, order_info: list):
    complition_time = order_info[2]
    order_id = order_info[1]
    courier_id = order_info[0]
    return await OrdersDAO.update_completed_order(order_id, courier_id, complition_time)

@router.post("/assign")
async def assign_orders(request: Request):
    pass