from app import db
from app.models import User, City, Forecast

def populate_db():
    if not User.query.first():
        u1 = User(user_ref='Chan', name="Chan", email='zcesclc@ucl.co.uk', password='pwpw1')
        u2 = User(user_ref='Choi', name="Choi", email="zcesclc1@ucl.co.uk", password="pwpw2")
        u3 = User(user_ref='Lin', name="Lin", email="zcesclc2@ucl.co.uk", password="pwpw3")

        c1 = City(name='London')
        c2 = City(name='Macau')
        c3 = City(name='Paris')

        f1 = Forecast(datetime='datetime', comment='Sunny', user_id=1, city_id=1)
        f2 = Forecast(datetime='datetime', comment='Rain', user_id=2, city_id=2)
        f3 = Forecast(datetime='datetime', comment='Storm', user_id=3, city_id=3)

        db.session.add_all([u1, u2, u3])
        db.session.add_all([c1, c2, c3])
        db.session.add_all([f1, f2, f3])


        c1.forecasts.append(f1)



        db.session.commit()
