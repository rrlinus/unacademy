from flask import jsonify
from . import main


@main.app_errorhandler(405)
def method_not_allowed(e):
    message = {
        'status': 405,
        'message': "Method not allowed please use post request"
    }

    resp = jsonify(message)
    resp.status_code = 405
    return resp


@main.app_errorhandler(404)
def page_not_found(e):
    message = {
        'status': 404,
        'message': "Page not found please enter the correct url"
    }
    print(message)
    resp = jsonify(message)
    resp.status_code = 404
    return resp


@main.app_errorhandler(500)
def internal_server_error(e):
    message = {
        'status': 500,
        'message': "something went wrong"
    }
    resp = jsonify(message)
    resp.status_code = 500
    return resp


@main.app_errorhandler(401)
def not_authorized(e):

    message = {
        'status': 401,
        'message': '''
                     request has not been applied because it lacks valid
                     authentication credentials for the target resource
                    '''
    }
    resp = jsonify(message)
    resp.status_code = 401
    return resp
