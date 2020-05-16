import os
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        directory = sys.argv[1]
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    print(os.path.join(root, file))