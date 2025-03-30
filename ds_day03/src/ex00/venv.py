#!/usr/bin/env python3
import os

def print_virtual_env():
    try:
        print(f"Your current virtual env is {os.environ['VIRTUAL_ENV']}")
    except KeyError:
        print("No virtual environment is currently activated.")

if __name__ == '__main__':
    print_virtual_env()
