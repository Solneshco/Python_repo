# api_client.py
import requests
import json
from typing import Dict, Any

class YougileAPIClient:
    def __init__(self, base_url: str, api_token: str):
        self.base_url = base_url.rstrip('/')
        self.api_token = api_token
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def _handle_response(self, response: requests.Response):
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            error_msg = f"HTTP ошибка: {e}"
            try:
                error_data = response.json()
                error_msg = f"{error_msg}. Ответ API: {error_data}"
            except:
                error_msg = f"{error_msg}. Текст ответа: {response.text}"
            raise Exception(error_msg)
        except json.JSONDecodeError:
            return {"text": response.text, "status_code": response.status_code}
    
    def create_project(self, project_data: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base_url}/projects"
        response = self.session.post(url, json=project_data)
        return self._handle_response(response)
    
    def get_project(self, project_id: str) -> Dict[str, Any]:
        url = f"{self.base_url}/projects/{project_id}"
        response = self.session.get(url)
        return self._handle_response(response)
    
    def update_project(self, project_id: str, update_data: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base_url}/projects/{project_id}"
        response = self.session.put(url, json=update_data)
        return self._handle_response(response)
    
    def delete_project(self, project_id: str) -> Dict[str, Any]:
        url = f"{self.base_url}/projects/{project_id}"
        response = self.session.delete(url)
        return self._handle_response(response)