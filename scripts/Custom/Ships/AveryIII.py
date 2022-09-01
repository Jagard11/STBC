#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "AveryIII"
iconName = "AveryIII"
longName = "Avery III"
shipFile = "AveryIII"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.AveryIII = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.AveryIII.desc = "Avery III was the third planet in the Avery system, located in the Vidiian Sodality in the Delta Quadrant."
Foundation.ShipDef.AveryIII.CloakingSFX = ""
Foundation.ShipDef.AveryIII.DeCloakingSFX = ""
Foundation.ShipDef.AveryIII.fCrew = 490713


if menuGroup:           Foundation.ShipDef.AveryIII.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.AveryIII.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
