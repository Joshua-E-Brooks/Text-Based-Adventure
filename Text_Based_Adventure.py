class Room(object):
	def __init__(self, description, items, exits):
		self.description = description
		self.items = items
		self.exits = exits
	
	def __repr__(self):
		listExits = ""
		if len(self.exits) == 1:
			listExits = "There is an exit to the " + self.exits[0]
		else:
			listExits = "There are exits to the " + self.exits[0] + " and " + self.exits[1]
		if len(self.items) > 0:	
			listItems = "There is "
			for i in range(len(self.items)):
				first = self.items[i][0]
				if first == "a" or first == "e" or first == "i" or first == "o" or first == "u":
					listItems += "an " + self.items[i]
				else:
					listItems += "a " + self.items[i]
				if i < len(self.items)-2:
					listItems += ", "
				elif i < len(self.items)-1:
					listItems += " and "
				else:
					listItems += " here."
			return self.description + "\n" + listItems + "\n" + listExits
		else:
			return self.description + "\n" + listExits
		
def pickupObject (item, myRoom, backpack):
        if item in myRoom.items:
                backpack.append(item)
                myRoom.items.remove(item)
                print ("I've picked up the " + item)
        elif item in backpack:
                print("I'm already carrying it!")
        else:
                print ("I don't see that here.")

cell = Room("You are in a dark, damp cell with a small bulb as the only light source, a still body is in the corner.",["Body","Key"], ["South"])
#
hall = Room("The hall is mostly empty except a guard that sometimes patrols", ["Piece of cell"], ["South","East"])
#
laundry = Room("You regularly do work here and know the layout well, no guards patrol here. A large washing machine is in the corner.",["uniform"],["South", "West"])
#
entrance_office = Room("A dark, wooden door stands between you and the officer's office, but suprisingly, the key is in the door and it is slightly open.",["Key"],["East","South"])
#
staff = Room ("No prisoners have ever been down here, so you have no clue how to get around, lots of warning signs are placed around and at the end is a door",[""],["South"])
#
office = Room ("A small but beautiful room filled with contraband items and pictures of his family. The old officer was kind, a large, geordie mand with a strange way of saying 'book'. But the new officer is a tyrant, a tall,skinny ginger man with a loud voice.",["fidget spinner", "firework"],["South"])
#
coridoor = Room ("A white corridor with muffled screams that can be heard all down the corridor, if you continue, you cannot go back.",[""],["South"])
#
grounds = Room ("The ground are bleak and grey, a broken basketball post stands alone and the fencing aound is broken",[""],["South"])
#
testing = Room ("There is no going back, the screams are clearer now and the smell is rotten, this is where the other prisoners are",[""],["South"])
#
entrance = Room ("A car is seen in the distance, a police car. But also are two guards, fully loaded with machine guns and ballistic vests, you would have to create a distraction or have some disguise.",[""],["South"])
#
hell = Room ("The walls are red with blood, bodies are everywhere, and dismembered limbs hang off the recently deceased corpses. You realise you have to escape, but how? The only way out is to go through one of the tests to the exit.",[""],["South"])
#

currentRoom = "cell"

playingGame = True

backpack = []



