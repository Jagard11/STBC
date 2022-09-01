#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'CGIVoyager_n_left'
iconName = 'CGIVoyager_left'
longName = 'U.S.S. Voyager'
shipFile = 'CGIVoyager_n_left' 
menuGroup = None
playerMenuGroup = None
#SubMenu = 'Intrepid Class'
species = App.SPECIES_GALAXY
#                                                                                     #
#######################################################################################
#                                                                                     #
# Mod Info.  Use this as an opportunity to describe your work in brief.  This may     #
# have use later on for updates and such.                                             #
#                                                                                     #
credits = {
	'modName': 'CGIVoyager_n_left',
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
Foundation.ShipDef.CGIVoyager_n_left = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.CGIVoyager_n_left.hasTGLName = 1
# Foundation.ShipDef.CGIVoyager_n_left.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.CGIVoyager_n_left.desc = 'No Description Available'
#                                                                                     #
#######################################################################################

#Foundation.ShipDef.CGIVoyager_n_left.SDTEntry = {
#	"Textures": [["voyager04_glow", "data/Models/Ships/CGIVoyager/High/intrepid04_glow.tga"]]
#}

