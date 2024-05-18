# pip install phonenumbers #
import phonenumbers
from phonenumbers import geocoder, carrier

# Enter your number with country code and area code #
phoneNumber = phonenumbers.parse("+5571982580222")

# Operator capture #
Carrier = carrier.name_for_number(phoneNumber, 'pt-br')

# Region capture #
Region = geocoder.description_for_number(phoneNumber, 'pt-br')

# Show results #
print("The operator is: " + Carrier)
print("The state is: " + Region)
