import os
import threading
import time

from flask import Flask
from app.main import bp as main_bp
from app.nodes import bp as node_bp
from app.devices import bp as devices_bp
from app.data import bp as data_bp

from . import db
from .mesh import mesh_master


def worker():
    print("yes")
    while True:
        time.sleep(1)
        print("counter")


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(node_bp)
    app.register_blueprint(data_bp)
    app.register_blueprint(devices_bp)

    #threading.Thread(target=mesh_master, daemon=True).start()

    return app
