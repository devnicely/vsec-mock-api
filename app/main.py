from fastapi import FastAPI
from app.api import clinics
from app.schemas.post_clinics_lists_request_schema import PostClinicsListsRequestSchema


app = FastAPI()

@app.get("/api/ClinicsLists")
def get_clinics_lists():
    return clinics.get_clinics_lists()


@app.post("/api/ClinicsLists")
def insert_clinics_list(request: PostClinicsListsRequestSchema):
    return clinics.insert_clinics_list(request)


@app.delete("/api/ClinicsLists/{listId}")
def delete_clinics_list(listId: int):
    return clinics.delete_clinics_list(listId)
    
    
@app.get("/api/clinics/vista-sites/{stationNumber}/users/{duz}")
def get_vista_sites(stationNumber: int, duz: int):
    return clinics.get_vista_sites(stationNumber, duz)