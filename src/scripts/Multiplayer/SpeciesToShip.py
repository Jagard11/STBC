from bcdebug import debug
import App

# types for initializing objects create from C.
UNKNOWN			= 0
AKIRA			= 1
AMBASSADOR		= 2
GALAXY			= 3
NEBULA			= 4
SOVEREIGN		= 5
BIRDOFPREY		= 6
VORCHA			= 7
WARBIRD			= 8
MARAUDER		= 9
GALOR			= 10
KELDON			= 11
CARDHYBRID		= 12
KESSOKHEAVY		= 13
KESSOKLIGHT		= 14
SHUTTLE			= 15
DEFIANT			= 16
INTREPID		= 17
USSLENNOX		= 18
NORWAY			= 19
NOVA			= 20
MPNEGHVAR		= 21
STEAMRUNNER		= 22
VALDORE			= 23
DELTAFLYER		= 24
PERAGRINEF1		= 25
DANUBEMKI		= 26
DANUBEMKII		= 27
BUG			= 28
LAKOTA			= 29
CARDFREIGHTER		= 30
FREIGHTER		= 31
TRANSPORT		= 32
MVAMPROMETHEUS		= 33
MVAMPROMETHEUSDORSAL	= 34
MVAMPROMETHEUSSAUCER	= 35
MVAMPROMETHEUSVENRAL	= 36
GALAXYSAUCER            = 37
GALAXYSTARDRIVE         = 38
HUTET			= 39
HIDEKI			= 40
BREENBB                 = 41
SCIMITAR		= 42
DOMBB			= 43
NOVAII			= 44
AEGIAN			= 45
KAZONRAIDER		= 46
DOMBC			= 47
GRIFFIN                 = 48
FALCON                  = 49
PRAETOR                 = 50
SHRIKE                  = 51
VENATOR                 = 52
KVORT                   = 53
FIREHAWK                = 54
LCRAPTOR                = 55
ROMULANSHUTTLE          = 56
KLINGONSHUTTLE          = 57
VENTURESCOUT            = 58
JUNK                    = 59
CLOAKFIREBIRDOFPREY     = 60
EXCELSIOR               = 61
FEKLHRMK2               = 62
SABRE                   = 63
CHEYENNE                = 64
PHOENIX                 = 65
KTINGA                  = 66
BORGDIAMOND             = 67
SPHERE                  = 68
WORKERBEE               = 69
SONAB                   = 70
TYPE9                   = 71
TYPE11                  = 72
SOVEREIGNYACHT          = 73
SOVEREIGN_NOYACHT	= 74
EXIMIUS                 = 75
CENTAUR                 = 76
MIRANDA                 = 77
MIRADORN                = 78
CONSTITUTION            = 79
MERCHANTMAN             = 80
KAREMMA                 = 81
VASKHOLHR		= 82
MIRANDAPOD		= 83
FEDCONST		= 84
FEDCONSTOPEN		= 85
SCORPION		= 86
BREENDN			= 87
BREENBCH		= 88
BREENCA			= 89
BREENCL			= 90
BREENDD			= 91
TYPE18			= 92
RAIDER1			= 93
PROMELLIAN		= 94
# Non-playable
QUANTAR			= 95
DJENTERPRISEG		= 96
DJENTERPRISEG_DRIVE	= 97
DJENTERPRISEG_SAUCER	= 98
DJENTERPRISEG_THUNDERB	= 99
EXCALIBUR		= 100
ROMULANOUTPOST	        = 101
CA8472                  = 102
SPACEFACILITY		= 103
COMMARRAY		= 104
COMMLIGHT		= 105
DRYDOCK			= 106
PROBE			= 107
DECOY			= 108
SUNBUSTER		= 109
CARDOUTPOST		= 110
CARDSTARBASE		= 111
CARDSTATION		= 112
FEDOUTPOST		= 113
FEDSTARBASE		= 114
ASTEROID		= 115
ASTEROID1		= 116
ASTEROID2		= 117
ASTEROID3		= 118
AMAGON			= 119
BIRANUSTATION		= 120
ENTERPRISE		= 121
GERONIMO		= 122
PEREGRINE		= 123
ASTEROIDH1		= 124
ASTEROIDH2		= 125
ASTEROIDH3		= 126
ESCAPEPOD		= 127
CARDPOD 		= 128
DEFPOD  		= 129
GALPOD  		= 130
GREENPOD                = 131
KESSOKMINE		= 132
LOWCUBE			= 133
DS9			= 134
ADMINDEF		= 135
MINE                    = 136
CITY                    = 137
STARBASE220             = 138
FIREPOINT               = 139
BIGFIREPOINT            = 140
DRYDOCKREPAIR           = 141
HIDDENCORE              = 142
IMPERIALBASE            = 143
STARBASE329		= 144
VAS_PORT_WING		= 145
VAS_STARPORT_WING	= 146
COWP			= 147
COWPASTEROID		= 148
PULSEMINE		= 149
TORPEDOMINE		= 150
INTREPID_N_LEFT		= 151
INTREPID_N_RIGHT	= 152
BLACKHOLE		= 153
CN_FEDSTARBASE		= 154

