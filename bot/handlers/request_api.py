import requests

from datetime import datetime

from config import config_db
from models.device_model import LogDevice


def get_history(url, device_id, offset=None, db=config_db.session):
    if offset is not None:
        log_data = f'?logTime={offset}'
        data = requests.get(url+log_data).json()
    else:
        data = requests.get(url).json()

    for values in data:
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


def convert_data(time):
    if time is not None:
        return datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
    else:
        return None
