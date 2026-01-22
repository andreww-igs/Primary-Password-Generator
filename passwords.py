from collections import defaultdict
from unicodedata import category
import sys, json, random, argparse, time


class PasswordCategory:
    def __init__(self, name: str = "default", words: list[str] = [], adjectives: list[str] = []):
        self.name = name
        self.words = words
        self.adjectives = adjectives
    
    def __str__(self) -> str:
        return f"name: {self.name} \nwords: {self.words} \nadjectives: {self.adjectives}"
    
    def has_adjectives(self) -> bool:
        return len(self.adjectives) > 0
    
    def shortest_word_length(self) -> int:
        min_length = sys.maxsize
        for word in self.words:
            if (len(word) < min_length):
                min_length = len(word)
        return min_length

    def longest_word_length(self) -> int:
        max_length = 0
        for word in self.words:
            if (len(word) > max_length):
                max_length = len(word)
        return max_length


password_categories: list[PasswordCategory] = []


def populate_password_categories():
    categories = load_categories_from_json()
    adjectives = load_adjectives_from_json()

    if (categories and adjectives):
        for category in categories:
            password_category = PasswordCategory(
                name=category['name'],
                words=category['words'],
                adjectives=adjectives.get(category.get('adjectives'), [])
            )
            password_categories.append(password_category)


def load_categories_from_json():
    try:
        with open('categories.json', 'r') as file:
            data = json.load(file)
            return data
    
    except FileNotFoundError:
        print("Error: The file 'categories.json' was not found.")


def load_adjectives_from_json():
    try:
        with open('adjectives.json', 'r') as file:
            data = json.load(file)
            return data
    
    except FileNotFoundError:
        print("Error: The file 'adjectives.json' was not found.")


def generate_password(category: PasswordCategory, use_adjective: bool, min_word_length: int, max_word_length: int) -> str:
    number = get_random_number()
    word = random.choice(category.words)

    min_word_length = min(category.longest_word_length(), min_word_length)
    max_word_length = max(category.shortest_word_length(), max_word_length)

    while (len(word) > max_word_length) or (len(word) < min_word_length):
        word = random.choice(category.words)
    
    new_password = f"{word}{number}"

    if (use_adjective):
        new_password = f"{random.choice(category.adjectives)}{new_password.capitalize()}"

    return new_password


def get_random_number(length: int = 2) -> int:
    random.seed(time.time())
    generated_number = str(random.randint(10**(length-1), (10**length)-1))
    while ("67" in str(generated_number)) or ("69" in str(generated_number)):
        generated_number = get_random_number(length)
    return int(generated_number)


def shuffle_passwords(pws: list[str]) -> list[str]:
    random.shuffle(pws)
    for i in range(1, len(pws)):
        if pws[i][0] == pws[i-1][0]:
            for j in range(i+1, len(pws)):
                if pws[j][0] != pws[i-1][0]:
                    pws[i], pws[j] = pws[j], pws[i]
                    break
    return pws


def main(arguments):
    populate_password_categories()

    number_of_passwords = arguments.num
    use_adjective = arguments.use_adjective
    force_lowercase = arguments.force_lowercase
    min_word_length = arguments.min_word_length
    max_word_length = arguments.max_word_length

    valid_categories = [category for category in password_categories if (not use_adjective or category.has_adjectives()) and (category.longest_word_length() >= min_word_length) and (category.shortest_word_length() <= max_word_length)]

    generated_passwords = []

    while (len(generated_passwords) < number_of_passwords):
        new_password = generate_password(category=random.choice(valid_categories), use_adjective=use_adjective, min_word_length=min_word_length, max_word_length=max_word_length)

        if (new_password in generated_passwords):
            new_password = generate_password(category=random.choice(valid_categories), use_adjective=use_adjective, min_word_length=min_word_length, max_word_length=max_word_length)
        
        if (force_lowercase):
            new_password = new_password.lower()
        
        generated_passwords.append(new_password)
    
    shuffled_passwords = shuffle_passwords(generated_passwords)
    
    # output to txt
    with open('generated_passwords.txt', 'w') as file:
        for password in shuffled_passwords:
            file.write(f"{password}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate random passwords.')
    parser.add_argument('--num', type=int, default=1, help='Number of passwords to generate')
    parser.add_argument('--use-adjective', action='store_true', help='Include an adjective at the beginning of the password; results will be in camelCase')
    parser.add_argument('--force-lowercase', action='store_true', help='Force all passwords to be lowercase')
    parser.add_argument('--min-word-length', type=int, default=0, help='Minimum length of the word part of the password')
    parser.add_argument('--max-word-length', type=int, default=sys.maxsize, help='Maximum length of the word part of the password')
    args = parser.parse_args()
    main(args)