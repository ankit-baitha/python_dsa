# #        Assigments
# """"
# 1Q. There are two variable.
# a=5 b=10
# what will be the output of following

# """
# a = 5
# b = 10
# print(a > 5 and b >= 10)
# print(a >= 5 or not b > 10)
# print(a > 5 and b > 5)
# print(not (a > 10 or not b < 10))
# print(not (not a <= 5 or not b >= 10))


# """"
# 2Q. python program to convert kilometers to miles.
# Ask kilometer from user.

# """
# kilometer = int(input("Enter the kilometer : "))
# miles = kilometer * 0.621371
# print(miles)

# """"
# 3Q. Ask 3 number from user and calculate the average.
# """
# n1 = int(input("enter the number : "))
# n2 = int(input("enter the number : "))
# n3 = int(input("enter the number : "))
# average = (n1 + n2 + n3) / 3
# print(average)


# """"
# 4Q. Ask value in rupees and convert into paisa
# """
# rupees = int(input("enter the rupess : "))
# paise = rupees * 100
# print("paise", paise)

# """"
# 5Q. calculate area of square by taking side from user.
# """
# n=int(input("enter the number of square : "))
# area_of_square = n*n
# print(area_of_square)

# """"
# 6Q. Ask number of games played in tournaments. ask the user number of games won and number of games loss .
# calculate number of tie and total points.(1 win=4 points , 1 tie=2 points)
# """

total_games = int(input("Enter the total number of games playes in the tournaments = "))
games_won = int(input("Enter the number of games won: "))
games_lost = int(input("Enter the number of games lost: "))
games_tied = total_games - (games_won + games_lost)
total_points = (games_won * 4) + (games_tied * 2)
print(f"Total games played: {total_games}")
print(f"Games won: {games_won}")
print(f"Games lost: {games_lost}")
print(f"Games tied: {games_tied}")
print(f"Total points: {total_points}")

# """"
# 7Q. check if the number entered by user is divisible by 3 or not

# """
# number=int(input("enter the numbr = "))
# if number %3==0:
#     print("Divisible")
# else:
#     print("Not divisible")

# """"
# 8Q. Ask a number from user .print if the number is ODD or EVEN
# """
# user_number=int(input("enter the number = "))
# if user_number%2==0:
#     print("EVEN")
# else:
#     print("ODD")
