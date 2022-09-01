#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSAeon"
iconName = "JLSAeon"
longName = "Timeship U.S.S. Aeon"
shipFile = "JLSAeon"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSAeon = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSAeon.desc = "The Aeon was a Federation Aeon type timeship that was in service with Starfleet in the 29th century. Piloted by Captain Braxton, the ship was capable of traveling through time via generation of temporal rifts."
Foundation.ShipDef.JLSAeon.SubMenu = "Future Ships"
Foundation.ShipDef.JLSAeon.CloakingSFX = ""
Foundation.ShipDef.JLSAeon.DeCloakingSFX = ""
Foundation.ShipDef.JLSAeon.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.JLSAeon.fCruiseWarp = 9.98 + 0.0001
Foundation.ShipDef.JLSAeon.fCrew = 1


Foundation.ShipDef.JLSAeon.dTechs = {
   "Drainer Immune": 1
}


if menuGroup:           Foundation.ShipDef.JLSAeon.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSAeon.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
