from pyramid.view import view_config
from pyramid.response import Response
from datetime import date
import transaction
from jinja2 import Template
from dateutil.parser import parse
from pyramid.httpexceptions import HTTPFound

from ..models.mymodel import Holiday

from sqlalchemy.exc import DBAPIError

from ..forms import HolidayForm

from .. import models



@view_config(route_name='home', renderer='../templates/index.jinja2')
def my_view(request):
    try:
        holidays = request.dbsession.query(models.mymodel.Holiday)
        today = holidays.filter(models.mymodel.Holiday.date == date.today())

        if request.POST:
            create_holiday(request)
            url = request.route_url('home')
            return HTTPFound(location=url)

    except DBAPIError:
        return Response(db_err_msg, content_type='text/plain', status=500)
    return {'project': 'MyCelebration', 'holidays': today, 'current_date': date.today()}

def create_holiday(request):
    if isinstance(request.params['date'], str):
        holiday = Holiday(name=request.params['name'])
        request.dbsession.add(holiday)
    else:
        holiday = Holiday(name=request.params['name'],
        date=parse(request.params['date']))
        request.dbsession.add(holiday)
    transaction.commit()



db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for descriptions and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
