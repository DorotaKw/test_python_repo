import json


def write_json_to_file():
    input_json = [
        {'imie': 'Antek'},
        {'imie': 'Marek'}
    ]
    try:
        with open("./cukierki.json", "w") as fd:
            json.dump(input_json, fd)
    except (IOError, json.JSONDecodeError, BaseException) as e:
        print(f"Masz błąd i więcej info {e.args}")


def read_json_to_file():
    output_json = []
    try:
        with open("./cukierki.json", "r") as fd:
            output_json = json.load(fd)
            print(output_json)
    except (IOError, BaseException) as e:
        print(f"Masz błąd i więcej info {e.args}")


def main():
    write_json_to_file()
    read_json_to_file()


if __name__ == "__main__":
    main()
