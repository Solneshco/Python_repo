import pytest
import uuid

class TestProjectsAPI:
    def test_create_project_positive(self, api_client, cleanup_project):
        project_name = f"Тестовый проект {uuid.uuid4().hex[:8]}"
        project_data = {
            "title": project_name,
            "description": "Описание тестового проекта",
            "companyId": "test_company"
        }
        
        response = api_client.create_project(project_data)
        
        assert "id" in response
        assert response["title"] == project_name
        assert response["description"] == project_data["description"]
        
        cleanup_project.append(response["id"])
    
    def test_get_project_positive(self, api_client, cleanup_project):
        project_name = f"Проект для получения {uuid.uuid4().hex[:8]}"
        create_data = {
            "title": project_name,
            "companyId": "test_company"
        }
        
        created_project = api_client.create_project(create_data)
        project_id = created_project["id"]
        cleanup_project.append(project_id)
        
        response = api_client.get_project(project_id)
        
        assert response["id"] == project_id
        assert response["title"] == project_name
    
    def test_update_project_positive(self, api_client, cleanup_project):
        project_name = f"Проект для обновления {uuid.uuid4().hex[:8]}"
        create_data = {
            "title": project_name,
            "companyId": "test_company"
        }
        
        created_project = api_client.create_project(create_data)
        project_id = created_project["id"]
        cleanup_project.append(project_id)
        
        update_data = {
            "title": f"Обновленный {project_name}",
            "description": "Новое описание"
        }
        
        response = api_client.update_project(project_id, update_data)
        
        assert response["id"] == project_id
        assert response["title"] == update_data["title"]
        assert response["description"] == update_data["description"]
    
    def test_create_project_negative_missing_required(self, api_client):
        invalid_data = {
            "description": "Только описание, без названия"
        }
        
        with pytest.raises(Exception) as exc_info:
            api_client.create_project(invalid_data)
        
        error_msg = str(exc_info.value).lower()
        assert "ошибка" in error_msg or "error" in error_msg
    
    def test_get_project_negative_not_found(self, api_client):
        non_existent_id = "non_existent_project_12345"
        
        with pytest.raises(Exception) as exc_info:
            api_client.get_project(non_existent_id)
        
        error_msg = str(exc_info.value)
        assert "404" in error_msg or "не найден" in error_msg.lower() or "not found" in error_msg.lower()
    
    def test_update_project_negative_invalid_data(self, api_client, cleanup_project):
        project_name = f"Проект для негативного теста {uuid.uuid4().hex[:8]}"
        create_data = {
            "title": project_name,
            "companyId": "test_company"
        }
        
        created_project = api_client.create_project(create_data)
        project_id = created_project["id"]
        cleanup_project.append(project_id)
        
        invalid_update = {
            "title": "",
            "description": "x" * 1000
        }
        
        with pytest.raises(Exception) as exc_info:
            api_client.update_project(project_id, invalid_update)
        
        error_msg = str(exc_info.value).lower()
        assert "ошибка" in error_msg or "error" in error_msg or "400" in error_msg
    
    def test_create_project_with_long_name(self, api_client, cleanup_project):
        long_name = "A" * 100
        project_data = {
            "title": long_name,
            "companyId": "test_company"
        }
        
        response = api_client.create_project(project_data)
        cleanup_project.append(response["id"])
        
        assert response["title"] == long_name
    
    @pytest.mark.parametrize("field,value", [
        ("title", "Простой проект"),
        ("description", "Детальное описание"),
        ("companyId", "different_company")
    ])
    def test_create_project_different_fields(self, api_client, cleanup_project, field, value):
        project_data = {
            "title": f"Параметризованный {uuid.uuid4().hex[:4]}",
            field: value
        }
        
        if field != "title":
            project_data["title"] = f"Проект с {field}"
        if field == "companyId":
            project_data["companyId"] = value
        
        response = api_client.create_project(project_data)
        cleanup_project.append(response["id"])
        
        assert field in response
        assert response[field] == value