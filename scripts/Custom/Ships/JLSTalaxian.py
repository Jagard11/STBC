#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSTalaxian"
iconName = "JLSTalaxian"
longName = "Talaxian Fighter"
shipFile = "JLSTalaxian"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSTalaxian = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSTalaxian.desc = "Talaxian fighters were small, highly manueverable combat craft used by Talaxian forces. Several Talaxian fighters, led by Commander Paxim supported Lieutenant Tom Paris in retaking USS Voyager from the Kazon-Nistrim in 2373."
Foundation.ShipDef.JLSTalaxian.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSTalaxian.SubSubMenu = "Talaxians"
Foundation.ShipDef.JLSTalaxian.CloakingSFX = ""
Foundation.ShipDef.JLSTalaxian.DeCloakingSFX = ""
Foundation.ShipDef.JLSTalaxian.fMaxWarp = 7 + 0.0001
Foundation.ShipDef.JLSTalaxian.fCruiseWarp = 5.5 + 0.0001
Foundation.ShipDef.JLSTalaxian.fCrew = 2


if menuGroup:           Foundation.ShipDef.JLSTalaxian.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSTalaxian.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
