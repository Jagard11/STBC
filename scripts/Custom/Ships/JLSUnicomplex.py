#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSUnicomplex"
iconName = "JLSUnicomplex"
longName = "Borg Unicomplex"
shipFile = "JLSUnicomplex"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = ""
Foundation.ShipDef.JLSUnicomplex = Foundation.StarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSUnicomplex.desc = "The Unicomplex was a vast Borg complex located within Borg space in the Delta Quadrant. It was composed of thousands of connected structures and hubs spanning at least 600km that housed hundreds of Borg ships and trillions of drones. The Unicomplex was destroyed in 2378, after the Borg Queen assimilated a neurolytic pathogen from the future Admiral Janeway, who had traveled back in time to bring Voyager home."
Foundation.ShipDef.JLSUnicomplex.SubMenu = "Stations"
Foundation.ShipDef.JLSUnicomplex.fCrew = 9999999


Foundation.ShipDef.JLSUnicomplex.dTechs = {
   "Fed Ablative Armor": {"Plates": ["Aft Ablative Armor","Engineering Ablative Armor","Top Ablative Armor","Forward Ablative Armor"]}
}


if menuGroup:           Foundation.ShipDef.JLSUnicomplex.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSUnicomplex.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
