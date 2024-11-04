from stellar_sdk import Keypair


def generate_keypair():
    """
    Generates a random keypair and stores it in a secret file.
    """
    # Generate a random keypair
    keypair = Keypair.random()

    # Extract private and public keys
    private_key = keypair.secret
    public_key = keypair.public_key
    print("Public Key: " + keypair.public_key)
    print("Secret Seed: " + keypair.secret)

    # Write keys to a file
    with open("keys.secret", "w") as f:
        f.write(f"private_key: {private_key}\n")
        f.write(f"public_key: {public_key}")

    print("Keys generated and stored in keys.secret")


generate_keypair()
