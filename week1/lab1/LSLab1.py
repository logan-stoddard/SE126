###########################################################################
#Logan Stoddard
#Lab 1
#1/15/2024
#Varibles
#       People = Number of people
#       maxcap = Maximmun number of people that can be in the room
#       meeting_name = Name of the meeting
#       room_capacity = 
#       peopleattending = Amount of people attending the meeting

################################################################################



# Part 1
def difference(people, max_cap):
    return people - max_cap

# Part 2
def decision(response):
    while response.lower() not in ['y', 'n']:
        print("Invalid input. Please enter 'y' or 'n'.")
        response = input("Do you want to continue? (y/n): ")
    return response.lower()

# Part 3
def main():
    while True:
        meeting_name = input("Enter the meeting name: ")
        room_capacity = int(input("What is the room capacity: "))
        people_attending = int(input("How many people are attending the meeting: "))

        diff = difference(people_attending, room_capacity)

        if diff <= 0:
            print("The meeting '{meeting_name}' meets fire safety regulations.")
            print("{abs(diff)} people can be added to the meeting.")
        else:
            print("The meeting '{meeting_name}' does not meet fire safety regulations.")
            print("{abs(diff)} people must be removed from the meeting.")

        response = decision(input("Do you want to check another meeting? (y/n): "))

        if response == 'n':
            print("Goodbye!")
            break

if name == "main":
    main()
