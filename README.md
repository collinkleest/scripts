# scripts
Repository for scripts in bash and python. 


## Dynamic DNS Script
A script for dynamically updating web servers ip address with google domains

### Usage 
Make sure you install the requirements in `requirements.txt` and set necessary environment variables in a `.env` file.

```bash
pip install -r requirements.txt
python ddns-update.py
```

### Environment Variables
```
DDNS_USERNAME=<username given by google>
DDNS_PASSWORD=<password given by google>
GOOGLE_HOSTNAME=<should be domains.google.com>
PERSONAL_HOSTNAME=<personal hostname registered with google domains, can also be subdomain>
```

## gorilla-bot script
Gorilla Mind Product Bot

## Usage
Set all configuration in `config.json`
```json
{
    "targetProducts": [
        "Gorilla Mode Nitric" // target products to monitor
    ],
    "targetProductPages": [
        "https://gorillamind.com/collections/supplements/products/gorilla-mode" // target product links to monitor 
    ],
    "targetPhones": [
        "+11234567890" // target phone numbers to send notification
    ]
}
```

Install dependencies and run bot file
```bash
pip install -r requirements.txt
python3 gorilla-bot.py
```

## Environment Variables
```
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_NUMBER=
```

# Password Vault Analyzer<a name="password-vault-analyzer"></a>
A command-line script for analyzing password vault files.

# Table of Contents

- [Password Vault Analyzer](#password-vault-analyzer)
  - [Usage](#usage)
    - [Positional Arguments](#positional-arguments)
    - [Optional Arguments](#optional-arguments)
  - [Installation](#installation)
  - [Example Usage](#example-usage)
  - [Supported Password Vaults](#supported-password-vaults)
  - [Valid File Extensions](#valid-file-extensions)
  - [Contributing](#contributing)

## Usage <a name="usage"></a>
```bash
python password_vault_analyzer.py [-h] [-e {json,xml,csv}] [-d] vault_type file_path
```

Positional Arguments:<a name="positional-arguments"></a>
* vault_type: The type of password vault (lastpass, bitwarden, onepassword).
* file_path: The path to the password vault file.

Optional Arguments: <a name="optional-arguments"></a>
* -h, --help: Show the help message and exit.
* -e {json,xml,csv}, --extension {json,xml,csv}: The file extension (json, xml, or csv). If not specified, the script will try to infer it from the file path.
* -d, --duplicates: Check for duplicate passwords. This option is only available for LastPass vaults.

### Installation <a name="installation"></a>
Clone this repository to your local machine.
1. Navigate to the cloned repository directory in your terminal.
2. Install the required Python packages by running the following command: pip install -r requirements.txt

### Example Usage <a name="example-usage"></a>
Check for duplicate passwords in a LastPass vault:
```bash
python password_vault_analyzer.py lastpass lastpass_vault.json -d
```

Analyze a Bitwarden vault file:

```bash
python password_vault_analyzer.py bitwarden bitwarden_vault.xml -e xml
```

Analyze a 1Password vault file:

```bash
python password_vault_analyzer.py onepassword onepassword_vault.csv -e csv
```

Supported Password Vaults<a name="password-vault-analyzer"></a>
This script currently supports the following password vault types:

- LastPass
- Bitwarden
- 1Password

Valid File Extensions<a name="valid-file-extensions"></a>
This script currently supports the following file extensions:

- .json (for LastPass vaults)
- .xml (for Bitwarden vaults)
- .csv (for 1Password vaults)

Contributing<a name="contributing"></a>
Contributions are welcome! If you find a bug or would like to suggest a new feature, please create a new issue or submit a pull request.