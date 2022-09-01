#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSNihydron"
iconName = "JLSNihydron"
longName = "Nihydron Warship"
shipFile = "JLSNihydron"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSNihydron = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSNihydron.desc = "A Nihydron warship was a type of warship utilized by the Nihydron government during the late 24th century. In 2374, three Nihydron warships aided the USS Voyager in the destruction of the Krenim weapon ship. In the end, however, two of these vessels were destroyed in the process."
Foundation.ShipDef.JLSNihydron.SubMenu = "Year of Hell Ships"
Foundation.ShipDef.JLSNihydron.CloakingSFX = ""
Foundation.ShipDef.JLSNihydron.DeCloakingSFX = ""
Foundation.ShipDef.JLSNihydron.fMaxWarp = 8.9 + 0.0001
Foundation.ShipDef.JLSNihydron.fCruiseWarp = 7.2 + 0.0001
Foundation.ShipDef.JLSNihydron.fCrew = 209

Foundation.ShipDef.JLSNihydron.dTechs = {
   "ChronitonTorpe Immune": 1,
}


if menuGroup:           Foundation.ShipDef.JLSNihydron.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSNihydron.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
