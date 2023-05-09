from datetime import date
from fastapi import HTTPException, status

from sqlalchemy import select
from app.dao.base import BaseDAO
from app.orders.models import Orders
from app.db import async_session_maker

class OrdersDAO(BaseDAO):
    model = Orders
    
    @classmethod
    async def update_completed_order(cls, order_id: int, courier_id: int, complition_date: date, complition_time: str):
        async with async_session_maker() as session:
            order = await session.execute(select(Orders).where(Orders.id == order_id))
            
            if not order or not order.id or order.courier_id != courier_id:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
            
            order.status = "COMPLETED"
            order.complition_date = complition_date
            order.complition_time = complition_time
            session.commit()
            return order_id