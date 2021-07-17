import os

# Constants
HOST_WEB = os.environ.get("HOST_WEB")
PORT_WEB = os.environ.get("PORT_WEB")
API_URL = f"http://{HOST_WEB}:{PORT_WEB}"
LIMIT_QUERY = 5
