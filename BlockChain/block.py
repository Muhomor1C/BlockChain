import json
import os


def write_block(name, amount, to_whom, prev_hash=""):
    blockcain_directory = os.curdir + os.sep + "blocks" + os.sep
    data = {"name": name,
            "amount": amount,
            "to_whom": to_whom,
            "hash": prev_hash}
    with open(blockcain_directory + "test", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    if not os.path.exists(os.curdir + os.sep + "blocks" + os.sep):
        os.mkdir(os.curdir + os.sep + "blocks" + os.sep)
    write_block("Vadim", 10, "Klava")


if __name__ == "__main__":
    main()
