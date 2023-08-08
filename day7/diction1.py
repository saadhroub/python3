# Data Structures تراكيب البيانات 


std_diction = {
    "name": "Saad Hroub",
    "age":37,
    "address":  {   
                "location": {
                        "city":"Ramallah",
                        "street":"Rukab",
                        "building": "Tannous"
                        },
                    "email": "saad@gmail.com",
                    "phone": "0599123456"
                },
    "languages": ["AR", "FR", "HB", "EN"],
    "is_graduated": False   
}
print(std_diction["address"]["location"]["city"])
print(std_diction["address"]["email"])
print(std_diction["languages"])

print(std_diction["address"]["location"].keys())
print(std_diction["address"]["location"].values())
print(std_diction["address"].values())
print(std_diction.values())

