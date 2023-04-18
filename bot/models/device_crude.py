from .device_model import Device, UrlDevice, LogDevice
from shemas import shemas_device
from bot.config import config_db


# Сохранение имени устройства и его url
def create_device(name):
    device = Device(name=name)
    config_db.get_db(device)
    return device


# Сохранение url устройства
def create_url_device(url, device):
    url = UrlDevice(url=url, device_id=device.id)
    config_db.get_db(url)
    return device


def get_all(db=config_db.session):
    device = db.query(Device).all()
    return [i for i in device if i.log_devices or i.url_devices]


# Сохранение логов
def create_log_device(logs_shema: shemas_device.LogDevice, device: shemas_device.Device):
    logs = LogDevice(
        level=logs_shema.level,
        category=logs_shema.category,
        log_time=logs_shema.log_time,
        prefix=logs_shema.prefix,
        message=logs_shema.message,
        device_id=device)
    config_db.get_db(logs)
    return logs


def get_all_logs_device(db=config_db.session):
    device = db.query(Device).all()
    return [i for i in device if i.log_devices]


def get_current_device(name, db=config_db.session):
    return db.query(Device).filter(Device.name == name).first()
