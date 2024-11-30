import os
import pytest
from django.urls import reverse
from django.test import Client

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

@pytest.mark.django_db
def test_homepage():
    client = Client()
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200
    assert "Hello" in response.content.decode()
    
@pytest.mark.django_db
def test_polls_index_page():
    client = Client()
    url = reverse('polls_index')
    response = client.get(url)
    assert response.status_code == 200
    assert "polls" in response.content.decode()