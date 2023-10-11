from pydantic import BaseModel

class ClinicAttributesSchema(BaseModel):
    stationId: str
    resourceIen: str
    clinicIen: str
    name: str

class ClinicResponseSchema(BaseModel):
    id: str
    type: str
    attributes: ClinicAttributesSchema