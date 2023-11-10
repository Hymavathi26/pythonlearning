a = {
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

a = {
    "bookingid": 2384,
    "booking": {
        "firstname": "hyma",
        "lastname": "kotha",
        "totalprice": 600,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2022-01-01",
            "checkout": "2022-01-01"
        },
        "additionalneeds": "Lunch"
    }
}

def filter_totalPrice(Tprice):
    return Tprice["booking"]["totalprice"] > 500

Filter_totalPrices=list(filter(filter_totalPrice,a))
print(Filter_totalPrices)