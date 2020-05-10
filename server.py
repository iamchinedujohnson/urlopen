import socket
import sys


def server(address):
    """initialize a socket server and wait for connection,"""
    try:
        s = socket,socket()
        s.bind(address)
        s.listen
        print("Server Initialize, I'm Listening...")
    except Exception as e:
        print ("/nit seems like something went wrong,")
        print(e)
        restart =input("\Do u want to reinitialize the server?'y/n")
        if restart.lower() =="y" or restart.lower() == "yes":
            print("\nRoger That. REinitializing the server...\n")
            server(address)
        else:
            print ("\nSo Long and Thanks for All The Fishes.\n")
            sys.exit()
    conn, client_addr = s.accept()
    print (f"Connection Established: {Client_addr}")
    
if__name__ == "__main__"
host =  "192.168.56.1"
port= 19876
server((host, port))
