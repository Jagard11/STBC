import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/Victory/Victory.nif",
		"FilenameMed": "data/Models/Ships/Victory/VictoryMed.nif",
		"FilenameLow": "data/Models/Ships/Victory/VictoryLow.nif",
		"Name": "Victory",
		"HardpointFile": "victory",
		"Species": Multiplayer.SpeciesToShip.MARAUDER
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 90, 300.0, 50.0, 50.0, 200, 8000, "_GLOW", None, "_SPEC")
		pLODModel.AddLOD(pStats["FilenameMed"],  90, 500.0, 50.0, 50.0, 200, 8000, "_GLOW", None, "_SPEC")
		pLODModel.AddLOD(pStats["FilenameLow"],  90, 700.0, 50.0, 50.0, 200, 8000, "_GLOW", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)
