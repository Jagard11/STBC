###############################################################################
#	Filename:	Unicomplex1_S.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
###############################################################################
import App
import loadspacehelper
import MissionLib
import SelfDefenseAI

def Initialize(pSet):

	# Create Ships
        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):


                #BUnicomplex
                pBUnicomplex1       = loadspacehelper.CreateShip("JLSUnicomplex", pSet, "Borg Unicomplex", "Unicomplex Location")



		#Create More Ships
		#Borg

		#HEY JB - what you were doing wrong here was the sShipClass variable, for all ships...
		#for example, you made them like:
		#    sShipClass = "<JLSBorgCube>"
		#while it should be:
		#    sShipClass = "JLSBorgCube"
		#Also, while it didn't matter, you were setting the sShipClass variable before and after each code block. Why? It just needed to be set
		#before each code block.

		GC_AddFundsToCreateShip("JLSBorgCube")  #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pBorg2       = loadspacehelper.CreateShip("JLSBorgCube", pSet, "Borg Cube 1", "Borg2 Location")

		GC_AddFundsToCreateShip("JLSBorgSphere") #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pBorg3      = loadspacehelper.CreateShip("JLSBorgSphere", pSet, "Borg Sphere", "Borg3 Location")

		GC_AddFundsToCreateShip("JLSBorgCube") #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pBorg4       = loadspacehelper.CreateShip("JLSBorgCube", pSet, "Borg Cube 2", "Borg1 Location")

		GC_AddFundsToCreateShip("JLSBorgTacticalCube") #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pBorg5       = loadspacehelper.CreateShip("JLSBorgTacticalCube", pSet, "Borg Tactical Cube", "Borg5 Location")

		GC_AddFundsToCreateShip("JLSBorgCube") #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pBorg6       = loadspacehelper.CreateShip("JLSBorgCube", pSet, "Borg Cube", "Borg6 Location")

		GC_AddFundsToCreateShip("JLSBorgSphere") #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pBorg7      = loadspacehelper.CreateShip("JLSBorgSphere", pSet, "Borg Sphere 1", "Borg7 Location")

		GC_AddFundsToCreateShip("JLSBorgTacticalCube") #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pBorg8       = loadspacehelper.CreateShip("JLSBorgTacticalCube", pSet, "Borg Tactical Cube 1", "Borg8 Location")

		GC_AddFundsToCreateShip("JLSBorgDiamond") #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pBorg9       = loadspacehelper.CreateShip("JLSBorgDiamond", pSet, "Borg Diamond", "Borg9 Location")

		GC_AddFundsToCreateShip("JLSBorgCube") #HEY JB - here am I, calling the function of the code block I made here, with the sShipClass string - the same as its used in the first argument to the loadspacehelper.CreateShip(...) function called below.
		pBorg10       = loadspacehelper.CreateShip("JLSBorgCube", pSet, "Borg Cube 4", "Borg10 Location")

        if (App.g_kUtopiaModule.IsMultiplayer()):
                pMission = MissionLib.GetMission ()
                SetupEventHandlers(pMission)
        else:
                pBUnicomplex1.SetAI(SelfDefenseAI.CreateAI(pBUnicomplex1))
                pBorg2.SetAI(SelfDefenseAI.CreateAI(pBorg2))    
                pBorg3.SetAI(SelfDefenseAI.CreateAI(pBorg3))
                pBorg4.SetAI(SelfDefenseAI.CreateAI(pBorg4))    
                pBorg5.SetAI(SelfDefenseAI.CreateAI(pBorg5))
                pBorg6.SetAI(SelfDefenseAI.CreateAI(pBorg6))
                pBorg7.SetAI(SelfDefenseAI.CreateAI(pBorg7))
                pBorg8.SetAI(SelfDefenseAI.CreateAI(pBorg8))    
                pBorg9.SetAI(SelfDefenseAI.CreateAI(pBorg9))
                pBorg10.SetAI(SelfDefenseAI.CreateAI(pBorg10))

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
                pNeutralGroup = pMission.GetNeutralGroup ()

                # First clear the groups.  We will be reading everybody
                # so we want to start with an empty group.
                #pEnemyGroup.RemoveAllNames ()

                #pPlayerList = pNetwork.GetPlayerList ()
                #iNumPlayers = pPlayerList.GetNumPlayers ()

                #for i in range(iNumPlayers):
                        #pPlayer = pPlayerList.GetPlayerAtIndex (i)
                        #iPlayerID = pPlayer.GetNetID ()
                        #pShip = pGame.GetShipFromPlayerID (iPlayerID)           

                        #if (pShip):
                        #        # Good, there is a ship for this player
                        #        # Determine which team the player is on
                        #        pEnemyGroup.AddName (pShip.GetName ())

                
                pSet = App.g_kSetManager.GetSet("Unicomplex1")
                pBUnicomplex1 = App.ShipClass_GetObject(pSet, "Borg Unicomplex")
     		pBorg2 = App.ShipClass_GetObject(pSet, "Borg Cube 1")
   		pBorg3 = App.ShipClass_GetObject(pSet, "Borg Sphere")
   		pBorg4 = App.ShipClass_GetObject(pSet, "Borg Cube 2")
   		pBorg5 = App.ShipClass_GetObject(pSet, "Borg Tactical Cube")
    		pBorg6 = App.ShipClass_GetObject(pSet, "Borg Cube")
    		pBorg7 = App.ShipClass_GetObject(pSet, "Borg Sphere 1")
    		pBorg8 = App.ShipClass_GetObject(pSet, "Borg Cube 3")
    		pBorg9 = App.ShipClass_GetObject(pSet, "Borg Diamond")
    		pBorg10 = App.ShipClass_GetObject(pSet, "Borg Tactical Cube 1")

                if pBUnicomplex1 != None:
                        pBUnicomplex1.SetAI(SelfDefenseAI.CreateAI(pBUnicomplex1))
                if pBorg2 != None:   
                        pBorg2.SetAI(SelfDefenseAI.CreateAI(pBorg2))    
                if pBorg3 != None:
                        pBorg3.SetAI(SelfDefenseAI.CreateAI(pBorg3))
                if pBorg4 != None:   
                        pBorg4.SetAI(SelfDefenseAI.CreateAI(pBorg4))    
                if pBorg5 != None:   
                        pBorg5.SetAI(SelfDefenseAI.CreateAI(pBorg5))
                if pBorg6 != None:  
                        pBorg6.SetAI(SelfDefenseAI.CreateAI(pBorg6))
                if pBorg7 != None: 
                        pBorg7.SetAI(SelfDefenseAI.CreateAI(pBorg7))
                if pBorg8 != None:   
                        pBorg8.SetAI(SelfDefenseAI.CreateAI(pBorg8))    
                if pBorg9 != None:   
                        pBorg9.SetAI(SelfDefenseAI.CreateAI(pBorg9))
                if pBorg10 != None:   
                        pBorg10.SetAI(SelfDefenseAI.CreateAI(pBorg10))



 
