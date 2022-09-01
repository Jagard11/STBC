#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSMaquisRaider"
iconName = "JLSMaquisRaider"
longName = "Maquis Raider"
shipFile = "JLSMaquisRaider"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSMaquisRaider = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSMaquisRaider.desc = "The Maquis raider was a type of small and maneuverable starship commonly utilized by the Maquis as a raider craft in their fight against the Cardassians. These ships had a runabout-size bridge which held four stations, with larger crew facilities in the aft sections. Some of these ships operated with impulse engines originally built around 2332."
Foundation.ShipDef.JLSMaquisRaider.SubMenu = "Federation Ships"
Foundation.ShipDef.JLSMaquisRaider.CloakingSFX = ""
Foundation.ShipDef.JLSMaquisRaider.DeCloakingSFX = ""
Foundation.ShipDef.JLSMaquisRaider.fMaxWarp = 7.1 + 0.0001
Foundation.ShipDef.JLSMaquisRaider.fCruiseWarp = 4 + 0.0001
Foundation.ShipDef.JLSMaquisRaider.fCrew = 18


if menuGroup:           Foundation.ShipDef.JLSMaquisRaider.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSMaquisRaider.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
