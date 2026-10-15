student = {
    "id": 101,
    "name": "Rahim Ahmed",
    "age": 21,
    # প্রথম নেস্টেড ডিকশনারি (ঠিকানা)
    "address": {
        "city": "Dhaka",
        "area": "Dhanmondi",
        "postal_code": 1205
    },
    # দ্বিতীয় নেস্টেড ডিকশনারি (একাডেমিক তথ্য)
    "academic": {
        "department": "Computer Science",
        "semester": "4th",
        "grades": {
            "python": "A+",
            "math": "A"
        }
    }
}

# for i in student:
#   print(i)

# for x in student.values():
#     print(x)

# for z in student.keys():
#   print(z)

# for a in student.items():
#   print(a)
#print(student["address"]['city'])
#print(student.get('address'))
#print(student.keys())
#print(student.values())
#student["name"] = "Dev"
# x = student.items()
# y= student.update({'age':'35'})
# print(student)

# z= student.update({'academic': 'CBHS'})
# print(student)
# student.pop('name')
# print(student)

# address= {
#         "city": "Dhaka",
#         "area": "Dhanmondi",
#         "postal_code": 1205
#     }

# x = address.copy()
# print(x)

# asw = student.copy()
# print(asw)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()

print(x)