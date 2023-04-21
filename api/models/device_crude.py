from config.config_db import get_db
from models.device_model import Device, UrlDevice, LogDevice, ErrorLogApi
from shemas import shemas_device

from sqlalchemy.orm import Session


# Сохранение имени устройства и его url
def create_device_and_url(db: Session, device: shemas_device.Device, url: shemas_device.UrlDevice):
    device = Device(name=device.name)
    db.add(device)
    db.commit()
    db.refresh(device)
    create_url_device(db, url, device)
    return device


# Сохранение url устройства
def create_url_device(db: Session, url: shemas_device.UrlDevice, device: Device):
    url = UrlDevice(url=url.url, device_id=device.id)
    db.add(url)
    db.commit()
    db.refresh(url)
    return device


def get_all(db: Session):
    device = db.query(Device)
    if device.scalar() is not None:
        return [{"id": i.id,
                 "name": i.name,
                 "company": i.company_id} for i in device.all()]
    else:
        return None


def get_current_logs_device(device: int, db: Session, offset: int, limit: int):
    device = db.query(LogDevice).filter(LogDevice.device_id == device) \
        .order_by(LogDevice.id.desc()).offset(offset).limit(limit)
    if device.scalar is not None:
        device_count = db.query(LogDevice).count()
        if device_count > 0:
            return [{"count": device_count, "data": i} for i in device.all()]
    else:
        return None


def create_eror_log(error, db: Session):
    if error['id_device'] == "":
        device = db.query(UrlDevice).filter(UrlDevice.device_id == error['id_device']).first()
        error = ErrorLogApi(
            datetime=error['date-time'],
            message=error['message'],
            devices=device.id if device is not None else error['id_device']
        )
        db.add(error)
        db.commit()
        db.refresh(error)
    return error
