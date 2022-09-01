#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSKrenimPatrol"
iconName = "JLSKrenimPatrol"
longName = "Krenim Patrol Ship"
shipFile = "JLSKrenimPatrol"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSKrenimPatrol = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSKrenimPatrol.desc = "A Krenim patrol ship was a ship used by the Krenim in an alternate timeline resulting from the actions of the Krenim weapon ship in 2374. The USS Voyager encountered a patrol ship during negotiations with the Zahl. The patrol ship believed Voyager to be in Krenim, rather than Zahl, space and opened fire. The patrol ship did little damage to Voyager but was transformed into a Krenim warship when a distortion wave created by the Krenim Weapon Ship passed through it."
Foundation.ShipDef.JLSKrenimPatrol.SubMenu = "Year of Hell Ships"
Foundation.ShipDef.JLSKrenimPatrol.SubSubMenu = "Krenim"
Foundation.ShipDef.JLSKrenimPatrol.CloakingSFX = ""
Foundation.ShipDef.JLSKrenimPatrol.DeCloakingSFX = ""
Foundation.ShipDef.JLSKrenimPatrol.fMaxWarp = 8.8 + 0.0001
Foundation.ShipDef.JLSKrenimPatrol.fCruiseWarp = 5.2 + 0.0001
Foundation.ShipDef.JLSKrenimPatrol.fCrew = 183


if menuGroup:           Foundation.ShipDef.JLSKrenimPatrol.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSKrenimPatrol.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
