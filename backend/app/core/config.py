import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class CommonConfig(BaseSettings):
    SECRET_KEY: str = os.environ.get('SECRET_KEY')
    DEBUG: str = os.environ.get('DEBUG')
    ALLOWED_HOSTS: list = ['*']


class AwsS3Config(BaseSettings):
    S3_ACCESS_KEY: str = os.environ.get('S3_ACCESS_KEY')
    S3_SECRET_ACCESS_KEY: str = os.environ.get('S3_SECRET_ACCESS_KEY')
    S3_BUCKET_NAME: str = os.environ.get('S3_BUCKET_NAME')
    S3_REGION_NAME: str = os.environ.get('S3_REGION_NAME')


class DbConfig(BaseSettings):
    DATABASE_ENGINE: str = os.environ.get('DATABASE_ENGINE')
    POSTGRES_DB: str = os.environ.get('POSTGRES_DB')
    POSTGRES_USER: str = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD')
    # For docker, DB_HOST should be set to the service name defined in your docker-compose.yml
    DB_HOST: str = os.environ.get('DB_HOST')
    DB_PORT: str = os.environ.get('PORT')


class CoreConfig(
    CommonConfig,
    AwsS3Config,
    DbConfig,
):
    model_config = SettingsConfigDict(case_sensitive=True)


config = CoreConfig()
