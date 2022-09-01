#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSNightShip"
iconName = "JLSNightShip"
longName = "Night Ship"
shipFile = "JLSNightShip"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSNightShip = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSNightShip.desc = "The Night alien ship was a starship operated by the Night Aliens in the 24th century in a Delta Quadrant region called the Void. In 2375 the USS Voyager first contact with the species after they had been boarded by seventeen of them. Tuvok modified a photon torpedo to use it as a light source and discovered three of these ships surrounding the Voyager."
Foundation.ShipDef.JLSNightShip.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSNightShip.CloakingSFX = ""
Foundation.ShipDef.JLSNightShip.DeCloakingSFX = ""
Foundation.ShipDef.JLSNightShip.fMaxWarp = 8 + 0.0001
Foundation.ShipDef.JLSNightShip.fCruiseWarp = 9.5 + 0.0001
Foundation.ShipDef.JLSNightShip.fCrew = 50


if menuGroup:           Foundation.ShipDef.JLSNightShip.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSNightShip.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
