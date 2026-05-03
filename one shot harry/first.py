
# print("%s to the right" % ("this is shiva"))

# print("this is a print statement 1", end= "")
# print("this is  print is statement 2")

# print("this "*5) 


cities = ["japan", "america", "russia","australia","india"]
heroes = ["jaguar", "amenda", "rupali","autrology","bakie"]

# def list_len(list):
#     print(len(list))
# print(cities)

def print_list(list):
    for item in list:
        print(item, end=" ")

print(list(heroes))
print(list(cities))