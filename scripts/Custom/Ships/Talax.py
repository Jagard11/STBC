#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Talax"
iconName = "Talax"
longName = "Talax"
shipFile = "Talax"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.Talax = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.Talax.desc = "No information available."
Foundation.ShipDef.Talax.CloakingSFX = ""
Foundation.ShipDef.Talax.DeCloakingSFX = ""
Foundation.ShipDef.Talax.fCrew = 590713


if menuGroup:           Foundation.ShipDef.Talax.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Talax.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
