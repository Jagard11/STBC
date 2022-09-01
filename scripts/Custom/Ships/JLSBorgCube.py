#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSBorgCube"
iconName = "JLSBorgCube"
longName = "Borg Cube"
shipFile = "JLSBorgCube"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSBorgCube = Foundation.BorgShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSBorgCube.desc = "The Borg cube was the primary starship class of the Borg Collective's fleet. Borg cubes are designed as a combined weapons platform and factory. Their main purpose was for destroying the military capacity of a species and assimilate the survivors into the Collective."
Foundation.ShipDef.JLSBorgCube.SubMenu = "Borg Ships"
Foundation.ShipDef.JLSBorgCube.CloakingSFX = ""
Foundation.ShipDef.JLSBorgCube.DeCloakingSFX = ""
Foundation.ShipDef.JLSBorgCube.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.JLSBorgCube.fCruiseWarp = 9.7 + 0.0001
Foundation.ShipDef.JLSBorgCube.fCrew = 150000
Foundation.ShipDef.JLSBorgCube.fShipCostModifier = 2000.0


Foundation.ShipDef.JLSBorgCube.dTechs = {
   "Regenerative Shields": 15,
   "Drainer Immune": 1,
   "AutoTargeting": {"Phaser": [8, 1], "Torpedo": [6, 1] },
}


if menuGroup:           Foundation.ShipDef.JLSBorgCube.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSBorgCube.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
