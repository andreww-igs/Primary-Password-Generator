## How to Use

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