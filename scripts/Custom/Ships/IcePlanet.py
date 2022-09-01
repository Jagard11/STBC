#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "IcePlanet"
iconName = "IcePlanet"
longName = "IcePlanet"
shipFile = "IcePlanet"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.IcePlanet = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.IcePlanet.desc = "In 2375, the starship Voyager crashed on a class L planet in the Takara sector, after attempting to use quantum slipstream drive to return to the Alpha Quadrant, due to a phase variance in the slipstream which caused Voyager to be thrown into normal space."
Foundation.ShipDef.IcePlanet.CloakingSFX = ""
Foundation.ShipDef.IcePlanet.DeCloakingSFX = ""
Foundation.ShipDef.IcePlanet.fCrew = 590713


if menuGroup:           Foundation.ShipDef.IcePlanet.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.IcePlanet.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
