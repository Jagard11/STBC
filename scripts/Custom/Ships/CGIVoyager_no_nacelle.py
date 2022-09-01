#######################################################################################
#                                                                                     #
import Foundation
import App
#                                                                                     #
#######################################################################################
#                                                                                     #
abbrev = 'CGIVoyager_no_nacelle'
iconName = 'CGIVoyager_no'
longName = 'U.S.S. Voyager'
shipFile = 'CGIVoyager_no_nacelle' 
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
	'modName': 'CGIVoyager_no_nacelle',
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
Foundation.ShipDef.CGIVoyager_no_nacelle = Foundation.FedShipDef(abbrev, species, { 'name': longName, 'iconName': iconName, 'shipFile': shipFile})
#                                                                                     #
#######################################################################################
#                                                                                     #
# Uncomment these if you have TGL                                                     #
#                                                                                     #
# Foundation.ShipDef.CGIVoyager_no_nacelle.hasTGLName = 1
# Foundation.ShipDef.CGIVoyager_no_nacelle.hasTGLDesc = 1
#                                                                                     #
# Otherwise, uncomment this and type something in:                                    #
#                                                                                     #
Foundation.ShipDef.CGIVoyager_no_nacelle.desc = 'No Description Available'
#                                                                                     #
#######################################################################################

#Foundation.ShipDef.CGIVoyager_no_nacelle.SDTEntry = {
#	"Textures": [["voyager04_glow", "data/Models/Ships/CGIVoyager/High/intrepid04_glow.tga"]]
#}

