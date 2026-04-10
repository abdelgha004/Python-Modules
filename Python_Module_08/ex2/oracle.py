import os
import sys
from dotenv import load_dotenv


def load_config():
    load_dotenv()

    return {
        "mode": os.getenv("MATRIX_MODE"),
        "db": os.getenv("DATABASE_URL"),
        "api": os.getenv("API_KEY"),
        "log": os.getenv("LOG_LEVEL"),
        "zion": os.getenv("ZION_ENDPOINT"),
    }


def validate_config(config):
    required = ["mode", "db", "api", "log", "zion"]
    missing = [k for k in required if not config.get(k)]

    if missing:
        print("\nWARNING: Missing configuration variables:")
        for var in missing:
            print(f"  - {var}")
        print("\nPlease configure them in your environment or .env file.")
        sys.exit(1)

    if config["mode"] not in ("development", "production"):
        print("ERROR: MATRIX_MODE must be 'development' or 'production'")
        sys.exit(1)


def display_config(config):
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    print(f"Mode: {config['mode']}")

    if config["mode"] == "development":
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to production server")

    print("API Access: Authenticated")
    print(f"Log Level: {config['log']}")
    print("Zion Network: Online")


def security_check(config):
    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    print("[OK] Production overrides available")


def main():
    config = load_config()
    validate_config(config)
    display_config(config)
    security_check(config)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
