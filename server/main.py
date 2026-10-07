import mysql.connector
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_connection():
    return mysql.connector.connect(
        database=os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_ROOT_PASSWORD"),
        port=3306,
        host=os.getenv("MYSQL_HOST"),
    )


@app.get("/users")
async def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("select * from utilisateur")
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)
    cursor.close()
    conn.close()
    return {"total": len(records), "utilisateurs": records}


@app.get("/health")
async def health():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    cursor.fetchall()
    cursor.close()
    conn.close()
    return {"status": "ok"}