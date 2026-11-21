from functools import lru_cache
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL



class Settings(BaseSettings):
    postgres_user: str
    postgres_db: str
    postgres_host: str
    postgres_port: int
    postgres_password: SecretStr
    algorithm: str = "HS256"
    refresh_token_expire_days: int = 30
    access_token_expire_minutes: int = 15
    environment: str = "dev"
    secret_key: SecretStr

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    @property
    def database_url(self) -> URL:
        url_object = URL.create(
            drivername="postgresql+psycopg",
            username=self.postgres_user,
            password=self.postgres_password.get_secret_value(),
            host=self.postgres_host,
            port=self.postgres_port,
            database=self.postgres_db
        )
        return url_object

@lru_cache
def get_settings() -> Settings:
    return Settings()