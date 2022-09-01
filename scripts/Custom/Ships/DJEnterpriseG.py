#####  Created by:
#####  Bridge Commander Universal Tool


import App
import Foundation


abbrev = "DJEnterpriseG"
iconName = "DJEnterpriseG"
longName = "DJ Enterprise G"
shipFile = "DJEnterpriseG"
species = App.SPECIES_GALAXY
menuGroup = "Fed Ships"
playerMenuGroup = "Fed Ships"
Foundation.ShipDef.DJEnterpriseG = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })


Foundation.ShipDef.DJEnterpriseG.desc = "U.S.S. Enterprise\nNCC-1701-G\nEclipse Class (2nd of her class)\nCommissioned 2431\n\nThe Enterprise sets a new standard for Starfleet vehicles in speed, scientific capacity, and defensive ability.  Armed with the latest phasers and quantum filament pulse weapons, the ship is capable of holding her own against virtually any known threat.  Rapidly recharging shields ensure that the Enterprise can not be damaged by anything but continous heavy fire.\n\nThe ship is protected by an ablative coating and equipped with MVAM; splitting into a saucer, drive section, and Auxillary Support Vehicle known as the Thunderbird."
Foundation.ShipDef.DJEnterpriseG.SubMenu = "Eclipse Class"
Foundation.ShipDef.DJEnterpriseG.SubSubMenu = "DJ Enterprise G"
Foundation.ShipDef.DJEnterpriseG.fMaxWarp = 9.99 + 0.0001
Foundation.ShipDef.DJEnterpriseG.fCruiseWarp = 8.5 + 0.0001


Foundation.ShipDef.DJEnterpriseG.dTechs = {
   "Fed Ablative Armor": {"Plates": ["Forward Ablative Armor","Aft Ablative Armor","Dorsal Ablative Armor","Ventral Ablative Armor"]}
}


if menuGroup:           Foundation.ShipDef.DJEnterpriseG.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.DJEnterpriseG.RegisterQBPlayerShipMenu(playerMenuGroup)


if Foundation.shipList._keyList.has_key(longName):
      Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
      Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
