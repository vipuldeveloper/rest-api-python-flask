friends = ["Nikunj", "Vaibhav", "Kavar", "Suarabh"]

starts_with_s = [friend for friend in friends if friend.startswith("S")]

print(starts_with_s)

print(id(starts_with_s))
print(type(starts_with_s))