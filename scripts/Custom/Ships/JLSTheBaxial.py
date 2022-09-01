#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSTheBaxial"
iconName = "JLSTheBaxial"
longName = "Neelix's Shuttle"
shipFile = "JLSTheBaxial"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSTheBaxial = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSTheBaxial.desc = "The Baxial was a Talaxian Baxial type freighter that was in service in the late 24th century. In the 2370s, the Baxial was owned by Neelix. During his stay aboard the USS Voyager, the Baxial was stored in the shuttlebay."
Foundation.ShipDef.JLSTheBaxial.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSTheBaxial.SubSubMenu = "Talaxians"
Foundation.ShipDef.JLSTheBaxial.CloakingSFX = ""
Foundation.ShipDef.JLSTheBaxial.DeCloakingSFX = ""
Foundation.ShipDef.JLSTheBaxial.fMaxWarp = 7 + 0.0001
Foundation.ShipDef.JLSTheBaxial.fCruiseWarp = 5.5 + 0.0001
Foundation.ShipDef.JLSTheBaxial.fCrew = 2


if menuGroup:           Foundation.ShipDef.JLSTheBaxial.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSTheBaxial.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
