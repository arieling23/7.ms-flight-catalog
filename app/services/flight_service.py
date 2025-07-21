from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.flight import Flight
from datetime import datetime
from app.logger import logger
from typing import Optional
from app.events.event_publisher import publish_flight_created  

class FlightService:
    @staticmethod
    async def get_all(session: AsyncSession) -> list[Flight]:
        result = await session.execute(select(Flight))
        return result.scalars().all()

    @staticmethod
    async def create(
        session: AsyncSession,
        code: str,
        origin: str,
        destination: str,
        departure_time: datetime
    ) -> Flight:
        logger.info(f"🛫 Creando vuelo {code}: {origin} → {destination}")
        flight = Flight(
            code=code,
            origin=origin,
            destination=destination,
            departure_time=departure_time
        )
        session.add(flight)
        await session.commit()
        await session.refresh(flight)

       
        await publish_flight_created(flight.id)

        return flight

    @staticmethod
    async def get_by_id(session: AsyncSession, flight_id: int) -> Optional[Flight]:
        flight = await session.get(Flight, flight_id)
        if flight:
            logger.info(f"✈️ Vuelo encontrado: ID={flight_id}, Código={flight.code}")
        else:
            logger.warning(f"⚠️ Vuelo con ID={flight_id} no encontrado.")
        return flight
