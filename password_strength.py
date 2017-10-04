import re
import argparse
from getpass import getpass
import sys
import string


def make_badlist(badlist):
    with open(badlist, 'r') as bad_pass_txt:
        return bad_pass_txt.readlines()


def regex_check(password):
    symbol_rating = 0
    password_minimum = 8
    if len(password) >= password_minimum:
        symbol_rating += 2
    if not password.isdigit():
        if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
            symbol_rating += 2
        if re.search(r'\d+', password):
            symbol_rating += 1
        if any(char in string.punctuation for char in password):
            symbol_rating += 2
    return symbol_rating


def additional_checks(password, personal_data, bad_passes):
    additional_rating = 0
    if personal_data['username'].lower() not in password.lower() and \
            personal_data['date_of_birth'] not in password:
        additional_rating += 2
    bad_pass_list = [bad_pass.strip() for bad_pass in bad_passes]
    if not any(bad_pass in password for bad_pass in bad_pass_list):
        additional_rating += 1
    return additional_rating


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Password strength checker')
    parser.add_argument('path_to_badlist',
                        help='path to txt file with bad passwords')
    args = parser.parse_args()
    badlist = args.path_to_badlist
    personal_data = {}
    bad_passes = make_badlist(badlist)
    username = input('Please enter your name: ')
    personal_data['username'] = username
    date_of_birth = input('Please enter your date '
                          'of birth (in YYYY-MM-DD format): ')
    if re.match('^\d{4}-\d{2}-\d{2}$', date_of_birth):
        personal_data['date_of_birth'] = date_of_birth.split('-')[0]
    else:
        personal_data['date_of_birth'] = date_of_birth
    password = getpass(prompt='Please enter your password: ')
    rank = regex_check(password) + \
        additional_checks(password, personal_data, bad_passes)
    print('Your password rating: {}'.format(rank))
