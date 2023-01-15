import pandas as pd
import re

# parse_address function to extract the house number and street from an address string
def parse_address(address):
    # Using regular expression to extract the house number from the address
    house_number = re.search(r'\d+', address).group()
    # Using regular expression to remove the house number from the address and extract the street
    street = re.sub(r'\d+', '', address).strip()
    # Return a dictionary containing the extracted street and house number
    return {"street": street, "housenumber": house_number}

# Create a pandas dataframe with the address column
address_df = pd.DataFrame({'address': ["4, rue de la revolution", "200 Broadway Av", "Calle Aduana, 29", "Calle 39 No 1540", "Am Bächle 23","Auf der Vogelwiese 23 b"]})
# Apply the parse_address function to the address column and create a new column 'parsed_address'
address_df['parsed_address'] = address_df['address'].apply(parse_address)
# Print the resulting dataframe
print(address_df)
