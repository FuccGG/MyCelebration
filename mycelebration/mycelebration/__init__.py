from pyramid.config import Configurator
from mycelebration.models.mymodel import User, Holiday

def sacrud_settings(config):
    config.include('pyramid_sacrud', route_prefix='admin')
    config.registry.settings['pyramid_sacrud.models'] = (
        ('Сelebration', [User, Holiday]),
        ('Group', [User])
    )

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_jinja2')
        config.include('.routes')
        # config.include('ps_alchemy')
        config.include(sacrud_settings)
        config.include('.models')
        config.scan()
    return config.make_wsgi_app()




