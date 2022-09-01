#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSBorgDiamond"
iconName = "JLSBorgDiamond"
longName = "Borg Diamond"
shipFile = "JLSBorgDiamond"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSBorgDiamond = Foundation.BorgShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSBorgDiamond.desc = "The Borg Queen's vessel was a unique, diamond-shaped starship that was used by the Borg Queen to travel. Little was known about its capabilities or specific purpose, except that the only Federation encounters with this starship design were when the vessel was used to transport the Queen, and thus it could be inferred that it is her ship. The ship was heavily armed, well protected, and, like all Borg ships, capable of transwarp speeds."
Foundation.ShipDef.JLSBorgDiamond.SubMenu = "Borg Ships"
Foundation.ShipDef.JLSBorgDiamond.CloakingSFX = ""
Foundation.ShipDef.JLSBorgDiamond.DeCloakingSFX = ""
Foundation.ShipDef.JLSBorgDiamond.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.JLSBorgDiamond.fCruiseWarp = 9.5 + 0.0001
Foundation.ShipDef.JLSBorgDiamond.fCrew = 5000
Foundation.ShipDef.JLSBorgDiamond.fShipCostModifier = 1000.0


Foundation.ShipDef.JLSBorgDiamond.dTechs = {
   "Drainer Immune": 1,
   "AutoTargeting": {"Phaser": [3, 1], "Torpedo": [2, 1], "Pulse": [2, 1] },
}


if menuGroup:           Foundation.ShipDef.JLSBorgDiamond.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSBorgDiamond.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
