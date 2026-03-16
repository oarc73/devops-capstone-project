"""
Database module for the application
"""
from flask_sqlalchemy import SQLAlchemy

# Create the SQLAlchemy object (no se inicializa con app todavía)
db = SQLAlchemy()

# Variable para rastrear si ya se inicializó
_initialized = False


def init_db(app):
    """Initialize database with app (solo una vez)"""
    global _initialized
    if not _initialized:
        app.logger.info("Initializing database for the first time")
        db.init_app(app)
        with app.app_context():
            db.create_all()
            app.logger.info("Database tables created")
        _initialized = True
        app.logger.info("Database initialized successfully")
    else:
        app.logger.info("Database already initialized, skipping")
