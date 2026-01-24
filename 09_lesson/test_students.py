import pytest
from models import Student
import uuid
from datetime import datetime

class TestStudentCRUD:
    def test_add_student(self, session, cleanup_data):
        unique_email = f"student_{uuid.uuid4().hex[:8]}@test.com"
        
        new_student = Student(
            name="Иван Иванов",
            email=unique_email,
            age=20
        )
        
        session.add(new_student)
        session.commit()
        session.refresh(new_student)
        
        cleanup_data.append(new_student.id)
        
        student_from_db = session.query(Student).filter(Student.id == new_student.id).first()
        
        assert student_from_db is not None
        assert student_from_db.name == "Иван Иванов"
        assert student_from_db.email == unique_email
        assert student_from_db.age == 20
        assert student_from_db.is_active == True
    
    def test_update_student(self, session, cleanup_data):
        unique_email = f"student_{uuid.uuid4().hex[:8]}@test.com"
        
        new_student = Student(
            name="Петр Петров",
            email=unique_email,
            age=22
        )
        
        session.add(new_student)
        session.commit()
        session.refresh(new_student)
        
        cleanup_data.append(new_student.id)
        
        student_to_update = session.query(Student).filter(Student.id == new_student.id).first()
        
        student_to_update.name = "Петр Сидоров"
        student_to_update.age = 23
        session.commit()
        
        updated_student = session.query(Student).filter(Student.id == new_student.id).first()
        
        assert updated_student.name == "Петр Сидоров"
        assert updated_student.age == 23
        assert updated_student.email == unique_email
    
    def test_soft_delete_student(self, session, cleanup_data):
        unique_email = f"student_{uuid.uuid4().hex[:8]}@test.com"
        
        new_student = Student(
            name="Анна Смирнова",
            email=unique_email,
            age=21
        )
        
        session.add(new_student)
        session.commit()
        session.refresh(new_student)
        
        student_to_delete = session.query(Student).filter(Student.id == new_student.id).first()
        
        student_to_delete.is_active = False
        student_to_delete.deleted_at = datetime.now()
        session.commit()
        
        deleted_student = session.query(Student).filter(Student.id == new_student.id).first()
        
        assert deleted_student.is_active == False
        assert deleted_student.deleted_at is not None
    
    def test_hard_delete_student(self, session):
        unique_email = f"student_{uuid.uuid4().hex[:8]}@test.com"
        
        new_student = Student(
            name="Тест на удаление",
            email=unique_email,
            age=25
        )
        
        session.add(new_student)
        session.commit()
        session.refresh(new_student)
        
        student_id = new_student.id
        
        student_to_delete = session.query(Student).filter(Student.id == student_id).first()
        
        session.delete(student_to_delete)
        session.commit()
        
        deleted_student = session.query(Student).filter(Student.id == student_id).first()
        
        assert deleted_student is None
    
    def test_add_student_without_required_fields(self, session):
        invalid_student = Student(
            name="Без email"
        )
        
        session.add(invalid_student)
        
        with pytest.raises(Exception):
            session.commit()
        
        session.rollback()
        