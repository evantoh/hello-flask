class Config:#parent class that is used in configurations
     MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    

    pass

class prodConfig(Config):# production configuration child class
    
    pass

class DevConfig(Config):# development configuration child class

    DEBUG = True #enables debug mode in our app
