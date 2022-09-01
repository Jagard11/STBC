#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSBorgTacticalCube"
iconName = "JLSBorgTacticalCube"
longName = "Borg Tactical Cube"
shipFile = "JLSBorgTacticalCube"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSBorgTacticalCube = Foundation.BorgShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSBorgTacticalCube.desc = "The Borg Class 4 tactical vessel was a type of heavily-armed Borg cube utilized by the Borg Collective. The tactical cube differed from the standard Borg cube in several ways, the most notable being the extensive hull armor that covered a large portion of the exterior hull of the ship. The interior was also slightly altered from what is known of Borg architecture. The vessel's central plexus was protected by multi-regenerative security fields."
Foundation.ShipDef.JLSBorgTacticalCube.SubMenu = "Borg Ships"
Foundation.ShipDef.JLSBorgTacticalCube.CloakingSFX = ""
Foundation.ShipDef.JLSBorgTacticalCube.DeCloakingSFX = ""
Foundation.ShipDef.JLSBorgTacticalCube.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.JLSBorgTacticalCube.fCruiseWarp = 9.8 + 0.0001
Foundation.ShipDef.JLSBorgTacticalCube.fCrew = 150000
Foundation.ShipDef.JLSBorgTacticalCube.fShipCostModifier = -2000.0


Foundation.ShipDef.JLSBorgTacticalCube.dTechs = {
   "Regenerative Shields": 15,
   "Drainer Immune": 1,
   "AutoTargeting": {"Phaser": [8, 1], "Torpedo": [6, 1] },
}


if menuGroup:           Foundation.ShipDef.JLSBorgTacticalCube.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSBorgTacticalCube.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
