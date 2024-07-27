# membership operator in / not in
# count vovel

my_string = "aeghuernir"
total = 0
for ch in my_string:
    if ch in "aeiouAEIOU":
        total += 1
print(total)
