deposit_file = open("deposit.txt", "r") #"r+", "w", "a"

print(deposit_file.readable())
print(deposit_file.read())
deposit_file.close()