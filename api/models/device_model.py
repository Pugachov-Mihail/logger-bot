from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from config.config_db import Base


class Device(Base):
    __tablename__ = "device"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    url_devices = relationship("UrlDevice", back_populates="devices")
    log_devices = relationship("LogDevice", back_populates="devices")


class UrlDevice(Base):
    __tablename__ = "url"

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    device_id = Column(Integer, ForeignKey("device.id"))

    devices = relationship("Device", back_populates="url_devices")


class LogDevice(Base):
    __tablename__ = "log_device"

    id = Column(Integer, primary_key=True)
    level = Column(String)
    category = Column(String)
    log_time = Column(String)
    prefix = Column(String)
    message = Column(String)

    device_id = Column(Integer, ForeignKey("device.id"))
    devices = relationship("Device", back_populates="log_devices")