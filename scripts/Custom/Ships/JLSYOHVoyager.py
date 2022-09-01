#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'JLSYOHVoyager'
iconName = 'JLSYOHVoyager'
longName = 'Year of Hell Voyager'
shipFile = 'JLSYOHVoyager' 
menuGroup = 'Delta Quadrant Ships'
playerMenuGroup = 'Delta Quadrant Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #

#                                                                                     #
#######################################################################################
#                                                                                     #
# This is the ShipDef that adds the Ship to the game... BC-Mod Packager has           #
# automatically generated the proper ShipDef Line for you.                            #
#                                                                                     #
Foundation.ShipDef.JLSYOHVoyager = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.JLSYOHVoyager.sBridge = 'intrepidbridge'
Foundation.ShipDef.JLSYOHVoyager.SubMenu = "Year of Hell Ships"
Foundation.ShipDef.JLSYOHVoyager.fMaxWarp = 5.975
Foundation.ShipDef.JLSYOHVoyager.fCruiseWarp = 3.0
Foundation.ShipDef.JLSYOHVoyager.fCrew = 5
Foundation.ShipDef.JLSYOHVoyager.desc = 'In several alternate timelines, The Year of Hell was the name that was given to the events of 2373 and 2374 by the crew of the USS Voyager, specifically a series of conflicts with the Krenim Imperium.'

Foundation.ShipDef.JLSYOHVoyager.dTechs = {
   "ChronitonTorpe Immune": 1,
						'SubModel': {
        "Setup":        {
                "Body":                 "JLSYOHVoyager_no_nacelle",
                "NormalModel":          "JLSYOHVoyager",
                "WarpModel":          "JLSYOHVoyager_Warp",
                "Hardpoints":       {
			"Star Warp":  [0.63, -1.15223, -0.15],
                },
                "WarpHardpoints":       {
			"Star Warp":  [0.6, -1.15223, 0],
                },
        },
                
       
        "Starboard Nacelle":     ["JLSYOHVoyager_n_right", {
                "Position":             [0.32, -1.07, -0.144],
                "Rotation":             [0, 0, 0],
                "WarpRotation":       [0, 0.45, 0],
                "WarpPosition":       [0.32, -1.07, -0.144],
                "WarpDuration":       150.0,
                }
        ],

}}

#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL  
#Foundation.ShipDef.JLSYOHVoyager.hasTGLName = 1
#Foundation.ShipDef.JLSYOHVoyager.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
#Foundation.ShipDef.JLSYOHVoyager.desc = ''
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.JLSYOHVoyager.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.JLSYOHVoyager.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
