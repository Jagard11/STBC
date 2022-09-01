#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "KrenimHomeworld"
iconName = "KrenimHomeworld"
longName = "KrenimHomeworld"
shipFile = "KrenimHomeworld"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.KrenimHomeworld = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.KrenimHomeworld.desc = "The Krenim were a technologically advanced humanoid species from the Delta Quadrant, first encountered by the Federation starship USS Voyager in 2374. The Krenim government was called the Krenim Imperium. At 98% restoration the Krenin Imperium of 2374 was composed of over 200 star systems, 900 planets and thousands of warp-capable vessels spread out over 5000 parsecs."
Foundation.ShipDef.KrenimHomeworld.CloakingSFX = ""
Foundation.ShipDef.KrenimHomeworld.DeCloakingSFX = ""
Foundation.ShipDef.KrenimHomeworld.fCrew = 590713


if menuGroup:           Foundation.ShipDef.KrenimHomeworld.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.KrenimHomeworld.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
