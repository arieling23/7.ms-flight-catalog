import strawberry
from datetime import datetime

@strawberry.type
class FlightType:
    id: int
    code: str
    origin: str
    destination: str
    departure_time: datetime
