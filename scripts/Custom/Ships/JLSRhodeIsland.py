#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSRhodeIsland"
iconName = "JLSRhodeIsland"
longName = "U.S.S. Rhode Island"
shipFile = "JLSRhodeIsland"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSRhodeIsland = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSRhodeIsland.desc = "The USS Rhode Island NCC 72701 was a variant Federation Nova class science vessel that was in service with Starfleet in the early 25th century. Even though the original Nova-class from the 2370s was limited to a maximum warp factor of warp 8 and was considered a planetary research vessel, the Rhode Island was designed for long term deep space assignments. In an alternate timeline, the Rhode Island was commanded by Captain Harry Kim, and assigned to a four-year exploration mission."
Foundation.ShipDef.JLSRhodeIsland.SubMenu = "Federation Ships"
Foundation.ShipDef.JLSRhodeIsland.CloakingSFX = ""
Foundation.ShipDef.JLSRhodeIsland.DeCloakingSFX = ""
Foundation.ShipDef.JLSRhodeIsland.fMaxWarp = 9.98 + 0.0001
Foundation.ShipDef.JLSRhodeIsland.fCruiseWarp = 8.5 + 0.0001
Foundation.ShipDef.JLSRhodeIsland.fCrew = 208


Foundation.ShipDef.JLSRhodeIsland.dTechs = {
   "Drainer Immune": 1,
	"AutoTargeting": {"Phaser": [4, 1], "Torpedo": [2, 1] },
	'Fed Ablative Armor': { "Plates": ["Aft Ablative Armor", "Engineering Ablative Armor", "Top Ablative Armor", "Forward Ablative Armor"]
}}


if menuGroup:           Foundation.ShipDef.JLSRhodeIsland.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSRhodeIsland.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
