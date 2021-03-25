from flask import Flask, session, request
from src.config import config
from .util.logger import logger as sys_logger
from .models import db
def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config.Config')
    db.init_app(app)
    db.app = app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    logger = sys_logger.get_network_logger
    @app.after_request
    def after_request(response):
        if session.get('root_uid'):
            session.pop('root_uid')
        if session.get('logged_in'):
            session.pop('logged_in')
        response.headers.add('Access-Control-Allow-origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
        logger.info('host: {0}, url: {1}, remote_addr: {2}, referrer: {3}, body: {4}, status: {5}'.format(
            request.headers['host'],
            request.url,
            request.remote_addr,
            request.referrer,
            request.get_data(),
            response.status_code
        ))
        return response

    with app.app_context():
        db.create_all()
        return app