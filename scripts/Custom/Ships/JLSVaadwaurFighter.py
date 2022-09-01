#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSVaadwaurFighter"
iconName = "JLSVaadwaurFighter"
longName = "Vaadwaur Assault Fighter"
shipFile = "JLSVaadwaurFighter"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSVaadwaurFighter = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSVaadwaurFighter.desc = "The Vaadwaur assault fighter was a small warship used by the Vaadwaur in the 15th century. It was capable of operation both in an atmosphere and in space, and is armed with particle cannons."
Foundation.ShipDef.JLSVaadwaurFighter.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSVaadwaurFighter.CloakingSFX = ""
Foundation.ShipDef.JLSVaadwaurFighter.DeCloakingSFX = ""
Foundation.ShipDef.JLSVaadwaurFighter.fMaxWarp = 5 + 0.0001
Foundation.ShipDef.JLSVaadwaurFighter.fCruiseWarp = 2 + 0.0001
Foundation.ShipDef.JLSVaadwaurFighter.fCrew = 2


if menuGroup:           Foundation.ShipDef.JLSVaadwaurFighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSVaadwaurFighter.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
