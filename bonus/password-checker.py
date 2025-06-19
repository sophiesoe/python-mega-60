password = input("Enter password: ")

result = {
  "length": False,
  "number": False,
  "uppercase": False
}

if len(password) >= 8:
  result["length"] = True

for char in password:
  if char.isdigit():
    result["number"] = True
  if char.isupper():
    result["uppercase"] = True

if all(result.values()):
  print("Strong Password")
else:
  print("Weak Password")