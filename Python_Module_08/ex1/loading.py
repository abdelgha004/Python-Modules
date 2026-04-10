import sys
import importlib
from typing import Dict
from types import ModuleType


def check_dependencies() -> Dict[str, ModuleType]:
    required = ["pandas", "numpy", "matplotlib"]
    modules: Dict[str, ModuleType] = {}

    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")

    for package in required:
        try:
            module = importlib.import_module(package)
            modules[package] = module

            msg = {
                "pandas": "Data manipulation ready",
                "numpy": "Numerical computation ready",
                "matplotlib": "Visualization ready",
            }
            print(f"[OK] {package} ({module.__version__}) - {msg[package]}")

        except ImportError:
            if package in required:
                print(f"[MISSING] {package} - REQUIRED")
            else:
                print(f"[OPTIONAL] {package} not installed")

    for pkg in required:
        if pkg not in modules:
            print("\nInstall dependencies with:")
            print("pip install -r requirements.txt")
            print("or")
            print("poetry install")
            sys.exit(1)

    return modules


def main() -> None:
    modules = check_dependencies()

    pd = modules["pandas"]
    np = modules["numpy"]
    plt = importlib.import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    data = pd.DataFrame({"matrix_code": np.random.randn(1000)})

    print("Generating visualization...")

    plt.plot(data["matrix_code"])
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
