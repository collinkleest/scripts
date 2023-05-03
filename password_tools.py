import argparse
import os
import json


def load_file(file_path):
    """Load a file from disk as JSON."""
    with open(file_path, 'r') as f:
        return json.load(f)


def validate_file(file_path, file_extension):
    """Validate that a file exists and has the correct extension."""
    if not os.path.exists(file_path):
        print(f"Error: File path '{file_path}' does not exist.")
        exit(1)

    if os.path.splitext(file_path)[1] != file_extension:
        print(f"Error: File extension '{file_extension}' does not match the actual extension of the file.")
        exit(1)


def find_duplicate_passwords(data):
    """Find duplicate passwords in a LastPass JSON file."""
    password_counts = {}
    duplicate_passwords = []

    for item in data['items']:
        if 'login' in item and 'password' in item['login']:
            password = item['login']['password']
            if password in password_counts:
                password_counts[password] += 1
                if password_counts[password] == 2:
                    duplicate_passwords.append(password)
            else:
                password_counts[password] = 1

    return duplicate_passwords

def get_item_uri(item):
    return item['login']['uris'][0]['uri'] if 'uris' in item['login'] and len(item['login']['uris'])> 0 else 'no uri'

def print_duplicate_password_items(data, duplicate_passwords):
    """Print the names and passwords of items with duplicate passwords."""
    for item in data['items']:
        if 'login' in item and 'password' in item['login']:
            password = item['login']['password']
            uri = get_item_uri(item)
            if password in duplicate_passwords:
                print(f"{item['name']}: {password} | {uri}")

# Define the valid file extensions
VALID_EXTENSIONS = ['.json', '.xml', '.csv']

# Define the valid vault types
VALID_VAULT_TYPES = ['lastpass', 'bitwarden', 'onepassword']

# Define the arguments for the script
parser = argparse.ArgumentParser(description='Process some files.')
parser.add_argument('-v', '--vault_type', type=str, choices=VALID_VAULT_TYPES, help='the type of vault')
parser.add_argument('-f', '--file_path', type=str, help='the file path')
parser.add_argument('-e', '--extension', type=str, choices=VALID_EXTENSIONS, help='the file extension')
parser.add_argument('-d', '--duplicates', action='store_true', help='check for duplicate passwords')

# Parse the arguments
args = parser.parse_args()

# If no file extension is specified, try to infer it from the file path
if not args.extension:
    args.extension = os.path.splitext(args.file_path)[1]

# Validate the file path and extension
validate_file(args.file_path, args.extension)

# Load the file
data = load_file(args.file_path)

# Check for duplicate passwords
if args.duplicates:
    if args.vault_type != 'bitwarden':
        print("Error: Checking for duplicate passwords is only supported for bitwarden vaults.")
        exit(1)

    duplicate_passwords = find_duplicate_passwords(data)

    if len(duplicate_passwords) > 0:
        print(f"Found {len(duplicate_passwords)} items with duplicate passwords:")
        print_duplicate_password_items(data, duplicate_passwords)
    else:
        print("No items found with duplicate passwords.")