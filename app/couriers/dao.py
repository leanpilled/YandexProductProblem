from datetime import date

from sqlalchemy import and_, select
from app.couriers.models import Couriers
from app.dao.base import BaseDAO
from app.db import async_session_maker
from app.assignments.models import Assignments
from app.orders.models import Orders

class CouriersDAO(BaseDAO):
    model = Couriers
    
    @classmethod
    async def get_courier_type(cls, courier_id: int):
        async with async_session_maker() as session:
            type = await session.execute(
                select(Couriers.type)
                .select_from(Couriers)
                .where(Couriers.id == courier_id)
            )
            return type.scalar()
    
    @classmethod
    async def get_raiting_info(cls, courier_id: int, start_date: date, end_date: date):
        async with async_session_maker() as session:
            trips = await session.execute(
                select(Assignments.order_id)
                .select_from(Assignments)
                .where(
                    and_(
                        Assignments.courier_id == courier_id,
                        Assignments.date > start_date,
                        Assignments.date <= end_date,
                    )
                )
            )
            orders_count = 0
            income = 0
            trips = trips.mappings().all()
            for trip in trips:
                trip_sum = []
                for order in trip["order_id"]:
                    price = await session.execute(
                        select(Orders.price)
                        .select_from(Orders)
                        .where(
                            and_(
                                Orders.id == order,
                                Orders.status == "COMPLETED"
                            )
                        )
                    )
                    price = price.scalar()
                    if price:
                        trip_sum.append(price)
                        orders_count += 1
                if len(trip["order_id"]) != len(trip_sum):
                    continue
                for i in range(1, len(trip_sum)):
                    trip_sum[i] = trip_sum[i] * 0.8
                income += sum(trip_sum)
            return income, orders_count