#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'CGIVoyager'
iconName = 'CGIVoyager'
longName = 'U.S.S. Voyager'
shipFile = 'CGIVoyager' 
menuGroup = 'Delta Quadrant Ships'
playerMenuGroup = 'Delta Quadrant Ships'
species = App.SPECIES_GALAXY
#                                                                                     #
                                                                               #                          #
#                                                                                     #
Foundation.ShipDef.CGIVoyager = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
Foundation.ShipDef.CGIVoyager.sBridge = 'intrepidbridge'
Foundation.ShipDef.CGIVoyager.fMaxWarp = 9.975
Foundation.ShipDef.CGIVoyager.fCruiseWarp = 6.0
Foundation.ShipDef.CGIVoyager.fCrew = 148
Foundation.ShipDef.CGIVoyager.SubMenu = "Federation Ships"
Foundation.ShipDef.CGIVoyager.desc = 'The USS Voyager is an Intrepid-class Federation starship which was launched in 2371 and was under the command of Captain Kathryn Janeway. On her first mission to capture a maquis ship, Voyager was thrown 70,000 light years across the galaxy to the Delta Quadrant were Starfleet and maquis would unite to return home one day.'

Foundation.ShipDef.CGIVoyager.dTechs = {'SubModel': {
        "Setup":        {
                "Body":                 "CGIVoyager_no_nacelle",
                "NormalModel":          "CGIVoyager",
                "WarpModel":          "CGIVoyager_Warp",
                "Hardpoints":       {
			"Port Warp":  [-0.63, -1.15223, -0.15],
			"Star Warp":  [0.63, -1.15223, -0.15],
                },
                "WarpHardpoints":       {
			"Port Warp":  [-0.6, -1.15223, 0],
			"Star Warp":  [0.6, -1.15223, 0],
                },
        },
                
        "Port Nacelle":     ["CGIVoyager_n_left", {
                "Position":             [-0.32, -1.07, -0.144],
                "Rotation":             [0, 0, 0], # normal Rotation used if not Warp
                "WarpRotation":       [0, -0.45, 0],
                "WarpPosition":       [-0.32, -1.07, -0.144],
                "WarpDuration":       150.0,
                }
        ],
        
        "Starboard Nacelle":     ["CGIVoyager_n_right", {
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
#Foundation.ShipDef.CGIVoyager.hasTGLName = 1
#Foundation.ShipDef.CGIVoyager.hasTGLDesc = 1

# Otherwise, uncomment this and type something in:
#Foundation.ShipDef.CGIVoyager.desc = ''
#                                                                                     #
#######################################################################################
#                                                                                     #
# These register the ship with the QuickBattle menus.  Don't touch them!!!            #
#                                                                                     #
if menuGroup:           Foundation.ShipDef.CGIVoyager.RegisterQBShipMenu(menuGroup)
if playerMenuGroup:     Foundation.ShipDef.CGIVoyager.RegisterQBPlayerShipMenu(playerMenuGroup)

if Foundation.shipList._keyList.has_key(longName):
     Foundation.ShipDef.__dict__[longName].friendlyDetails[2] = Foundation.shipList[longName].friendlyDetails[2]
     Foundation.ShipDef.__dict__[longName].enemyDetails[2] = Foundation.shipList[longName].enemyDetails[2]
#                                                                                     #
#######################################################################################
