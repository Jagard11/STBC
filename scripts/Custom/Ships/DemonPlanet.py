#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "DemonPlanet"
iconName = "DemonPlanet"
longName = "DemonPlanet"
shipFile = "DemonPlanet"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.DemonPlanet = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.DemonPlanet.desc = "In 2374, the USS Voyager was forced to land on a class Y planet in the Vaskan sector after detecting desperately needed deuterium on the surface. There, they discovered the deuterium was in fact contained in a biomimetic lifeform called the Silver Blood, which duplicated the crew and ship."
Foundation.ShipDef.DemonPlanet.CloakingSFX = ""
Foundation.ShipDef.DemonPlanet.DeCloakingSFX = ""
Foundation.ShipDef.DemonPlanet.fCrew = 590713


if menuGroup:           Foundation.ShipDef.DemonPlanet.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DemonPlanet.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
