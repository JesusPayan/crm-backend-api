from bd_config import app,db
import os

# from app.routes import group_routes

# #app.register_blueprint(student_api)
# app.register_blueprint(group_routes)
if __name__ == "__main__":
    db.create_all()
    app.app_context().push()
    app.run(debug=True)