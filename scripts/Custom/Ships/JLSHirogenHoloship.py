#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSHirogenHoloship"
iconName = "JLSHirogenHoloship"
longName = "Hirogen Holoship"
shipFile = "JLSHirogenHoloship"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSHirogenHoloship = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSHirogenHoloship.desc = "A Hirogen holoship was a type of starship utilized by the Hirogen that was especially outfitted with holographic projectors. Such a vessel was stolen by Iden and a number of Hirogen created holograms in 2377, it was vehicle used to drive Iden's Rebellion."
Foundation.ShipDef.JLSHirogenHoloship.SubMenu = "Hirogen Ships"
Foundation.ShipDef.JLSHirogenHoloship.CloakingSFX = ""
Foundation.ShipDef.JLSHirogenHoloship.DeCloakingSFX = ""
Foundation.ShipDef.JLSHirogenHoloship.fMaxWarp = 9.1 + 0.0001
Foundation.ShipDef.JLSHirogenHoloship.fCruiseWarp = 7.5 + 0.0001
Foundation.ShipDef.JLSHirogenHoloship.fCrew = 50


if menuGroup:           Foundation.ShipDef.JLSHirogenHoloship.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSHirogenHoloship.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
