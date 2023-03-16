def login():
    # Get user input
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Get user from database
    # Note: This is just an example, replace with your own database implementation
    user = db.get_user(username)

    if user:
        # Extract salt and hashed password
        salt = user['password'][:64]
        stored_password = user['password'][64:]

        # Hash input password with stored salt
        hashed_password = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt.encode('ascii'), 100000)
        hashed_password = binascii.hexlify(hashed_password)

        # Check if passwords match
        if hashed_password == stored_password:
            print("Login successful")
        else:
            print("Invalid password")
    else:
        print("User not found")
