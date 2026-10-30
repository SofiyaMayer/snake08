import importlib

PACKAGES = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization",
}
OUTPUT_FILE = "matrix_analysis.png"


def check_dependencies() -> list[str]:
    print("Checking dependencies:")
    missing = []
    for name, purpose in PACKAGES.items():
        try:
            version = importlib.import_module(name).__version__
            print(f"[OK] {name} ({version}) - {purpose} ready")
        except ImportError:
            print(f"[KO] {name} - {purpose} missing")
            missing.append(name)
    return missing


def show_pip_vs_poetry() -> None:
    print(
        "\npip vs Poetry:\n"
        "pip:    deps in requirements.txt, you create the venv yourself,\n"
        "        versions are pinned only if you run pip freeze\n"
        "Poetry: deps in pyproject.toml, creates the venv for you,\n"
        "        pins exact versions in poetry.lock automatically\n"
    )


def show_install_instructions() -> None:
    print(
        "LOADING FAILED: missing programs.\n\n"
        "Install them with pip:\n"
        "python3 -m venv matrix_env\n"
        "source matrix_env/bin/activate\n"
        "pip install -r requirements.txt\n\n"
        "Or with Poetry:\n"
        "poetry install\n"
        "poetry run python loading.py"
    )


def analyze_matrix_data() -> None:
    import numpy as np
    import pandas as pd
    from matplotlib import pyplot as plt

    print("Analyzing Matrix data...")
    signal = np.random.default_rng(42).normal(50, 10, 1000)
    data = pd.DataFrame({"signal": signal})
    data["trend"] = data["signal"].rolling(50).mean()
    print(f"Processing {len(data)} data points...")

    print("Generating visualization...")
    data.plot(title="Matrix signal")
    try:
        plt.savefig(OUTPUT_FILE)
    except OSError as error:
        print(f"LOADING FAILED: cannot save {OUTPUT_FILE} ({error})")
        return
    print(f"\nAnalysis complete!\nResults saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...\n")
    missing = check_dependencies()
    show_pip_vs_poetry()
    if missing:
        show_install_instructions()
    else:
        analyze_matrix_data()
