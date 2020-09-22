from flask import Flask, request, render_template, redirect, flash, session, jsonify
from models import db, connect_db, Cupcake


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = "SECRET!"

connect_db(app)
db.create_all()


@app.route('/')
def index_page():
	""" Renders html template """

	cakes = Cupcake.query.all()
	return render_template('index.html', cakes=cakes)


@app.route('/api/cupcakes')
def cupcakes_list():
	"""
	Get data about all cupcakes
	Respond with JSON like: {cupcakes: [{id, flavor, size, rating, image}, ...]}.
	"""

	cupcakes = [cake.serialize() for cake in Cupcake.query.all()]
	return jsonify(cupcakes=cupcakes)


@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
	"""
	Get data about a single cupcake
	Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}.
	This should raise a 404 if the cupcake cannot be found.
	"""

	cupcake = Cupcake.query.get_or_404(id)
	return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=["POST"])
def add_cupcake():
	"""
	Create a cupcake with flavor, size, rating and image data from the body of the request.
	Respond with JSON like: {cupcake: {id, flavor, size, rating, image}}.
	"""
	flavor=request.json["flavor"]
	size=request.json["size"]
	rating=request.json["rating"]
	image=request.json["image"]

	new_cupcake = Cupcake(flavor=flavor,
						size=size,
						rating=rating,
						image=image)
	db.session.add(new_cupcake)
	db.session.commit()
	response_json = jsonify(cupcake=new_cupcake.serialize())

	return (response_json, 201)

@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcakes(id):
	"""
	Update a cupcake with the id passed in the URL and flavor, size,
	rating and image data from the body of the request.
	You can always assume that the entire cupcake object will be
	passed to the backend.
	This should raise a 404 if the cupcake cannot be found.

	Respond with JSON of the newly-updated cupcake, like this:
	{cupcake: {id, flavor, size, rating, image}}.
	"""

	cupcake = Cupcake.query.get_or_404(id)

	cupcake.flavor = request.json.get('flavor', cupcake.flavor)
	cupcake.size = request.json.get('size', cupcake.size)
	cupcake.rating = request.json.get('rating', cupcake.rating)
	cupcake.image = request.json.get('image', cupcake.image)

	db.session.commit()

	return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcakes(id):
	"""
	This should raise a 404 if the cupcake cannot be found.
	Delete cupcake with the id passed in the URL.
	Respond with JSON like {message: "Deleted"}.
	"""
	cupcake = Cupcake.query.get_or_404(id)

	db.session.delete(cupcake)
	db.session.commit()

	return jsonify(message="deleted")
