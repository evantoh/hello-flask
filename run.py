from app import app

# app.run() method to launch our server. We pass in the debug = Trueargument 
# to allow us to run on debug mode so that we can easily track errors in our 
# application.
if __name__=='__main__':
    app.run()#remove debug=true because debug mode has been enabled in configuration file