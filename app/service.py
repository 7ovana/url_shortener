from fastapi.responses import JSONResponse
import sqlite3 as sql
import secrets


def _generate_short_url():
    return secrets.token_urlsafe(8)


def get_db_url_by_key(conn: sql.dbapi2.Connection, url_key: str) -> str:
    c = conn.cursor()
    c.execute(
        f"""
        SELECT * FROM url_map WHERE short_url = "{url_key}"
        """
    )
    row = c.fetchone()
    c.close()
    return row


def _find_db_url(conn: sql.dbapi2.Connection, target_url: str):
    c = conn.cursor()
    c.execute(
        f"""
        SELECT * FROM url_map WHERE target_url = "{target_url}"
        """
    )
    row = c.fetchone()
    c.close()
    return row


def get_unique_short_url(conn: sql.dbapi2.Connection, target_url: str):
    row = _find_db_url(conn=conn, target_url=target_url)
    if row:
        return row["short_url"]

    key = _generate_short_url()
    while get_db_url_by_key(conn, url_key=key):
        key = _generate_short_url()

    return key


def add_url_to_db(conn: sql.dbapi2.Connection, target_url: str, short_url: str):
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO url_map (target_url, short_url) VALUES (?, ?)",
            (target_url, short_url),
        )
        conn.commit()
    except sql.IntegrityError:
        return (
            JSONResponse(
                content={"error": "Short URL already exists!"},
            ),
            500,
        )
    finally:
        c.close()
