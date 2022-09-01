##### Created by:
##### Bridge Commander Ship Menu Creator v4.0



import App
import Foundation



abbrev = 'TEBorgGalaxy'
iconName = 'TEBorgGalaxy'
longName = 'TEBorgGalaxy'
shipFile = 'TEBorgGalaxy'
species = App.SPECIES_GALAXY
SubMenu = 'Assimilated Feds'
menuGroup = 'Borg Ships'
playerMenuGroup = 'Borg Ships'


Foundation.ShipDef.TEBorgGalaxy = Foundation.BorgShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, 'SubMenu': SubMenu })


# Foundation.ShipDef.TEBorgGalaxy.fMaxWarp
# Foundation.ShipDef.TEBorgGalaxy.fCruiseWarp
Foundation.ShipDef.TEBorgGalaxy.desc = 'Assimilated ISS Valkyrie'


if menuGroup:           Foundation.ShipDef.TEBorgGalaxy.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.TEBorgGalaxy.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
