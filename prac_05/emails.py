def main():
    """Store users' emails (keys) and names (values) in a dictionary, checks name validity, and outputs the
    email-name pairs."""
    emails = get_user_name_and_email()
    print_user_email_and_name(emails)


def get_user_name_and_email():
    """Ask users for their name and store in a dictionary"""
    emails = {}
    email = input("Email: ").strip()
    while email != "":
        username = email.split('@')[0]
        parts = username.split('.')
        username = ' '.join(parts).title()
        check_name = input(f"Is your name {username}? (Y/n) ").strip().lower()
        if check_name in ('', 'y', 'yes'):
            name = username.title()
        else:
            name = input("Name: ").title()
        emails[email] = name
        email = input("Email: ").strip()
    return emails


def print_user_email_and_name(emails):
    for email, name in emails.items():
        print(f"{name} ({email})")
