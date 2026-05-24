from fastapi import APIRouter, Depends, HTTPException
from ..database import get_db
from ..schemas import ProductCreate, ProductUpdate
import sqlite3

router = APIRouter()

def is_exists(id: int, db):
    product = db.execute("SELECT * FROM products WHERE id=?", (id, )).fetchone()
    if not product:
        raise HTTPException(404, "Product not found")
    return product

@router.post("/products/create")
def create_product(product: ProductCreate, db=Depends(get_db)):
    cur = db.execute("INSERT INTO products (name, description, price) VALUES (?, ?, ?)",
                     (product.name, product.description, product.price))

    db.commit()
    return {"status": "ok", "id": cur.lastrowid}

@router.delete("/products/{id}")
def delete_product(id: int, db=Depends(get_db)):
    is_exists(id, db)

    cur = db.execute("DELETE FROM products WHERE id=?", (id,))
    db.commit()
    return {"status": "ok", "deleted_id": id}

@router.get("/products")
def get_products(db=Depends(get_db)):
    return db.execute("SELECT * FROM products").fetchall()

@router.get("/products/{id}")
def get_product(id: int, db=Depends(get_db)):
    product = is_exists(id, db)
    return product

@router.put("/products/{id}")
def update_product(id: int, product: ProductUpdate, db=Depends(get_db)):
    is_exists(id, db)

    updated = product.model_dump(exclude_unset=True)
    fields = [f"{k} = ?" for k in updated.keys()]
    values = list(updated.values()) + [id]
    query = f"UPDATE products SET {', '.join(fields)} WHERE id = ?"
    db.execute(query, values)
    db.commit()
