__author__ = 'Sadi'

from app import db, models


# student = models.Student(nickname='Sadi', email='joh@email.com')

# student = [models.Student(nickname='Sadi', email='joh@email.com'),
#            models.Student(nickname='Azad', email='jo@email.com'),
#            models.Student(nickname='Saiful', email='ohn@email.com')]

# db.session.add_all(student)
# db.session.commit()

# our_user = models.Student.query.all()
# for students in our_user:
#     print  students.nickname+ ' ' + students.email

# our_user = models.Student.query.get(1)
# print our_user

# our_user = models.Student.query.all()
# print our_user
# p = models.Address(house = 51/1, area= 'Manikdi Bazar', user= our_user)
# # db.session.add(p)
# # db.session.commit()

our_user = models.Student.query.get(3)
addresses= our_user.addresses.all()




for a in addresses:
    print a.area+' '+ a.user.nickname
# p = models.Address(house = 51/1, area= 'Manikdi Bazar', user= our_user)
# db.session.add(p)
# db.session.commit()


# u = models.User(nickname='susan', email='susan@email.com')
# # db.session.add(u)
# # db.session.commit()
# u = models.User.query.get(1)
# print u
#
import datetime
# u = models.User.query.get(1)
# posts = u.posts.get(1)
# print  posts.body
# p = models.Post(body='my first post!', timestamp=datetime.datetime.utcnow(), author=u)
# db.session.add(p)
# db.session.commit()