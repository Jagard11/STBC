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
abbrev = 'DJValiant'				# Short name, no spaces, used as a preface for descriptions
iconName = 'DJValiant'					# Name of icon .tga file
longName = 'DJValiant'					# Long name with spaces
shipFile = 'DJValiant'				# Name of the file in Scripts\Ships\ to use.
menuGroup = 'Fed Ships'			# Menu to appear under in Quick Battle
playerMenuGroup = 'Fed Ships'		# ...set to None if you don't want to appear here.
species = App.SPECIES_MARAUDER			# I'm not sure how important this is.
# Thats mainly for the icon, but unused


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.
credits = {
	'modName': 'DJValiant',			# The full name of your mod if applicable
	'author': 'DJValiant',					# Your name here
	'version': '0.7',						# No more than one period please!  
										# I'd like to be able to do a numeric comparison.
	'sources': [ 'http://startrek.webhop.info' ],				# Source for this mod
	'comments': ''						# General info
}


Foundation.ShipDef.DJValiant = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.DJValiant.dTechs = { 'Fed Ablative Armor': {
	"Plates": ["Aft Ablative Armor", "Forward Ablative Armor", "Left Ablative Armor", "Right Ablative Armor"]
}}
Foundation.ShipDef.DJValiant.sBridge = 'defiantbridge'
Foundation.ShipDef.DJValiant.fMaxWarp = 9.5
Foundation.ShipDef.DJValiant.fWarpEntryDelayTime = 2.0

if menuGroup:           Foundation.ShipDef.DJValiant.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DJValiant.RegisterQBPlayerShipMenu(playerMenuGroup)
