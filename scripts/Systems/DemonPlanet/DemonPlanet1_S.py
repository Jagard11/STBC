import App
import MissionLib
import Tactical.LensFlares
import loadspacehelper
import SelfDefenseAI

def Initialize(pSet):


	if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
		# Create ship
		pDemonPlanet	= loadspacehelper.CreateShip("DemonPlanet", pSet, "DemonPlanet", "DemonPlanet Location")

		pDemonPlanet.SetInvincible(1)
		pDemonPlanet.SetHurtable(0)
		pDemonPlanet.SetTargetable(1)
		pDemonPlanet.SetCollisionsOn(1)
		pDemonPlanet.SetScale(24.0)
		vCurVelocity = App.TGPoint3()
		vCurVelocity.SetXYZ(0, 0, -0.01)
		pDemonPlanet.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		MissionLib.HideSubsystems(pDemonPlanet)

		from Custom.Autoload import PlanetShipAddon
		PlanetShipAddon.SetPlanetShipGlowSize(pDemonPlanet, 55)
		PlanetShipAddon.SetPlanetShipGlowColor(pDemonPlanet, 0.996078, 0.800000, 0.580392, 0.22)
		PlanetShipAddon.SetPlanetShipAtmosphereScript(pDemonPlanet, "AtmosphereE")
		PlanetShipAddon.SetPlanetShipAtmosphereScaleBonus(pDemonPlanet, 0.001)
		PlanetShipAddon.SetPlanetShipAtmosphereAngularVelocity(pDemonPlanet, 0, 0, -0.015)

	if (App.g_kUtopiaModule.IsMultiplayer()):
		pMission = MissionLib.GetMission ()
		SetupEventHandlers(pMission)

	else:
		pDemonPlanet.SetAI(SelfDefenseAI.CreateAI(pDemonPlanet)) 

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


	pSet = App.g_kSetManager.GetSet("DemonPlanet1")
	pEarth = App.Planet_GetObject(pSet, "Earth")
	pDemonPlanet = App.ShipClass_GetObject(pSet, "DemonPlanet")
	if pDemonPlanet != None:
		pNeutralGroup.AddName("DemonPlanet")
		pDemonPlanet.SetAI(SelfDefenseAI.CreateAI(pDemonPlanet))
