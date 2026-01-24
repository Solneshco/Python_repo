# conftest.py
import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def api_client():
    from tests.api_client import YougileAPIClient
    
    token = os.getenv("YOUGILE_API_TOKEN")
    base_url = os.getenv("YOUGILE_BASE_URL", "https://yougile.com/api-v2")
    
    if not token:
        pytest.skip("YOUGILE_API_TOKEN не установлен")
    
    return YougileAPIClient(base_url=base_url, api_token=token)

@pytest.fixture
def cleanup_project(api_client):
    created_projects = []
    
    yield created_projects
    
    for project_id in created_projects:
        try:
            api_client.delete_project(project_id)
        except Exception:
            pass