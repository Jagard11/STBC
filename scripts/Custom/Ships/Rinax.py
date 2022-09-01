#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "Rinax"
iconName = "Rinax"
longName = "Rinax"
shipFile = "Rinax"
species = App.SPECIES_GALAXY
menuGroup = ""
playerMenuGroup = ""
Foundation.ShipDef.Rinax = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.Rinax.desc = "Rinax is a moon of the planet Talax. It was one of the most pleasant locations in the system. A once-famous region on Rinax was the Rinax marshlands, known for the hottest climate of the sector. In 2355, the metreon cascade, a destructive weapon, was deployed on Rinax by the Haakonian Order. The cascade wrecked the moons ecosystem, resulting in an endless frigid winter and the deaths of approximately 300,000 Talaxians."
Foundation.ShipDef.Rinax.CloakingSFX = ""
Foundation.ShipDef.Rinax.DeCloakingSFX = ""
Foundation.ShipDef.Rinax.fCrew = 0


if menuGroup:           Foundation.ShipDef.Rinax.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.Rinax.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
