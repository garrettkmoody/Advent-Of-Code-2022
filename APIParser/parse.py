import json
from datetime import datetime

# Parse the JSON string
with open("current_status.txt") as f:
    lineInput = f.read()
    json_obj = json.loads(lineInput)

    
    # Iterate over the members in the JSON object
    for member_id, member_info in json_obj['members'].items():
        # Print the member's ID and name
        print("ID:", member_id)
        print("Name:", member_info['name'])

        # Print the member's star information
        print("Stars:", member_info['stars'])
        print("Local score:", member_info['local_score'])
        print("Global score:", member_info['global_score'])

        # Convert the Unix timestamp to a readable date and time
        last_star_ts = datetime.fromtimestamp(member_info['last_star_ts'])
        print("Last star timestamp:", last_star_ts)

        # Print the member's completion day level information
        print("Completion day level:")
        for day, day_info in member_info['completion_day_level'].items():
            print("Day", day)
            for level, level_info in day_info.items():
                print("Level", level)
                print("Star index:", level_info['star_index'])

                # Convert the Unix timestamp to a readable date and time
                get_star_ts = datetime.fromtimestamp(level_info['get_star_ts'])
                print("Get star timestamp:", get_star_ts)

        print()  # Add a blank line between each member's information