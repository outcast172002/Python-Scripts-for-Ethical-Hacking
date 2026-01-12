#!/usr/bin/env python3

#Latin 1 encoding used to ensure this program will run with all wordlists including rockyou.txt

import hashlib
import pyfiglet
    
GREEN = '\033[32m'
RED = "\033[31m"
RESET = '\033[0m'

ascii_banner = pyfiglet.figlet_format("HASH CRACKER", font = 'slant')
print(f'{GREEN}{ascii_banner}{RESET}')

hash_input = str(input('Enter hash to be cracked: '))
encryption = str(input(f"Enter the encryption hash type: {GREEN}(options: sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512, blake2b, blake2s, md5):{RESET} "))
wordlist_location = str(input('Enter wordlist file location: '))

print(f"{GREEN}\nAttempting to crack hash...")


with open(wordlist_location, 'r', encoding='latin-1') as file:
    for line in file.readlines():
        hash_ob = getattr(hashlib, encryption)(line.strip().encode())
        hashed_pass = hash_ob.hexdigest()
        if hashed_pass == hash_input:
            print(f"{GREEN}\nPASSWORD FOUND --> {RESET}"  + line.strip()) 
            break          
    if hashed_pass != hash_input:
        print(f"{RED}\nPASSWORD NOT FOUND IN WORDLIST! {RESET}")
        exit(0)
