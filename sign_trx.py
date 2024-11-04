from stellar_base import Keypair, TransactionBuilder, Network

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

# Message to sign
message = "DEV30K"

# Build transaction
tx = TransactionBuilder(source_account=public_key,
                        network=Network.TESTNET,  # Replace with desired network
                        fee=100)  # Adjust fee as needed

# Add manage_data operation with MEMO field containing the signature
tx.add_operation(TransactionBuilder.manage_data_op(
  key="memo",
  value=keypair.sign(message.encode()).decode()
))

# Build the transaction envelope
tx_envelope = tx.build()

# Print the transaction envelope (includes the signed message in MEMO)
print(tx_envelope.to_xdr())
