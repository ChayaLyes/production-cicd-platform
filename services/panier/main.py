from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Panier Service", version="1.0.0")
Instrumentator().instrument(app).expose(app)

panier = {}

@app.get("/health")
def health():
    return {"status": "healthy", "service": "panier"}

@app.post("/panier/{user_id}/add/{product_id}")
def add_to_cart(user_id: str, product_id: int, quantity: int = 1):
    if user_id not in panier:
        panier[user_id] = []
    panier[user_id].append({"product_id": product_id, "quantity": quantity})
    return {"message": "Produit ajouté", "panier": panier[user_id]}

@app.get("/panier/{user_id}")
def get_cart(user_id: str):
    return {"user_id": user_id, "panier": panier.get(user_id, [])}

@app.delete("/panier/{user_id}")
def clear_cart(user_id: str):
    panier[user_id] = []
    return {"message": "Panier vidé"}
