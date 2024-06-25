import requests
import colorama
from colorama import Fore, Style

# The colorama module will need installing via the terminal. To do this, enter the below command:
# pip install colorama (See README.md for an example).

# The below function is fetching the data from the Dictionary API.
def fetch_dictionary_data(word):
    endpoint = 'https://api.dictionaryapi.dev/api/v2/entries/en/' + word
    response = requests.get(endpoint)
    return response.json()

# This function prints the meanings of each word.
def print_meanings(data):
    meanings_output = []
    for type_data in data['meanings']:
        word_type = type_data['partOfSpeech']
        definitions = type_data['definitions']

        word_type_capitalized = word_type.capitalize()

        if definitions:
            definition_data = definitions[0]
            definition = definition_data['definition']
            if len(definition) > 500:
                definition = definition[:500] + '...'  # Slice definition to limit length

            meanings_output.append(Fore.GREEN + word_type_capitalized + Style.RESET_ALL + " : " + definition + "\n")

            if 'example' in definition_data:
                meanings_output.append(
                    Fore.BLUE + 'Example:' + Style.RESET_ALL + ' ' + definition_data['example'] + "\n")

            meanings_output.append("\n")  # Add a new line between the word types.
        else:
            meanings_output.append(Fore.RED + f"No definition found for '{word_type}'." + Style.RESET_ALL + "\n")
    return "".join(meanings_output)


# This is accepting an input from the user and storing it to the variable 'word'
word = input(Fore.BLUE + "Welcome to our Online English Dictionary 📖!" + Style.RESET_ALL + "\nPlease enter a word: ")

confirm = input("You've entered " + Fore.BLUE + f"{word.capitalize()}" + Style.RESET_ALL + ". Is that correct? y/n ")
if confirm.lower() != 'y':
    print(Fore.RED + "Please restart the program and enter the correct word.")
    exit()

result = fetch_dictionary_data(word)

if isinstance(result, list) and result:
    data = result[0]
    print("\nShowing results for: " + Fore.BLUE + f"{data['word'].capitalize()}" + Style.RESET_ALL)
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    print(Fore.BLUE + 'Definition:' + Style.RESET_ALL)
    print("♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")
    meanings_output = print_meanings(data)
    print(f"{meanings_output}♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥")

    # The below block writes to the final_results.txt file. Instead of including encoding, I decided not to print
    # that to make it easier to read.
    final_results_file = "final_results.txt"
    with open(final_results_file, "w") as file:
        file.write("\nShowing results for: " + f"{data['word'].capitalize()}\n")
        file.write('Definition:\n')
        file.write(meanings_output)

    print(Fore.GREEN + f"Your results have been saved in {final_results_file}" + Style.RESET_ALL)
else:
    print(Fore.RED + f"No results found for the word '{word}'. Please check the spelling or try a different word." + Style.RESET_ALL)