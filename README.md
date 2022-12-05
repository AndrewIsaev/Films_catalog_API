
### Authentication ###

**POST request /auth/register/** - register user is system

Exapmle: 

    { 
        "email": "email@email",
        "password": "password"
    }
**POST request /auth/login/** - log user in system

Exapmle: 

    { 
        "email": "email@email",
        "password": "password"
    }
**PUT request /auth/login/** - update tokens

Exapmle: 

    { 
        "refresh_token": "agha;lkghjas;gh"
    }

### Users ###

**GET request /user/** - get user 

**PATCH request /user/** - update users info (name, surname, favorite genre)

Example: 

    { 
        "name": "Petr",
        "surname": "Petrov"
        "favorite_genre": 1
    }
**PUT request /user/** - update users password

Example: 

    { 
        "email": "emeil@email",
        "password_1": "qwerty"
        "password_2": "qwerty2"
    }

### Favorites ###


**POST request /favorites/movies/<int:movie_id>** - add movie to users favorites

Example: 

    { 
        "user_id": "1",
        "movie_id": "1"
    }

**DELETE request /favorites/movies/<int:movie_id>** - route to delete movie from users favorites

### Movies ###

**GET request /movies/** - get all movies (params - status, page)

**GET request /movies/<int:movie_id>** - get one movie

### Directors ###

**GET request /directors/** - route to get all directors (params - page)

**GET request /directors/<int:director_id>** - get one director

### Genres ###

**GET request /genres/** - get all genres (params - page)

**GET request /genres/<int:genre_id>** - get one genre