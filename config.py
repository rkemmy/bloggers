class Config:
    SECRET_KEY = 'amsecret'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://remmy:bxt@localhost/bloggin'





config_options = {
  "production":ProdConfig,
  "default":DevConfig
}
