import os

def main():
    print("Hello!!")
    param = os.getenv("PARAM")
    print("PARAM={}".format(param))

if __name__ == "__main__":
    main()
