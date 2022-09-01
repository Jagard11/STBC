#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "MalonPlanet"
iconName = "MalonPlanet"
longName = "MalonPlanet"
shipFile = "MalonPlanet"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.MalonPlanet = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.MalonPlanet.desc = "Malon Prime was a planet in the Delta Quadrant and homeworld of the Malon species. It was said to be one of the most beautiful planets in the quadrant, despite the fact that Malon industry produced massive quantities of antimatter waste. This was made possible by waste export vessels, that transported the hazardous waste far from Malon home space."
Foundation.ShipDef.MalonPlanet.CloakingSFX = ""
Foundation.ShipDef.MalonPlanet.DeCloakingSFX = ""
Foundation.ShipDef.MalonPlanet.fCrew = 590713


if menuGroup:           Foundation.ShipDef.MalonPlanet.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.MalonPlanet.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
