try:
  file = open(r"a.txt")
  print("File can be read properly.")
finally:
  print("Error")
  file.close()
  
  
with open(r"a.txt") as file:
  pass
  print("File can be read properly.")