#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSKrenimWarship"
iconName = "JLSKrenimWarship"
longName = "Krenim Warship"
shipFile = "JLSKrenimWarship"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSKrenimWarship = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSKrenimWarship.desc = "The Krenim warship was a type of warship utilized by the Krenim during the 24th century. These vessels were larger than an Intrepid-class starship. The Krenim warships had the upper hand thanks to the chroniton torpedoes until Voyager devised a new kind of shielding to protect themselves."
Foundation.ShipDef.JLSKrenimWarship.SubMenu = "Year of Hell Ships"
Foundation.ShipDef.JLSKrenimWarship.SubSubMenu = "Krenim"
Foundation.ShipDef.JLSKrenimWarship.CloakingSFX = ""
Foundation.ShipDef.JLSKrenimWarship.DeCloakingSFX = ""
Foundation.ShipDef.JLSKrenimWarship.fMaxWarp = 9.6 + 0.0001
Foundation.ShipDef.JLSKrenimWarship.fCruiseWarp = 8.2 + 0.0001
Foundation.ShipDef.JLSKrenimWarship.fCrew = 583


if menuGroup:           Foundation.ShipDef.JLSKrenimWarship.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSKrenimWarship.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
