import re


def get_password_strength(password, p_data):
    password_rating = 0
    if len(password) >= 8:
        password_rating += 2
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        password_rating += 2
    if re.search(r'\d+', password):
        password_rating += 1
    if  re.search(r'[~!@#$%^&*()_+]', password):
        password_rating += 2
    date_of_birth = p_data.get("date_of_birth").split("-")[0]
    #checks for similar substrings in password and data provided by user (date of birth and name)
    if p_data.get("name").lower() not in password.lower() and date_of_birth not in password:
        password_rating += 2
    #checks if passwords in blacklist (blacklist.txt) are substrings of user password
    with open("badlist.txt", "r") as bad_pass_txt:
        bad_passes = bad_pass_txt.readlines()
    bad_pass_list = [password.strip() for password in bad_passes]
    if not any (i in password for i in bad_pass_list):
        password_rating += 1
    return password_rating


if __name__ == "__main__":
    personal_data = {}
    name = input("Please enter your name: ")
    personal_data["name"] = name
    while True:
        date_of_birth = input("Please enter your date of birth (in YYYY-MM-DD format): ")
        if re.match("^\d{4}-\d{2}-\d{2}$", date_of_birth):
            break
        else:
            print("Wrong data format!")
    personal_data["date_of_birth"] = date_of_birth
    password = input("Please enter password: ")
    print("Your password rating: {}".format(get_password_strength(password, personal_data)))
