#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSCaretakerArray"
iconName = "JLSCaretakerArray"
longName = "Caretaker Array"
shipFile = "JLSCaretakerArray"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = ""
Foundation.ShipDef.JLSCaretakerArray = Foundation.StarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSCaretakerArray.desc = "The Caretaker's array was a large space station in the Delta Quadrant not far from the planet Ocampa. Built by the Nacene, the array served as a location from which the Caretaker could protect and serve the Ocampa. It was armed with energy weapons and was also capable of generating a displacement wave that could drag ships from other parts of the galaxy."
Foundation.ShipDef.JLSCaretakerArray.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSCaretakerArray.CloakingSFX = ""
Foundation.ShipDef.JLSCaretakerArray.DeCloakingSFX = ""
Foundation.ShipDef.JLSCaretakerArray.fCrew = 94


Foundation.ShipDef.JLSCaretakerArray.dTechs = {
   "Drainer Immune": 1
}


if menuGroup:           Foundation.ShipDef.JLSCaretakerArray.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSCaretakerArray.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
