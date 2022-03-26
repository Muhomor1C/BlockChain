import json
import os


blockcain_directory = os.curdir + os.sep + "blocks" + os.sep
if not os.path.exists(blockcain_directory):
    os.mkdir(blockcain_directory)

def get_filename():
    files = sorted(int(i) for i in os.listdir(blockcain_directory))
    try:
        return int(files[-1])
    except:
        return -1


def write_block(name, amount, to_whom, prev_hash=""):
    file_name = get_filename()
    data = {"name": name,
            "amount": amount,
            "to_whom": to_whom,
            "hash": prev_hash}
    with open(blockcain_directory + str(file_name+1), "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    write_block("Vadim", 10, "Klava")


if __name__ == "__main__":
    main()
