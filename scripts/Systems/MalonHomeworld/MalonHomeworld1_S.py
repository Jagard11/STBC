import App
import MissionLib
import Tactical.LensFlares
import loadspacehelper
import SelfDefenseAI

def Initialize(pSet):


	if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
		# Create ship
		pMalonPlanet	= loadspacehelper.CreateShip("MalonPlanet", pSet, "MalonHomeworld", "Malon Location")

		pMalonPlanet.SetInvincible(1)
		pMalonPlanet.SetHurtable(0)
		pMalonPlanet.SetTargetable(1)
		pMalonPlanet.SetCollisionsOn(1)
		pMalonPlanet.SetScale(30.0)
		vCurVelocity = App.TGPoint3()
		vCurVelocity.SetXYZ(0, 0, -0.01)
		pMalonPlanet.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		MissionLib.HideSubsystems(pMalonPlanet)

		from Custom.Autoload import PlanetShipAddon
		PlanetShipAddon.SetPlanetShipGlowSize(pMalonPlanet, 55)
		PlanetShipAddon.SetPlanetShipGlowColor(pMalonPlanet, 0.501961, 1.000000, 0.000000, 0.22)
		PlanetShipAddon.SetPlanetShipAtmosphereScript(pMalonPlanet, "AtmosphereMP")
		PlanetShipAddon.SetPlanetShipAtmosphereScaleBonus(pMalonPlanet, 0.001)
		PlanetShipAddon.SetPlanetShipAtmosphereAngularVelocity(pMalonPlanet, 0, 0, -0.015)

	if (App.g_kUtopiaModule.IsMultiplayer()):
		pMission = MissionLib.GetMission ()
		SetupEventHandlers(pMission)

	else:
		pMalonPlanet.SetAI(SelfDefenseAI.CreateAI(pMalonPlanet)) 

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


	pSet = App.g_kSetManager.GetSet("MalonHomeworld1")
	pMalon = App.Planet_GetObject(pSet, "Malon")
	pMalonPlanet = App.ShipClass_GetObject(pSet, "MalonHomeworld")
	if pMalonPlanet != None:
		pNeutralGroup.AddName("MalonHomeworld")
		pMalonPlanet.SetAI(SelfDefenseAI.CreateAI(pMalonPlanet))
