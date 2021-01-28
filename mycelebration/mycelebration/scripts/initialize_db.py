import argparse
import sys
from datetime import date

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from ..models.mymodel import (MyModel,User, Holiday)




def setup_models(dbsession):
    """
    Add or update models / fixtures in the database.

    """
    user = User(name='Mattias', email='asdfff@gg.com', password= '12334')
    holidays = [Holiday(name='Day Of Shikolays Death', date= date(2021,1,27), user=1),
                Holiday(name='Day Of Worst Shikolays Songs', date= date(2021,1,27), user=1),
                Holiday(name='Day Of Asphalt', date= date(2021,1,27), user=1),
                Holiday(name='International Concrete Day', date= date(2021,1,27), user=1),
                Holiday(name='Somebody-Once-Told-Me Day', date= date(2021,1,27), user=1),
                Holiday(name='The-World-Was-Gonna-Roll-Me Day', date= date(2021,1,28), user=1),
                Holiday(name='Day Of My Divorce', date= date(2021,1,28), user=1),
                Holiday(name='My Breakup Anniversary', date=date(2021, 1, 28), user=1),
                Holiday(name='Day Of Russian Doomer Music', date=date(2021, 1, 28), user=1),
                Holiday(name='My First Rehearsal', date=date(2021, 1, 29), user=1),
                Holiday(name='September Burns Out', date=date(2021, 1, 29), user=1),
                Holiday(name='Highly-Likely Day', date=date(2021, 1, 29), user=1),
                Holiday(name='Day Of Salad With Nails', date=date(2021, 1, 29), user=1),
                ]
    dbsession.add(user)
    for h in holidays:
        dbsession.add(h)


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config_uri',
        help='Configuration file, e.g., development.ini',
    )
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)

    try:
        with env['request'].tm:
            dbsession = env['request'].dbsession
            setup_models(dbsession)
    except OperationalError:
        print('''
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for description and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.
            ''')
