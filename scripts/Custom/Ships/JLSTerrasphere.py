#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSTerrasphere"
iconName = "JLSTerrasphere"
longName = "Species 8472 Terrasphere"
shipFile = "JLSTerrasphere"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSTerrasphere = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSTerrasphere.desc = "Terraspheres were a series of simulators built by Species 8472 in 2374, designed to mimic conditions of Starfleet Headquarters on Earth. Overall, there were approximately a dozen terraspheres scattered throughout the Delta Quadrant. Terraspheres were heavily fortified, and were protected by an unknown type of force field and shields. In all, they were powered by thirteen thermionic generators located beneath the surface of the simulated city."
Foundation.ShipDef.JLSTerrasphere.SubMenu = "Species 8472"
Foundation.ShipDef.JLSTerrasphere.CloakingSFX = ""
Foundation.ShipDef.JLSTerrasphere.DeCloakingSFX = ""
Foundation.ShipDef.JLSTerrasphere.fCrew = 1090


Foundation.ShipDef.JLSTerrasphere.dTechs = {
   "Drainer Immune": 1,
   'FiveSecsGodPhaser': 1,
}


if menuGroup:           Foundation.ShipDef.JLSTerrasphere.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSTerrasphere.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
