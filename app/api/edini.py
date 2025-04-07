from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from app.database import get_db
from app.models.request import Request as RequestModel
from app.models.sticker import Sticker
from sqlalchemy import extract, func
from fastapi.responses import JSONResponse
import datetime

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/")
def edini_home(request: Request):
    return templates.TemplateResponse("edini_home.html", {"request": request})


@router.get("/edini/calendar")
def edini_calendar(request: Request):
    return templates.TemplateResponse("edini_calendar.html", {"request": request})


@router.get("/edini/request")
def edini_request_form(request: Request):
    return templates.TemplateResponse("edini_request.html", {"request": request})


@router.post("/edini/request")
def submit_request(request: Request, message: str = Form(...), db: Session = Depends(get_db)):
    new_request = RequestModel(message=message)
    db.add(new_request)
    db.commit()
    return RedirectResponse(url="/", status_code=302)


@router.get("/edini/statistics")
def edini_statistics(request: Request):
    return templates.TemplateResponse("edini_statistics.html", {"request": request})


@router.get("/api/statistics")
def get_statistics(db: Session = Depends(get_db)):
    now = datetime.datetime.now()

    # 월별 스티커 수
    month_data = (
        db.query(extract("month", Sticker.date).label(
            "month"), func.sum(Sticker.count))
        .group_by("month")
        .all()
    )
    result = {f"{int(month)}월": count for month, count in month_data}

    # 이번 달, 이번 주 계산
    start_of_month = now.replace(day=1)
    start_of_week = now - datetime.timedelta(days=now.weekday())

    monthly_total = (
        db.query(func.sum(Sticker.count))
        .filter(Sticker.date >= start_of_month)
        .scalar() or 0
    )
    weekly_total = (
        db.query(func.sum(Sticker.count))
        .filter(Sticker.date >= start_of_week)
        .scalar() or 0
    )

    return JSONResponse({
        "monthly_chart": result,
        "this_month": monthly_total,
        "this_week": weekly_total
    })


@router.get("/api/stickers")
def get_all_stickers(db: Session = Depends(get_db)):
    stickers = db.query(Sticker).all()
    return [
        {
            "date": s.date.strftime("%Y-%m-%d"),
            "reason": s.reason,
            "count": s.count,
            "source": s.source
        }
        for s in stickers
    ]


@router.get("/api/sticker-summary")
def get_sticker_summary(db: Session = Depends(get_db)):
    from sqlalchemy import func

    total = db.query(func.sum(Sticker.count)).scalar() or 0

    if total >= 50:
        badge = "🥇 골드"
    elif total >= 30:
        badge = "🥈 실버"
    elif total >= 10:
        badge = "🥉 브론즈"
    else:
        badge = "🌱 새싹"

    return {"total": total, "badge": badge}
