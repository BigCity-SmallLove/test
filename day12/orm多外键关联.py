# Author:Jacke

from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    billing_address_id = Column(Integer, ForeignKey("address.id")) #账单地址
    shipping_address_id = Column(Integer, ForeignKey("address.id")) #收货地址

    billing_address = relationship("Address")
    shipping_address = relationship("Address")


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))

#参数echo=True  会打印所有参数
engine = create_engine("mysql+pymysql://root:1234@192.168.0.103/lee",
                       encoding='utf-8')
Base.metadata.create_all(engine)  # 创建表结构