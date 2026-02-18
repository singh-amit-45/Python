marks = {
    "Amit": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Amit"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Amit": 99, "Renuka": 100})
# print(marks)

print(marks.get("Amit2")) # Prints None
print(marks["Amit2"]) # Returns an error