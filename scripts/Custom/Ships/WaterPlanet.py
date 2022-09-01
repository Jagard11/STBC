#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "waterPlanet"
iconName = "WaterPlanet"
longName = "waterPlanet"
shipFile = "waterPlanet"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.waterPlanet = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.waterPlanet.desc = "No information available."
Foundation.ShipDef.waterPlanet.CloakingSFX = ""
Foundation.ShipDef.waterPlanet.DeCloakingSFX = ""
Foundation.ShipDef.waterPlanet.fCrew = 90713


if menuGroup:           Foundation.ShipDef.waterPlanet.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.waterPlanet.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
