import App
import MissionLib
import Tactical.LensFlares
import loadspacehelper
import SelfDefenseAI
import DefendAI

def Initialize(pSet):



	if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):

                pHub1       = loadspacehelper.CreateShip("JLSBorgHub", pSet, "Transwarp Hub", "Hub Location")

		# Create ship
		pTranswarpHubSunC	= loadspacehelper.CreateShip("TranswarpHubSun", pSet, "Sun", "Sun Location")

		pTranswarpHubSunC.SetInvincible(1)
		pTranswarpHubSunC.SetHurtable(0)
		pTranswarpHubSunC.SetTargetable(0)
		pTranswarpHubSunC.SetCollisionsOn(0)
		pTranswarpHubSunC.SetScale(320.0)
		vCurVelocity = App.TGPoint3()
		vCurVelocity.SetXYZ(0, 0, -0.01)
		pTranswarpHubSunC.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)


		MissionLib.HideSubsystems(pTranswarpHubSunC)

		#Create More Ships
                #Borg
                pBorg2       = loadspacehelper.CreateShip("JLSBorgCube", pSet, "Borg Cube 1", "Borg2 Location")

                #Borg
                pBorg3      = loadspacehelper.CreateShip("JLSBorgSphere", pSet, "Borg Sphere", "Borg3 Location")

                #Borg
                pBorg4       = loadspacehelper.CreateShip("JLSBorgCube", pSet, "Borg Cube 2", "Borg1 Location")

                #Borg
                pBorg5       = loadspacehelper.CreateShip("JLSBorgTacticalCube", pSet, "Borg Tactical Cube", "Borg5 Location")

                #Borg
                pBorg6       = loadspacehelper.CreateShip("JLSBorgCube", pSet, "Borg Cube", "Borg6 Location")

                #Borg
                pBorg7      = loadspacehelper.CreateShip("JLSBorgSphere", pSet, "Borg Sphere 1", "Borg7 Location")

                #Borg
                pBorg8       = loadspacehelper.CreateShip("JLSBorgTacticalCube", pSet, "Borg Tactical Cube 1", "Borg8 Location")

                #Borg
                pBorg9       = loadspacehelper.CreateShip("JLSBorgDiamond", pSet, "Borg Diamond", "Borg9 Location")

                #Borg
                pBorg10       = loadspacehelper.CreateShip("JLSBorgCube", pSet, "Borg Cube 4", "Borg10 Location")
                

	if (App.g_kUtopiaModule.IsMultiplayer()):
		pMission = MissionLib.GetMission ()
		SetupEventHandlers(pMission)

	else:
		pTranswarpHubSunC.SetAI(SelfDefenseAI.CreateAI(pTranswarpHubSunC)) 
                pBorg2.SetAI(SelfDefenseAI.CreateAI(pBorg2))    
                pBorg3.SetAI(SelfDefenseAI.CreateAI(pBorg3))
                pBorg4.SetAI(SelfDefenseAI.CreateAI(pBorg4))    
                pBorg5.SetAI(SelfDefenseAI.CreateAI(pBorg5))
                pBorg6.SetAI(SelfDefenseAI.CreateAI(pBorg6))
                pBorg7.SetAI(SelfDefenseAI.CreateAI(pBorg7))
                pBorg8.SetAI(SelfDefenseAI.CreateAI(pBorg8))    
                pBorg9.SetAI(SelfDefenseAI.CreateAI(pBorg9))
                pBorg10.SetAI(SelfDefenseAI.CreateAI(pBorg10))


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


	pSet = App.g_kSetManager.GetSet("TranswarpHub1")
	pTranswarpHubSunC = App.ShipClass_GetObject(pSet, "TranswarpHubC")

        pBorg2 = App.ShipClass_GetObject(pSet, "Borg Cube 1")
        pBorg3 = App.ShipClass_GetObject(pSet, "Borg Sphere")
        pBorg4 = App.ShipClass_GetObject(pSet, "Borg Cube 2")
        pBorg5 = App.ShipClass_GetObject(pSet, "Borg Tactical Cube")
        pBorg6 = App.ShipClass_GetObject(pSet, "Borg Cube")
        pBorg7 = App.ShipClass_GetObject(pSet, "Borg Sphere 1")
        pBorg8 = App.ShipClass_GetObject(pSet, "Borg Cube 3")
        pBorg9 = App.ShipClass_GetObject(pSet, "Borg Diamond")
        pBorg10 = App.ShipClass_GetObject(pSet, "Borg Tactical Cube 1")


	if pTranswarpHubSunC != None:
		pNeutralGroup.AddName("TranswarpHub")
		pTranswarpHubSunC.SetAI(SelfDefenseAI.CreateAI(pTranswarpHubSunC))
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
                        pBorg19.SetAI(SelfDefenseAI.CreateAI(pBorg9))
                if pBorg10 != None:   
                        pBorg10.SetAI(SelfDefenseAI.CreateAI(pBorg10))
