#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Veloce"
iconName = "Veloce"
longName = "Veloce"
shipFile = "Veloce"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.Veloce = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.Veloce.desc = "No information available."
Foundation.ShipDef.Veloce.CloakingSFX = ""
Foundation.ShipDef.Veloce.DeCloakingSFX = ""
Foundation.ShipDef.Veloce.fCrew = 490713


if menuGroup:           Foundation.ShipDef.Veloce.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Veloce.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
