from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
	db.app = app
	db.init_app(app)


DEFAULT_IMAGE = 'https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg'

class Cupcake(db.Model):
	__tablename__ = 'cupcakes'

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	flavor = db.Column(db.String(50), nullable=False)
	size = db.Column(db.String(50), nullable=False)
	rating = db.Column(db.Float, nullable=False)
	image = db.Column(db.String(1000), nullable=False, default=DEFAULT_IMAGE)

	def serialize(self):
		""" turn into JSON """
		return {
				'id': self.id,
				'flavor': self.flavor,
				'size': self.size,
				'rating': self.rating,
				'image': self.image
			}

