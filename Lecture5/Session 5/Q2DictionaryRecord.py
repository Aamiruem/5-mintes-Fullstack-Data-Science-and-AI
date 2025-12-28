# Create dictionary
student = {"name": "kamran", "age": 23, "course": "Python"}
print("Original Dictionary:", student)

# Add new key
student["marks"] = 98
print("After Adding Marks:", student)

# Update age
student["age"] = 24
print("After Updating Age:", student)

# Remove course
student.pop("course")
print("After Removing Course:", student)

# Print all keys and values
print("Keys:", student.keys())
print("Values:", student.values())

# Clear dictionary
student.clear()
print("After Clearing Dictionary:", student)
