import sys
import importlib


def check_dependencies():
    required_packages = ["pandas", "numpy", "requests", "matplotlib"]
    imported_modules = {}
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    for package in required_packages:
        try:
            module = importlib.import_module(package)
            imported_modules[package] = module

            if package == "pandas":
                print(f"[OK] {package} ({module.__version__}) - Data manipulation ready")
            elif package == "numpy":
                print(f"[OK] {package} ({module.__version__}) - Numerical computation ready")
            elif package == "requests":
                print(f"[OK] {package} ({module.__version__}) - Network access ready")
            elif package == "matplotlib":
                print(f"[OK] {package} ({module.__version__}) - Visualization ready")

        except ImportError:
            print(f"[MISSING] {package} - please install it")
    if len(imported_modules) < len(required_packages):
        print("\nPlease install missing dependencies using:")
        print("pip install -r requirements.txt")
        print("or")
        print("poetry install")
        sys.exit(1)

    return imported_modules


def main():
    modules = check_dependencies()

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    pd = modules["pandas"]
    np = modules["numpy"]
    plt = importlib.import_module("matplotlib.pyplot")

    data = pd.DataFrame({"matrix_code": np.random.randn(1000)})

    print("Generating visualization...")

    plt.plot(data["matrix_code"], color="blue")
    plt.title("Random Data Plot")
    plt.xlabel("Index")
    plt.ylabel("Signal Strength")
    plt.grid(True)


    plt.savefig("matrix_analysis.png")
    plt.close()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
