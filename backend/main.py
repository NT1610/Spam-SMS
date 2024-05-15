from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from main import main
import uvicorn
from fastapi.staticfiles import StaticFiles

import os
from dotenv import load_dotenv
load_dotenv()
PATH2 = os.getenv("OUTPUT_PATH2")

app = FastAPI()

# Thêm middleware để cho phép truy cập từ tên miền khác
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    input_comment: str
    input_option: float
