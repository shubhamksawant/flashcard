import requests
import os
import pytest

# Get the base URL from environment variable or use a default
BASE_URL = os.getenv('BASE_URL', 'http://flashcard-seven-jade.vercel.app')

def test_homepage():
    """Test if homepage loads successfully"""
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert 'DevOps Flashcards' in response.text

def test_static_assets():
    """Test if static assets (CSS) are loading"""
    response = requests.get(f"{BASE_URL}/static/style.css")
    assert response.status_code == 200
    assert 'css' in response.headers.get('content-type', '')

def test_topics_available():
    """Test if topics are accessible"""
    topics = ['aws', 'kubernetes', 'docker']
    for topic in topics:
        response = requests.get(f"{BASE_URL}/topic/{topic}")
        assert response.status_code == 200
        assert topic.upper() in response.text

def test_api_endpoints():
    """Test if API endpoints are working"""
    response = requests.get(f"{BASE_URL}/api/questions/aws")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if len(data) > 0:
        assert 'question' in data[0]
        assert 'answer' in data[0]

def test_error_handling():
    """Test if error pages are handled properly"""
    response = requests.get(f"{BASE_URL}/nonexistent-page")
    assert response.status_code in [404, 302]

def test_flashcard_functionality():
    """Test if flashcard page loads with required elements"""
    response = requests.get(f"{BASE_URL}/topic/aws")
    assert response.status_code == 200
    assert 'flashcard' in response.text.lower()
    assert 'question' in response.text.lower()

def test_responsive_headers():
    """Test if security headers are present"""
    response = requests.head(BASE_URL)
    headers = response.headers
    assert 'content-type' in headers
    assert 'x-frame-options' in headers or 'content-security-policy' in headers

if __name__ == '__main__':
    pytest.main([__file__])