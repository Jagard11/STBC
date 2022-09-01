import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"DamageRadMod" : 0.75, 
		"DamageStrMod" : 0.75, 
		"FilenameHigh": "data/Models/Bases/KrenimHomeworld/KrenimHomeworld.nif",
		"FilenameMed": "data/Models/Bases/KrenimHomeworld/KrenimHomeworld.nif",
		"FilenameLow": "data/Models/Bases/KrenimHomeworld/KrenimHomeworld.nif",
		"Name": "KrenimHomeworld",
		"HardpointFile": "KrenimHomeworld",
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 90, 2000.0, 100.0, 100.0, 400, 900, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  90, 3000.0, 100.0, 100.0, 400, 900, "_glow", None, None)
		pLODModel.AddLOD(pStats["FilenameLow"],  90, 8000.0, 100.0, 100.0, 400, 900, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)
