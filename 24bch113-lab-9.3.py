contact_name = input("Enter contact name: ")
phone_number = input("Enter phone number: ")

vcard_content = f"""BEGIN:VCARD
VERSION:3.0
FN:{contact_name}
TEL;TYPE=VOICE:{phone_number}
END:VCARD"""

with open(f"{contact_name}.vcf", "w") as file:
    file.write(vcard_content)

print("vCard created successfully.")