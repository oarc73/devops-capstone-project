"""
Test CLI Commands
"""
import os
from unittest import TestCase
from unittest.mock import patch, MagicMock
from click.testing import CliRunner
from service import app
from service.common.cli_commands import db_create


class TestCLICommands(TestCase):
    """Test CLI Commands"""

    def setUp(self):
        self.runner = CliRunner()
        app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///:memory:'
        app.config["TESTING"] = True

    def test_db_create(self):
        """It should call the db-create command"""
        with app.app_context():
            result = self.runner.invoke(db_create, [])
            self.assertEqual(result.exit_code, 0, f"Command failed with output: {result.output}")