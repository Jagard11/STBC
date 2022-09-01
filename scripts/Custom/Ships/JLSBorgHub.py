#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSBorgHub"
iconName = "JLSBorgHub"
longName = "Borg Transwarp Hub"
shipFile = "JLSBorgHub"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = ""
Foundation.ShipDef.JLSBorgHub = Foundation.StarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSBorgHub.desc = "A transwarp hub was a structure used by the Borg Collective to connect the vast network of transwarp conduits which it maintained across the galaxy. Connecting to thousands of exit apertures in all four quadrants, this allowed the Borg to deploy vessels almost anywhere in the galaxy in a matter of minutes, giving them a decisive tactical advantage. The hubs were characterized by extremely high neutrino emissions accompanied by intermittent graviton flux. Supported by a series of interspatial manifolds whose shielding was regulated from the central nexus by the Borg Queen herself, there were only six hubs in the entire galaxy."
Foundation.ShipDef.JLSBorgHub.SubMenu = "Stations"
Foundation.ShipDef.JLSBorgHub.fCrew = 2000000


Foundation.ShipDef.JLSBorgHub.dTechs = {
   "Drainer Immune": 1
}


if menuGroup:           Foundation.ShipDef.JLSBorgHub.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSBorgHub.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
