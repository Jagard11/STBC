import App
import MissionLib
import Tactical.LensFlares
import loadspacehelper
import SelfDefenseAI

def Initialize(pSet):

	if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
		# Create ship
		pDeltoriaC	= loadspacehelper.CreateShip("Deltoria", pSet, "Deltoria Gas Giant", "Deltoria Location")

		pDeltoriaC.SetInvincible(1)
		pDeltoriaC.SetHurtable(0)
		pDeltoriaC.SetTargetable(1)
		pDeltoriaC.SetCollisionsOn(1)
		pDeltoriaC.SetScale(30.0)
		vCurVelocity = App.TGPoint3()
		vCurVelocity.SetXYZ(0, 0, -0.01)
		pDeltoriaC.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		MissionLib.HideSubsystems(pDeltoriaC)

		from Custom.Autoload import PlanetShipAddon
		PlanetShipAddon.SetPlanetShipGlowSize(pDeltoriaC, 55)
		PlanetShipAddon.SetPlanetShipGlowColor(pDeltoriaC, 0.992157, 0.756863, 0.215686, 0.32)
		PlanetShipAddon.SetPlanetShipAtmosphereScript(pDeltoriaC, "AtmosphereGas")
		PlanetShipAddon.SetPlanetShipAtmosphereScaleBonus(pDeltoriaC, 0.001)
		PlanetShipAddon.SetPlanetShipAtmosphereAngularVelocity(pDeltoriaC, 0, 0, -0.015)

		# Create ship

		pTarokC	= loadspacehelper.CreateShip("Tarok", pSet, "Tarok Training Camp", "Tarok Location")

		pTarokC.SetInvincible(1)
		pTarokC.SetHurtable(0)
		pTarokC.SetTargetable(1)
		pTarokC.SetCollisionsOn(1)
		pTarokC.SetScale(17.0)
		vCurVelocity = App.TGPoint3()
		vCurVelocity.SetXYZ(0, 0, -0.01)
		pTarokC.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		MissionLib.HideSubsystems(pTarokC)

		from Custom.Autoload import PlanetShipAddon
		PlanetShipAddon.SetPlanetShipGlowSize(pTarokC, 55)
		PlanetShipAddon.SetPlanetShipGlowColor(pTarokC, 0.992157, 0.756863, 0.215686, 0.32)
		PlanetShipAddon.SetPlanetShipAtmosphereScript(pTarokC, "AtmosphereO")
		PlanetShipAddon.SetPlanetShipAtmosphereScaleBonus(pTarokC, 0.001)
		PlanetShipAddon.SetPlanetShipAtmosphereAngularVelocity(pTarokC, 0, 0, -0.015)

	if (App.g_kUtopiaModule.IsMultiplayer()):
		pMission = MissionLib.GetMission ()
		SetupEventHandlers(pMission)

	else:
		pDeltoriaC.SetAI(SelfDefenseAI.CreateAI(pDeltoriaC)) 
		pTarokC.SetAI(SelfDefenseAI.CreateAI(pTarokC)) 

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


	pSet = App.g_kSetManager.GetSet("Tarok1")
	pDeltoriaC = App.ShipClass_GetObject(pSet, "Deltoria Gas Giant")
	pTarokC = App.ShipClass_GetObject(pSet, "Tarok Training Camp")

	if pDeltoriaC != None:
		pNeutralGroup.AddName("Deltoria Gas Giant")
		pDeltoriaC.SetAI(SelfDefenseAI.CreateAI(pDeltoriaC))
	if pTarokC != None:
		pNeutralGroup.AddName("Tarok Training Camp")
		pTarokC.SetAI(SelfDefenseAI.CreateAI(pTarokC))
