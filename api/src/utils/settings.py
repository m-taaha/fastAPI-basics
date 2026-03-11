from pydantic_setting import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


    DB_CONNECTION = Settings()



