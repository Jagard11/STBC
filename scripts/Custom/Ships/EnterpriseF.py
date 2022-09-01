from bcdebug import debug
import Foundation
import App

#
#Foundation.ShipDef.Defiant.hasTGLName = 1
#Foundation.ShipDef.Defiant.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
# Foundation.ShipDef.Defiant.desc = 'Foundation
import App

Foundation.SoundDef("sfx/Weapons/PPhaser.wav", "PPhaser", 0.7)

# Usually, you need only edit these seven lines
abbrev = 'EnterpriseF'				# Short name, no spaces, used as a preface for descriptions
iconName = 'Century'					# Name of icon .tga file
longName = 'EnterpriseF'					# Long name with spaces
shipFile = 'EnterpriseF'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_MARAUDER			# I'm not sure how important this is.
# Thats mainly for the icon, but unused


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'EnterpriseF',			# The full name of your mod if applicable
	'author': 'EnterpriseF',					# Your name here
	'version': '1.0',						# No more than one period please!  
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://startrek.webhop.info' ],				# Source for this mod
	'comments': ''						# General info
}


Foundation.ShipDef.EnterpriseF = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.EnterpriseF.dTechs = { 'Fed Ablative Armor': {
	"Plates": ["Forward Ablative Armor", "Aft Ablative Armor", "Dorsal Ablative Armor", "Ventral Ablative Armor"]
}}
Foundation.ShipDef.EnterpriseF.sBridge = 'defiantbridge'
Foundation.ShipDef.EnterpriseF.fMaxWarp = 9.995
Foundation.ShipDef.EnterpriseF.fWarpEntryDelayTime = 3.5

if menuGroup:           Foundation.ShipDef.EnterpriseF.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.EnterpriseF.RegisterQBPlayerShipMenu(playerMenuGroup)
