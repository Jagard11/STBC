#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSHirogenDecoy"
iconName = "JLSHirogenDecoy"
longName = "Hirogen Decoy"
shipFile = "JLSHirogenDecoy"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSHirogenDecoy = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSHirogenDecoy.desc = "The Hirogen decoy was used by the holograms to lure the Hirogen hunters into a trap. The decoy is used to send out the same readings as the prey. When the hunter arrives at the decoy, believing he has his prey, the decoy unleashes its true nature and detonates itself, taking or crippling the hunter."
Foundation.ShipDef.JLSHirogenDecoy.SubMenu = "Hirogen Ships"
Foundation.ShipDef.JLSHirogenDecoy.CloakingSFX = ""
Foundation.ShipDef.JLSHirogenDecoy.DeCloakingSFX = ""
Foundation.ShipDef.JLSHirogenDecoy.fCrew = 1


if menuGroup:           Foundation.ShipDef.JLSHirogenDecoy.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSHirogenDecoy.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
