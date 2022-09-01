#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSThinkTank"
iconName = "JLSThinkTank"
longName = "Think Tank"
shipFile = "JLSThinkTank"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSThinkTank = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSThinkTank.desc = "The Think Tank, so-named by Captain Kathryn Janeway, was a cooperative of technologically-advanced alien intellectuals whose alleged purpose was to solve the problems of others for a price. Together they operated their group out of an advanced vessel. By their own count, the Think Tank were opportunistic explorers who had solved problems for hundreds of clients, many of whom were at war."
Foundation.ShipDef.JLSThinkTank.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSThinkTank.CloakingSFX = ""
Foundation.ShipDef.JLSThinkTank.DeCloakingSFX = ""
Foundation.ShipDef.JLSThinkTank.fMaxWarp = 8 + 0.0001
Foundation.ShipDef.JLSThinkTank.fCruiseWarp = 4 + 0.0001
Foundation.ShipDef.JLSThinkTank.fCrew = 5

Foundation.ShipDef.JLSThinkTank.dTechs = {
   "AutoTargeting": {"Phaser": [8, 1] },
}


if menuGroup:           Foundation.ShipDef.JLSThinkTank.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSThinkTank.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
