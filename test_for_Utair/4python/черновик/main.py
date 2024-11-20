import subprocess
import json


result_for_only_owner = subprocess.run(["python", "get_participants_and_check_empty.py"], capture_output=True, text=True)
result_for_only_owner = result_for_only_owner.stdout.strip()
json_data = json.dumps(result_for_only_owner).replace(r'\n', ', ')
with open('only_owner.json', 'w') as file:
    file.write(json_data)



result_for_missing_users = subprocess.run(["python", "get_all_id_not_in_users.py"], capture_output=True, text=True)
result_for_missing_users =result_for_missing_users.stdout.strip()
json_data = json.dumps(result_for_missing_users).replace(r'\n', ', ')
with open('missing_users.json', 'w') as file:
    file.write(json_data)



