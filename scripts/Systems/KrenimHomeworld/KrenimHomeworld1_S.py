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

	if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
		# Create ship
		pKrenimHomeworld2	= loadspacehelper.CreateShip("KrenimHomeworld", pSet, "Krenim Homeworld2", "Krenim Homeworld Location")

		pKrenimHomeworld2.SetInvincible(1)
		pKrenimHomeworld2.SetHurtable(0)
		pKrenimHomeworld2.SetTargetable(1)
		pKrenimHomeworld2.SetCollisionsOn(1)
		pKrenimHomeworld2.SetScale(30.0)
		vCurVelocity = App.TGPoint3()
		vCurVelocity.SetXYZ(0, 0, -0.01)
		pKrenimHomeworld2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		from Custom.Autoload import PlanetShipAddon
		PlanetShipAddon.SetPlanetShipGlowSize(pKrenimHomeworld2, 55)
		PlanetShipAddon.SetPlanetShipGlowColor(pKrenimHomeworld2, 0.509804, 0.509804, 1.000000, 0.22)
		PlanetShipAddon.SetPlanetShipAtmosphereScript(pKrenimHomeworld2, "AtmosphereAv")
		PlanetShipAddon.SetPlanetShipAtmosphereScaleBonus(pKrenimHomeworld2, 0.001)
		PlanetShipAddon.SetPlanetShipAtmosphereAngularVelocity(pKrenimHomeworld2, 0, 0, -0.015)

		MissionLib.HideSubsystems(pKrenimHomeworld2)


	if (App.g_kUtopiaModule.IsMultiplayer()):
		pMission = MissionLib.GetMission ()
		SetupEventHandlers(pMission)

	else:
		pKrenimHomeworld2.SetAI(SelfDefenseAI.CreateAI(pKrenimHomeworld2)) 

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


	pSet = App.g_kSetManager.GetSet("KrenimHomeworld1")
	pKrenimHomeworld2 = App.ShipClass_GetObject(pSet, "KrenimHomeworld")
	if pKrenimHomeworld2 != None:
		pNeutralGroup.AddName("EarthC")
		pKrenimHomeworld2.SetAI(SelfDefenseAI.CreateAI(pKrenimHomeworld2))
