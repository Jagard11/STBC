#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSBorgSphere"
iconName = "JLSBorgSphere"
longName = "Borg Sphere"
shipFile = "JLSBorgSphere"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSBorgSphere = Foundation.BorgShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSBorgSphere.desc = "Borg spheres were used by the Borg as scout ships or long-range tactical vessels. Borg sphere were also embedded into some Borg cubes, and were used as auxiliary craft. Borg spheres had a crew complement of 11,000 Borg drones. The spheres were approximately 600 meters in diameter, and had an interior bay large enough to hold an Intrepid-class starship. Borg spheres had transwarp capability and ablative hull armor. They were also equipped with a tractor beam."
Foundation.ShipDef.JLSBorgSphere.SubMenu = "Borg Ships"
Foundation.ShipDef.JLSBorgSphere.CloakingSFX = ""
Foundation.ShipDef.JLSBorgSphere.DeCloakingSFX = ""
Foundation.ShipDef.JLSBorgSphere.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.JLSBorgSphere.fCruiseWarp = 9.8 + 0.0001
Foundation.ShipDef.JLSBorgSphere.fCrew = 11000
Foundation.ShipDef.JLSBorgSphere.fShipCostModifier = 2000.0


Foundation.ShipDef.JLSBorgSphere.dTechs = {
   "Drainer Immune": 1,
   "AutoTargeting": {"Phaser": [3, 1], "Torpedo": [2, 1] },
}


if menuGroup:           Foundation.ShipDef.JLSBorgSphere.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSBorgSphere.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
