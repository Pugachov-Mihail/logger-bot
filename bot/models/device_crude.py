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
    return url.id


def create_url_error(device, url_error, db=config_db.session):
    if url_error is not None:
        api = db.query(UrlDevice).filter(UrlDevice.device_id == device.id)
        if api.scalar() is not None:
            api.update({
                UrlDevice.error_flag: 1,
                UrlDevice.url: url_error
            })
            db.commit()
            return True
    else:
        return False


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
    if name == "":
        devices = db.query(Device).join(UrlDevice).filter(Device.name == name)
        if devices.scalar is not None:
            device = devices.first()
            return [i for i in device.url_devices]
        else:
            return []
    else:
        return []


def edit_url_device(name, url, id, db=config_db.session):
    device = db.query(Device).filter(Device.name == name).first()
    if device is not None and id is not None:
        urls = db.query(UrlDevice).filter(UrlDevice.id == id, UrlDevice.device_id == device.id)
        if url is not None and urls.scalar() is not None:
            urls.update({
                UrlDevice.url: url
            })
            # db.add(urls)
            db.commit()
            return True
        else:
            return False
    else:
        return False

