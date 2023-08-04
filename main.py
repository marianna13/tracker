from fastapi import FastAPI, status, HTTPException
from database import Base, engine
from pydantic import BaseModel
from sqlalchemy.orm import Session
from models import Item


class ItemRequest(BaseModel):
    id: str
    status: str


# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()


@app.get("/")
def root():
    return "works"


@app.get("/items/{id}")
def read_item(id: str):

    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the item item with the given id
    item = session.query(Item).get(id)

    # close the session
    session.close()

    return f"item item with id: {item.id} and status: {item.status}"


@app.put("/item/{id}")
def update_item(id: str, status: str):

    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the item item with the given id
    item = session.query(Item).get(id)

    # update item item with the given task (if an item with the given id was found)
    if item:
        item.status = status
        session.commit()

    # close the session
    session.close()

    # check if item item with given id exists. If not, raise exception and return 404 not found response
    if not item:
        raise HTTPException(
            status_code=404, detail=f"item with id {id} not found")

    return item


@app.delete("/item/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(id: str):

    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the item item with the given id
    item = session.query(Item).get(id)

    # if item item with given id exists, delete it from the database. Otherwise raise 404 error
    if item:
        session.delete(item)
        session.commit()
        session.close()
    else:
        raise HTTPException(
            status_code=404, detail=f"item with id {id} not found")

    return None


@app.get("/items")
def read_item_list():
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get all item items
    item_list = session.query(Item).all()

    # close the session
    session.close()

    return item_list


@app.post("/item", status_code=status.HTTP_201_CREATED)
def create_item(item: ItemRequest):

    session = Session(bind=engine, expire_on_commit=False)

    # create an instance of the item database model
    itemdb = Item(status=item.status, id=item.id)

    session.add(itemdb)
    session.commit()
    id = itemdb.id

    session.close()

    return f"created item with id {id}"
