#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSType9"
iconName = "JLSType9"
longName = "Type 9 Shuttle Craft"
shipFile = "JLSType9"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = "Delta Quadrant Ships"
Foundation.ShipDef.JLSType9 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSType9.desc = "The Class-2 shuttle, also referred to as a Type-9 shuttlecraft, was an auxiliary space vessel utilized by Starfleet for use as an embarked craft from starships. A standard Class-2 shuttle has a top speed of warp 4. However, in 2372, the crew of USS Voyager discovered a new form of dilithium that could remain stable at a much higher warp frequency, and modified the Class 2 shuttle to achieve high-warp engine performance, reaching significantly past warp 9."
Foundation.ShipDef.JLSType9.SubMenu = "Federation Ships"
Foundation.ShipDef.JLSType9.CloakingSFX = ""
Foundation.ShipDef.JLSType9.DeCloakingSFX = ""
Foundation.ShipDef.JLSType9.fMaxWarp = 9.5 + 0.0001
Foundation.ShipDef.JLSType9.fCruiseWarp = 8 + 0.0001
Foundation.ShipDef.JLSType9.fCrew = 4


if menuGroup:           Foundation.ShipDef.JLSType9.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSType9.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
