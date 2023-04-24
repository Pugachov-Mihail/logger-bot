from pydantic import BaseModel


class UrlDevice(BaseModel):
    id: int
    url: str


class LogDevice(BaseModel):
    id: int
    level: str
    category: str
    log_time: str
    prefix: str
    message: str


class DeviceBase(BaseModel):
    id: int
    name: str


class Device(DeviceBase):
    url_devices: list[UrlDevice]
    log_devices: list[LogDevice]

    class Config:
        orm_mode = True


class ErrorLogApi(BaseModel):
    date_time: str
    message: str
    id_device: int
