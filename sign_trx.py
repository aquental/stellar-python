import base64
from stellar_sdk import Keypair, TransactionBuilder, Network, Server

# Function to read keys from file (with error handling)


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
server = Server(horizon_url="https://horizon-testnet.stellar.org")

message = "DEV30K".encode()
message_b64 = base64.b64encode(message)
print(f"base64: {message_b64.decode()}")
# assinar
assinatura = keypair.sign(message_b64)
print(f"assinatura (hex): {assinatura.hex()}")

# trx
transaction = (
    TransactionBuilder(
        source_account=public_key,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=100
    )
    .set_timeout(30)
    .append_manage_data_op(data_name="desafio", data_value=assinatura)
    .build()
)

transaction.sign(keypair)

# try:
response = server.submit_transaction(transaction)
print(f"Hash: {response['hash']}")
