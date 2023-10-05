import py_compile
import sys

def list_hidden_names(pyc_file):
    # Compile the module without executing it
    try:
        py_compile.compile(pyc_file, doraise=True)
    except py_compile.PyCompileError as e:
        print(f"Error compiling {pyc_file}: {e}")
        sys.exit(1)

    # Import the module
    module_name = pyc_file[:-4]  # Remove '.pyc' extension
    try:
        module = __import__(module_name)
    except ImportError as e:
        print(f"Error importing {module_name}: {e}")
        sys.exit(1)

    # Get the names defined in the module
    module_names = [name for name in dir(module) if not name.startswith("__")]

    # Print the names in alphabetical order
    for name in sorted(module_names):
        print(name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 4-hidden_discovery.py <pyc_file>")
        sys.exit(1)

    pyc_file = sys.argv[1]
    list_hidden_names(pyc_file)
