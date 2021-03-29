from sqlalchemy import create_engine

DATABASE_PATH="sqlite+pysqlite:///database/data/courses.db"

engine = create_engine(DATABASE_PATH, echo=True, future=True)
  