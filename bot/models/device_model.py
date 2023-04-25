from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from config.config_db import Base


class Device(Base):
    __tablename__ = "device"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    company_id = Column(Integer)

    user = Column(Integer, ForeignKey("user.id"))
    url_devices = relationship("UrlDevice", back_populates="devices")
    user_id = relationship("User", back_populates="device_id")
    log_devices = relationship("LogDevice", back_populates="devices")
    error_log_devices = relationship("ErrorLogApi", back_populates="devices")


class UrlDevice(Base):
    """error_flag отвечает за получение только ошибок 0 получает все, 1 только error и warrning"""
    __tablename__ = "url"

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    error_flag = Column(Integer, default=0)
    device_id = Column(Integer, ForeignKey("device.id"))

    devices = relationship("Device", back_populates="url_devices")


class LogDevice(Base):
    __tablename__ = "log_device"

    id = Column(Integer, primary_key=True)
    level = Column(String)
    category = Column(String)
    log_time = Column(String)
    data_time_log = Column(String)
    prefix = Column(String)
    message = Column(String)

    device_id = Column(Integer, ForeignKey("device.id"))
    devices = relationship("Device", back_populates="log_devices")


class ErrorLogApi(Base):
    __tablename__ = "error_log_api"

    id = Column(Integer, primary_key=True)
    datetime = Column(String)
    message = Column(String)

    url_error = Column(Integer, ForeignKey("device.id"))
    devices = relationship("Device", back_populates="error_log_devices")
    counter = relationship("CounterErrorsLog", back_populates="error_log")


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer)

    device_id = relationship("Device", back_populates="user_id")


class CounterErrorsLog(Base):
    __tablename__ = "counter_error_log"

    id = Column(Integer, primary_key=True)
    status = Column(Boolean, default=False)

    message_id = Column(Integer, ForeignKey("error_log_api.id"))
    error_log = relationship("ErrorLogApi", back_populates="counter")
