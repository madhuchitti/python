email = input("Enter student email: ")
reg_id = input("Enter registration ID: ")
if "@" not in email:
    print("Email Error: Missing @ symbol")
elif email.count("@") != 1:
    print("Email Error: Multiple @ symbols")
elif "." not in email:
    print("Email Error: Missing dot")
elif " " in email:
    print("Email Error: Contains spaces")
elif email.startswith("@") or email.endswith("@"):
    print("Email Error: Missing email component")
elif email.startswith(".") or email.endswith("."):
    print("Email Error: Invalid dot position")
else:
    print("Email & Registration ID: Valid")
