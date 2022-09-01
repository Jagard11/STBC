#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSBomar"
iconName = "JLSBomar"
longName = "Bomar Patrol Ship"
shipFile = "JLSBomar"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSBomar = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSBomar.desc = "The Bomar were a humanoid species native to the Delta Quadrant. Their government was known as the Bomar Sovereignty. Extremely officious and xenophobic, the Bomar reluctantly allowed the Federation starship USS Voyager passage through their space in 2374, though only on the condition of following an extremely circuitous route that avoided all Bomar planets and colonies, maintaining a rather slow speed of warp 3."
Foundation.ShipDef.JLSBomar.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSBomar.CloakingSFX = ""
Foundation.ShipDef.JLSBomar.DeCloakingSFX = ""
Foundation.ShipDef.JLSBomar.fMaxWarp = 7.5 + 0.0001
Foundation.ShipDef.JLSBomar.fCruiseWarp = 5.5 + 0.0001
Foundation.ShipDef.JLSBomar.fCrew = 30


if menuGroup:           Foundation.ShipDef.JLSBomar.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSBomar.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
