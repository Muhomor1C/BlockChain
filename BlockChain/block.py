import hashlib
import json
import os

blockchain_directory = os.curdir + os.sep + "blocks" + os.sep
file_type = ".blc"


def get_fullname(file):  # full name of files for OS
    return blockchain_directory + str(file) + file_type


def get_files_list():
    """
    :return: list integers for file names
    """
    return sorted(int(i.replace(file_type, "")) for i in os.listdir(blockchain_directory) if i.endswith(file_type))


def get_last_file():
    """
    :return: int -> name of last file
    """
    files = get_files_list()
    try:
        return int(files[-1])
    except FileNotFoundError:
        return -1


def get_hash(file):
    """
    :param file:  int
    :return:   hash of file width name "file"
    """
    file = open(get_fullname(file), "rb").read()
    return hashlib.md5(file).hexdigest()


def check_hash():
    """
    verify blockchain
    :return:   boolean
    """
    for file in get_files_list()[1:]:
        prev_hash = get_hash(file - 1)  # hash of preview file
        verified_hash = json.load(open(get_fullname(file)))["hash"]
        if verified_hash != prev_hash:
            return False
    return True


def write_block(name, amount, to_whom, prev_hash=""):
    file = get_last_file()
    data = {"name": name,
            "amount": amount,
            "to_whom": to_whom,
            "hash": prev_hash}
    with open(get_fullname(file + 1), "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    prev_hash = str(get_hash(str(get_last_file())))  # hash of preview file
    write_block("Vadim", 10, "Klava", prev_hash)


if __name__ == "__main__":
    if not os.path.exists(blockchain_directory):
        os.mkdir(blockchain_directory)
    if not os.path.exists(blockchain_directory + "0" + file_type):
        write_block("GENESIS", 0, "Genesis")
    main()
    print(check_hash())
