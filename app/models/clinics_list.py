from pydantic import BaseModel
from typing import List

class ClinicsList(BaseModel):
    id: int
    userId: int
    name: str
    stationId: int
    role: str
    userDefault: bool
    
