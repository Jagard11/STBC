import App
import MissionLib
import Tactical.LensFlares
import loadspacehelper
import SelfDefenseAI

def Initialize(pSet):

	#Add Nebular
	# name of external texture (no need for alpha)
#	print("Building nebula")
	pNebula = App.MetaNebula_Create(10.0 / 87.75, 99.0 / 40.0, 40.0 / 40.5, 40.0, 5.0, "data/Backgrounds/JLSWater.tga", "data/Backgrounds/JLSWater.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(20.0, 20.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size 
	pNebula.AddNebulaSphere(1500.827942, 50.803833, 40.0, 700.0)

	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Water")


	# Add a sun, far far away
	pSun = App.Sun_Create(5000.0, 5000.0, 500, "data/Textures/SunYellow.tga", "data/Textures/Effects/SunFlaresYellow.tga")
	pSet.AddObjectToSet(pSun, "Sun")
        
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Yellow lens flare, attached to the sun
	Tactical.LensFlares.YellowLensFlare(pSet, pSun)

	if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
		# Create ship
		pWaterPlanetA	= loadspacehelper.CreateShip("WaterPlanet", pSet, "WaterPlanet", "WaterPlanet Location")

		pWaterPlanetA.SetInvincible(1)
		pWaterPlanetA.SetHurtable(0)
		pWaterPlanetA.SetTargetable(1)
		pWaterPlanetA.SetCollisionsOn(0)
		pWaterPlanetA.SetScale(31.4)
		vCurVelocity = App.TGPoint3()
		vCurVelocity.SetXYZ(0, 0, -0.01)
		pWaterPlanetA.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		MissionLib.HideSubsystems(pWaterPlanetA)

		from Custom.Autoload import PlanetShipAddon
		PlanetShipAddon.SetPlanetShipGlowSize(pWaterPlanetA, 55)
		PlanetShipAddon.SetPlanetShipGlowColor(pWaterPlanetA, 0.133333, 0.062745, 0.772549, 0.92)
		PlanetShipAddon.SetPlanetShipAtmosphereScript(pWaterPlanetA, "AtmosphereD")
		PlanetShipAddon.SetPlanetShipAtmosphereScaleBonus(pWaterPlanetA, 0.001)
		PlanetShipAddon.SetPlanetShipAtmosphereAngularVelocity(pWaterPlanetA, 0, 0, -0.015)

	if (App.g_kUtopiaModule.IsMultiplayer()):
		pMission = MissionLib.GetMission ()
		SetupEventHandlers(pMission)

	else:
		pWaterPlanetA.SetAI(SelfDefenseAI.CreateAI(pWaterPlanetA)) 


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


	pSet = App.g_kSetManager.GetSet("WaterPlanet1")
	pWaterPlanetA = App.Planet_GetObject(pSet, "WaterPlanet")
	pWaterPlanetA = App.ShipClass_GetObject(pSet, "WaterPlanet")
	if pWaterPlanet != None:
		pNeutralGroup.AddName("WaterPlanet")
		pWaterPlanetA.SetAI(SelfDefenseAI.CreateAI(pWaterPlanet))