MAX_SHIPS = 155
MAX_FLYABLE_SHIPS = 95

# Setup tuples
kSpeciesTuple = (
	(None, 0, "Neutral", 0),
	("Akira", App.SPECIES_AKIRA, "Federation", 1),
	("Ambassador", App.SPECIES_AMBASSADOR, "Federation", 1),
	("Galaxy", App.SPECIES_GALAXY, "Federation", 1),
	("Nebula" , App.SPECIES_NEBULA, "Federation", 1),
	("Sovereign" , App.SPECIES_SOVEREIGN, "Federation", 1),
	("BirdOfPrey", App.SPECIES_BIRD_OF_PREY, "Klingon", 1),
	("Vorcha" , App.SPECIES_VORCHA, "Klingon", 1),
	("Warbird" , App.SPECIES_WARBIRD, "Romulan", 1),
	("Marauder" , App.SPECIES_MARAUDER, "Ferengi", 1),
	("Galor" , App.SPECIES_GALOR, "Cardassian", 1),
	("Keldon" , App.SPECIES_KELDON, "Cardassian", 1),
	("CardHybrid", App.SPECIES_CARDHYBRID, "Cardassian", 1),
	("KessokHeavy" , App.SPECIES_KESSOK_HEAVY, "Kessok", 1),
	("KessokLight" , App.SPECIES_KESSOK_LIGHT, "Kessok", 1),  
	("Shuttle" , App.SPECIES_SHUTTLE, "Federation", 1),
	("Defiant",	136, "Federation", 1),
	("LCIntrepid",	114, "Federation", 1),
	("USSLennox",	128, "Federation", 1),
	("norway",	116, "Federation", 1),
	("Nova",	117, "Federation", 1),
	("MPneghvar",	403, "Klingon", 1),
	("Steamrunner",	120, "Federation", 1),
	("ValdoreG",	302, "Romulan", 1),
	("deltaflyer",	112, "Federation", 1),
	("PeragrineF1",	119, "Federation", 1),
	("DanubemkI",	111, "Federation", 1),
        ("DanubemkII",	127, "Federation", 1),
	("bug",		923, "Other", 1),
	("PsExcelsiorRefitTNG1" , 110, "Federation", 1),
	("CardFreighter", App.SPECIES_CARDFREIGHTER, "Cardassian", 1),
	("Freighter" , App.SPECIES_FREIGHTER, "Federation", 1),
	("Transport" , App.SPECIES_TRANSPORT, "Federation", 1),
        ("MvamPrometheus" , 113, "Federation", 1),
	("MvamPrometheusDorsal" , 121, "Federation", 1),
        ("MvamPrometheusSaucer" , 122, "Federation", 1),
        ("MvamPrometheusVentral" , 123, "Federation", 1),
        ("GalaxySaucer" , 125, "Federation", 1),
        ("GalaxyStardrive" , 126, "Federation", 1),
	("Hutet", 205, "Cardassian", 1),
        ("Hideki", 206, "Cardassian", 1),
        ("BreenBB", 717, "Other", 1),
	("Reman Scimitar" , 718, "Romulan", 1),
	("DomBB" , 901, "Other", 1),
	("novaII",	118, "Federation", 1),
	("Aegian",	109, "Federation", 1),
        ("Kazonraider",	915, "Other", 1),
        ("DomBC" , 902, "Other", 1),
        ("griffin",	303, "Romulan", 1),
        ("Falcon",	304, "Romulan", 1),
        ("Praetor",	305, "Romulan", 1),
        ("Shrike",	306, "Romulan", 1),
        ("venator",	307, "Romulan", 1),
        ("Kvort",	404, "Klingon", 1),
        ("Firehawk",	308, "Romulan", 1),
        ("LCRaptor",	309, "Romulan", 1),
        ("romulanshuttle", 310, "Romulan", 1),
        ("KlingonShuttle", 405, "Klingon", 1),
        ("VentureScout",	139, "Federation", 1),
        ("Junk",	918, "Other", 1),
        ("CloakFireBirdOfPrey",	App.SPECIES_BIRD_OF_PREY, "Klingon", 1),
        ("ExcelsiorP81" , 129, "Federation", 1),
        ("FeklhrMK2",	406, "Klingon", 1),
        ("Sabre",	130, "Federation", 1),
        ("Cheyenne",	131, "Federation", 1),
        ("Phoenix",	132, "Federation", 1),
        ("KTinga",	407, "Klingon", 1),
        ("BorgDiamond" , 720, "Borg", 1),
        ("sphere" , 721, "Borg", 1),
        ("WorkerBee",	919, "Other", 1),
        ("SonaB",	920, "Other", 1),
        ("type9",	133, "Federation", 1),
        ("Type11",	146, "Federation", 1),
        ("WCNemEntEyacht",	134, "Federation", 1),
        ("WCNemEntEnoyacht",	135, "Federation", 1),
        ("Eximius",	143, "Federation", 1),
        ("LCCentaur",   144, "Federation", 1),
        ("Miranda",   147, "Federation", 1),
        ("Miradorn", 922, "Other", 1),
        ("EnterpriseNCC1701",   148, "Federation", 1),
        ("Merchantman", 924, "Other", 1),
        ("Karemman", 925, "Other", 1),
	("VasKholhr", 311, "Romulan", 1),
	("ZZSaratogaPod2", 150, "Federation", 1),
	("FedConst",	140, "Federation", 1),
	("FedConstOpen",	141, "Federation", 1),
	("scorpion", 719, "Romulan", 1),
	("BreenDN", 722, "Other", 1),
	("BreenBCH", 723, "Other", 1),
	("BreenCA", 724, "Other", 1),
	("BreenCL", 725, "Other", 1),
	("BreenDD", 726, "Other", 1),
	("SFRD_T18", 158, "Federation", 1),
	("Raider1", 927, "Other", 1),
	("SFRD_Promellian", 928, "Other", 1),
	("QuanTar", 929, "Other", 1),
	("DJEnterpriseG", 159, "Federation", 1),
	("DJEnterpriseGDrive", 160, "Federation", 1),
	("DJEnterpriseGSaucer", 161, "Federation", 1),
	("DJEnterpriseGThunderbird", 162, "Federation", 1),
        ("DyExcalibur",	138, "Federation", 1),
	("RomulanOutpost", 716, "Romulan", 1),
        ("CA8472" , 903, "Other", 1),
	("SpaceFacility" , App.SPECIES_SPACE_FACILITY, "Federation", 1),
	("CommArray" , App.SPECIES_COMMARRAY, "Federation", 1),
	("CommLight", App.SPECIES_COMMLIGHT, "Cardassian", 1),
	("DryDock" , App.SPECIES_DRYDOCK, "Federation", 1),
	("Probe" , App.SPECIES_PROBE, "Federation", 1),
	("Decoy" , App.SPECIES_PROBETYPE2, "Federation", 1),
	("Sunbuster" , App.SPECIES_SUNBUSTER, "Kessok", 1),
	("CardOutpost" , App.SPECIES_CARD_OUTPOST, "Cardassian", 1),
	("CardStarbase" , App.SPECIES_CARD_STARBASE, "Cardassian", 1),
	("CardStation" , App.SPECIES_CARD_STATION, "Cardassian", 1),
	("FedOutpost" , App.SPECIES_FED_OUTPOST, "Federation", 1),
	("FedStarbase" , App.SPECIES_FED_STARBASE, "Federation", 1),
	("Asteroid" , App.SPECIES_ASTEROID, "Neutral", 1),
	("Asteroid1" , App.SPECIES_ASTEROID, "Neutral", 1),
	("Asteroid2" , App.SPECIES_ASTEROID, "Neutral", 1),
	("Asteroid3" , App.SPECIES_ASTEROID, "Neutral", 1),
	("Amagon", App.SPECIES_ASTEROID, "Cardassian", 1),
	("BiranuStation", App.SPECIES_SPACE_FACILITY, "Neutral", 1),
	("Enterprise", App.SPECIES_SOVEREIGN, "Federation", 1),
	("Geronimo", App.SPECIES_AKIRA, "Federation", 1),
	("Peregrine", App.SPECIES_NEBULA, "Federation", 1),
	("Asteroidh1" , App.SPECIES_ASTEROID, "Neutral", 1),
	("Asteroidh2" , App.SPECIES_ASTEROID, "Neutral", 1),
	("Asteroidh3" , App.SPECIES_ASTEROID, "Neutral", 1),
	("Escapepod" , App.SPECIES_ESCAPEPOD, "Neutral", 1),
        ("card pod" , App.SPECIES_ESCAPEPOD, "Neutral", 1),
        ("defpod" , App.SPECIES_ESCAPEPOD, "Neutral", 1),
        ("Galaxy Escape Pod" , App.SPECIES_ESCAPEPOD, "Neutral", 1),
        ("greenmisc" , App.SPECIES_ESCAPEPOD, "Neutral", 1),
	("KessokMine" , App.SPECIES_KESSOKMINE, "Kessok", 1),
	("LowCube" , App.SPECIES_BORG, "Borg", 1),
	("ds9" , 137, "Federation", 1),
	("AdminDef" , 157, "Federation", 1),
        ("Mine" , 155, "Federation", 1),
        ("City", 917, "Neutral", 1),
        ("Starbase220", 145, "Federation", 1),
        ("Firepoint", App.SPECIES_PROBE, "Other", 1),
        ("BigFirepoint", App.SPECIES_PROBE, "Other", 1),
        ("DryDockRepair", App.SPECIES_DRYDOCK, "Federation", 1),
        ("HiddenCore",	921, "Other", 1),
        ("KlingonImperialStarbase", 408, "Klingon", 1),
	("StarBase329", 149, "Federation", 1),
	("VasKholhr_PortWing", 312, "Romulan", 1),
	("VasKholhr_Starboardwing", 313, "Romulan", 1),
	("cOWP", 207, "Cardassian", 1),
	("CowpAsteroid", 208, "Cardassian", 1),
	("pulsemine", 151, "Federation", 1),
	("torpedomine", 152, "Federation", 1),
	("LCIntrepid_n_left", 153, "Federation", 1),
	("LCIntrepid_n_right", 154, "Federation", 1),
	("blackhole", 926, "Other", 1),
	("CN_FedStarbase", 156, "Federation", 1),
	
	(None, 0, "Neutral", 1))
	
