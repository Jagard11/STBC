#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSBubbleCatapult"
iconName = "JLSBubbleCatapult"
longName = "Bubble Catapult"
shipFile = "JLSBubbleCatapult"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.JLSBubbleCatapult = Foundation.RomulanShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSBubbleCatapult.desc = "No information available."
Foundation.ShipDef.JLSBubbleCatapult.CloakingSFX = ""
Foundation.ShipDef.JLSBubbleCatapult.DeCloakingSFX = ""
Foundation.ShipDef.JLSBubbleCatapult.fCrew = 1


if menuGroup:           Foundation.ShipDef.JLSBubbleCatapult.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSBubbleCatapult.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
