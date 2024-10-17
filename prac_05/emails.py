def main():
    """Store users' emails (keys) and names (values) in a dictionary, checks name validity, and outputs the
    email-name pairs."""
    emails = get_user_name_and_email()
    print_user_email_and_name(emails)


def get_user_name_and_email():
    emails = {}
    email = input("Email: ").strip()

