from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Catalogue Service", version="1.0.0")
Instrumentator().instrument(app).expose(app)

products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "stock": 50},
    {"id": 2, "name": "Phone", "price": 499.99, "stock": 100},
    {"id": 3, "name": "Tablet", "price": 299.99, "stock": 75},
]

@app.get("/health")
def health():
    return {"status": "healthy", "service": "catalogue"}

@app.get("/products")
def get_products():
    return {"products": products}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return {"error": "Product not found"}
    return product
