#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLS8472"
iconName = "JLS8472"
longName = "Species 8472 Bioship"
shipFile = "JLS8472"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLS8472 = Foundation.DominionShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLS8472.desc = "The bioship was an organic vessel that was used by Species 8472 and had a similar genetic makeup to their pilots. The bioships, and Species 8472 themselves, were resistant to assimilation by the Borg and had enough firepower to destroy a Borg ship with only a couple of shots."
Foundation.ShipDef.JLS8472.SubMenu = "Species 8472"
Foundation.ShipDef.JLS8472.CloakingSFX = ""
Foundation.ShipDef.JLS8472.DeCloakingSFX = ""
Foundation.ShipDef.JLS8472.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.JLS8472.fCruiseWarp = 9.95 + 0.0001
Foundation.ShipDef.JLS8472.fCrew = 1


Foundation.ShipDef.JLS8472.dTechs = {
   "Drainer Immune": 1,
   'FiveSecsGodPhaser': 1,
}


if menuGroup:           Foundation.ShipDef.JLS8472.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLS8472.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
