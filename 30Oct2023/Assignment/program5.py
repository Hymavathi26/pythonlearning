# Program 5:
# Convert to Dict JSON Response and Print and Booking Id AND checkin and Checkout Data
# {
# "bookingid": 2384,
# "booking": {
# "firstname": "PRAMOD",
# "lastname": "Dutta",
# "totalprice": 432,
# "depositpaid": False,
# "bookingdates": {
# "checkin": "2022-01-01",
# "checkout": "2022-01-01"
# },
# "additionalneeds": "Lunch"
# }
# }

json_response={
          "bookingid": 2384,
          "booking": {
          "firstname": "PRAMOD",
          "lastname": "Dutta",
          "totalprice": 432,
          "depositpaid": False,
          "bookingdates": {
          "checkin": "2022-01-01",
          "checkout": "2022-01-01"
 },
          "additionalneeds": "Lunch"
 }
 }

print("json_resomse :",json_response)
print("booking_id : ",json_response["bookingid"])
print("Checkin_date :",json_response["booking"]["bookingdates"]["checkin"])
print("Check_Out date :",json_response["booking"]["bookingdates"]["checkout"])

