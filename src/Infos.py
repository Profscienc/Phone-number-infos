import phonenumbers

from phonenumbers import geocoder, carrier


phone_number = phonenumbers.parse("")


print(geocoder.description_for_number(phone_number, 'en'),
      carrier.name_for_number(phone_number, 'en'))
