class Config(object):
    DEBUG = False
    TESTING = False
    #google 
    PROJET_ID = "vegetablegrow"
    #IOT google configuration
    IOT_REGION = "europe-west1"
    REGISTER_ID = "gardenSensor"

class ProductionConfig(Config):
    SECRET_KEY = b'{_M}?O0)$V+<@I-;0GK~TroHqACf9x'
    #ENV = "production"

class DevelopmentConfig(Config):
    SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'
    #ENV = "development"
    DEBUG = True
    GOOGLE_JSON = "/Users/delporte/dev/project/Vegetablegrow/VegetableGrow-2256a0cc9140.json"

