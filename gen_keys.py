from stellar_base import Keypair

def generate_keypair():
  """
  Generates a random keypair and stores it in a secret file.
  """
  # Generate a random keypair
  keypair = Keypair.random()

  # Extract private and public keys
  private_key = keypair.secret().decode()
  public_key = keypair.public_key().decode()

  # Write keys to a file (NOT recommended for production)
  with open("keys.secret", "w") as f:
    f.write(f"private_key: {private_key}\n")
    f.write(f"public_key: {public_key}")

  print("Keys generated and stored in keys.secret")

if __name__ == "__main__":
  generate_keypair()
