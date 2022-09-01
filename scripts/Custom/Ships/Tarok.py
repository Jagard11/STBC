#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Tarok"
iconName = "Tarok"
longName = "Tarok"
shipFile = "Tarok"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.Tarok = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.Tarok.desc = "No information available."
Foundation.ShipDef.Tarok.CloakingSFX = ""
Foundation.ShipDef.Tarok.DeCloakingSFX = ""
Foundation.ShipDef.Tarok.fCrew = 900


if menuGroup:           Foundation.ShipDef.Tarok.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Tarok.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
