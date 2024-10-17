def main():
    """This program is stores users' emails (unique keys) and names (values) in a dictionary
    and check if the name is correct, then output the emails and names"""
    emails = get_user_name_and_email()
    print_user_email_and_name(emails)
