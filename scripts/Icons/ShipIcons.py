from bcdebug import debug
# ShipIcons.py
#
# Load Ship Icons for interface.
#
#

import App
import Foundation
import Registry

shipIconNames = {}
shipIconNums = {}
topSpecies = 0

class ShipIconDef:
	def __init__(self, name, dict = { 'x': 128, 'y': 128 }):
		debug(__name__ + ", __init__")
		global topSpecies, shipIcons
		self.name = name
		self.__dict__.update(dict)

		if not self.__dict__.has_key('file'):
			self.file = 'Data/Icons/Ships/' + name + '.tga'

		if self.__dict__.has_key('species'):
			if self.species > topSpecies:	topSpecies = self.species
		else:
			self.species = topSpecies + 1
			topSpecies = self.species

		shipIconNames[name] = self
		shipIconNums[self.species] = self

# Function to load LCARS icon group
def LoadShipIcons(ShipIcons = None):

	debug(__name__ + ", LoadShipIcons")
	if ShipIcons is None:
		ShipIcons = App.g_kIconManager.CreateIconGroup("ShipIcons")
		# Add LCARS icon group to IconManager
		App.g_kIconManager.AddIconGroup(ShipIcons)

	# Glass for when no ship is selected
	TextureHandle = ShipIcons.LoadIconTexture('Data/Icons/Bridge/Background/ScreenBlock.tga')
	ShipIcons.SetIconLocation(App.SPECIES_UNKNOWN, TextureHandle, 0, 0, 8, 8)

	ShipIconDef('Galaxy', { 'species': App.SPECIES_GALAXY } )
	ShipIconDef('Sovereign', { 'species': App.SPECIES_SOVEREIGN } )
	ShipIconDef('Akira', { 'species': App.SPECIES_AKIRA } )
	ShipIconDef('Ambassador', { 'species': App.SPECIES_AMBASSADOR } )
	ShipIconDef('Nebula', { 'species': App.SPECIES_NEBULA } )
	ShipIconDef('FedShuttle', { 'species': App.SPECIES_SHUTTLE } )
	ShipIconDef('Transport', { 'species': App.SPECIES_TRANSPORT } )
        ShipIconDef('Defiant', { 'species': 136 } )
        ShipIconDef('Defiant', { 'species': 157 } )
        ShipIconDef('Intrepid', { 'species': 114 } )
        ShipIconDef('USSLennox', { 'species': 128 } )
        ShipIconDef('Norway', { 'species': 116 } )
        ShipIconDef('Nova', { 'species': 117 } )
        ShipIconDef('MPNeghvar', { 'species': 403 } )
        ShipIconDef('Steamrunner', { 'species': 120 } )
        ShipIconDef('ValdoreG', { 'species': 302 } )
        ShipIconDef('griffin', { 'species': 303 } )
        ShipIconDef('Falcon', { 'species': 304 } )
        ShipIconDef('Praetor', { 'species': 305 } )
        ShipIconDef('Shrike', { 'species': 306 } )
        ShipIconDef('venator', { 'species': 307 } )
        ShipIconDef('Firehawk', { 'species': 308 } )
        ShipIconDef('LCRaptor', { 'species': 309 } )
        ShipIconDef('romulanshuttle', { 'species': 310 } )
        ShipIconDef('KlingonShuttle', { 'species': 405 } )
        ShipIconDef('Kvort', { 'species': 404 } )
        ShipIconDef('deltaflyer', { 'species': 112 } )
        ShipIconDef('PeragrineF1', { 'species': 119 } )
        ShipIconDef('DanubemkI', { 'species': 111 } )
        ShipIconDef('DanubemkII', { 'species': 127 } )
        ShipIconDef('bug', { 'species': 923 } )
        ShipIconDef('PsExcelsiorRefit', { 'species': 110 } )
        ShipIconDef('ExcelsiorP81', { 'species': 129 } )
        ShipIconDef('DYExcalibur', { 'species': 113 } )
        ShipIconDef('type9', { 'species': 133 } )
        ShipIconDef('Type11', { 'species': 146 } )
        ShipIconDef('Hutet', { 'species': 205 } )
        ShipIconDef('Hideki', { 'species': 206 } )
	ShipIconDef('cOWP', { 'species': 207 } )
	ShipIconDef('Asteroid', { 'species': 208 } )
        ShipIconDef('Scorpion', { 'species': 719 } )
        ShipIconDef('Reman Scimitar', { 'species': 718 } )
        ShipIconDef('DomBB', { 'species': 901 } )
        ShipIconDef('novaII', { 'species': 118 } )
        ShipIconDef('Aegian', { 'species': 109 } )
        ShipIconDef('Nebula', { 'species': 115 } )
        ShipIconDef('Kazonraider', { 'species': 915 } )
        ShipIconDef('RomulanOutpost', { 'species': 716 } )
        ShipIconDef('MvamPrometheus', { 'species': 113 } )
        ShipIconDef('CardStarbase', { 'species': 137 } )
        ShipIconDef('DYExcalibur', { 'species': 138 } )
        ShipIconDef('DomBC', { 'species': 902 } )
        ShipIconDef('MvamPrometheusDorsal', { 'species': 121 } )
        ShipIconDef('MvamPrometheusSaucer', { 'species': 122 } )
        ShipIconDef('MvamPrometheusVentral', { 'species': 123 } )
        ShipIconDef('MvamGalaxy', { 'species': 124 } )
        ShipIconDef('MvamGalaxySaucer', { 'species': 125 } )
        ShipIconDef('MvamGalaxyStardrive', { 'species': 126 } )
        ShipIconDef('VentureScout', { 'species': 139 } )
        ShipIconDef('City', { 'species': 917 } )
        ShipIconDef('Junk', { 'species': 918 } )
        ShipIconDef('exeter', { 'species': 140 } )
        ShipIconDef('Valkyrie', { 'species': 141 } )
        ShipIconDef('BreenBB', { 'species': 717 } )
        ShipIconDef('Eximius', { 'species': 143 } )
        ShipIconDef('LCcentaur', { 'species': 144 } )
        ShipIconDef('Miranda', { 'species': 147 } )
        ShipIconDef('Starbase220', { 'species': 145 } )
        ShipIconDef('FekLhrMK2', { 'species': 406 } )
        ShipIconDef('Sabre', { 'species': 130 } )
        ShipIconDef('Cheyenne', { 'species': 131 } )
        ShipIconDef('CA8472', { 'species': 903 } )
        ShipIconDef('Phoenix', { 'species': 132 } )
        ShipIconDef('sovereignyacht', { 'species': 134 } )
        ShipIconDef('sovereign', { 'species': 135 } )
        ShipIconDef('KTinga', { 'species': 407 } )
        ShipIconDef('BorgDiamond', { 'species': 720 } )
        ShipIconDef('sphere', { 'species': 721 } )
        ShipIconDef('WorkerBee', { 'species': 919 } )
        ShipIconDef('SonaB', { 'species': 920 } )
        ShipIconDef('HiddenCore', { 'species': 921 } )
        ShipIconDef('KlingonImperialStarbase', { 'species': 408 } )
        ShipIconDef('Miradorn', { 'species': 922 } )
        ShipIconDef('EnterpriseNCC1701', { 'species': 148 } )
        ShipIconDef('Merchantman', { 'species': 924 } )
        ShipIconDef('Karemman', { 'species': 925 } )
        ShipIconDef('Mine', { 'species': 155 } )
	ShipIconDef('StarBase329', { 'species': 149 } )
	ShipIconDef('VasKholhr', { 'species': 311 } )
	ShipIconDef('ZZSaratogaPod', { 'species': 150 } )
	ShipIconDef('pulsemine', { 'species': 151 } )
	ShipIconDef('torpedomine', { 'species': 152 } )
	ShipIconDef('blackhole', { 'species': 926 } )
	ShipIconDef('FedStarbase', { 'species': 156 } )
	ShipIconDef('SFRD_T18', { 'species': 158 } )
	ShipIconDef('DJEnterpriseG', { 'species': 159 } )
	ShipIconDef('DJEnterpriseGDrive', { 'species': 160 } )
	ShipIconDef('DJEnterpriseGSaucer', { 'species': 161 } )
	ShipIconDef('DJEnterpriseGThunderbird', { 'species': 162 } )
	ShipIconDef('BreenDN', { 'species': 722 } )
	ShipIconDef('BreenBCH', { 'species': 723 } )
	ShipIconDef('BreenCA', { 'species': 724 } )
	ShipIconDef('BreenCL', { 'species': 725 } )
	ShipIconDef('BreenDD', { 'species': 726 } )
	ShipIconDef('Raider1', { 'species': 927 } )
	ShipIconDef('SFRD_Promellian', { 'species': 928 } )
	ShipIconDef('QuanTar', { 'species': 929 } )
        ShipIconDef('lowcube', { 'species': App.SPECIES_BORG } )
	ShipIconDef('Freighter', { 'species': App.SPECIES_FREIGHTER } )
	ShipIconDef('Galor', { 'species': App.SPECIES_GALOR } )
	ShipIconDef('Keldon', { 'species': App.SPECIES_KELDON } )
	ShipIconDef('CardFreighter', { 'species': App.SPECIES_CARDFREIGHTER } )
	ShipIconDef('Hybrid', { 'species': App.SPECIES_CARDHYBRID } )
	ShipIconDef('Warbird', { 'species': App.SPECIES_WARBIRD } )
	ShipIconDef('BirdOfPrey', { 'species': App.SPECIES_BIRD_OF_PREY } )
	ShipIconDef('Vorcha', { 'species': App.SPECIES_VORCHA } )
	ShipIconDef('KessokHeavy', { 'species': App.SPECIES_KESSOK_HEAVY } )
	ShipIconDef('KessokLight', { 'species': App.SPECIES_KESSOK_LIGHT } )
	ShipIconDef('KessokMine', { 'species': App.SPECIES_KESSOKMINE } )
	ShipIconDef('Marauder', { 'species': App.SPECIES_MARAUDER } )
	ShipIconDef('FedStarbase', { 'species': App.SPECIES_FED_STARBASE } )
	ShipIconDef('FedOutpost', { 'species': App.SPECIES_FED_OUTPOST } )
	ShipIconDef('CardStarbase', { 'species': App.SPECIES_CARD_STARBASE } )
	ShipIconDef('CardOutpost', { 'species': App.SPECIES_CARD_OUTPOST } )
	ShipIconDef('CardStation', { 'species': App.SPECIES_CARD_STATION } )
	ShipIconDef('DryDock', { 'species': App.SPECIES_DRYDOCK } )
	ShipIconDef('SpaceFacility', { 'species': App.SPECIES_SPACE_FACILITY } )
	ShipIconDef('CommArray', { 'species': App.SPECIES_COMMARRAY } )
	ShipIconDef('CommLight', { 'species': App.SPECIES_COMMLIGHT } )
	ShipIconDef('Probe', { 'species': App.SPECIES_PROBE } )
	ShipIconDef('ProbeType2', { 'species': App.SPECIES_PROBETYPE2 } )
	ShipIconDef('Asteroid', { 'species': App.SPECIES_ASTEROID } )
	ShipIconDef('Sunbuster', { 'species': App.SPECIES_SUNBUSTER } )
	ShipIconDef('LifeBoat', { 'species': App.SPECIES_ESCAPEPOD } )
	

	global topSpecies
	topSpecies = topSpecies + 100

	for shipDef in Foundation.shipList._keyList.values():
		if shipIconNames.has_key(shipDef.iconName):
			iconDef = shipIconNames[shipDef.iconName]
		else:
			iconDef = ShipIconDef(shipDef.iconName)
		shipDef.species = iconDef.species

	for i in shipIconNums.values():
		# print i.file, i.species, ' : ',
		TextureHandle = ShipIcons.LoadIconTexture(i.file)
		ShipIcons.SetIconLocation(i.species, TextureHandle, 0, 0, 128, 128)

