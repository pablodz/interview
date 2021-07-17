import os

# Constants
HOST_WEB = os.environ.get("HOST_WEB")
PORT_WEB = os.environ.get("PORT_WEB")
API_URL = f"http://{HOST_WEB}:{PORT_WEB}"
DATABASE_DEFAULT = "api_dev_db"
COLLECTION_DEFAULT = "dogs"
MONGO_URI = ""#"mongodb://interview:interview@localhost:27017/api_dev_db"
LIMIT_QUERY = 5
