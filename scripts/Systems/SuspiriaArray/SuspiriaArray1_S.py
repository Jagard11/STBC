###############################################################################
#	Filename:	SuspiriaArray1_S.py
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

                #Suspiria
                pSuspiria1       = loadspacehelper.CreateShip("JLSSuspiriaArray", pSet, "Suspiria Array", "Suspiria Location")
		fSpeed = 360.0/3.5                           # Rotation speed, in degrees per seconds
		vVelocity = App.TGPoint3()
		vVelocity.SetXYZ(0.0, 1.0, 0.0)              # Rotation direction
		vVelocity.Unitize()
		vVelocity.Scale(fSpeed*App.HALF_PI/180.0)    # Convert fSpeed from degrees to radians (game works with)
		pSuspiria1.SetAngularVelocity(vVelocity, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)

        if (App.g_kUtopiaModule.IsMultiplayer()):
                pMission = MissionLib.GetMission ()
                SetupEventHandlers(pMission)
        else:
                pSuspiria1.SetAI(SelfDefenseAI.CreateAI(pSuspiria1))


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

                
                pSet = App.g_kSetManager.GetSet("SuspiriaArray1")
                pSuspiria1 = App.ShipClass_GetObject(pSet, "Suspiria Array")
                if pSuspiria1 != None:
                        pSuspiria1.SetAI(SelfDefenseAI.CreateAI(pSuspiria1))
