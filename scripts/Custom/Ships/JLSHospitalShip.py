#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSHospitalShip"
iconName = "JLSHospitalShip"
longName = "Dinaali Hospital Ship"
shipFile = "JLSHospitalShip"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = ""
Foundation.ShipDef.JLSHospitalShip = Foundation.StarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSHospitalShip.desc = "Hospital Ship 4-2 was a Dinaali hospital ship. The ship was commanded by Chellick, and controlled by an artificial intelligence program called The Allocator, which served to distribute available resources most efficiently. It was also equipped with an unknown type of device that allowed it to levitate above the surface of a planet in need of its services."
Foundation.ShipDef.JLSHospitalShip.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSHospitalShip.CloakingSFX = ""
Foundation.ShipDef.JLSHospitalShip.DeCloakingSFX = ""


if menuGroup:           Foundation.ShipDef.JLSHospitalShip.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSHospitalShip.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
