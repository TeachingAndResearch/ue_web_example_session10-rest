#TODO: Faire les bons imports

import json

app = Flask(__name__)

PORT = 5000
HOST = '0.0.0.0'

# Chargement de la "Base de donnes en format JSON"
with open('{}/databases/movies.json'.format("."), 'r') as jsf:
    movies = json.load(jsf)
    print(movies)

# TODO: traiter les requetes: GET /json

# TODO: traiter les requetes: GET /movies/<movieid>

# TODO: traiter les requetes: GET /moviesbytitle

# TODO: traiter les requetes: POST /movies/<movieid>

# TODO: traiter les requetes: PUT /movies/<movieid>/<rate>

# TODO: traiter les requetes: DELETE /movies/<movieid>

if __name__ == "__main__":
    print("Server running in port %s"%(PORT))
    app.run(host=HOST, port=PORT)
