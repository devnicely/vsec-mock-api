from typing import List
from app.models.clinics_list import ClinicsList

class PostClinicsListResponseSchema():
    success: bool
    severity: str
    responseStatus: int
    message: str
    path: str
    payload: List[ClinicsList] | ClinicsList | str 