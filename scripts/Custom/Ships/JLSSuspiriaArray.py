#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "JLSSuspiriaArray"
iconName = "JLSSuspiriaArray"
longName = "Suspiria Array"
shipFile = "JLSSuspiriaArray"
species = App.SPECIES_GALAXY
menuGroup = "Delta Quadrant Ships"
playerMenuGroup = ""
Foundation.ShipDef.JLSSuspiriaArray = Foundation.StarBaseDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.JLSSuspiriaArray.desc = "Suspiria's array was a large space station in the Delta Quadrant. Built by the Nacene and powered by a tetryon reactor, the array served as a location from which Suspiria could protect and serve the Ocampa on board. In 2372, USS Voyager found Suspiria's array, after being pulled into the Delta Quadrant by her mate with a similar array. Aboard the array lived several hundred Ocampa. The residents of the array, with the help of Suspiria, had developed heightened mental powers and extended their lifespans."
Foundation.ShipDef.JLSSuspiriaArray.SubMenu = "Delta Quadrant Species"
Foundation.ShipDef.JLSSuspiriaArray.CloakingSFX = ""
Foundation.ShipDef.JLSSuspiriaArray.DeCloakingSFX = ""
Foundation.ShipDef.JLSSuspiriaArray.fCrew = 300


if menuGroup:           Foundation.ShipDef.JLSSuspiriaArray.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSSuspiriaArray.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