while playingGame == True:
        while currentRoom == "cell":
                print(cell)
                userInput = input(">")
                if userInput == "south":
                        currentRoom = "hall"
                elif (userInput == "north") or (userInput == "east") or (userInput == "west"):
                        print ("Are you stupid? There is a wall there!")
                elif "pickup" == userInput:
                        pickupObject(userInput[8:len(userInput)], cell, backpack)
                else:

                        print ("Please, don't be stupid, only moving around or picking things up :)")
               
                       
               
        while currentRoom == "hall":
                print(hall)
                userInput = input(">")
                if userInput == "south":
                        currentRoom = "entrance_office"
                elif userInput == "north":
                        currentRoom = "cell"
                elif userInput == "east":
                        currentRoom = "laundry"
                elif (userInput == "west") :
                        print ("Are you stupid? There is a wall there!")
                elif "pickup" in userInput:
                        pickupObject(userInput[8:len(userInput)], hall, backpack)
                else:
                        print ("Please, don't be stupid, only moving around or picking things up :)")
    
        while currentRoom == "laundry":
                print(laundry)
                userInput = input(">")
                if userInput == "south":
                        currentRoom = "staff"
                if userInput == "west":
                        currentRoom = "hall"
                elif (userInput == "east") or (userInput == "north") :
                        print ("Are you stupid? There is a wall there!")
                elif "pickup" in userInput:
                        pickupObject(userInput[8:len(userInput)], laundry, backpack)
                else:
                        print ("Please, don't be stupid, only moving around or picking things up :)")           

        while currentRoom == "entrance_office":
                print(entrance_office)
                userInput = input(">")
                if userInput == "south":
                        currentRoom = "office"
                elif userInput == "north":
                        currentRoom = "hall"
                elif userInput == "east":
                        currentRoom = "staff"
                elif (userInput == "west") :
                        print ("Are you stupid? There is a wall there!")
                elif "pickup" in userInput:
                        pickupObject(userInput[8:len(userInput)], entrance_office, backpack)
                else:
                        print ("Please, don't be stupid, only moving around or picking things up :)")

               
    
        while currentRoom == "staff":
                print(staff)
                userInput = input(">")
                if userInput == "south":
                        currentRoom = "corridor"
                elif userInput == "north":
                        currentRoom = "laundry"
                elif userInput == "west":
                        currentRoom = "entrance_office"
                elif (userInput == "east") :
                        print ("Are you stupid? There is a wall there!")
                elif "pickup" in userInput:
                        pickupObject(userInput[8:len(userInput)], staff, backpack)
                else:   
                        print ("Please, don't be stupid, only moving around or picking things up :)")


    
        while currentRoom == "office":
                print(office)
                userInput = input(">")
                if userInput == "south":
                        currentRoom = "grounds"
                elif userInput == "north":
                        currentRoom = "office"
                elif (userInput == "west") or (userInput == "east") :
                        print ("Are you stupid? There is a wall there!")
                elif "pickup" in userInput:
                        pickupObject(userInput[8:len(userInput)], grounds, backpack)
                else:
                        print ("Please, don't be stupid, only moving around or picking things up :)")



        while currentRoom == "coridoor":
                print(entrance_office)
                userInput = input(">")
                if userInput == "south":
                        currentRoom = "testing"
                elif userInput == "north":
                        currentRoom = "staff"
                elif (userInput == "west") or (userInput == "east") :
                        print ("Are you stupid? There is a wall there!")
                elif "pickup" in userInput:
                        pickupObject(userInput[8:len(userInput)], coridoor, backpack)
                else:
                        print ("Please, don't be stupid, only moving around or picking things up :)")

        while currentRoom == "testing":
                print(testing)
                userInput = input(">")
                if userInput == "south":
                        currentRoom = "hell"
                elif userInput == "north":
                        print ("YOU CANNOT RETURN")
                elif (userInput == "west") or (userInput == "east"):
                        print ("Are you stupid? There is a wall there!")
                elif "pickup" in userInput:
                        pickupObject(userInput[8:len(userInput)], testing, backpack)
                else:
                        print ("Please, don't be stupid, only moving around or picking things up :)")

    
        while currentRoom == "entrance":
                print(entrance_office)
                userInput = input(">")
                if userInput == "north":
                        currentRoom = "grounds"
                elif userInput == "east":
                        currentRoom = "hell"
                elif (userInput == "west") :
                        print ("Are you stupid? There is a wall there!")
                elif "pickup" in userInput:
                        pickupObject(userInput[8:len(userInput)], entrance, backpack)
                elif userInput == "use uniform":
                        if "uniform" in backpack:
                                print ("You wear the stolen uniform and escape in a stolen police cruiser, the other officers only glanced at you. Free finally, never to return to that horrid prison, but... you will never know what happened to the other...")
                                playingGame = False
                                break
                else:
                        print ("Please, don't be stupid, only moving around or picking things up :)")

        
        while currentRoom == "hell":
                print(hell)
                userInput = input(">")
                if userInput == "north":
                        print ("YOU CANNOT GO BACK NOW!")
                elif userInput == "south":
                        currentRoom = "win2"
                elif (userInput == "west") or (userInput == "east") or (userInput == "north") :
                        print ("Are you stupid? There is a wall there!")
                elif "pickup" in userInput:
                        pickupObject(userInput[8:len(userInput)], hell, backpack)
                else:
                        print ("Please, don't be stupid, only moving around or picking things up :)")
