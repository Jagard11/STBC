#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSDeltaFlyer"
iconName = "JLSDeltaflyer"
longName = "Delta Flyer II"
shipFile = "JLSDeltaFlyer"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSDeltaFlyer = Foundation.StarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSDeltaFlyer.desc = "The Delta Flyer II was a reconstruction of the original Delta Flyer that was in service aboard the USS Voyager in the 2370s. Its predecessor had been destroyed during a mission to infiltrate a Borg tactical cube in early 2377. It was equipped with pulse phased weapons and a duranium-enforced hull."
Foundation.ShipDef.JLSDeltaFlyer.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSDeltaFlyer.CloakingSFX = ""
Foundation.ShipDef.JLSDeltaFlyer.DeCloakingSFX = ""
Foundation.ShipDef.JLSDeltaFlyer.SubMenu = "Federation Ships"
Foundation.ShipDef.JLSDeltaFlyer.fMaxWarp = 9.5
Foundation.ShipDef.JLSDeltaFlyer.fCruiseWarp = 6.5
Foundation.ShipDef.JLSDeltaFlyer.fCrew = 4


if menuGroup:           Foundation.ShipDef.JLSDeltaFlyer.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSDeltaFlyer.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
