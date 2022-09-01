#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSRaven"
iconName = "JLSRaven"
longName = "S.S. Raven"
shipFile = "JLSRaven"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSRaven = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSRaven.desc = "The USS Raven NAR-32450 was a Federation Raven type exploration vessel that was in service with Starfleet in the mid-24th century. This ship was on loan to the Federation Council on Exobiology, and was given the NAR prefix. On her last mission, the Raven had three crewmembers, the exobiologists Magnus Hansen and Erin Hansen and their daughter, Annika Hansen."
Foundation.ShipDef.JLSRaven.SubMenu = "Federation Ships"
Foundation.ShipDef.JLSRaven.CloakingSFX = ""
Foundation.ShipDef.JLSRaven.DeCloakingSFX = ""
Foundation.ShipDef.JLSRaven.fMaxWarp = 8.5 + 0.0001
Foundation.ShipDef.JLSRaven.fCruiseWarp = 4.5 + 0.0001
Foundation.ShipDef.JLSRaven.fCrew = 3


if menuGroup:           Foundation.ShipDef.JLSRaven.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSRaven.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
