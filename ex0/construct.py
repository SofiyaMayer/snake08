import os
import site
import sys


def show_global_environment() -> None:
    print(
        "MATRIX STATUS: You're still plugged in\n\n"
        f"Current Python: {sys.executable}\n"
        "Virtual Environment: None detected\n\n"
        "WARNING: You're in the global environment!\n"
        "The machines can see everything you install.\n\n"
        "Global package installation path:\n"
        f"{site.getsitepackages([sys.prefix])[0]}\n\n"
        "To enter the construct, run:\n"
        "python -m venv matrix_env\n"
        "source matrix_env/bin/activate # On Unix\n"
        "matrix_env\\Scripts\\activate # On Windows\n\n"
        "Then run this program again."
    )


def show_virtual_environment() -> None:
    print(
        "MATRIX STATUS: Welcome to the construct\n\n"
        f"Current Python: {sys.executable}\n"
        f"Virtual Environment: {os.path.basename(sys.prefix)}\n"
        f"Environment Path: {sys.prefix}\n\n"
        "SUCCESS: You're in an isolated environment!\n"
        "Safe to install packages without affecting\n"
        "the global system.\n\n"
        "Package installation path:\n"
        f"{site.getsitepackages([sys.prefix])[0]}\n\n"
        "Global package installation path:\n"
        f"{site.getsitepackages([sys.base_prefix])[0]}"
    )


if __name__ == "__main__":
    if sys.prefix == sys.base_prefix:
        show_global_environment()
    else:
        show_virtual_environment()
