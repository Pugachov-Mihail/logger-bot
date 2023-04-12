from pydantic import BaseModel


class UrlDevice(BaseModel):
    id: int | None = None
    url: str | None = None


class LogDevice(BaseModel):
    id: int | None = None
    level: str | None = None
    category: str | None = None
    log_time: str | None = None
    prefix: str | None = None
    message: str | None = None


class DeviceBase(BaseModel):
    id: int | None = None
    name: str | None = None


class Device(DeviceBase):
    url_devices: list[UrlDevice] | None = []
    log_devices: list[LogDevice] | None = []

    class Config:
        orm_mode = True

