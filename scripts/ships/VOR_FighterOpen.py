import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = { 
		"FilenameHigh": "data/Models/Ships/VOR_Fighter/VOR_FighterOpen.nif",
		"FilenameMed": "data/Models/Ships/VOR_Fighter/VOR_FighterOpen.nif",
		"FilenameLow": "data/Models/Ships/VOR_Fighter/VOR_FighterOpen.nif",
		"Name": "VOR_FighterOpen",
		"HardpointFile": "VOR_FighterOpen",
		"Species": Multiplayer.SpeciesToShip.VORCHA
	}
	return kShipStats

def LoadModel(bPreLoad = 0):
	pStats = GetShipStats()

	# Create the LOD info
	if (not App.g_kLODModelManager.Contains(pStats["Name"])):
		# Params are: File Name, PickLeafSize, SwitchOut Distance,
		# Surface Damage Res, Internal Damage Res, Burn Value, Hole Value,
		# Search String for Glow, Search string for Specular, Suffix for specular
		pLODModel = App.g_kLODModelManager.Create(pStats["Name"])
		pLODModel.AddLOD(pStats["FilenameHigh"], 10,  50.0, 15.0, 15.0, 6000, 8000, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 100.0, 15.0, 15.0, 6000, 8000, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 750.0, 15.0, 30.0, 6000, 8000, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)
