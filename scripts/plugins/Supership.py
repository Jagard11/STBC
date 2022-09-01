import Foundation
import App
# Usually, you need only edit these seven lines

abbrev = 'Supership'
iconName = 'Supership'
longName = 'Fed Warship'
shipFile = 'Supership' 
menuGroup = 'War Ships'
playerMenuGroup = 'War Ships'
species = App.SPECIES_GALAXY


# Mod info.  Use this as an opportunity to describe your work in brief.  This may have
# use later on for updates and such.

credits = {
	'modName': 'Supership',   # The full name of your mod if applicable
	'author': 'Shipyard4',              # Your name here
	'version': '0.9 Beta',                     # No more than one period please!
	                                      # I'd like to be able to do a numeric comparison.
	'sources': [ 'http://www.STARYARDS.com' ],             # Source for this mod
	'comments': ''                        # General info
}

# Uncomment (remove the # symbol from) the line which has a ShipDef you want.
# A generic ship should use ShipDef.  If you want a Federation Ship, put a #
# in front of the first line and uncomment the line with FedShipDef.

Foundation.ShipDef.Supership = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })

# These register the ship with the QuickBattle menus.  Don't touch them.
if menuGroup:           Foundation.ShipDef.Supership.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Supership.RegisterQBPlayerShipMenu(playerMenuGroup)

Foundation.SoundDef("sfx/Weapons/Transphasic.wav", "Transphasic", 1)

Foundation.SoundDef("sfx/Weapons/tricobolt.WAV", "tricobolt", 2)

Foundation.SoundDef("sfx/Weapons/PulsePhsr.wav", "PulsePhsr", 3)

