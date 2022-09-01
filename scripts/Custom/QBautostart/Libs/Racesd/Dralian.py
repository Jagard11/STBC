##########################################################################################################################
#        Race Plugin script   (created by the Race Plugin Creator Tool (v1.0.0.0)
###########
# this script sets up a race and info about her that some mods like Construct, Distress Signal (Distress call), and
# Galaxy Charts uses, to get a race's ship, escorts, and other things.
##########################################################################################################################

########
##  Name of this race
sName = "Dralian"

########
## List of strings containing the names of the enemy races  (put a "ALL" to make it enemy to everybody)
lEnemies = ["Borg", "Federation", "Vaadwaur", ]

########
## List of strings containing the names of the friendly races
lFriendlies = ["Dinaali", "Talaxian", ]

########
## a float representing the peace value  (in the range of 0 to 1, being 1 the most peacefull races )
fPeaceValue = 0.60

########
## the name of the ship selecting menu (you know, in QuickBattle), in which we can look for ships to add to this race
sLookInMenu = "Delta Quadrant Ships"

########
## list of the ship script name  of ships of this race, to be added manually (that is, besides looking in the above 
## mentioned menu)
lDefaultShips = ["JLSDralian", ]

########
## dictionary showing the escorts of a ship class  (for a example, check the Dominion race script)
## "ship class to be escorted": list of ship classes that escort it
dEscorts = {
}

########
## list of the ship script name of starbase ships of this race, to be added manually (that is, besides looking in the
## above mentioned menu)
lDefaultBases = []

########
## the name of the ship selecting menu (you know, in QuickBattle), in which we can look for ships to add to this race
sInitialShipBuild = ""

########
## Dictionary of resources of this race
## "resource name": amount of resources
dResources = {
}

########
## A list of names of ships of this race
lShipNames = [
"Gars Ship",
]

## We are all done now. The Races script will take care of setting up the RaceInfo objects.
