#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "VaadwaurHomeworld"
iconName = "VaadwaurHomeworld"
longName = "VaadwaurHomeworld"
shipFile = "VaadwaurHomeworld"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.VaadwaurHomeworld = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.VaadwaurHomeworld.desc = "No information available."
Foundation.ShipDef.VaadwaurHomeworld.CloakingSFX = ""
Foundation.ShipDef.VaadwaurHomeworld.DeCloakingSFX = ""
Foundation.ShipDef.VaadwaurHomeworld.fCrew = 590713


if menuGroup:           Foundation.ShipDef.VaadwaurHomeworld.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.VaadwaurHomeworld.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
