import sys
import os
import pytest

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Import your Flask app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Secure Flask App!" in response.data
