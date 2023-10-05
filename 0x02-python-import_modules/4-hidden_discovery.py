import marshal
import sys

def list_hidden_names(pyc_file):
    try:
        with open(pyc_file, "rb") as f:
            code = marshal.load(f)

        # Extract and print names that do not start with '__'
        for name in code.co_names:
            if not name.startswith("__"):
                print(name)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 4-hidden_discovery.py <pyc_file>")
        sys.exit(1)

    pyc_file = sys.argv[1]
    list_hidden_names(pyc_file)
