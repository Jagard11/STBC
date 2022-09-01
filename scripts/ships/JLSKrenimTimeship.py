import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/DQP/JLSKrenimTimeship/KrenimTimeship.nif",
		"FilenameMed": "data/Models/Ships/DQP/JLSKrenimTimeship/KrenimTimeship.nif",
		"FilenameLow": "data/Models/Ships/DQP/JLSKrenimTimeship/KrenimTimeship.nif",
		"Name": "Species KrenimTimeship",
		"HardpointFile": "JLSKrenimTimeship",
		"Species": Multiplayer.SpeciesToShip.GALAXY,
		"DamageRadMod" : 1.8,
		"DamageStrMod" : 1.2,
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
		pLODModel.AddLOD(pStats["FilenameHigh"], 10, 2000.0, 100.0, 100.0, 200, 2000, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  10, 4000.0, 100.0, 100.0, 200, 2000, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  10, 8000.0, 100.0, 100.0, 200, 2000, "_glow", None, None)

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)
