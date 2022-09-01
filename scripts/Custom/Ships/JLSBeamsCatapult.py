#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSBeamsCatapult"
iconName = "JLSBeamsCatapult"
longName = "Beams Catapult"
shipFile = "JLSBeamsCatapult"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.JLSBeamsCatapult = Foundation.RomulanShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSBeamsCatapult.desc = "No information available."
Foundation.ShipDef.JLSBeamsCatapult.CloakingSFX = ""
Foundation.ShipDef.JLSBeamsCatapult.DeCloakingSFX = ""
Foundation.ShipDef.JLSBeamsCatapult.fCrew = 1


if menuGroup:           Foundation.ShipDef.JLSBeamsCatapult.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSBeamsCatapult.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
