import os
import uvicorn
import psycopg2

from fastapi import FastAPI, Body

app = FastAPI()


def get_db():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT"),
    )
    return conn


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/message")
def create_message(message: dict = Body(...)):
    text = message.get("message")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO messages (text) VALUES (%s)", (text,))
    conn.commit()

    cursor.close()
    conn.close()

    return {"status": "ok", "message": text}


@app.get("/message")
def get_messages(page: int = 1, limit: int = 10):
    conn = get_db()
    cursor = conn.cursor()
    offset = (page - 1) * limit

    cursor.execute(
        "SELECT text FROM messages ORDER BY id DESC LIMIT %s OFFSET %s",
        (limit, offset),
    )
    messages = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT COUNT(*) FROM messages")
    total_count = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return {
        "messages": messages,
        "page": page,
        "limit": limit,
        "total": total_count,
        "pages": (total_count + limit - 1) // limit
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
