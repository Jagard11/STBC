#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "OcampaPlanet"
iconName = "Ocampa"
longName = "Ocampa"
shipFile = "OcampaPlanet"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.OcampaPlanet = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.OcampaPlanet.desc = "The planet Ocampa was the homeworld of the Ocampa species and the fifth planet from a G-type star located in the Delta Quadrant approximately 75,000 light years from the Badlands in the Alpha Quadrant. Ocampa had all the characteristics of a class-M planet, with the sole exception of the absence of nucleogenic particles which left the planet's atmosphere incapable of producing rain, and turning its surface into a desert."
Foundation.ShipDef.OcampaPlanet.CloakingSFX = ""
Foundation.ShipDef.OcampaPlanet.DeCloakingSFX = ""
Foundation.ShipDef.OcampaPlanet.fCrew = 590713


if menuGroup:           Foundation.ShipDef.OcampaPlanet.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.OcampaPlanet.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
