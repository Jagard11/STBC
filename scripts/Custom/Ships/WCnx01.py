#######################################################################################
#  Custom Ship Plugin                                                                 #
#  Created by BC - Mod Packager                                                       #
#  Date: 05/25/2013                                                                    #
#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'WCnx01'
iconName = 'WCnx01'
longName = 'WC Enterprise NX-01'
shipFile = 'WCnx01' 
menuGroup = 'Fed Ships'
playerMenuGroup = 'Fed Ships'
species = App.SPECIES_GALAXY
SubMenu = "WC NX Class"
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'WCnx01',
	'author': '',
	'version': '1.0',
	'sources': [ 'http://' ],
	'comments': ''
}
#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.WCnx01 = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile, "SubMenu": SubMenu })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.WCnx01.hasTGLName = 1
#Foundation.ShipDef.WCnx01.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
Foundation.ShipDef.WCnx01.desc = 'NX-01 by WileyCoyote'
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.WCnx01.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.WCnx01.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
