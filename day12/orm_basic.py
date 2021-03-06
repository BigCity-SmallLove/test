# Author:Jacke



# sql语句
# CREATE TABLE user (
#     id INTEGER NOT NULL AUTO_INCREMENT,
#     name VARCHAR(32),
#     password VARCHAR(64),
#     PRIMARY KEY (id)
# )
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

#参数echo=True  会打印所有参数
engine = create_engine("mysql+pymysql://root:1234@192.168.0.103/yi",
                       encoding='utf-8', echo=True)

Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


Base.metadata.create_all(engine)  # 创建表结构

#开始添加数据
Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

user_obj = User(name="alex", password="alex3714")  # 生成你要创建的数据对象
user_obj2 = User(name="yi", password="yi15")  # 生成你要创建的数据对象
print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None

Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
Session.add(user_obj2)  # 把要创建的数据对象添加到这个session里， 一会统一创建
print(user_obj.name, user_obj.id)  # 此时也依然还没创建

#Session.commit()  # 现此才统一提交，创建数据
