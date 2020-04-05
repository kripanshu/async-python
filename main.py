import sys
from client.client import Client


def main():
    args = sys.argv[1:]
    print("-" * 20)
    print("fetching data for :", args)
    c = Client()
    c.call_reddit(args)
    c.run_forever()
    print("-" * 20)


if __name__ == '__main__':
    main()
