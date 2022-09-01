import App
import MissionLib
import Tactical.LensFlares
import loadspacehelper
import SelfDefenseAI

def Initialize(pSet):

	if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
		# Create ship
		pSikaris	= loadspacehelper.CreateShip("Sikaris", pSet, "Sikaris", "Sikaris Location")

		pSikaris.SetInvincible(1)
		pSikaris.SetHurtable(0)
		pSikaris.SetTargetable(1)
		pSikaris.SetCollisionsOn(1)
		pSikaris.SetScale(20.0)
		vCurVelocity = App.TGPoint3()
		vCurVelocity.SetXYZ(0, 0, -0.01)
		pSikaris.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		MissionLib.HideSubsystems(pSikaris)

		from Custom.Autoload import PlanetShipAddon
		PlanetShipAddon.SetPlanetShipGlowSize(pSikaris, 55)
		PlanetShipAddon.SetPlanetShipGlowColor(pSikaris, 0.133333, 0.062745, 0.772549, 0.92)
		PlanetShipAddon.SetPlanetShipAtmosphereScript(pSikaris, "AtmosphereAv")
		PlanetShipAddon.SetPlanetShipAtmosphereScaleBonus(pSikaris, 0.001)
		PlanetShipAddon.SetPlanetShipAtmosphereAngularVelocity(pSikaris, 0, 0, -0.015)

	if (App.g_kUtopiaModule.IsMultiplayer()):
		pMission = MissionLib.GetMission ()
		SetupEventHandlers(pMission)

	else:
		pSikaris.SetAI(SelfDefenseAI.CreateAI(pSikaris)) 

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


	pSet = App.g_kSetManager.GetSet("Sikaris1")
	pSikaris = App.ShipClass_GetObject(pSet, "Sikaris")
	if pSikaris != None:
		pNeutralGroup.AddName("Sikaris")
		pSikaris.SetAI(SelfDefenseAI.CreateAI(pSikaris))
