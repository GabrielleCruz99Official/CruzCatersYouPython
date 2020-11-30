from clients import client
"""
This module aims to store client information in a text file
(or eventually a database)
"""

if __name__ == "__main__":
    try:
        """
        because of the second parameter, if the text file
        doesn't exist, we can create one instead of raising
        an exception
        """
        client_list = open("clientlist.txt", "w")
        test = client.Client("Ar", "Jay")
        client_list.write(test.fullname())
        client_list.close()

        """
        from testing the methods, you have to close or stop writing
        the file before you are able to read it. this is why
        we need to open the file for the second time
        """
        read_list = open("clientlist.txt")
        for line in read_list:
            print(line)
        client_list.close()
    except Exception as e:
        print(e)
