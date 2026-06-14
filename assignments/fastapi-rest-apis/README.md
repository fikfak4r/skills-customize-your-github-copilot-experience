# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a RESTful API using the FastAPI framework, define request and response models with Pydantic, and expose endpoints for creating, retrieving, and filtering data.

## 📝 Tasks

### 🛠️ Create a FastAPI app and root endpoint

#### Description
Create a FastAPI application and add a root endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Create a `FastAPI` application instance.
- Add a `GET /` endpoint that returns a JSON welcome message.
- Ensure the app can start with `uvicorn`.

### 🛠️ Define a Pydantic model and POST endpoint

#### Description
Define an `Item` model using Pydantic and add an endpoint to create new items in an in-memory list.

#### Requirements
Completed program should:

- Define an `Item` Pydantic model with fields `id`, `name`, `description`, `price`, and `available`.
- Add a `POST /items/` endpoint that accepts an `Item` and stores it in a list.
- Return the created item as JSON.

### 🛠️ Read items with path and query parameters

#### Description
Add endpoints for retrieving a single item by ID and filtering items by availability.

#### Requirements
Completed program should:

- Add a `GET /items/{item_id}` endpoint that returns the item with the specified ID.
- Add a `GET /items/` endpoint that uses an optional query parameter to filter available items.
- Return a clear error or empty result if no matching item is found.

### 🛠️ Run and test the API locally

#### Description
Run the FastAPI app locally and test the endpoints using the browser, HTTP client, or `curl`.

#### Requirements
Completed program should:

- Start the application with `uvicorn main:app --reload` (or similar).
- Respond with JSON for each endpoint.
- Demonstrate successful requests for creating items and fetching them.
