#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSKazonRaider"
iconName = "JLSKazonRaider"
longName = "Kazon Raider"
shipFile = "JLSKazonRaider"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSKazonRaider = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSKazonRaider.desc = "The Kazon raider was a medium-sized starship originally used by the Trabe. These vessels were later seized and used by the Kazon, following their uprising against the Trabe. The armaments aboard this class of vessel included two forward energy weapons and photonic charges with variable yields, and were protected with shields."
Foundation.ShipDef.JLSKazonRaider.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSKazonRaider.SubSubMenu = "Kazon"
Foundation.ShipDef.JLSKazonRaider.CloakingSFX = ""
Foundation.ShipDef.JLSKazonRaider.DeCloakingSFX = ""
Foundation.ShipDef.JLSKazonRaider.fMaxWarp = 7.9 + 0.0001
Foundation.ShipDef.JLSKazonRaider.fCruiseWarp = 6 + 0.0001
Foundation.ShipDef.JLSKazonRaider.fCrew = 80


if menuGroup:           Foundation.ShipDef.JLSKazonRaider.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSKazonRaider.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
