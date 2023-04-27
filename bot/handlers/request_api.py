import requests

from datetime import datetime

from config import config_db
from models.device_model import LogDevice, Device


def get_history(url, device_id, offset=None, db=config_db.session):
    if offset is not None:
        try:
           log_data = f'?logTime={offset}'
           data = requests.get(url + log_data).json()
        except Exception:
            raise Exception("Тут упал")
    else:
        try:
            data = requests.get(url).json()
            edit_url_device(device_id, data['id_device'])
        except Exception:
            raise Exception("Бред")

    for values in data['message']:
        logs = LogDevice(
            level=values['level'],
            category=values['category'],
            log_time=values['log_time'],
            prefix=values['prefix'],
            message=values['message'],
            device_id=device_id,
            data_time_log=convert_data(values['log_time'])
        )
        db.add(logs)

    db.commit()
    return True


def edit_url_device(id, company_id, db=config_db.session):
    device = db.query(Device).filter(Device.id == id)
    if device.scalar is not None and id is not None:
        device.update({
            Device.company_id: company_id
        })
        # db.add(urls)
        db.commit()
        return True
    else:
        return False


def convert_data(time):
    if time is not None:
        return datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
    else:
        return None

