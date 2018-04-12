print("Hello world")
some_value = 14

def determine_count(count):
   if count <= 50:
       x = count
   elif 51 >= count <= 100:
       x = "Wowzers"
   else:
       x = 10
   return x

print(determine_count(some_value))