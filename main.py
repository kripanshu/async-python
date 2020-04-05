from client.client import Client


def main():
    c = Client()
    c.call_reddit(['python', 'covid'])
    c.run_forever()


if __name__ == '__main__':
    main()
