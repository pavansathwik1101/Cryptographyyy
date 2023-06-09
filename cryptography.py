import argparse
import base64
from cryptography.fernet import Fernet

# Initialize argument parser
parser = argparse.ArgumentParser(description='Cryptography command line tool')

# Define arguments
parser.add_argument('-g', '--generate-key', action='store_true', help='Generate a new encryption key')
parser.add_argument('-e', '--encrypt', metavar='MESSAGE', help='Encrypt a message')
parser.add_argument('-d', '--decrypt', metavar='ENCRYPTED_MESSAGE', help='Decrypt a message')
parser.add_argument('-k', '--key', metavar='ENCRYPTION_KEY', help='Encryption key')

# Parse arguments
args = parser.parse_args()

if args.generate_key:
    # Generate a new encryption key
    key = Fernet.generate_key()
    print(f"Encryption key: {key.decode()}")

elif args.encrypt:
    # Encrypt a message
    if args.key:
        key = args.key.encode()
    else:
        print("Error: encryption key is missing.")
        exit(1)

    f = Fernet(key)
    message = args.encrypt.encode()
    encrypted_message = f.encrypt(message)
    print(f"Encrypted message: {encrypted_message.decode()}")

elif args.decrypt:
    # Decrypt a message
    if args.key:
        key = args.key.encode()
    else:
        print("Error: encryption key is missing.")
        exit(1)

    f = Fernet(key)
    encrypted_message = args.decrypt.encode()
    decrypted_message = f.decrypt(encrypted_message)
    print(f"Decrypted message: {decrypted_message.decode()}")

else:
    # Print help message if no arguments are provided
    parser.print_help()
