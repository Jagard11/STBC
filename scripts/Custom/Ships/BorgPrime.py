#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "BorgPrime"
iconName = "BorgPrime"
longName = "Borg Prime"
shipFile = "BorgPrime"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.BorgPrime = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.BorgPrime.desc = "Borg colony where billions of drones work."
Foundation.ShipDef.BorgPrime.CloakingSFX = ""
Foundation.ShipDef.BorgPrime.DeCloakingSFX = ""
Foundation.ShipDef.BorgPrime.fCrew = 590713


if menuGroup:           Foundation.ShipDef.BorgPrime.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.BorgPrime.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
