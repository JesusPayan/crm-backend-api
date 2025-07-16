from app import app, db
from app.routes.microserviceClient.clientsApi import clients_api
from app.routes.microserviceProducts.productsApi import products_api
import os

app.register_blueprint(clients_api, url_prefix="/v1/clients")
app.register_blueprint(products_api, url_prefix="/v1/products")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, use_reloader=False, port=5000)