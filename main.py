import hashlib
import os
from typing import Union


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


def hash_sum(data: bytes, algorithm: str) -> Union[str, None]:
    if algorithm == "md5":
        return hashlib.md5(data).hexdigest()
    elif algorithm == "sha1":
        return hashlib.sha1(data).hexdigest()
    elif algorithm == "sha256":
        return hashlib.sha256(data).hexdigest()
    else:
        return None


def check_hash_sum(path_input_file: str, dir_file: str):
    for key, value in read_input_file(path_input_file).items():
        file_path = os.path.join(dir_file, key)
        try:
            with open(file_path, "rb") as data:
                if hash_sum(data.read(), value[0]) == value[1]:
                    print(key, "OK")
                else:
                    print(key, "FAIL")
        except FileNotFoundError:
            print(key, "NOT FOUND")


if __name__ == "__main__":
    path_input_file = input("Enter path to the input file: ")
    dir_file = input("Enter path to the directory containing the files to check: ")
    check_hash_sum(path_input_file, dir_file)
