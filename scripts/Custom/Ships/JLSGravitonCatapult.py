#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSGravitonCatapult"
iconName = "JLSGravitonCatapult"
longName = "Graviton Catapult"
shipFile = "JLSGravitonCatapult"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = ""
Foundation.ShipDef.JLSGravitonCatapult = Foundation.RomulanShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSGravitonCatapult.desc = "A graviton catapult propels spacecraft across space. The power core of the catapult generates a massive graviton surge, that locks on to a ship through an array of projectors. The surge sends the ship hurtling into null space for some hours. Upon emerging back to normal space, the vessel has jumped many hundreds or even thousands of light years. The distance is determined by the graviton field strength."
Foundation.ShipDef.JLSGravitonCatapult.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSGravitonCatapult.CloakingSFX = ""
Foundation.ShipDef.JLSGravitonCatapult.DeCloakingSFX = ""
Foundation.ShipDef.JLSGravitonCatapult.fCrew = 1


if menuGroup:           Foundation.ShipDef.JLSGravitonCatapult.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSGravitonCatapult.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
