from .device_model import Device, UrlDevice, LogDevice, User, ErrorLogApi, CounterErrorsLog
from config import config_db


# Сохранение имени устройства и его url
def create_device(name, user, db=config_db.session):
    user = db.query(User).filter(User.id_user == user).first()
    device = Device(name=name, user=user.id)
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


def find_end_log(device_id, db=config_db.session):
    logs = db.query(LogDevice).filter(LogDevice.device_id == device_id).order_by(LogDevice.id.desc())

    if logs.scalar is not None:
        log = logs.first()
        return log
    else:
        return None


def create_user(user_id, db=config_db.session):
    user = db.query(User).filter(User.id_user == user_id)
    if user.scalar() is None:
        user = User(id_user=user_id)
        db.add(user)
        db.commit()
        db.refresh(user)
    return user


def observe_db_query(db=config_db.session):
    counter = db.query(CounterErrorsLog).filter(CounterErrorsLog.status == False).all()
    return counter


def send_info(id, db=config_db.session):
    model = db.query(CounterErrorsLog).filter(CounterErrorsLog.id == id)
    if model.scalar is not None:
        model.update({CounterErrorsLog.status: True})
        db.commit()
        return True
    else:
        return False

