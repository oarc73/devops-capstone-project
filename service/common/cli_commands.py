"""
CLI Commands Module

This module contains the CLI commands for the application.
"""
import click
from flask import current_app
from flask.cli import with_appcontext
from service.database import db, init_db


@click.command("db-create")
@with_appcontext
def db_create():
    """Creates the database tables"""
    current_app.logger.info("Creating database tables...")
    
    try:
        # Inicializar la base de datos
        init_db(current_app)
        
        # Crear todas las tablas
        with current_app.app_context():
            db.create_all()
            db.session.commit()
        
        current_app.logger.info("Database tables created successfully")
        return 0
    except Exception as e:
        current_app.logger.error(f"Error creating database tables: {e}")
        return 1