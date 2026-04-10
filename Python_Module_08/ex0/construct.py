import sys
import os
import site


def is_venv() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    python_path = sys.executable
    env_path = sys.prefix
    venv_name = os.path.basename(env_path)

    if is_venv():
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {python_path}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {env_path}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting\n"
              "the global system.\n")
        print("Package installation path:")

        for path in site.getsitepackages():
            if env_path in path and "site-packages" in path:
                print(path)
                break
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {python_path}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
