import re


def regex_check(password):
    symbol_rating = 0
    if len(password) >= 8:
        symbol_rating += 2
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        symbol_rating += 2
    if re.search(r'\d+', password):
        symbol_rating += 1
    if  re.search(r'[~!@#$%^&*()_+]', password):
        symbol_rating += 2
    return symbol_rating
    

def additional_checks(password, p_data):
    additional_rating = 0
    date_of_birth = p_data.get("date_of_birth").split("-")[0]
    #checks for similar substrings in password and data provided by user (date of birth and username)
    if p_data.get("username").lower() not in password.lower() and date_of_birth not in password:
        additional_rating += 2
    #checks if passwords in blacklist (blacklist.txt) are substrings of user password
    with open("badlist.txt", "r") as bad_pass_txt:
        bad_passes = bad_pass_txt.readlines()
    bad_pass_list = [password.strip() for password in bad_passes]
    if not any (bad_pass in password for bad_pass in bad_pass_list):
        additional_rating += 1
    return additional_rating


if __name__ == "__main__":
    personal_data = {}
    username = input("Please enter your name: ")
    personal_data["username"] = username
    while True:
        date_of_birth = input("Please enter your date of birth (in YYYY-MM-DD format): ")
        if re.match("^\d{4}-\d{2}-\d{2}$", date_of_birth):
            break
        else:
            print("Wrong data format!")
    personal_data["date_of_birth"] = date_of_birth
    password = input("Please enter your password: ")
    rank = regex_check(password) + additional_checks(password, personal_data)
    print("Your password rating: {}".format(rank))
