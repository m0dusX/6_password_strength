# Password Strength Calculator

Rates strength of user password on a scale of 1 to 10. To acheive best ranking, you must follow this rules:

1) Use of both upper-case and lower-case letters (case sensitivity)
2) Include one or more numerical digits
3) Include special characters, such as @, #, $
3) Don't use passwords found in a password blacklist
4) Don't use your name or date of birth in password

# Quickstart

Place password_strength.py & blacklist.txt somewhere. Then run command line, go to folder in which you moved script and execute it with one parameter containing path to text file with bad passwords.

Script usage on Linux, Python 3.5:

```bash

$ python password_strength.py [-h] <path_to_badlist>

```

Example of script work (with input):

```#!bash

Please enter your name: Nikita
Please enter your date of birth (in YYYY-MM-DD format): 1980-23-12
Please enter your password: 2376234123nikita*A
Your password rating: 7

```



# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
