#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSReptoHumanoid"
iconName = "JLSReptoHumanoid"
longName = "ReptoHumanoid Ship"
shipFile = "JLSReptoHumanoid"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSReptoHumanoid = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSReptoHumanoid.desc = "A repto-humanoid vessel was a starship utilized by a repto-humanoid species in the Delta Quadrant. In 2372, this vessel came into conflict with USS Voyager and fired on it while both ships were in orbit of Planet Hell. The repto-humanoid vessel was in orbit looking for a newborn hatchling on the surface of the planet. Fortunately, Voyager was able to rescue Tom Paris and Neelix from the surface before the repto-humanoid vessel could do more damage to them."
Foundation.ShipDef.JLSReptoHumanoid.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSReptoHumanoid.CloakingSFX = ""
Foundation.ShipDef.JLSReptoHumanoid.DeCloakingSFX = ""
Foundation.ShipDef.JLSReptoHumanoid.fMaxWarp = 9.6 + 0.0001
Foundation.ShipDef.JLSReptoHumanoid.fCruiseWarp = 8.2 + 0.0001
Foundation.ShipDef.JLSReptoHumanoid.fCrew = 561


if menuGroup:           Foundation.ShipDef.JLSReptoHumanoid.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSReptoHumanoid.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
