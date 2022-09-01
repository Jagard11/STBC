###############################################################################
#	Filename:	CaretakerArray1_S.py
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

                #Kazon
                pKazon1       = loadspacehelper.CreateShip("JLSKazonRaider", pSet, "Kazon Raider", "Kazon1 Location")

                #Kazon
                pKazon2       = loadspacehelper.CreateShip("JLSKazonPredator", pSet, "Kazon Predator", "Kazon2 Location")

                #Kazon
                pKazon3      = loadspacehelper.CreateShip("JLSKazonRaider", pSet, "Kazon Raider1", "Kazon3 Location")

                #Caretaker
                pCaretaker1       = loadspacehelper.CreateShip("JLSCaretakerArray", pSet, "Caretaker Array", "Caretaker Location")
		fSpeed = 360.0/3.5                           # Rotation speed, in degrees per seconds
		vVelocity = App.TGPoint3()
		vVelocity.SetXYZ(0.0, 1.0, 0.0)              # Rotation direction
		vVelocity.Unitize()
		vVelocity.Scale(fSpeed*App.HALF_PI/180.0)    # Convert fSpeed from degrees to radians (game works with)
		pCaretaker1.SetAngularVelocity(vVelocity, App.PhysicsObjectClass.DIRECTION_WORLD_SPACE)

        if (App.g_kUtopiaModule.IsMultiplayer()):
                pMission = MissionLib.GetMission ()
                SetupEventHandlers(pMission)
        else:
                pCaretaker1.SetAI(SelfDefenseAI.CreateAI(pCaretaker1))
                pKazon1.SetAI(SelfDefenseAI.CreateAI(pKazon1))
                pKazon2.SetAI(SelfDefenseAI.CreateAI(pKazon2))    
                pKazon3.SetAI(SelfDefenseAI.CreateAI(pKazon3))


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

                
                pSet = App.g_kSetManager.GetSet("CaretakerArray1")
                pCaretaker1 = App.ShipClass_GetObject(pSet, "Caretaker Array")
                pKazon1 = App.ShipClass_GetObject(pSet, "Kazon Raider")
                pKazon2 = App.ShipClass_GetObject(pSet, "Kazon Predator")
                pKazon3 = App.ShipClass_GetObject(pSet, "Kazon Raider1")
                if pCaretaker1 != None:
                        pCaretaker1.SetAI(SelfDefenseAI.CreateAI(pCaretaker1))
                if pKazon1 != None:   
                        pKazon1.SetAI(SelfDefenseAI.CreateAI(pKazon1))
                if pKazon2 != None:   
                        pKazon2.SetAI(SelfDefenseAI.CreateAI(pKazon2))    
                if pKazon3 != None:   
                        pKazon1.SetAI(SelfDefenseAI.CreateAI(pKazon3))


 
