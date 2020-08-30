import csv


def csv_write():
    users = [("Adam", "Nowak", "2345678901"),
             ("Michał", "Nowakowski", "76031134791"), ("Krystian", "Kowalski", "58123078329")]
    try:
        with open("./lizaki.csv", "w") as fd:
            writer = csv.writer(fd)
            for user in users:
                writer.writerow(user)
    except (IOError, csv.Error, BaseException) as e:
        print(f"Masz błąd i więcej info {e.args}")


def csv_read():
    users = []
    try:
        with open("./lizaki.csv", "r") as fd:
            csv_reader = csv.reader(fd)
            for row in csv_reader:
                if row:
                    users.append(row)
    except (IOError, csv.Error, BaseException) as e:
        print(f"Masz błąd i więcej info {e.args}")
    print(users)


def main():
    csv_write()
    csv_read()


if __name__ == "__main__":
    main()
