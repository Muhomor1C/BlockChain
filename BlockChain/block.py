import hashlib
import json
import os

blockcain_directory = os.curdir + os.sep + "blocks" + os.sep


def get_filename():

    files = sorted(int(i.replace(".blc", "")) for i in os.listdir(blockcain_directory) if i.endswith(r".blc"))
    try:
        return int(files[-1])
    except:
        return -1


def get_hash(filename):
    file = open(filename + ".blc", "rb").read()
    return hashlib.md5(file).hexdigest()


def write_block(name, amount, to_whom, prev_hash=""):
    file_name = get_filename()
    data = {"name": name,
            "amount": amount,
            "to_whom": to_whom,
            "hash": prev_hash}
    with open(blockcain_directory + str(file_name+1) + ".blc", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    prev_hash = str(get_hash(blockcain_directory + str(get_filename())))
    write_block("Vadim", 10, "Klava", prev_hash)


if __name__ == "__main__":
    if not os.path.exists(blockcain_directory):
        os.mkdir(blockcain_directory)
    if not os.path.exists(blockcain_directory + "0.blc"):
        write_block("GENESIS", 0, "Genesis")
    main()
