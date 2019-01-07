import re
email =input("Email:")
if re.search(".+@(poala.)?(qwert|xyz).com", email):
    print("thanks for the email")
else:
    print("Not Found")
