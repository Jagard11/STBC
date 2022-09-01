#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Sikaris"
iconName = "Sikaris"
longName = "Sikaris"
shipFile = "Sikaris"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.Sikaris = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.Sikaris.desc = "No information available."
Foundation.ShipDef.Sikaris.CloakingSFX = ""
Foundation.ShipDef.Sikaris.DeCloakingSFX = ""
Foundation.ShipDef.Sikaris.fCrew = 590713


if menuGroup:           Foundation.ShipDef.Sikaris.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Sikaris.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
