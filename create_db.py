from app import db, app
from app.models import User  # noqa: F401

with app.app_context():
    inspector = db.inspect(db.engine)
    if 'user' not in inspector.get_table_names():
        db.create_all()