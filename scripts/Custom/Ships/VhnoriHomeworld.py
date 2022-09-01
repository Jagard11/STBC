#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "VhnoriHomeworld"
iconName = "VhnoriHomeworld"
longName = "Vhnori Homeworld"
shipFile = "VhnoriHomeworld"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.VhnoriHomeworld = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.VhnoriHomeworld.desc = "No information available."
Foundation.ShipDef.VhnoriHomeworld.CloakingSFX = ""
Foundation.ShipDef.VhnoriHomeworld.DeCloakingSFX = ""
Foundation.ShipDef.VhnoriHomeworld.fCrew = 50736


if menuGroup:           Foundation.ShipDef.VhnoriHomeworld.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.VhnoriHomeworld.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
