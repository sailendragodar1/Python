# -----------------------------
# Loop List
# -----------------------------
# 1. Loop through a list
# 2. Loop through the index numbers
# 3. Using a while loop
# 4. Looping using list comprehension

# ==========================================
# 1. Loop through a list
# ==========================================

lists = ["kxa", 2, 3, "ram"]

print("Loop Through a List")
for x in lists:
    print(x)

print()

ram = ["RAM", "BABU", 23, 34, 35, 56, 67, 78]

print("Another Example")
for x in ram:
    print(x)

print()


# ==========================================
# 2. Loop Through the Index Numbers
# ==========================================

my_list = ["ram", "babu", 23, "Ghimire"]

print("Loop Through Index Numbers")
for i in range(len(my_list)):
    print(my_list[i])

print()


# ==========================================
# 3. Using a While Loop
# ==========================================

my_list = ["ram", "babu", 23, "Ghimire"]

print("Using While Loop")

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

print()


# ==========================================
# 4. Looping Using List Comprehension
# ==========================================

my_list = ["ram", "babu", 23, "Ghimire"]

print("Using List Comprehension")

[print(x) for x in my_list]