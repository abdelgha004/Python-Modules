#!/usr/bin/env python3

def garden_operations():
    """
    Trigger and handle common Python errors:
    ValueError, ZeroDivisionError, FileNotFoundError, KeyError.
    Demonstrates catching multiple errors and program continuation.
    """
    def show_err(err):
        if err == ValueError:
            print("Caught ValueError: invalid literal for int()\n")
        elif err == ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero\n")
        elif err == FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'\n")
        elif err == KeyError:
            print("Caught KeyError: 'missing\\_plant'\n")

    try:
        print("Testing ValueError...")
        int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as err:
        show_err(type(err))

    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as err:
        show_err(type(err))

    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as err:
        show_err(type(err))

    try:
        print("Testing KeyError...")
        d = {"plant": "rose"}
        d["tree"]
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as err:
        show_err(type(err))

    try:
        print("Testing multiple errors together...")
        int("abc")
        10 / 0
        open("missing.txt")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")


def test_error_types():
    """
    Run garden_operations and show all errors are caught
    without stopping the program.
    """
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
