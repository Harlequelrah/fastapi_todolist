import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()
project_name = os.getenv("PROJECT_NAME")
if __name__ == "__main__":
    uvicorn.run(
        f"{project_name}.__main__:app", host="127.0.0.1", port=8000, reload=True
    )