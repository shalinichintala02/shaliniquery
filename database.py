# from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker, declarative_base
from psycopg2 import connect
# ==============================
# DATABASE CONFIG (HARDCODED)
# ==============================

# DB_HOST = "dev-lms-server.postgres.database.azure.com"
# DB_PORT = 5432
# DB_NAME = "lms_Db"
# DB_USER = "lmsadmin@dev-lms-server"
# DB_PASSWORD = "Lorem@784109"


conn = psycopg2.connect(
    host="dev-lms-server.postgres.database.azure.com",
    user="lmsadmin",
    password="Lorem@784109",
    dbname="lms_db",
    port="5432"
)

# DATABASE_URL = (
#     f"postgresql://{DB_USER}:{DB_PASSWORD}"
#     f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
#     "?sslmode=require"
# )

# # ==============================
# # SQLALCHEMY SETUP
# # ==============================

# engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# Base = declarative_base()

