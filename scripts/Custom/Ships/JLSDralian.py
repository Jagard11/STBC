#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSDralian"
iconName = "JLSDralian"
longName = "Gars Ship"
shipFile = "JLSDralian"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSDralian = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSDralian.desc = "The Dralian vessel was a scout ship in use by the Dralian people in the late-24th century."
Foundation.ShipDef.JLSDralian.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSDralian.CloakingSFX = ""
Foundation.ShipDef.JLSDralian.DeCloakingSFX = ""
Foundation.ShipDef.JLSDralian.fMaxWarp = 8.8 + 0.0001
Foundation.ShipDef.JLSDralian.fCruiseWarp = 6.2 + 0.0001
Foundation.ShipDef.JLSDralian.fCrew = 1


if menuGroup:           Foundation.ShipDef.JLSDralian.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSDralian.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
