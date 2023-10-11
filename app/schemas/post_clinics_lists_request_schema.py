from pydantic import BaseModel
from typing import List

class ClinicSchema(BaseModel):
    ien: str
    name: str

class PostClinicsListsRequestSchema(BaseModel):
    name: str
    stationId: str
    role: str
    userDefault: bool
    clinics: List[ClinicSchema]
    

