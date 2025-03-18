import requests
import pytest

# Replace this URL with your actual Vercel deployment URL
BASE_URL = "https://flashcard-shubhamksawant.vercel.app"

def test_site_is_up():
    """Test if the site is up by checking headers"""
    try:
        response = requests.head(f"{BASE_URL}/")
        assert response.status_code in [200, 401]  # Accept either success or auth required
        print("\n✅ Site is up and responding!")
        
    except requests.RequestException as e:
        print(f"\n❌ Error accessing site: {e}")
        raise

if __name__ == '__main__':
    pytest.main(['-v', __file__]) 