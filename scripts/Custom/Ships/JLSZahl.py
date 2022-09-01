#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSZahl"
iconName = "JLSZahl"
longName = "Zahl Cruiser"
shipFile = "JLSZahl"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSZahl = Foundation.CardShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSZahl.desc = "No information available."
Foundation.ShipDef.JLSZahl.SubMenu = "Year of Hell Ships"
Foundation.ShipDef.JLSZahl.CloakingSFX = ""
Foundation.ShipDef.JLSZahl.DeCloakingSFX = ""
Foundation.ShipDef.JLSZahl.fMaxWarp = 8.5 + 0.0001
Foundation.ShipDef.JLSZahl.fCruiseWarp = 6.8 + 0.0001
Foundation.ShipDef.JLSZahl.fCrew = 298

Foundation.ShipDef.JLSZahl.dTechs = {
   "ChronitonTorpe Immune": 1,
}


if menuGroup:           Foundation.ShipDef.JLSZahl.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSZahl.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
