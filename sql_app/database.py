from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 接続先DBの設定
SQLALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.db'

# Engine の作成
engine = create_engine(
  SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread' : False}
)
Base = declarative_base()

# Session の作成
SessionLocal = sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=engine)
