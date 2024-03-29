#!/usr/bin/python3

import re

def scan():
    memory = input("Enter memory dump file to scan: ")
    size = int(input("Enter chunk size to be used during scan [GB]: "))
    chunk_size = size * (1024 ** 3)
    found = False
    
    print("\nScanning...\n")

    with open(f"{memory}", "rb") as f:
        while True:
            chunk = f.read(chunk_size)

            if not chunk:
                break

            pattern = b'"client_id":"poczta.onet.pl.front.onetapi.pl",'

            if re.search(pattern, chunk) is not None:
                for match in re.finditer(pattern, chunk):
                    print(chunk[match.start()+46:match.start()+101].decode('utf-8'))
                    found = True


    if found is False:
        print("Login credentials to konto.onet.pl were not found")


if __name__ == "__main__":
    scan()