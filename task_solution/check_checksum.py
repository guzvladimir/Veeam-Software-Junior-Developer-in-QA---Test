import hashlib
import os
from typing import Union


# Read input file and add name, algorithm and checksum in dictionary. If input file or path doesn't exist raise an error
def read_input_file(path_input_file: str) -> dict:
    input_files = {}
    try:
        with open(path_input_file, "r") as file:
            for line in file.readlines():
                text = line.rstrip("\n").split()
                input_files[text[0]] = text[1], text[2]
        return input_files
    except FileNotFoundError:
        raise FileNotFoundError(
            f"No such input file or path to the input file: {path_input_file}"
        )


# Computing checksum and return. If algorithm doesn't approach return None
def checksum(data: bytes, algorithm: str) -> Union[str, None]:
    if algorithm == "md5":
        return hashlib.md5(data).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(data).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(data).hexdigest()
    else:
        return None


# Function returns OK if checksum is the same. It returns FAIL if checksum is different or not such algorithm. If file doesn't exist function returns NOT FOUND
def check_checksum(path_input_file: str, dir_file: str):
    for key, value in read_input_file(path_input_file).items():
        file_path = os.path.join(dir_file, key)
        try:
            with open(file_path, "rb") as data:
                if checksum(data.read(), value[0]) == value[1]:
                    print(key, "OK")
                else:
                    print(key, "FAIL")
        except FileNotFoundError:
            print(key, "NOT FOUND")


if __name__ == "__main__":
    path_input_file = input("Enter path to the input file: ")
    dir_file = input("Enter path to the directory containing the files to check: ")
    check_checksum(path_input_file, dir_file)
