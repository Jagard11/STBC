#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSVidiian"
iconName = "JLSVidiian"
longName = "Vidiian Ship"
shipFile = "JLSVidiian"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSVidiian = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSVidiian.desc = "The Vidiian starship was a massive starship utilized by the Vidiians in 2371 and 2372. This class of vessel operated with a crew of well over three hundred, and was armed with hypothermic charges and grapplers, which was used to access captured ships."
Foundation.ShipDef.JLSVidiian.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSVidiian.CloakingSFX = ""
Foundation.ShipDef.JLSVidiian.DeCloakingSFX = ""
Foundation.ShipDef.JLSVidiian.fMaxWarp = 9.6 + 0.0001
Foundation.ShipDef.JLSVidiian.fCruiseWarp = 8.2 + 0.0001
Foundation.ShipDef.JLSVidiian.fCrew = 403


if menuGroup:           Foundation.ShipDef.JLSVidiian.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSVidiian.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
