from fastapi import HTTPException, status

from sqlalchemy import and_, select, any_, update
from app.dao.base import BaseDAO
from app.orders.models import Orders
from app.db import async_session_maker
from app.assignments.models import Assignments

class OrdersDAO(BaseDAO):
    model = Orders
    
    @classmethod
    async def update_completed_order(cls, order_id: int, courier_id: int, complition_time: str):
        async with async_session_maker() as session:
            check = await session.execute(
                select(Assignments.order_id)
                .select_from(Assignments)
                .where(
                    and_(
                        Assignments.courier_id == courier_id,
                        order_id == any_(Assignments.order_id)
                    )
                )
            )
            
            check = check.scalar()
            if not check:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
            
            await session.execute(
                update(Orders)
                .where(Orders.id == order_id)
                .values(status = "COMPLETED", complition_time = complition_time, courier_id = courier_id)
            )
            
            await session.commit()
            return order_id