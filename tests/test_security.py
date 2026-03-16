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
        # Headers que Talisman 1.0.0 incluye
        self.assertIn("X-Frame-Options", resp.headers)
        self.assertEqual(resp.headers["X-Frame-Options"], "SAMEORIGIN")
        
        self.assertIn("X-Content-Type-Options", resp.headers)
        self.assertEqual(resp.headers["X-Content-Type-Options"], "nosniff")
        
        self.assertIn("X-XSS-Protection", resp.headers)
        self.assertEqual(resp.headers["X-XSS-Protection"], "1; mode=block")
        
        self.assertIn("Referrer-Policy", resp.headers)
        self.assertEqual(resp.headers["Referrer-Policy"], "strict-origin-when-cross-origin")

    def test_cors_headers(self):
        """It should return CORS headers"""
        resp = self.app.get("/")
        self.assertIn("Access-Control-Allow-Origin", resp.headers)
        # Por defecto, CORS permite todos los orígenes
        self.assertEqual(resp.headers["Access-Control-Allow-Origin"], "*")
