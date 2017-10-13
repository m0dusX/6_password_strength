import re
import argparse
from getpass import getpass
import string


def load_badpasses(filepath):
    with open(filepath, 'r') as bad_pass_txt:
        loaded_txt = bad_pass_txt.readlines()
    return [bad_pass.strip() for bad_pass in loaded_txt]


def password_strength_check(password):
    password_strength = 0
    minimum_length = 8
    if len(password) >= minimum_length:
        password_strength += 2
    if not password.isdigit():
        if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
            password_strength += 2
        if re.search(r'\d+', password):
            password_strength += 1
        if any(char in string.punctuation for char in password):
            password_strength += 2
    return password_strength


def bad_password_check(password, bad_passes):
    return not any(bad_pass in password for bad_pass in bad_passes)


def user_data_check(password, strings_to_check):
    return 2 * all(string not in password for string in strings_to_check)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Password strength checker")
    parser.add_argument("path_to_badlist",
                        help="path to txt file with bad passwords")
    args = parser.parse_args()
    filepath = args.path_to_badlist
    strings_to_check = []
    bad_passes = load_badpasses(filepath)
    username = input('Please enter your name: ')
    if username is not "":
        strings_to_check.append(username.lower())
    user_input = input('Please enter your date '
                       'of birth (in YYYY-MM-DD format): ')
    if re.match('^\d{4}-\d{2}-\d{2}$', user_input):
        strings_to_check.append(user_input.split('-')[0])
    password = getpass(prompt='Please enter your password: ')
    rank = (password_strength_check(password) +
            + int(bad_password_check(password, bad_passes)) +
            + user_data_check(password.lower(), strings_to_check))
    print('Your password rating: {}'.format(rank))
