a = ["Yes", "No", "Hello", "Hii", "Bye"]
b = ["Apple", "Banana", "Pineapple"]
print(a)
print(len(a))
print(type(a))
print(a[2])
print(a[2:4])
if "Y" in a:
    print("Yes, available")
else:
    print("Unavailable")
a[1] = "Sanket"
print(a)
a[1:3] = ["Sanjivani", "Kopargaon"]
print(a)
a.insert(2, "Good_Night")
print(a)

a.extend(b)
print(a)
