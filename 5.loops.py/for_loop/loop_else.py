for i in range(1, 11):
    print(i, end=" ")
else:
    print("done")
# 1 2 3 4 5 6 7 8 9 10
# done

for j in range(1, 11):
    print(j, end=" ")
    if j == 4:
        break

else:
    print("done")
# 1 2 3 4
