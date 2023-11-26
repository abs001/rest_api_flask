from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 2000
            }
        ]
    }
]

@app.get("/store")

def get_store():
    return {"stores": stores}