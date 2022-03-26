import json


def write_block(name, amount, to_whom, prev_hash=""):
    data = {"name": name,
            "amount": amount,
            "to_whom": to_whom,
            "hash": prev_hash}
    with open("test", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    write_block("Vadim", 10, "Klava")


if __name__ == "__main__":
    main()
