from config.config_api import app, get_db
from models import device_crude
from shemas import shemas_device

from sqlalchemy.orm import Session
from fastapi import Depends, Query, Request


@app.get("/get-current-device-log/{id}")
def get_all_logs(id: int,  pages: int = Query(default=0), limit: int = Query(ge=1, default=50), db: Session = Depends(get_db)):
    pages = pages if pages == 0 else pages * 50
    return device_crude.get_current_logs_device(id, db, pages, limit)


@app.get("/get-history-all")
def get_all_history(db: Session = Depends(get_db)):
    return device_crude.get_all(db)


@app.post("/set-error-api")
def set_error_api(error: shemas_device.ErrorLogApi, db: Session = Depends(get_db)):
    return device_crude.create_eror_log(error, db)


@app.get("/get-user")
def get_user(db: Session = Depends(get_db)):
    return device_crude.get_user(db)



# @app.post("/create")
# def create(device: Device, url: UrlDevice, db: Session = Depends(get_db)):
#     return create_device_and_url(db, device, url)
#
#
#
#
# @app.post("/create-log/{device_id}", status_code=status.HTTP_201_CREATED)
# def create_device_logs(device_id: int, logs: list[LogDevice], db: Session = Depends(get_db)):
#     try:
#         for i in logs:
#             create_log_device(db, i, device_id)
#     except:
#         return HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Ошибка получения")
#     return {
#         'status': 201,
#         'data': {
#             "msg": "Save"
#         }
#     }
