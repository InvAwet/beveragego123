from fastapi import FastAPI
import sqlite3

app = FastAPI()
conn = sqlite3.connect("orders.db")

@app.post("/orders")
def create_order(product: str, price: float):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders VALUES (NULL, ?, ?)", (product, price))
    conn.commit()
    return {"status": "Order created!"}

@app.get("/orders")
def get_orders():
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, product TEXT, price REAL)")
    return {"orders": cursor.execute("SELECT * FROM orders").fetchall()}
