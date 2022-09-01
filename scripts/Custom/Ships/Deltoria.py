#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Deltoria"
iconName = "Deltoria"
longName = "Deltoria"
shipFile = "Deltoria"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.Deltoria = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.Deltoria.desc = "No information available."
Foundation.ShipDef.Deltoria.CloakingSFX = ""
Foundation.ShipDef.Deltoria.DeCloakingSFX = ""
Foundation.ShipDef.Deltoria.fCrew = 0


if menuGroup:           Foundation.ShipDef.Deltoria.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Deltoria.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
