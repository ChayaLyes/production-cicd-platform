from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import uuid

app = FastAPI(title="Paiement Service", version="1.0.0")
Instrumentator().instrument(app).expose(app)

paiements = {}

@app.get("/health")
def health():
    return {"status": "healthy", "service": "paiement"}

@app.post("/paiement")
def process_payment(user_id: str, amount: float):
    transaction_id = str(uuid.uuid4())
    paiements[transaction_id] = {
        "user_id": user_id,
        "amount": amount,
        "status": "success"
    }
    return {"transaction_id": transaction_id, "status": "success", "amount": amount}

@app.get("/paiement/{transaction_id}")
def get_payment(transaction_id: str):
    return paiements.get(transaction_id, {"error": "Transaction not found"})
