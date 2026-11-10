marks={
    "harry":78,
    "priyanshu":65,
    "ashok":76,
     0: "Harry"
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry": 99, "Renuka": 100})
print(marks)

print(marks.get("Harry2")) # Prints None
#print(marks["Harry2"]) # Returns an error