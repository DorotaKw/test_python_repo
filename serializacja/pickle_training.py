import pickle

def pickle_write():
    strings = ["Island", "Sweden", "Bali-Bali"]
    try:
        with open("./picklowanie.pickle", "wb") as fd:
            pickle.dump(strings, fd)
            print(pickle.dumps(strings))
    except (IOError, pickle.PickleError, BaseException) as e:
        print(f"Exception while pickling. More info: {e.args}")

def pickle_read():
    strings = ["Island", "Sweden", "Bali-Bali"]
    try:
        with open("./picklowanie.pickle", "rb") as fd:
            strings = pickle.load(fd)
            print(strings)
    except (IOError, pickle.PickleError, BaseException) as e:
        print(f"Exception while pickling. More info: {e.args}")

def main():
    pickle_write()
    pickle_read()

if __name__ == "__main__":
    main()