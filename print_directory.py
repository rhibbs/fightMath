import os

def print_directory_structure(rootdir):
    """
    Print the structure of a directory recursively.

    :param rootdir: The root directory to print.
    """
    for subdir, dirs, files in os.walk(rootdir):
        level = subdir.replace(rootdir, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(subdir)}/")
        for file in files:
            print(f"{indent}    {file}")

print_directory_structure('.')