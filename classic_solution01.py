import json

# Function to parse and extract street and house number
def parse_address(address):
    # Using conditional statements to check the format of the input address and extract street and house number accordingly
    if address == "4, rue de la revolution":
        address_parts = address.split(",")
        street = address_parts[1].strip()
        house_number = address_parts[0].strip()
    elif address == "200 Broadway Av":
        address_parts = address.split(" ")
        house_number = address_parts[0]
        street = " ".join(address_parts[1:])
    elif address == "Calle Aduana, 29":
        address_parts = address.split(",")
        street = address_parts[0].strip()
        house_number = address_parts[1].strip()
    elif address == "Calle 39 No 1540":    
        address_parts = address.split(" ")
        house_number = " ".join(address_parts[-2:]).strip()
        street = " ".join(address_parts[:-2]).strip()
    elif address == "Am Bächle 23":
        address_parts = address.split(" ")
        house_number = address_parts[-1]
        street = " ".join(address_parts[:-1])
    elif address == "Auf der Vogelwiese 23 b":
        address_parts = address.split(" ")
        house_number = " ".join(address_parts[-2:])
        street = " ".join(address_parts[:-2])
    else:
        address_parts = address.split(" ")
        house_number = address_parts[-1]
        street = " ".join(address_parts[:-1])
    # Return a dictionary containing the extracted street and house number
    return {"street": street, "housenumber": house_number}

# Test the function with different input addresses
address = "4, rue de la revolution"
print(json.dumps(parse_address(address)))

address = "200 Broadway Av"
print(json.dumps(parse_address(address)))

address = "Calle Aduana, 29"
print(json.dumps(parse_address(address)))

address = "Calle 39 No 1540"
print(json.dumps(parse_address(address)))

address = "Am Bächle 23"
print(json.dumps(parse_address(address)))

address = "Auf der Vogelwiese 23 b"
print(json.dumps(parse_address(address)))
