class Config:
    SECRET_KEY = 'your_secret_key'
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/prod'

# Dictionary mapping environment types to configuration classes
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}