# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Fawaz"
my_age = 23
my_bio = "Computer Nerd"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)

def options():
	repeat = False
	while(True):
		if repeat == False:
			print("---------------------------\nWould you like to:")
			opt = input("1) Create a new club.\n2) Browse and join clubs.\n3) View existing clubs.\n4) Display members of a club.\n-1) Close application.\n> ")
		else:
			repeat = False
			opt = input("> ")
		if opt == '1':
			create_club()
		elif opt == '2':
			join_clubs()
		elif opt == '3':
			view_clubs()
			input("Press \"Enter\" to continue.")
		elif opt == '4':
			view_club_members()
		elif opt == '-1':
			break
		else:
			print("Invalid option!")
			repeat = True

def create_club():
    name = input("What is your club name?\n> ")
    desc = input("What will it be about?\n> ")
    club = Club(name, desc)
    clubs.append(club)
    print("Type the number of the person that you would like to add to your club, and type \"-1\" when you are done.\n----------------------------------------------")
    iteration = 1
    for person in population:
    	print("[%d] %s" %(iteration ,person.name))
    	iteration += 1
    while(True):
    	opt = int(input("> "))
    	if opt > 0 and opt < iteration:
    		for member in club.members:
    			if member.name == population[opt - 1].name:
    				print("That member is already in your club.")
    				break
    		else:
    			club.recruit_member(population[opt - 1])
    	elif opt == -1:
    		break
    	else:
    		print("Invalid option, try again.")
    club.assign_president(myself)
    club.recruit_member(myself)
    print("Here is your club: \nClub name: %s \nClub description: %s \nMembers:" %(club.name, club.description))
    club.print_member_list()
    total_age = 0.0
    for member in club.members:
    	total_age += member.age
    print("Average age in this club is: %.1fyr" %(total_age / len(club.members)))

    

def view_clubs():
	for club in clubs:
		print("      Name: %s \n      Desciption: %s \n      Members: %d\n" %(club.name, club.description, len(club.members)))
	
    

def view_club_members():
	view_clubs()
	print("Type the name of the club that you would like to view its members.")
	while(True):
		opt = input("> ")
		for club in clubs:
			if opt.lower() == club.name.lower():
				club.print_member_list()
				input("Press \"Enter\" to continue.")
				return
		else:
			print("Invalid option, try again.")

    
    

def join_clubs():
	view_clubs()
	print("Type the name of the club that you would like to join.")
	while(True):
		opt = input("> ")
		for club in clubs:
			if opt.lower() == club.name.lower():
				for member in club.members:
					if member.name == myself.name:
						print("You are already in that club.")
						return
				else:
					club.members.append(myself)
					print("%s has joined %s" %(myself.name, club.name))
					return
		else:
			print("Invalid option, try again.")
    

def application():
    introduction()
    options()

    
    
