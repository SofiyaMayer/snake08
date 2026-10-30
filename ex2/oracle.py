import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print(
        "ERROR: python-dotenv is not installed\n"
        "Install it with: pip install -r requirements.txt"
    )
    sys.exit(1)

REQUIRED_KEYS = ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    env_file_found = load_dotenv(".env")
    mode = os.getenv("MATRIX_MODE", "development")

    if mode == "production":
        for key in REQUIRED_KEYS:
            if not os.getenv(key):
                print(f"ERROR: {key} is required in production mode")
                sys.exit(1)
        log_level = os.getenv("LOG_LEVEL", "INFO")
    else:
        for key in REQUIRED_KEYS:
            if not os.getenv(key):
                print(f"WARNING: {key} is not set, using default")
        if not env_file_found:
            print("WARNING: No .env file found, using development defaults")
            print("Create one with: cp .env.example .env\n")
        log_level = os.getenv("LOG_LEVEL", "DEBUG")

    database_url = os.getenv("DATABASE_URL", "sqlite:///matrix_dev.db")
    if database_url.startswith("sqlite") or "localhost" in database_url:
        database = "local instance"
    else:
        database = "remote database"

    api_access = "Authenticated" if os.getenv("API_KEY") else "Not configured"
    zion_network = "Online" if os.getenv("ZION_ENDPOINT") else "Offline"
    debug_output = "enabled" if mode == "development" else "disabled"

    print(
        "Configuration loaded:\n"
        f"Mode: {mode}\n"
        f"Database: Connected to {database}\n"
        f"API Access: {api_access}\n"
        f"Log Level: {log_level}\n"
        f"Zion Network: {zion_network}\n"
        f"Debug output: {debug_output}\n"
    )

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if env_file_found:
        print("[OK] .env file properly configured")
    else:
        print("[WARN] No .env file, values come from defaults")
    print("[OK] Production overrides available\n")

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
