#dictionary keep information and information in keys and pair values.#

student_1 = {
    "name": "Arya",
    "stream":"Dev-Ops",
    "grades": 5,
    "completed_modules": ["git","github","business week", " variables", "data types"],
}

student_2 = {
    "name": "John",
    "stream":"Dev-Ops",
    "grades": 5,
    "completed_modules": ["git","github","business week", " variables", "data types", "protecting the wall", "commanrgder of the knights watch"],
}
student_2["completed_modules"] += ["BACK FROM THE DEAD", "STEEL"]
print(student_2)

print(student_2["completed_modules"])

# += ADDS OF INCREMENTS TO EXISTING OBJECTS.#
