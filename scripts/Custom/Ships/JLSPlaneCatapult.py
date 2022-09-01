#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSPlaneCatapult"
iconName = "JLSPlaneCatapult"
longName = "Plane Catapult"
shipFile = "JLSPlaneCatapult"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.JLSPlaneCatapult = Foundation.RomulanShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSPlaneCatapult.desc = "No information available."
Foundation.ShipDef.JLSPlaneCatapult.CloakingSFX = ""
Foundation.ShipDef.JLSPlaneCatapult.DeCloakingSFX = ""
Foundation.ShipDef.JLSPlaneCatapult.fCrew = 1


if menuGroup:           Foundation.ShipDef.JLSPlaneCatapult.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSPlaneCatapult.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
