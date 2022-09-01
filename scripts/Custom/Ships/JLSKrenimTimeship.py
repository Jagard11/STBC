#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSKrenimTimeship"
iconName = "JLSKrenimTimeship"
longName = "Krenim Timeship"
shipFile = "JLSKrenimTimeship"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSKrenimTimeship = Foundation.KessokShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSKrenimTimeship.desc = "The Krenim weapon ship was a weapon developed by the Krenim Imperium some time prior to 2174. Its design and construction was spearheaded by Annorax, a military temporal scientist. Its main weapon was a beam that pushed objects out of the spacetime continuum, effectively erasing them from history. Careful and meticulous calculations were required to create the exact changes in the timeline that were desired."
Foundation.ShipDef.JLSKrenimTimeship.SubMenu = "Year of Hell Ships"
Foundation.ShipDef.JLSKrenimTimeship.SubSubMenu = "Krenim"
Foundation.ShipDef.JLSKrenimTimeship.CloakingSFX = ""
Foundation.ShipDef.JLSKrenimTimeship.DeCloakingSFX = ""
Foundation.ShipDef.JLSKrenimTimeship.fMaxWarp = 7 + 0.0001
Foundation.ShipDef.JLSKrenimTimeship.fCruiseWarp = 3 + 0.0001
Foundation.ShipDef.JLSKrenimTimeship.fCrew = 950


Foundation.ShipDef.JLSKrenimTimeship.dTechs = {
   "Drainer Immune": 1,
   'FiveSecsTempPhaser': 1,
   "AutoTargeting": {"Pulse": [10, 1] },

}


if menuGroup:           Foundation.ShipDef.JLSKrenimTimeship.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSKrenimTimeship.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
