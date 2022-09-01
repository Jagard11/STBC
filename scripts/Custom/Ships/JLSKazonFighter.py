#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSKazonFighter"
iconName = "JLSKazonFighter"
longName = "Kazon Fighter Shuttle"
shipFile = "JLSKazonFighter"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSKazonFighter = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSKazonFighter.desc = "Kazon fighters are small attack ships originally used by the Trabe, but were later seized from them during the Kazon uprising. Nearly identical in appearance to the Kazon raider, these vessels are approximately the size of a Federation shuttlecraft. They are able to be operated by a crew of one, and are armed with three forward phaser banks and an aft photon torpedo launcher."
Foundation.ShipDef.JLSKazonFighter.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSKazonFighter.SubSubMenu = "Kazon"
Foundation.ShipDef.JLSKazonFighter.CloakingSFX = ""
Foundation.ShipDef.JLSKazonFighter.DeCloakingSFX = ""
Foundation.ShipDef.JLSKazonFighter.fMaxWarp = 5 + 0.0001
Foundation.ShipDef.JLSKazonFighter.fCruiseWarp = 3 + 0.0001
Foundation.ShipDef.JLSKazonFighter.fCrew = 1


if menuGroup:           Foundation.ShipDef.JLSKazonFighter.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSKazonFighter.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
