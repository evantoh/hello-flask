class Config:#parent class that is used in configurations


    pass

class prodConfig(Config):# production configuration child class
    
    pass

class DevConfig(Config):# development configuration child class

    DEBUG = True #enables debug mode in our app
