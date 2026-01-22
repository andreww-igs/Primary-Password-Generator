## How to Use

### Generating passwords with Python script

1. Clone Github repo
2. Run `python3 passwords.py` to generate passwords which will be saved to `generated_passwords.txt`

The script supports several CLI arguments to customise the number of passwords generated, their length, whether an adjective should be applied, etc.

| Argument            | Type      | Description                                                                         |
|---------------------|-----------|-------------------------------------------------------------------------------------|
| `--num`             | `integer` | Number of passwords to be generated                                                 |
| `--force-lowercase` | `boolean` | Force all passwords to be lowercase                                                 |
| `--use-adjective`   | `boolean` | Include an adjective at the beginning of the password; results will be in camelCase |
| `-min-word-length`  | `integer` | Minimum length of the word part of the password                                     |
| `-max-word-length`  | `integer` | Maximum length of the word part of the password                                     |

Modify the JSON files to suit your preferences. There are two: `adjectives.json` and `categories.json`.

In the `categories.json` file you may specify an `adjectives` value, which will be used when the `--use-adjective` argument is provided.

### Create Google Sheet spreadsheet

1. Create a new Google Sheet
2. Run `SelectStudentsForPasswordSpreadsheet.sql` query against the Identity1 database to get all current primary students (KG-6) in the correct format
3. Copy + paste into Google Sheets
4. Copy + paste passwords from the `generated_passwords.txt` file
5. Share with relevant teachers

### Set passwords in Active Directory

1. Create a .CSV with two columns: `UPN` and `password`
2. For every student in the spreadsheet grab their email address as the UPN and the relevant password
3. Edit `SetPrimaryPasswords.ps1` to point to your CSV
4. Run the PowerShell script to set passwords; bear in mind you will need to run PowerShell/PowerShell ISE as an administrator and ensure you have sufficient permissions in AD (e.g. Global Admin)