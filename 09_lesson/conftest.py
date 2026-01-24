import pytest
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Student
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def engine():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        db_url = "postgresql://myuser:mypassword@localhost:5432/mydatabase"
    
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture
def session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session
    
    session.rollback()
    session.close()

@pytest.fixture
def cleanup_data(session):
    created_ids = []
    
    yield created_ids
    
    for student_id in created_ids:
        student = session.query(Student).filter(Student.id == student_id).first()
        if student:
            session.delete(student)
    
    session.commit()