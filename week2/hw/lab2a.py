###########################################################################

#Logan Stoddard
#Lab 1
#1/15/2024

############################################################################

import csv

def process_rooms(file_path):
    # Lists to store rooms over the limit and their details
    over_limit_rooms = []
    
    # Variables to keep track of total records and rooms over the limit
    total_recs = 0
    over_limit_count = 0

    # Open the CSV file and read its content
    with open(file_path, 'r') as csv_file:
        file = csv.reader(csv_file)
        next(file)  # Skip the header row if it exists

        # Iterate through each row in the CSV file
        for row in file:
            total_recs += 1
            room, max_cap, current_reg = row
            max_cap = int(max_cap)
            current_reg = int(current_reg)

            # Check if the room is over the limit
            if current_reg > max_cap:
                over_limit_count += 1
                over_limit_rooms.append({'room': room,'max_capacity': max_cap,'current_registered': current_reg,'over': current_reg - max_cap})

    # Display header
    print("{:<20} {:<15} {:<15} {:<15}".format("Room", "Max", "Min", "Over"))

    # Display rooms over the limit
    for room_info in over_limit_rooms:
        print("{:<20} {:<15} {:<15} {:<15}".format(
            room_info['room'],
            room_info['max_capacity'],
            room_info['current_registered'],
            room_info['over']
        ))

    # Display summary information
    print("\nSummary:")
    print(f"Number of records processed: {total_recs}")
    print(f"Number of rooms over the limit: {over_limit_count}")

process_rooms('week2/hw/lab2a.csv')
