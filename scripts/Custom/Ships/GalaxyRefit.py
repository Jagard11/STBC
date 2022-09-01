#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "GalaxyRefit"
iconName = "GalaxyRefit"
longName = "RBG GalaxyRefit"
shipFile = "GalaxyRefit"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.GalaxyRefit = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.GalaxyRefit.desc = "This is a Retro Badger update to the original Galaxy Class Refit Mod. With uograded Weapons and Shields, this fully represents a Dominion War Upgrade Galaxy Class. Lets see what this Galaxy Class Starship can do - Jean-Luc Picard"


if menuGroup:           Foundation.ShipDef.GalaxyRefit.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.GalaxyRefit.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
