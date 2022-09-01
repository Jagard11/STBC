import Foundation
import App

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.BreenDN.desc = 'oundation
import App

# Usually, you need only edit these seven lines
abbrev = 'BreenDN'				# Short name, no spaces, used as a preface for descriptions
iconName = 'BreenDN'				# Name of icon .tga file
longName = 'Breen Dreadnought'				# Long name with spaces
shipFile = 'BreenDN'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Breen Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Breen Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_SOVEREIGN		# I'm not sure how important this is.

Foundation.ShipDef.BreenDN = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.BreenDN.dTechs = { 'Breen Drainer Immune': 1 }
Foundation.ShipDef.BreenDN.fMaxWarp = 9.3
Foundation.SoundDef("sfx/Weapons/Breen1.wav", "Breen1", 1.0)
Foundation.SoundDef("sfx/Weapons/Breen2.wav", "Breen2", 1.0)
Foundation.ShipDef.BreenDN.hasTGLName = 1
Foundation.ShipDef.BreenDN.hasTGLDesc = 1

if menuGroup:			Foundation.ShipDef.BreenDN.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:		Foundation.ShipDef.BreenDN.RegisterQBPlayerShipMenu(playerMenuGroup)
