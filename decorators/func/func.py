def check_file_wrapper(func):
    def inner(*args, **kwargs):
        path = ""
        if len(args) > 0:
            path = args[0]
        elif kwargs.get("source", ""):
            path = kwargs.get("source")
        import os
        if path and os.path.exists(path):
            print("File exists")
        elif path:
            print("path not exists - file will be created")
            from pathlib import Path
            Path(path).touch()
        else:
            print("No argument")
            import sys
            sys.exit(1)
    
        return func(*args, **kwargs)

    return inner

@check_file_wrapper
def writing_file(source: str):
    with open(source, "r") as fd:
        fd.read()


def main():
    writing_file(source="./deco")


if __name__ == "__main__":
    main()
