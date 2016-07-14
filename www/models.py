#!/usr/bin/python3
# -*- encoding:utf-8 -*-

from orm import StringField, FloatField, BooleanField, Model, IntegerField, TextField
import time, uuid, orm
import asyncio


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(Model):
    __table__ = 'users'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    name = StringField(ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    admin = BooleanField()
    image = StringField(ddl='varchar(500)')
    passwd = StringField(ddl='varchar(50)')
    created_at = FloatField(default=time.time)


class Blog(Model):
    __table__ = 'blogs'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)


class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)


async def test(loop):
    await orm.create_pool(ploop=loop, user='root', password='123456', db='awesome')
    u = User(name='test7', email='test7@test.com', passwd='test', image='about:blank')
    await u.save()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [test(loop)]
    loop.run_until_complete(asyncio.wait(tasks))
    # u = User(name='test7', email='test7@test.com', passwd='test', image='about:blank')
    print('here')
