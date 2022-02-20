# Beautiful is always better than ugly


import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'In_numbers.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
            return username
    except FileNotFoundError:
        return None


def get_new_username():
    """提示用户输入用户名"""
    filename = 'In_numbers.json'
    username = input("Please input your name:")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    print("Ok," + username + " I'll remember you")
    return username


def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("You are " + username + " right?")
        choice = input("If not ,please input 'no' :")
        if choice == 'no' or choice == 'No':
            print("--------")
            get_new_username()
        else:
            print("Welcome back!" + username)
    else:
        print("this is else")
        username = get_new_username()
        print("Ok," + username + " I'll remember you")


greet_user()
