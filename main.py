from bd_config import app,db
import os


from app.routes.microserviceClient.clientsApi import clients_api  # ✅ importa el Blueprint, no el módulo

app.register_blueprint(clients_api, url_prefix="/v1/clients")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, use_reloader=False)