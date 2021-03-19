from pydantic import BaseSettings


class Settings(BaseSettings):
    '''
    .env config
    '''
    predict_db_host: str = "0.0.0.0"
    predict_db: str = "dbname"
    predict_db_user: str = "db_user"
    predict_db_password: str = "***"
    path_log_predict: str = "/path/to/log"
    rotation: str = "5 Mb"
    retention: int = 7
    compression: str = "gz"
    log_format: str = (
        "<level>{level: <8}</level>"
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> - "
        "<cyan>Source:{name}</cyan> - Fonction: <cyan>{function}</cyan> - "
        "<cyan>ligne: {line}</cyan> - "
        "<level>Message: {message}</level>"
        )

    class Config:
        env_file = ".env"
