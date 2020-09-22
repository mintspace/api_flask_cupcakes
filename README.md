##JSON API

* GET /api/cupcakes
* GET /api/cupcakes/[cupcake-id]
* POST /api/cupcakes
* PATCH /api/cupcakes/[cupcake-id]
* DELETE /api/cupcakes/[cupcake-id]

![Rendering preferences pane](https://mintspace.github.io/api_flask_cupcakes/cupcake.png)

##Setup


###Clone directory:

	$ git clone https://github.com/mintspace/api_flask_cupcakes.git

###Create Python virtual environment:

	$ python -m venv venv
	$ source venv/bin/activate
	(venv) $ pip install -r requirements.txt

###Setup and seed database:

	(venv) $ createdb cupcakes
	(venv) $ python seed.py

###Start server:

	(venv) $ flask run

##Testing

	(venv) $ python -m unittest

##Built With

* [Axios](https://github.com/axios/axios)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
* [PostgresSQL](https://www.postgresql.org/)
* [Twitter Bootstrap](https://getbootstrap.com/)
