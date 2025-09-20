import os
from dotenv import load_dotenv
load_dotenv()

def main():
    print("open_api_key:", os.getenv("open_api_key"))
    print("Hello from complete-mcp-server-mastery-with-langchain-and-ollama!")


if __name__ == "__main__":
    main()
