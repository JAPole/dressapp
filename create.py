from application import db
from application.models import outfit, # change this Users

db.drop_all()
db.create_all()