def GetShipFromSpecies(iSpecies):
    debug(__name__ + ", GetShipFromSpecies")
    # fix signed stuff
    if iSpecies < 0:
	    iSpecies = iSpecies + 256
    if ((iSpecies <= 0) or (iSpecies >= MAX_SHIPS)):
        return None
    pSpecTuple = kSpeciesTuple[iSpecies]
    pcScript = pSpecTuple[0]
    ShipScript = __import__(('ships.' + pcScript))
    ShipScript.LoadModel()
    return ShipScript.GetShipStats()


def GetScriptFromSpecies(iSpecies):
    debug(__name__ + ", GetScriptFromSpecies")
    if ((iSpecies <= 0) or (iSpecies >= MAX_SHIPS)):
        return None
    pSpecTuple = kSpeciesTuple[iSpecies]
    return pSpecTuple[0]


def InitObject(self, iType):
        debug(__name__ + ", InitObject")
        kStats = GetShipFromSpecies(iType)
        if (kStats == None):
                return 0
        self.SetupModel(kStats['Name'])
	sShipScript = GetScriptFromSpecies(iType)
	if sShipScript:
		self.SetScript('ships.' + sShipScript)
        pPropertySet = self.GetPropertySet()
        if kStats.has_key("NormalHP"):
                mod = __import__(('ships.Hardpoints.' + kStats["NormalHP"]))
        else:
                mod = __import__(('ships.Hardpoints.' + kStats['HardpointFile']))
        App.g_kModelPropertyManager.ClearLocalTemplates()
        reload(mod)
        mod.LoadPropertySet(pPropertySet)
        self.SetupProperties()
        self.UpdateNodeOnly()
        return 1


