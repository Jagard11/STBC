import App
import MissionLib
import Tactical.LensFlares
import loadspacehelper
import SelfDefenseAI

def Initialize(pSet):

	# Add a sun, far far away
	pSun = App.Sun_Create(500000.0, 500000.0, 5000, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun, "Sun")
        
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Yellow lens flare, attached to the sun
	Tactical.LensFlares.YellowLensFlare(pSet, pSun)


	if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
		# Create ship
		pIcePlanet1	= loadspacehelper.CreateShip("IcePlanet", pSet, "IcepIanet", "IcePlanet Location")

		pIcePlanet1.SetInvincible(1)
		pIcePlanet1.SetHurtable(0)
		pIcePlanet1.SetTargetable(1)
		pIcePlanet1.SetCollisionsOn(1)
		pIcePlanet1.SetScale(18.0)
		vCurVelocity = App.TGPoint3()
		vCurVelocity.SetXYZ(0, 0, -0.01)
		pIcePlanet1.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		MissionLib.HideSubsystems(pIcePlanet1)

		from Custom.Autoload import PlanetShipAddon
		PlanetShipAddon.SetPlanetShipGlowSize(pIcePlanet1, 55)
		PlanetShipAddon.SetPlanetShipGlowColor(pIcePlanet1, 0.509804, 0.509804, 1.000000, 0.22)
		PlanetShipAddon.SetPlanetShipAtmosphereScript(pIcePlanet1, "AtmosphereAv")
		PlanetShipAddon.SetPlanetShipAtmosphereScaleBonus(pIcePlanet1, 0.001)
		PlanetShipAddon.SetPlanetShipAtmosphereAngularVelocity(pIcePlanet1, 0, 0, -0.015)

	if (App.g_kUtopiaModule.IsMultiplayer()):
		pMission = MissionLib.GetMission ()
		SetupEventHandlers(pMission)

	else:
		pIcePlanet1.SetAI(SelfDefenseAI.CreateAI(pIcePlanet1)) 

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


	pSet = App.g_kSetManager.GetSet("IcePlanet1")
	pIcePlanet1 = App.ShipClass_GetObject(pSet, "IcepIanet")

	if pIcePlanet1 != None:
		pNeutralGroup.AddName("IcepIanet")
		pIcePlanet1.SetAI(SelfDefenseAI.CreateAI(pIcePlanet1))
