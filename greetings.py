# Accept gender from user and print a greeting message.

gender = input("Please enter your gender(M/F): ")

if gender in "Mm":
    print("Good morning, Sir")

elif gender in "Ff":
    print("Good morning, Ma'am")

else:
    print("Try again")
