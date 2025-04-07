from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.database import Base, engine
from app.api import admin, edini

Base.metadata.create_all(bind=engine)

app = FastAPI(title="에디니의 칭찬일기")

# 라우터 등록
app.include_router(admin.router)
app.include_router(edini.router)

# 정적 파일 및 템플릿 설정
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
