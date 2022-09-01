import App
import MissionLib
import Tactical.LensFlares
import loadspacehelper
import SelfDefenseAI

def Initialize(pSet):

	if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
		# Create ship
		pTalaxC	= loadspacehelper.CreateShip("Talax", pSet, "Talaxian Homeworld", "Talax Location")

		pTalaxC.SetInvincible(1)
		pTalaxC.SetHurtable(0)
		pTalaxC.SetTargetable(1)
		pTalaxC.SetCollisionsOn(1)
		pTalaxC.SetScale(30.0)
		vCurVelocity = App.TGPoint3()
		vCurVelocity.SetXYZ(0, 0, -0.01)
		pTalaxC.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		MissionLib.HideSubsystems(pTalaxC)

		from Custom.Autoload import PlanetShipAddon
		PlanetShipAddon.SetPlanetShipGlowSize(pTalaxC, 55)
		PlanetShipAddon.SetPlanetShipGlowColor(pTalaxC, 0.509804, 0.509804, 1.000000, 0.92)
		PlanetShipAddon.SetPlanetShipAtmosphereScript(pTalaxC, "AtmosphereAv")
		PlanetShipAddon.SetPlanetShipAtmosphereScaleBonus(pTalaxC, 0.001)
		PlanetShipAddon.SetPlanetShipAtmosphereAngularVelocity(pTalaxC, 0, 0, -0.015)

		# Create ship

		pRinaxC	= loadspacehelper.CreateShip("Rinax", pSet, "Devastated Rinax", "Rinax Location")

		pRinaxC.SetInvincible(1)
		pRinaxC.SetHurtable(0)
		pRinaxC.SetTargetable(1)
		pRinaxC.SetCollisionsOn(1)
		pRinaxC.SetScale(15.0)
		vCurVelocity = App.TGPoint3()
		vCurVelocity.SetXYZ(0, 0, -0.01)
		pRinaxC.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		MissionLib.HideSubsystems(pRinaxC)

		from Custom.Autoload import PlanetShipAddon
		PlanetShipAddon.SetPlanetShipGlowSize(pRinaxC, 50)
		PlanetShipAddon.SetPlanetShipGlowColor(pRinaxC, 0.992157, 0.756863, 0.215686, 0.92)
		PlanetShipAddon.SetPlanetShipAtmosphereScript(pRinaxC, "AtmosphereO")
		PlanetShipAddon.SetPlanetShipAtmosphereScaleBonus(pRinaxC, 0.001)
		PlanetShipAddon.SetPlanetShipAtmosphereAngularVelocity(pRinaxC, 0, 0, -0.015)


	if (App.g_kUtopiaModule.IsMultiplayer()):
		pMission = MissionLib.GetMission ()
		SetupEventHandlers(pMission)

	else:
		pTalaxC.SetAI(SelfDefenseAI.CreateAI(pTalaxC)) 
		pRinaxC.SetAI(SelfDefenseAI.CreateAI(pRinaxC)) 


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


	pSet = App.g_kSetManager.GetSet("Talax1")
	pTalaxC = App.ShipClass_GetObject(pSet, "Talaxian Homeworld")
	pRinaxC = App.ShipClass_GetObject(pSet, "Devastated Rinax")


	if pTalaxC != None:
		pNeutralGroup.AddName("Talaxian Homeworld")
		pTalaxC.SetAI(SelfDefenseAI.CreateAI(pTalaxC))
	if pRinaxC != None:
		pNeutralGroup.AddName("Devastated Rinax")
		pRinaxC.SetAI(SelfDefenseAI.CreateAI(pRinaxC))

