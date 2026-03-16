"""
Package: service
Package for the application models and service routes
This module creates and configures the Flask app and sets up the logging
and SQL database
"""
import sys
from flask import Flask
from service import config
from service.common import log_handlers
from .database import db, init_db
from flask_talisman import Talisman
from flask_cors import CORS

# Create Flask application
app = Flask(__name__)
app.config.from_object(config)

# Configurar Talisman para headers de seguridad
talisman = Talisman(
    app,
    force_https=False,  # Deshabilitar HTTPS forzado para desarrollo
    content_security_policy=None,  # Deshabilitar CSP para simplificar
)

# Configurar CORS
CORS(app)

# Inicializar base de datos (esto SOLO se ejecuta una vez)
init_db(app)

# Import the routes After the Flask app is created
# pylint: disable=wrong-import-position, cyclic-import, wrong-import-order
from service import routes, models  # noqa: F401 E402

# pylint: disable=wrong-import-position
from service.common import error_handlers, cli_commands  # noqa: F401 E402

# Set up logging for production
log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  A C C O U N T   S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")
app.logger.info("Service initialized!")
