import requests
from stellar_sdk import Keypair


def read_keys():
    try:
        with open("keys.secret", "r") as f:
            lines = f.readlines()
            private_key = lines[0].split(": ")[1].strip()
            public_key = lines[1].split(": ")[1].strip()
            return Keypair.from_secret(private_key), public_key
    except FileNotFoundError:
        print("Error: keys.secret file not found!")
        exit(1)
    except IndexError:
        print("Error: Invalid format in keys.secret file!")
        exit(1)


# Read keys
keypair, public_key = read_keys()

response = requests.get(f"https://friendbot.stellar.org?addr={public_key}")
if response.status_code == 200:
    print(f"SUCCESS! You have a new account :)\n{response.text}")
else:
    print(f"ERROR! Response: \n{response.text}")
