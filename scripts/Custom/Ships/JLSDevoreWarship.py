#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSDevoreWarship"
iconName = "JLSDevoreWarship"
longName = "Devore Warship"
shipFile = "JLSDevoreWarship"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSDevoreWarship = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSDevoreWarship.desc = "The Devore warship was a type of warship operated by the Devore Imperium during the the 24th century. In 2375, the USS Voyager was stopped for inspection by several pairs of Devore warships while passing through Devore space. The inspections were for the purpose of finding telepathic beings, which they would move to relocation centres."
Foundation.ShipDef.JLSDevoreWarship.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSDevoreWarship.CloakingSFX = ""
Foundation.ShipDef.JLSDevoreWarship.DeCloakingSFX = ""
Foundation.ShipDef.JLSDevoreWarship.fMaxWarp = 8.9 + 0.0001
Foundation.ShipDef.JLSDevoreWarship.fCruiseWarp = 6 + 0.0001
Foundation.ShipDef.JLSDevoreWarship.fCrew = 650


if menuGroup:           Foundation.ShipDef.JLSDevoreWarship.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSDevoreWarship.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
