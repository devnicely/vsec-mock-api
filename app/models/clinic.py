from pydantic import BaseModel

class Clinic(BaseModel):
    id: int
    type: str
    stationId: int
    clinicIen: int
    name: str
    resourcId: int
    listId: int

    
