import wikipedia

"""it prompts the user for a page title or search phrase, then prints some details of that page."""


def main():
    """ask users to input page title, when enter blank, quit"""
    while True:
        title = input("Enter page title: ")
        if not title:
            print("Thank you.")
            break
        get_wikipedia_page(title)


def get_wikipedia_page(title):
    """display details of that page"""
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(f"{page.title}")
        print(f"{page.summary}")
        print(f"{page.url}")
    except wikipedia.exceptions.DisambiguationError as e:
        print("\nWe need a more specific title. Try one of the following, or a new search:")
        print(e.options)
    except wikipedia.exceptions.PageError:
        print(f'\nPage id "{title}" does not match any pages. Try another id!')


if __name__ == "__main__":
    main()
