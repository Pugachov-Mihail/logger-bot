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


def create_url_error(device, url_error):
    if url_error is not None:
        url = UrlDevice(
            url=url_error,
            error_flag=1,
            device_id=device.id
        )
        config_db.get_db(url)
        return True
    else:
        return False


def get_all(db=config_db.session):
    device = db.query(Device).all()
    return [i for i in device if i.log_devices or i.url_devices]


def get_all_logs_device(db=config_db.session):
    device = db.query(Device).all()
    return [i for i in device if i.log_devices]


def get_current_device(name, db=config_db.session):
    if name != "":
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


def find_logs_url(name, db=config_db.session):
    device = db.query(UrlDevice).join(Device).filter(Device.name == name)
    if device.scalar is not None:
        device_url = device.first()
        return device_url
    else:
        return None


def find_end_log(name, db=config_db.session):
    logs = db.query(LogDevice).filter(LogDevice.device_id == name).order_by(LogDevice.id.desc())

    if logs.scalar is not None:
        log = logs.first()
        return log
    else:
        return None



