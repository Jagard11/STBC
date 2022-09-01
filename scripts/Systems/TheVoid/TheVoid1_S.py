import App
import MissionLib
import Tactical.LensFlares
import loadspacehelper
import SelfDefenseAI

def Initialize(pSet):

	if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
		# Create ship

		GC_AddFundsToCreateShip("JLSNightShip")  #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pNightShip2       = loadspacehelper.CreateShip("JLSNightShip", pSet, "Night Ship 1", "Night Ship2 Location")

		GC_AddFundsToCreateShip("JLSNightShip") #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pNightShip3      = loadspacehelper.CreateShip("JLSNightShip", pSet, "Night Ship 2", "Night Ship3 Location")

		GC_AddFundsToCreateShip("JLSNightShip") #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pNightShip4       = loadspacehelper.CreateShip("JLSNightShip", pSet, "Night Ship 3", "Night Ship1 Location")

		GC_AddFundsToCreateShip("JLSNightShip") #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pNightShip5       = loadspacehelper.CreateShip("JLSNightShip", pSet, "Night Ship 4", "Night Ship5 Location")

		GC_AddFundsToCreateShip("JLSNightShip") #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pNightShip6       = loadspacehelper.CreateShip("JLSNightShip", pSet, "Night Ship 5", "Night Ship6 Location")

		GC_AddFundsToCreateShip("JLSNightShip") #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pNightShip7      = loadspacehelper.CreateShip("JLSNightShip", pSet, "Night Ship 6", "Night Ship7 Location")

		GC_AddFundsToCreateShip("JLSNightShip") #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pNightShip8       = loadspacehelper.CreateShip("JLSNightShip", pSet, "Night Ship 7", "Night Ship8 Location")

		GC_AddFundsToCreateShip("JLSNightShip") #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pNightShip9       = loadspacehelper.CreateShip("JLSNightShip", pSet, "Night Ship 8", "Night Ship9 Location")

	if (App.g_kUtopiaModule.IsMultiplayer()):
		pMission = MissionLib.GetMission ()
		SetupEventHandlers(pMission)

	else:
                pNightShip2.SetAI(SelfDefenseAI.CreateAI(pNightShip2))    
                pNightShip3.SetAI(SelfDefenseAI.CreateAI(pNightShip3))
                pNightShip4.SetAI(SelfDefenseAI.CreateAI(pNightShip4))    
                pNightShip5.SetAI(SelfDefenseAI.CreateAI(pNightShip5))
                pNightShip6.SetAI(SelfDefenseAI.CreateAI(pNightShip6))
                pNightShip7.SetAI(SelfDefenseAI.CreateAI(pNightShip7))
                pNightShip8.SetAI(SelfDefenseAI.CreateAI(pNightShip8))    
                pNightShip9.SetAI(SelfDefenseAI.CreateAI(pNightShip9))

############################
# HEY JB (like you asked:  "ill put it as simple as i can, evn though it will not be enough"  :P)
# This function is that code block I gave ya. Really, I've made her and just pasted the code block inside :P
# Passing the ShipClass string as an parameter, makes it easier to use the code block when creating the ships specially when creating multiple ships.
# To add this in another script, just copy this function there
def GC_AddFundsToCreateShip(sShipClass):
	try:
		import Custom.GalaxyCharts.GalaxyLIB
		pShipDef = Custom.GalaxyCharts.GalaxyLIB.GetShipDefByScript(sShipClass)
		sRaceName = Custom.GalaxyCharts.GalaxyLIB.GetShipDefRace(pShipDef)
		pRaceObj = Custom.GalaxyCharts.GalaxyLIB.GetRaceClassObj(sRaceName)
		fShipCost = Custom.GalaxyCharts.GalaxyLIB.GetShipClassFundCost(sShipClass)
		pRaceObj.AddFunds(fShipCost)
	except:
		pass



###############################################################################
#       SetupEventHandlers()
#
#       Set up event handlers used by the Starbase 12 set.
#
#       Args:   pSet    - The Starbase 12 set.
#
#       Return: none
###############################################################################
def SetupEventHandlers(pMission):
	import Multiplayer.MissionShared
	App.g_kEventManager.AddBroadcastPythonFuncHandler(App.ET_OBJECT_CREATED_NOTIFY, pMission, __name__ + ".ObjectCreatedHandler")

	return 0


def ObjectCreatedHandler (TGObject, pEvent):
	import Multiplayer.SpeciesToShip

	# We only care about ships.
	pShip = App.ShipClass_Cast (pEvent.GetDestination ())
	if (pShip):
		# We only care about ships.
		if (pShip.IsPlayerShip ()):
			ResetEnemyFriendlyGroups ()
		elif (pShip.GetNetType () == Multiplayer.SpeciesToShip.FEDSTARBASE):
			pass
	return 0

def ResetEnemyFriendlyGroups ():
	# Go through player list, trying to find all the ships

	pNetwork = App.g_kUtopiaModule.GetNetwork ()
	pGame = App.MultiplayerGame_Cast (App.Game_GetCurrentGame ())

	if (pNetwork and pGame):
		pMission = MissionLib.GetMission ()
		pEnemyGroup = MissionLib.GetEnemyGroup ()
		pFriendyGroup = MissionLib.GetFriendlyGroup()
		pNeutralGroup = pMission.GetNeutralGroup ()


	pSet = App.g_kSetManager.GetSet("BorgPrime1")

        pNightShip2 = App.ShipClass_GetObject(pSet, "Night Ship 1")
        pNightShip3 = App.ShipClass_GetObject(pSet, "Night Ship 2")
        pNightShip4 = App.ShipClass_GetObject(pSet, "Night Ship 3")
        pNightShip5 = App.ShipClass_GetObject(pSet, "Night Ship 4")
        pNightShip6 = App.ShipClass_GetObject(pSet, "Night Ship 5")
        pNightShip7 = App.ShipClass_GetObject(pSet, "Night Ship 6")
        pNightShip8 = App.ShipClass_GetObject(pSet, "Night Ship 7")
        pNightShip9 = App.ShipClass_GetObject(pSet, "Night Ship 8")


        if pNightShip2 != None:   
		pNightShip2.SetAI(SelfDefenseAI.CreateAI(pNightShip2))    
        if pNightShip3 != None:
		pNightShip3.SetAI(SelfDefenseAI.CreateAI(pNightShip3))
        if pNightShip4 != None:   
		pNightShip4.SetAI(SelfDefenseAI.CreateAI(pNightShip4))    
        if pNightShip5 != None:   
		pNightShip5.SetAI(SelfDefenseAI.CreateAI(pNightShip5))
        if pNightShip6 != None:  
		pNightShip6.SetAI(SelfDefenseAI.CreateAI(pNightShip6))
        if pNightShip7 != None: 
		pNightShip7.SetAI(SelfDefenseAI.CreateAI(pNightShip7))
        if pNightShip8 != None:   
		pNightShip8.SetAI(SelfDefenseAI.CreateAI(pNightShip8))    
        if pNightShip9 != None:   
		pNightShip9.SetAI(SelfDefenseAI.CreateAI(pNightShip9))
