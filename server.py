from flask_app.templates.__init__ import app
from flask_app.controllers import usuarios, peliculas

if __name__ == "__main__":
    app.run(debug=True, port=5000)
