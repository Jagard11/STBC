#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSMawasi"
iconName = "JLSMawasi"
longName = "Mawasi Cruiser"
shipFile = "JLSMawasi"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSMawasi = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSMawasi.desc = "A Mawasi cruiser was a type of cruiser utilized by the Mawasi government during the late 24th century. In 2374, two Mawasi cruisers and three Nihydron warships aided the USS Voyager in the destruction of the Krenim weapon ship after a series of timeline changes altered history in the region."
Foundation.ShipDef.JLSMawasi.SubMenu = "Year of Hell Ships"
Foundation.ShipDef.JLSMawasi.CloakingSFX = ""
Foundation.ShipDef.JLSMawasi.DeCloakingSFX = ""
Foundation.ShipDef.JLSMawasi.fMaxWarp = 8 + 0.0001
Foundation.ShipDef.JLSMawasi.fCruiseWarp = 6.5 + 0.0001
Foundation.ShipDef.JLSMawasi.fCrew = 350

Foundation.ShipDef.JLSMawasi.dTechs = {
   "ChronitonTorpe Immune": 1,
}


if menuGroup:           Foundation.ShipDef.JLSMawasi.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSMawasi.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
