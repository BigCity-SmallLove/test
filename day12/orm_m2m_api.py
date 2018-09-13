# Author:Jacke

from day12 import orm_m2m
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_m2m.engine)
session=Session_class()

#插入数据
# b1 = orm_m2m.Book(name='learn java with yi',pub_date='2014-05-02')
# b2 = orm_m2m.Book(name='learn qwe with yi',pub_date='2015-05-12')
# b3 = orm_m2m.Book(name='learn zhuangx with yi',pub_date='2015-11-02')
b3 = orm_m2m.Book(name='插入中文',pub_date='2015-11-02')


#
# a1 = orm_m2m.Author(name='yi')
# a2 = orm_m2m.Author(name='lee')
# a3 = orm_m2m.Author(name='hua')
#
# b1.authors = [a1,a2]
# b3.authors = [a1,a2,a3]
#
# session.add_all([a1,a2,a3,b1,b2,b3])
session.add_all([b3,])

#查询数据
# author_obj= session.query(orm_m2m.Author).filter(orm_m2m.Author.name=='yi').first()
# print(author_obj.books[1].pub_date)
# book_obj = session.query(orm_m2m.Book).filter(orm_m2m.Book.id==2).first()
# print(book_obj.authors)


session.commit()
