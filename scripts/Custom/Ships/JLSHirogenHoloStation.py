#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSHirogenHoloStation"
iconName = "JLSHirogenHoloStation"
longName = "Hirogen Holo Station"
shipFile = "JLSHirogenHoloStation"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSHirogenHoloStation = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSHirogenHoloStation.desc = "The Hirogen training facility was a space station built by the Hirogen incorporating holographic technology from the Federation starship, USS Voyager."
Foundation.ShipDef.JLSHirogenHoloStation.SubMenu = "Hirogen Ships"
Foundation.ShipDef.JLSHirogenHoloStation.CloakingSFX = ""
Foundation.ShipDef.JLSHirogenHoloStation.DeCloakingSFX = ""
Foundation.ShipDef.JLSHirogenHoloStation.fCrew = 47


if menuGroup:           Foundation.ShipDef.JLSHirogenHoloStation.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSHirogenHoloStation.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
