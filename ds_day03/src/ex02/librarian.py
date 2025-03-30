#!/usr/bin/env python3
import os, sys
import subprocess

def check_venv():
    if 'VIRTUAL_ENV' not in os.environ:
        raise Exception("Script is not running inside a virtual environment.")
    if os.environ['VIRTUAL_ENV'] != os.path.abspath('env02'):
        raise Exception("Script is not running inside the correct virtual environment.")

def install_libraries():
    with open('requirements.txt', 'w') as f:
        f.write("beautifulsoup4\npytest\n")

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

def list_installed_libraries():
    installed_packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    return installed_packages.decode('utf-8').strip()

def main():
    try:
        check_venv()
        install_libraries()
        libraries = list_installed_libraries()
        print(libraries)

        with open('requirements.txt', 'a') as f:
            f.write(libraries)
            
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
