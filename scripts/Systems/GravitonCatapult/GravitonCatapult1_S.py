###############################################################################
#	Filename:	GravitonCatapult1_S.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
###############################################################################
import App
import loadspacehelper
import MissionLib
import SelfDefenseAI																		
import FriendlyNWAI
import EnemyNWAI

def Initialize(pSet):

	# Create Ships
        if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):


                #GravitonCatapult
                pGravitonCatapult1       = loadspacehelper.CreateShip("JLSGravitonCatapult", pSet, "Graviton Catapult", "Subspace Graviton Catapult")

        if (App.g_kUtopiaModule.IsMultiplayer()):
                pMission = MissionLib.GetMission ()
                SetupEventHandlers(pMission)
        else:
                pGravitonCatapult1.SetAI(SelfDefenseAI.CreateAI(pGravitonCatapult1))



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

                
                pSet = App.g_kSetManager.GetSet("GravitonCatapult1")
                pGravitonCatapult1 = App.ShipClass_GetObject(pSet, "Graviton Catapult")


                if pGravitonCatapult1 != None:
                        pGravitonCatapult1.SetAI(SelfDefenseAI.CreateAI(pGravitonCatapult1))



        pGame = App.Game_GetCurrentGame()

        pPlayer = pGame.GetPlayer()

        pEpisode = pGame.GetCurrentEpisode()
        pMission = pEpisode.GetCurrentMission()
        pFriendlies = pMission.GetFriendlyGroup()
        pEnemies = pMission.GetEnemyGroup()
       

        import Custom.NanoFXv2.NanoFX_Lib
        sRace = Custom.NanoFXv2.NanoFX_Lib.GetSpeciesName(pPlayer)

        if (sRace == "Federation") or (sRace == "Klingon"):
            pFriendlies.AddName("Graviton Catapult")

          
            
            # AI's:
            import FriendlyNWAI     
            pGravitonCatapult1.SetAI(FriendlyNWAI.CreateAI(pGravitonCatapult1))


        else:
            pEnemies.AddName("Graviton Catapult")           



            # AI's:
            import EnemyNWAI        
            pGravitonCatapult1.SetAI(EnemyNWAI.CreateAI(pGravitonCatapult1))


	