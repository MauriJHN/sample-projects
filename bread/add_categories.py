import json
import enum


CATEGORY_MAPPING = "categories.json"

class PromptOptions(enum.Enum):
    READ = "read"
    WRITE = "write"
    ADD = "add"


def print_options(options: list) -> None:
    """Helper function that prints the list of `options`
    
    Args:
        options: list of options to be printed to the screen
    """
    for i in options:
        print(i)


def get_option_input(options: list) -> str:
    """Helper function that asks for an input repeatedly 
    until user inputs one included in `options`

    Args:
        message: the message that will be shown in the prompt
        options: options for user input
    Return:
        a string with the option the user wrote as input
    """
    print("Enter one of the following options: ")
    print_options(options)
    user_input = input("Enter option: ")

    while user_input not in options:
        print("Enter one of the following options: ")
        print_options(options)
        user_input = input("Enter option: ")
    
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
    

def ask_operation(category_data: dict) -> str:
    """Determines what operation to execute based on user input

    Return:
        enum describing operation
    """
    operation_options = list(map(lambda x: x.value, PromptOptions))
    operation = get_option_input(options=operation_options)

    return operation
        

def main():
    # read the contents of categories.json
    # ask which category you want to work in or if you want to add a new category
    # ask if you want to read the keywords under a category or to add new ones
    # if a new category is created, ask if keywords should be inserted
    ask_operation({})


if __name__ == '__main__':
    main()
