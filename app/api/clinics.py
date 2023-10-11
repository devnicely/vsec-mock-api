import sqlite3
from app.models.clinics_list import ClinicsList
from app.schemas.clinics_list_response_schema import PostClinicsListResponseSchema
from app.schemas.post_clinics_lists_request_schema import PostClinicsListsRequestSchema
from app.schemas.clinic_response_schema import ClinicResponseSchema, ClinicAttributesSchema


def get_clinics_lists():
    with sqlite3.connect("db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM clinics_lists")
        data = cur.fetchall()

        payload = [
            ClinicsList(
                id=row["id"],
                userId=str(row["userId"]),
                name=row["name"],
                stationId=str(row["stationId"]),
                role=row["role"],
                userDefault=bool(int(row["userDefault"]))
            )
            for row in data
        ]
        
        response = PostClinicsListResponseSchema()
        response.success = True
        response.severity = "string"
        response.responseStatus = 200
        response.message = ""
        response.path = "string"
        response.payload = payload

        return response



def insert_clinics_list(request: PostClinicsListsRequestSchema):
    
    name = request.name
    stationId = request.stationId
    role = request.role
    userDefault = request.userDefault
    clinics = request.clinics

    with sqlite3.connect("db.sqlite3") as conn:
        cur = conn.cursor()
        sql = "INSERT INTO clinics_lists (userId, name, stationId, role, userDefault) VALUES (?, ?, ?, ?, ?)"
        cur.execute(sql, (1234, name, stationId, role, userDefault))
        
        inserted_id = cur.lastrowid
        
        for clinic in clinics:
            ien = clinic.ien
            clinic_name = clinic.name
            
            sql = "INSERT INTO clinics (ien, name, list_id) VALUES (?, ?, ?)"
            cur.execute(sql, (ien, clinic_name, inserted_id))
        
        conn.commit()
        
    response_payload = ClinicsList(
        id=inserted_id,
        userId=1234,
        name=name,
        stationId=int(stationId),
        role=role,
        userDefault=bool(userDefault)
    )
    
    response = PostClinicsListResponseSchema()
    response.success = True
    response.severity = "string"
    response.responseStatus = 200
    response.message = ""
    response.path = "string"
    response.payload = response_payload
    
    return response


def delete_clinics_list(listId: int):
    with sqlite3.connect("db.sqlite3") as conn:
        cursor = conn.cursor()
        sql = "DELETE FROM clinics_lists WHERE id = ?"
        cursor.execute(sql, (listId,))
        conn.commit()

        if cursor.rowcount > 0:
            response_message = f"Clinic List {listId} has been deleted."
        else:
            response_message = f"Failed to delete Clinic List {listId}."
        
    response = PostClinicsListResponseSchema()
    response.success = True
    response.severity = "string"
    response.responseStatus = 200
    response.message = response_message
    response.path = "string"
    response.payload = response_message
     
    return response
     
     
        

def get_vista_sites(stationNumber: int, duz: int):
    with sqlite3.connect("db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        sql = "SELECT * FROM clinics Where station_id = ?"
        cur.execute(sql, (stationNumber,))
        data = cur.fetchall()
    
    response = [
        ClinicResponseSchema(
            id=str(row["id"]),
            type="clinic",
            attributes=ClinicAttributesSchema(
                stationId=str(row["station_id"] if row["station_id"] else ''),
                resourceIen=str(row["resource_ien"] if row["resource_ien"] else ''),
                clinicIen=str(row["ien"]),
                name=row["name"]
            )
        )
        for row in data
    ]

    return data
