import json
import enum


CATEGORY_MAPPING = "categories.json"


class ModifyOptions(enum.Enum):
    READ_KEYWORDS = "read keywords"
    ADD_KEYWORD = "add keyword"


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
    operation_options = list(map(lambda x: x.value, ModifyOptions))
    operation = get_option_input(options=operation_options)

    return operation


def add_keyword(categories: dict, category: str, keyword: str) -> None:
    """Adds a keyword to a specific category
    
    Args:
        categories: dictionary containing category data
        category: category where keywords are going to be added
        keyword: keyword to be added
    """
    categories[category].append(keyword)


def add_category(categories: dict, category: str) -> None:
    """Adds a new category
    
    Args:
        categories: dictionary containing category data
        category: category where keywords are going to be added
    """
    categories[category] = []


def yes_no_input(message: str) -> bool:
    """Helper function to get a yes or no input
    
    Args:
        message: the message displayed in the prompt
    Returns:
        True if 'yes' or False if 'no' input
    """
    accepted_answers = ["yes", "y", "no", "n"]
    answer = input(message)

    while answer.lower() not in accepted_answers:
        print(f"Please enter one of the following: {', '.join(accepted_answers)}")
        answer = input(message)

    if answer.lower() in accepted_answers[:2]:
        return True
    
    if answer.lower() in accepted_answers[2:]:
        return False


def main() -> None:
    categories = read_categories()
    add_new_category = yes_no_input("Would you like to add a new category?: ")


    # TODO: create a logic to decide whether to add new category and end program or 
    #       add new keyword and end program
    if add_new_category:
        new_category = input("Please enter the new category: ")
        add_category(categories, category=new_category)
        add_new_keyword = yes_no_input(f"Would you like to input keywords for {new_category}?: ")
        if add_new_keyword:
            new_keyword = input(f"Enter a keyword for {new_category} category: ")
            add_keyword(categories, category=new_category, keyword=new_keyword)

    category = get_option_input(categories, message="Select one of the categories: ")
    operation = ask_operation()

    if operation == ModifyOptions.ADD_KEYWORD.value:
        keyword = input(f"Enter a keyword for {category} category: ")
        add_keyword(categories, category, keyword)

    if operation == ModifyOptions.READ_KEYWORDS.value:
        print_options(categories[category])

    write_categories(categories)


if __name__ == '__main__':
    main()
