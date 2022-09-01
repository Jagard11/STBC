#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSHirogenComm"
iconName = "JLSHirogenComm"
longName = "Hirogen Comm Array"
shipFile = "JLSHirogenComm"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSHirogenComm = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSHirogenComm.desc = "The Hirogen communications network was an ancient array of modules which spanned the Delta Quadrant, and reached into Alpha and Beta Quadrants as well. The series of modules, dating back over 100,000 years in age, was claimed by the Hirogen by the mid-24th century. The communications network was first encountered by the USS Voyager in 2374. One of the arrays encountered by Voyager was powered by an artificial quantum singularity, generating almost four terawatts of energy."
Foundation.ShipDef.JLSHirogenComm.SubMenu = "Hirogen Ships"
Foundation.ShipDef.JLSHirogenComm.CloakingSFX = ""
Foundation.ShipDef.JLSHirogenComm.DeCloakingSFX = ""
Foundation.ShipDef.JLSHirogenComm.fCrew = 1


if menuGroup:           Foundation.ShipDef.JLSHirogenComm.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSHirogenComm.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
