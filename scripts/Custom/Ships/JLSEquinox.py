#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSEquinox"
iconName = "JLSEquinox"
longName = "U.S.S. Equinox Damaged"
shipFile = "JLSEquinox"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSEquinox = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSEquinox.desc = "The USS Equinox NCC-72381 was a Federation Nova-class science vessel that was in service with Starfleet in the late 24th century. The Nova Class was designed as a science and scout vessel, intended for short-term planetary research and analysis. It is not typically suitable for combat operations. The Nova design has a maximum speed of warp 8. Though Novas were science vessels, they had a wide assortment of weaponry, allowing the vessel to handle many threats on its own. It was equipped with eleven strategically-placed phaser arrays."
Foundation.ShipDef.JLSEquinox.SubMenu = "Federation Ships"
Foundation.ShipDef.JLSEquinox.CloakingSFX = ""
Foundation.ShipDef.JLSEquinox.DeCloakingSFX = ""
Foundation.ShipDef.JLSEquinox.fMaxWarp = 8 + 0.0001
Foundation.ShipDef.JLSEquinox.fCruiseWarp = 6 + 0.0001
Foundation.ShipDef.JLSEquinox.fCrew = 78


if menuGroup:           Foundation.ShipDef.JLSEquinox.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSEquinox.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
