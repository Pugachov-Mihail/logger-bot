from .device_model import Device, UrlDevice, LogDevice
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
    device = db.query(Device).all()
    return [i for i in device if i.log_devices or i.url_devices]


# Сохранение логов
def create_log_device(db: Session, logs_shema: shemas_device.LogDevice, device: shemas_device.Device):
    logs = LogDevice(
        level=logs_shema.level,
        category=logs_shema.category,
        log_time=logs_shema.log_time,
        prefix=logs_shema.prefix,
        message=logs_shema.message,
        device_id=device)
    db.add(logs)
    db.commit()
    db.refresh(logs)
    return logs


def get_all_logs_device(db: Session):
    device = db.query(Device).all()
    return [i for i in device if i.log_devices]

