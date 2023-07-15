import json
import enum


CATEGORY_MAPPING = "categories.json"


class Operations(enum.Enum):
    READ = "read"
    ADD_KEYWORD = "add keyword"
    ADD = "add"


def print_options(options: list) -> None:
    """Helper function that prints the list of `options`
    
    Args:
        options: list of options to be printed to the screen
    """
    for i in options:
        print(i)


def get_option_input(options: list, message="") -> str:
    """Helper function that asks for an input repeatedly 
    until user inputs one included in `options`

    Args:
        message: the message that will be shown in the prompt
        options: options for user input
    Return:
        a string with the option the user wrote as input
    """
    prompt1 = message or "Enter one of the following options: "
    prompt2 = "Enter option: "
    print(prompt1)
    print_options(options)
    user_input = input(prompt2)

    while user_input not in options:
        print("Enter one of the following options: ")
        print_options(options)
        user_input = input(prompt2)
    
    return user_input


def read_categories() -> dict:
    """Read categories from json and return a dict with the data
    
    Return:
        a dictionary containing the json category data
    """
    category_data = {}

    with open(CATEGORY_MAPPING) as file:
        category_data = json.loads(file.read())
        return category_data
    

def write_categories(categories: dict) -> dict:
    """Write categories to a json formatted file
    
    Args:
        categories: dictionary containing category data
    """
    with open(CATEGORY_MAPPING, "w") as file:
        category_data = json.dumps(categories, indent=4, sort_keys=True)
        file.write(category_data)


def ask_operation() -> str:
    """Determines what operation to execute based on user input

    Return:
        enum describing operation
    """
    operation_options = list(map(lambda x: x.value, Operations))
    operation = get_option_input(options=operation_options)

    return operation


def add_keyword(categories: dict, category: str, keyword: str):
    """Adds a keyword to a specific category"""
    categories[category].append(keyword)


def add_category(categories: dict, category: str):
    """Adds a new category"""
    categories[category] = []


def main():
    # read the contents of categories.json
    # ask which category you want to work in or if you want to add a new category
    # ask if you want to read the keywords under a category or to add new ones
    # if a new category is created, ask if keywords should be inserted
    categories = read_categories()
    category = get_option_input(categories, message="Select one of the categories: ")
    operation = ask_operation()

    if operation == Operations.ADD_KEYWORD.value:
        keyword = input(f"Enter a keyword for {category} category: ")
        add_keyword(categories, category, keyword)

    write_categories(categories)


if __name__ == '__main__':
    main()
