#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'JLSYOHVoyager_n_right'
iconName = 'JLSYOHVoyager_right'
longName = 'U.S.S. Voayger'
shipFile = 'JLSYOHVoyager_n_right' 
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
	'modName': 'JLSYOHVoyager_n_right',
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
Foundation.ShipDef.JLSYOHVoyager_n_right = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile })
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.JLSYOHVoyager_n_right.hasTGLName = 1
# Foundation.ShipDef.JLSYOHVoyager_n_right.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.JLSYOHVoyager_n_right.desc = 'No Description Available'
#                                                                                     #
#######################################################################################

#Foundation.ShipDef.JLSYOHVoyager_n_right.SDTEntry = {
#	"Textures": [["voyager04_glow", "data/Models/Ships/JLSYOHVoyager/High/intrepid04_glow.tga"]]
#}

