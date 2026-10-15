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
#print(student["address"]['city'])
#print(student.get('address'))
#print(student.keys())
#print(student.values())
#student["name"] = "Dev"
x = student.items()
print(student)