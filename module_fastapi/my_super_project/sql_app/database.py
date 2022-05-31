from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# sqlite3: By default, check_same_thread is True and only the creating thread may use the connection.
# If set False, the returned connection may be shared across multiple threads.
# When using multiple threads with the same connection writing operations should be serialized by the user
# to avoid data corruption.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
