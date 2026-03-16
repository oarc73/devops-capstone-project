"""
Security Test Cases

Tests that security headers and CORS are properly configured
"""
import unittest
from service import app


class TestSecurity(unittest.TestCase):
    """Test Security Features"""

    def setUp(self):
        """Runs before each test"""
        self.app = app.test_client()

    def test_security_headers(self):
        """It should return security headers"""
        resp = self.app.get("/")
        # Headers estándar que Talisman siempre incluye
        self.assertIn("X-Frame-Options", resp.headers)
        self.assertEqual(resp.headers["X-Frame-Options"], "SAMEORIGIN")
        
        self.assertIn("X-Content-Type-Options", resp.headers)
        self.assertEqual(resp.headers["X-Content-Type-Options"], "nosniff")
        
        # X-XSS-Protection ya no está presente en versiones modernas de Talisman
        # En su lugar, verificamos otros headers modernos
        self.assertIn("Permissions-Policy", resp.headers)
        self.assertIn("Referrer-Policy", resp.headers)

    def test_cors_headers(self):
        """It should return CORS headers"""
        resp = self.app.get("/")
        self.assertIn("Access-Control-Allow-Origin", resp.headers)
        # Por defecto, CORS permite todos los orígenes
        self.assertEqual(resp.headers["Access-Control-Allow-Origin"], "*")
