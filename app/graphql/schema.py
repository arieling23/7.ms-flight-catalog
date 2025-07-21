import strawberry
from typing import List, Optional  
from strawberry.types import Info
from datetime import datetime

from app.db import get_session
from app.services.flight_service import FlightService
from app.graphql.types import FlightType
from app.auth.dependencies import get_current_user
from app.models.flight import Flight

@strawberry.type
class Query:
    @strawberry.field
    async def get_flights(self, info: Info) -> List[FlightType]:
        session = info.context["session"]
        return await FlightService.get_all(session)

    @strawberry.field
    async def flight(self, info: Info, id: int) -> Optional[FlightType]:  
        session = info.context["session"]
        return await FlightService.get_by_id(session, id)

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_flight(
        self,
        info: Info,
        code: str,
        origin: str,
        destination: str,
        departure_time: datetime
    ) -> FlightType:
        user = get_current_user(info.context["request"])
        if user["role"] != "admin":
            raise Exception("Access denied")

        session = info.context["session"]
        return await FlightService.create(session, code, origin, destination, departure_time)


schema = strawberry.Schema(query=Query, mutation=Mutation)
