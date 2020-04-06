import sys
from client.client import Client


def main():
    args = sys.argv[1:]
    print("-" * 20)
    print("fetching data for :", args)
    c = Client()
    fut = c.call_reddit(args)
    c.complete_loop_now(fut)
    print("-" * 20)


if __name__ == '__main__':
    main()
