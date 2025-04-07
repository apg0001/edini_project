from app.models.request import Request
from app.schemas.request import RequestCreate
from sqlalchemy.orm import Session

def create_request(db: Session, request_data: RequestCreate):
    request = Request(message=request_data.message)
    db.add(request)
    db.commit()
    db.refresh(request)
    return request

def get_all_requests(db: Session):
    return db.query(Request).all()

def approve_request(db: Session, request_id: int):
    request = db.query(Request).get(request_id)
    if not request:
        return {"error": "Request not found"}
    request.approved = True
    db.commit()
    return request