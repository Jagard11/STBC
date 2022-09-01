from bcdebug import debug
##########################################################################################################################
#        Race Plugin script   (created by the Race Plugin Creator Tool (v1.0.0.0)
###########
# this script sets up a race and info about her that some mods like Construct, Distress Signal (Distress call), and
# Galaxy Charts uses, to get a race's ship, escorts, and other things.
##########################################################################################################################

########
##  Name of this race
sName = "Romulan"

########
## List of strings containing the names of the enemy races  (put a "ALL" to make it enemy to everybody)
lEnemies = ["Borg", "Breen", "Cardassian", "Dominion", "8472", "Sona", "Federation", "Klingon"]

########
## List of strings containing the names of the friendly races
lFriendlies = []

########
## a float representing the peace value  (in the range of 0 to 1, being 1 the most peacefull races )
fPeaceValue = 0.40

########
## the name of the ship selecting menu (you know, in QuickBattle), in which we can look for ships to add to this race
sLookInMenu = "Romulan Ships"

########
## list of the ship script name  of ships of this race, to be added manually (that is, besides looking in the above 
## mentioned menu)
lDefaultShips = ["Warbird", "Falcon", "Firehawk", "LCRaptor", "Praetor", "Reman Scimitar", "Shrike", "ValdoreG", "VasKholhr", "griffin", "romulanshuttle", "venator", "Scimitar", ]

########
## dictionary showing the escorts of a ship class  (for a example, check the Dominion race script)
## "ship class to be escorted": list of ship classes that escort it
dEscorts = {
}

########
## list of the ship script name of starbase ships of this race, to be added manually (that is, besides looking in the
## above mentioned menu)
lDefaultBases = ["RomulanOutpost", ]

########
## the name of the ship selecting menu (you know, in QuickBattle), in which we can look for ships to add to this race
sInitialShipBuild = "romulanshuttle"

########
## Dictionary of resources of this race
## "resource name": amount of resources
dResources = {
}

########
## A list of names of ships of this race
lShipNames = [
"Adrodius",
"Anturunia",
"Avarek",
"Avenius",
"Bandis",
"Celleius",
"Copidius",
"Dejerek",
"D'lassus",
"D'oras",
"D'pas",
"D'relan",
"D'thal",
"D'yl",
"Equitus",
"Flardius",
"Grocus",
"Imderia",
"Infini",
"Inydar",
"Irixidon",
"Kellem",
"Kerata",
"Kessar",
"Lemal",
"Lirilius",
"Lossal",
"Lukan",
"Marrus",
"Meret",
"Metollis",
"Nucarrus",
"Pespedius",
"Quarius",
"Rumaal",
"Seres",
"Suratak",
"S'alpal",
"S'pala",
"S'paut",
"Theron",
"Toralan",
"T'ala",
"T'anis",
"T'endadar",
"T'lasadon",
"T'mera",
"T'nar",
"T'onara",
"T'ossan",
"T'rarn",
"T'rassis",
"T'salin",
"T'san",
"T'sassan",
"T'varian",
"Vastar",
"Vestela",
"V'ashnu",
"V'eshan",
"V'laneth",
"V'lrath",
"V'tar",
"V'terex",
]

## We are all done now. The Races script will take care of setting up the RaceInfo objects.
