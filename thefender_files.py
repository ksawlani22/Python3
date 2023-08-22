# Import modules
import csv
import json

# List to store compromised user details
compromised_users = []

# Read the passwords.csv file
with open("passwords.csv") as password_file:
    parsed_csv = csv.DictReader(password_file)
    
    # Loop through each row in the CSV
    for password_row in parsed_csv:
        # Append username of the compromised user to our list
        compromised_users.append(password_row["Username"])

# Write the compromised usernames to a new file
with open("compromised_users.txt", "w") as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user + "\n")

# Create a message for the boss to indicate success
with open("boss_message.json", "w") as boss_message:
    boss_message_dict = {
        "recipient": "The Boss",
        "message": "Mission Success"
    }
    # Dump the message dictionary to a JSON file
    json.dump(boss_message_dict, boss_message)

# Hacker signature to be added to the new passwords file
slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""

# Write hacker signature to the new passwords file
with open("new_passwords.csv", "w") as new_passwords_obj:
    new_passwords_obj.write(slash_null_sig)