def CreateShip(iType):
        debug(__name__ + ", CreateShip")
        kStats = GetShipFromSpecies(iType)
        if (kStats == None):
                return None
        pShip = App.ShipClass_Create(kStats['Name'])
        sModule = ('ships.' + kSpeciesTuple[iType][0])
        pShip.SetScript(sModule)
        pPropertySet = pShip.GetPropertySet()
        mod = __import__(('ships.Hardpoints.' + kStats['HardpointFile']))
        App.g_kModelPropertyManager.ClearLocalTemplates()
        reload(mod)
        mod.LoadPropertySet(pPropertySet)
        pShip.SetupProperties()
        pShip.UpdateNodeOnly()
        pShip.SetNetType(iType)
        return pShip


def GetIconNum(iSpecies):
    debug(__name__ + ", GetIconNum")
    pSpecTuple = kSpeciesTuple[iSpecies]
    iNum = pSpecTuple[1]
    return iNum


def GetSideFromSpecies(iSpecies):
    debug(__name__ + ", GetSideFromSpecies")
    pSpecTuple = kSpeciesTuple[iSpecies]
    pcSide = pSpecTuple[2]
    return pcSide


def GetClassFromSpecies(iSpecies):
    debug(__name__ + ", GetClassFromSpecies")
    pSpecTuple = kSpeciesTuple[iSpecies]
    iClass = pSpecTuple[3]
    return iClass

