#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSHirogenHunter"
iconName = "JLSHirogenHunter"
longName = "Hirogen Hunter"
shipFile = "JLSHirogenHunter"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSHirogenHunter = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSHirogenHunter.desc = "The Hirogen warship, was a small, heavily-armed warship used by Hirogen hunters during the 2370s as they hunted throughout the Delta Quadrant. This class of vessel was usually piloted by two Hunters. The vessels were equipped with monotanium armor plating, and had dicyclic warp signatures."
Foundation.ShipDef.JLSHirogenHunter.SubMenu = "Hirogen Ships"
Foundation.ShipDef.JLSHirogenHunter.CloakingSFX = ""
Foundation.ShipDef.JLSHirogenHunter.DeCloakingSFX = ""
Foundation.ShipDef.JLSHirogenHunter.fMaxWarp = 8.8 + 0.0001
Foundation.ShipDef.JLSHirogenHunter.fCruiseWarp = 7.5 + 0.0001
Foundation.ShipDef.JLSHirogenHunter.fCrew = 2


if menuGroup:           Foundation.ShipDef.JLSHirogenHunter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSHirogenHunter.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
