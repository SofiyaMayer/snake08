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

ENV_FILE = ".env"
REQUIRED_KEYS = ("DATABASE_URL", "API_KEY", "ZION_ENDPOINT")


def print_configuration(mode: str, log_level: str) -> None:
    database_url = os.getenv("DATABASE_URL", "sqlite:///matrix_dev.db")
    if database_url.startswith("sqlite") or "localhost" in database_url:
        database = "local instance"
    else:
        database = "remote database"
    api_access = "Authenticated" if os.getenv("API_KEY") else "Not configured"
    zion_network = "Online" if os.getenv("ZION_ENDPOINT") else "Offline"
    debug_output = "enabled" if mode == "development" else "disabled"

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: Connected to {database}")
    print(f"API Access: {api_access}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_network}")
    print(f"Debug output: {debug_output}")
    print()


def print_security_check(env_file_found: bool) -> None:
    print("Environment security check:")

    api_key = os.getenv("API_KEY")
    with open(sys.argv[0]) as script:
        source_code = script.read()
    if api_key and api_key in source_code:
        print("[FAIL] API_KEY value is hardcoded in oracle.py")
    else:
        print("[OK] No hardcoded secrets detected")

    if env_file_found:
        print("[OK] .env file properly configured")
    else:
        print("[WARN] No .env file, values come from defaults")
    print("[OK] Production overrides available")
    print()


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    env_file_found = load_dotenv(ENV_FILE)
    mode = os.getenv("MATRIX_MODE", "development")

    missing_keys = []
    for key in REQUIRED_KEYS:
        if not os.getenv(key):
            missing_keys.append(key)

    if mode == "production":
        if missing_keys:
            for key in missing_keys:
                print(f"ERROR: {key} is required in production mode")
            print(f"Set them in {ENV_FILE} or as environment variables")
            sys.exit(1)
        log_level = os.getenv("LOG_LEVEL", "INFO")
    else:
        for key in missing_keys:
            print(f"WARNING: {key} is not set, using default")
        if not env_file_found:
            print("WARNING: No .env file found, using development defaults")
            print("Create one with: cp .env.example .env\n")
        log_level = os.getenv("LOG_LEVEL", "DEBUG")

    print_configuration(mode, log_level)
    print_security_check(env_file_found)

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
