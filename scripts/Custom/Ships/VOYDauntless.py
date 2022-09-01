##### Created by:
##### Bridge Commander Ship Menu Creator



import App
import Foundation



abbrev = 'VOYDauntless'
iconName = 'VOYDauntless'
longName = 'U.S.S. Dauntless'
shipFile = 'VOYDauntless'
species = App.SPECIES_GALAXY
menuGroup = 'Delta Quadrant Ships'
playerMenuGroup = 'Delta Quadrant Ships'


Foundation.ShipDef.VOYDauntless = Foundation.ShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.VOYDauntless.fMaxWarp = 9.5
Foundation.ShipDef.VOYDauntless.fCrew = 148
Foundation.ShipDef.VOYDauntless.fCruiseWarp = 6.5
Foundation.ShipDef.VOYDauntless.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.VOYDauntless.desc = 'The Dauntless class was a type of starship designed by Arturis of Species 116 during the 2370s. It employed quantum slipstream technology, which allowed it to go higher than the standard Starfleet warp scale. Although created by alien technology, the ship was modified to resemble Federation starships on the interior and exterior by the means of particle synthesis. The Dauntless was equipped with an experimental quantum slipstream drive allowing it to travel 60,000 light years in three months and was capable of traveling over fifteen light years in only a short time, which otherwise took Voyager two days to cover at high warp.'


if menuGroup:           Foundation.ShipDef.VOYDauntless.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.VOYDauntless.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
