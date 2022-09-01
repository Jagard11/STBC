#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSKazonPredator"
iconName = "JLSKazonPredator"
longName = "Kazon Predator"
shipFile = "JLSKazonPredator"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSKazonPredator = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSKazonPredator.desc = "Kazon carrier vessels were a type of 24th century starship originally designed by the Trabe, that was later commandeered by the Kazon and used as a massive warship. This class of vessel is much clumsier in battle at lower speeds than at warp and can be easily out maneuvered by an agile craft."
Foundation.ShipDef.JLSKazonPredator.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSKazonPredator.SubSubMenu = "Kazon"
Foundation.ShipDef.JLSKazonPredator.CloakingSFX = ""
Foundation.ShipDef.JLSKazonPredator.DeCloakingSFX = ""
Foundation.ShipDef.JLSKazonPredator.fMaxWarp = 6.7 + 0.0001
Foundation.ShipDef.JLSKazonPredator.fCruiseWarp = 4 + 0.0001
Foundation.ShipDef.JLSKazonPredator.fCrew = 1200


if menuGroup:           Foundation.ShipDef.JLSKazonPredator.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSKazonPredator.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
