from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
import validators
from .database import initialize_db, get_db_connection
from . import schemas
from .service import (
    get_db_url_by_key,
    get_unique_short_url,
    add_url_to_db,
)


app = FastAPI()

initialize_db()


@app.get("/")
def read_root():
    return "Welcome :)"


@app.post("/url", response_model=schemas.URLInfo)
def create_short_url(url: schemas.URLBase):
    if not validators.url(url.target_url):
        raise HTTPException(status_code=400, detail="The URL you provided is invalid.")

    conn = get_db_connection()

    short_url = get_unique_short_url(conn=conn, target_url=url.target_url)
    add_url_to_db(conn, url.target_url, short_url)

    return JSONResponse(content={"short_url": short_url})


@app.get("/{short_url}")
def redirect_to_target_url(short_url: str):
    conn = get_db_connection()
    row = get_db_url_by_key(conn=conn, url_key=short_url)
    conn.close()

    if row is None:
        raise HTTPException(
            status_code=404, detail="The url doesn't exist, cannot redirect."
        )

    return RedirectResponse(url=row["target_url"])


if __name__ == "__main__":
    app.run(debug=True)
