from clients import client
import sys

def add_to_client_list(client):
    client_list.write(client)

if __name__ == "__main__":
    try:
        test = client.Client("Ar", "Jay")
        client_list = open("clientlist.txt", "w")
        add_to_client_list(test)
        print(client_list.read())
        client_list.close()
    except Exception as e:
        print(e)

