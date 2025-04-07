from datetime import datetime
from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.sticker import Sticker
from app.models.request import Request as RequestModel
from app.core.security import FAKE_ADMIN_TOKEN
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/admin/login")
def admin_login_form(request: Request):
    return templates.TemplateResponse("admin_login.html", {"request": request})


@router.post("/admin/login")
def admin_login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "admin":
        response = RedirectResponse(url="/admin/dashboard", status_code=302)
        response.set_cookie("admin_token", FAKE_ADMIN_TOKEN)
        return response
    return templates.TemplateResponse("admin_login.html", {"request": request, "error": "로그인 실패"})


@router.get("/admin/dashboard")
def admin_dashboard(request: Request, db: Session = Depends(get_db)):
    requests = db.query(RequestModel).order_by(
        RequestModel.date_created.desc()).all()
    stickers = db.query(Sticker).order_by(Sticker.date.desc()).all()
    return templates.TemplateResponse("admin_dashboard.html", {
        "request": request,
        "requests": requests,
        "stickers": stickers
    })


@router.get("/admin/requests/{request_id}/approve")
def approve_request(request_id: int, db: Session = Depends(get_db)):
    req = db.query(RequestModel).get(request_id)
    if req:
        req.approved = True
        db.commit()
    return RedirectResponse(url="/admin/dashboard", status_code=302)


@router.post("/admin/sticker")
def give_manual_sticker(
    date: str = Form(...),
    reason: str = Form(...),
    count: int = Form(...),
    db: Session = Depends(get_db)
):
    # 문자열로 받은 날짜를 date 객체로 변환
    try:
        parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return {"error": "날짜 형식이 올바르지 않습니다."}

    sticker = Sticker(
        date=parsed_date,
        reason=reason,
        count=count,
        source="admin"
    )
    db.add(sticker)
    db.commit()

    return RedirectResponse(url="/admin/dashboard", status_code=302)


@router.get("/admin/sticker/{sticker_id}/delete")
def delete_sticker(sticker_id: int, db: Session = Depends(get_db)):
    sticker = db.query(Sticker).get(sticker_id)
    if sticker:
        db.delete(sticker)
        db.commit()
    return RedirectResponse(url="/admin/dashboard", status_code=302)
