from app import create_app
from config import config
app = create_app()

hostEnv = config.HOST
portEnv = config.PORT
debugFlag = config.DEBUG


if __name__ == '__main__':
    app = create_app().run(host=hostEnv, port=portEnv, debug=True)
