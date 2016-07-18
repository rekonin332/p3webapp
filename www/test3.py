import www.orm
import asyncio
import sys
from www.models import User, Blog, Comment

# def test(loop):
#     yield from www.orm.create_pool(user='root', password='password', database='awesome',loop=loop)
#
#     u = User(name='victoria', email='457855140@qq.com', passwd='1234567890', image='about:blank')
#
#     yield from u.save()
#
@asyncio.coroutine
def test(loop):
    yield from www.orm.create_pool(loop=loop, host='localhost', port=3306, user='root', password='123456', db='awesome')
    u = User(name='test85',email='test85@test.com',passwd='test',image='about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)



# import orm
# from models import User, Blog, Comment
#
# def test():
#     yield from orm.create_pool(user='root', password='123456', database='awesome')
#
#     u = User(name='Test#', email='test#@example.com', passwd='1234567890', image='about:blank')
#
#     yield from u.save()
#
# for x in test():
#     pass