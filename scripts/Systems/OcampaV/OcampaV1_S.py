import App
import MissionLib
import Tactical.LensFlares
import loadspacehelper
import SelfDefenseAI

def Initialize(pSet):

	# Add a sun, far far away
	pSun = App.Sun_Create(5000.0, 5000.0, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun, "Sun")
        
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Yellow lens flare, attached to the sun
	Tactical.LensFlares.YellowLensFlare(pSet, pSun)

	# Create the Planet - 12,756 km diameter
	pOcampa = App.Planet_Create(743.00, "data/models/environment/earth.nif")
	pSet.AddObjectToSet(pOcampa, "Ocampa")

	# Place the object at the specified location.
	pOcampa.PlaceObjectByName( "Ocampa" )
	pOcampa.UpdateNodeOnly()
	pOcampa.SetHidden(1)

	if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
		# Create ship
		pOcampaPlanet        = loadspacehelper.CreateShip("OcampaPlanet", pSet, "0campa", "Ocampa Location")

		pOcampaPlanet.SetInvincible(1)
		pOcampaPlanet.SetHurtable(0)
		pOcampaPlanet.SetTargetable(1)
		pOcampaPlanet.SetCollisionsOn(1)
		pOcampaPlanet.SetScale(30.0)
		vCurVelocity = App.TGPoint3()
		vCurVelocity.SetXYZ(0, 0, -0.01)
		pOcampaPlanet.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		from Custom.Autoload import PlanetShipAddon
		PlanetShipAddon.SetPlanetShipGlowSize(pOcampaPlanet, 55)
		PlanetShipAddon.SetPlanetShipGlowColor(pOcampaPlanet, 0.992157, 0.756863, 0.215686, 0.32)
		PlanetShipAddon.SetPlanetShipAtmosphereScript(pOcampaPlanet, "AtmosphereO")
		PlanetShipAddon.SetPlanetShipAtmosphereScaleBonus(pOcampaPlanet, 0.001)
		PlanetShipAddon.SetPlanetShipAtmosphereAngularVelocity(pOcampaPlanet, 0, 0, -0.0051)

		MissionLib.HideSubsystems(pOcampaPlanet)

	if (App.g_kUtopiaModule.IsMultiplayer()):
		pMission = MissionLib.GetMission ()
		SetupEventHandlers(pMission)

	else:
		pOcampaPlanet.SetAI(SelfDefenseAI.CreateAI(pOcampaPlanet)) 

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


	pSet = App.g_kSetManager.GetSet("OcampaV1")
	pOcampa = App.Planet_GetObject(pSet, "0campa")

	pOcampaPlanet = App.ShipClass_GetObject(pSet, "0campa")

	if pOcampaPlanet != None:
		pNeutralGroup.AddName("Ocampa")
		pOcampaPlanet.SetAI(SelfDefenseAI.CreateAI(pOcampaPlanet))
