from typing import Any
from a import get_history
from config.config_api import app, get_db
from models.device_crude import create_device_and_url, get_all, create_log_device, get_all_logs_device
from shemas.shemas_device import Device, UrlDevice, LogDevice
from sqlalchemy.orm import Session

from config.config_db import Base, engine

from fastapi import Depends, HTTPException, status

Base.metadata.create_all(bind=engine)


@app.post("/create")
def create(device: Device, url: UrlDevice, db: Session = Depends(get_db)):
    return create_device_and_url(db, device, url)


@app.get("/all-url")
def get(db: Session = Depends(get_db)):
    return get_all(db)


@app.post("/create-log/{device_id}", status_code=status.HTTP_201_CREATED)
def create_device_logs(device_id: int, logs: list[LogDevice], db: Session = Depends(get_db)):
    try:
        for i in logs:
            create_log_device(db, i, device_id)
    except:
        return HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Ошибка получения")
    return {
        'status': 201,
        'data': {
            "msg": "Save"
        }
    }



@app.get("/all")
def get_all_logs(db: Session = Depends(get_db)):
    return get_all_logs_device(db)
