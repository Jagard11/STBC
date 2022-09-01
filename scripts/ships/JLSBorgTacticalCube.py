import App
import Multiplayer.SpeciesToShip

def GetShipStats():
	kShipStats = {
		"FilenameHigh": "data/Models/Ships/DQP/JLSBorgTacticalCube/TacticalCube.nif",
		"FilenameMed": "data/Models/Ships/DQP/JLSBorgTacticalCube/TacticalCube.nif",
		"FilenameLow": "data/Models/Ships/DQP/JLSBorgTacticalCube/TacticalCube.nif",
		"Name": "Borg Tactical Cube",
		"HardpointFile": "JLSBorgTacticalCube",
		"Species": Multiplayer.SpeciesToShip.GALAXY,
		"DamageRadMod" : 0.8,
		"DamageStrMod" : 0.2,
		 }
	return kShipStats

def LoadModel(bPreLoad = 0):
	pStats = GetShipStats()

	# Create the LOD info
	if (not App.g_kLODModelManager.Contains(pStats["Name"])):
		# Params are: File Name, PickLeafSize, SwitchOut Distance,
		# Surface Damage Res, Internal Damage Res, Burn Value, Hole Value,
		# Search String for Glow, Search string for Specular, Suffix for specular
		pLODModel = App.g_kLODModelManager.Create(pStats["Name"], 10000, 1)
		# ***FIXME: Not all 3 levels of detail need OBB trees.  PickLeafSize should be 0 for the unused ones.
		pLODModel.AddLOD(pStats["FilenameHigh"], 62, 20000.0, 600.0, 0.0, 800, 1800, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameMed"],  62, 40000.0, 600.0, 0.0, 800, 1800, "_glow", None, "_specular")
		pLODModel.AddLOD(pStats["FilenameLow"],  62, 20000.0, 600.0, 0.0, 800, 1800, "", None, None)
		pLODModel.SetTextureSharePath("data/Models/SharedTextures/FedBases")

#		kDebugObj = App.CPyDebug()
		if (bPreLoad == 0):
			pLODModel.Load()
#			kDebugObj.Print("Loading " + pStats["Name"] + "\n")
		else:
			pLODModel.LoadIncremental()
#			kDebugObj.Print("Queueing " + pStats["Name"] + " for pre-loading\n")

def PreLoadModel():
	LoadModel(1)
