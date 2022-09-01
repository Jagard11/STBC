import App
import MissionLib
import Tactical.LensFlares
import loadspacehelper
import SelfDefenseAI

def Initialize(pSet):

	if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
		# Create ship

		pVhnoriHomeworldC	= loadspacehelper.CreateShip("VhnoriHomeworld", pSet, "The Vhnori Homeworld", "Vhnori Homeworld Location")

		pVhnoriHomeworldC.SetInvincible(1)
		pVhnoriHomeworldC.SetHurtable(0)
		pVhnoriHomeworldC.SetTargetable(1)
		pVhnoriHomeworldC.SetCollisionsOn(1)
		pVhnoriHomeworldC.SetScale(17.0)
		vCurVelocity = App.TGPoint3()
		vCurVelocity.SetXYZ(0, 0, -0.01)
		pVhnoriHomeworldC.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		MissionLib.HideSubsystems(pVhnoriHomeworldC)

		pVhnoriR	= loadspacehelper.CreateShip("VhnoriRings", pSet, "The Vhnori Rings", "Vhnori Rings Location")

		pVhnoriR.SetInvincible(1)
		pVhnoriR.SetHurtable(0)
		pVhnoriR.SetTargetable(1)
		pVhnoriR.SetCollisionsOn(1)
		pVhnoriR.SetScale(19.0)
		vCurVelocity = App.TGPoint3()
		vCurVelocity.SetXYZ(0, 0, -0.01)
		pVhnoriR.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		MissionLib.HideSubsystems(pVhnoriR)

		from Custom.Autoload import PlanetShipAddon
		PlanetShipAddon.SetPlanetShipGlowSize(pVhnoriHomeworldC, 55)
		PlanetShipAddon.SetPlanetShipGlowColor(pVhnoriHomeworldC, 0.623529, 0.733333, 0.196078, 0.42)
		PlanetShipAddon.SetPlanetShipAtmosphereScript(pVhnoriHomeworldC, "AtmosphereAv")
		PlanetShipAddon.SetPlanetShipAtmosphereScaleBonus(pVhnoriHomeworldC, 0.001)
		PlanetShipAddon.SetPlanetShipAtmosphereAngularVelocity(pVhnoriHomeworldC, 0, 0, -0.015)











	if (App.g_kUtopiaModule.IsMultiplayer()):
		pMission = MissionLib.GetMission ()
		SetupEventHandlers(pMission)

	else: 
		pVhnoriHomeworldC.SetAI(SelfDefenseAI.CreateAI(pVhnoriHomeworldC)) 
		pVhnoriR.SetAI(SelfDefenseAI.CreateAI(pVhnoriR))


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


	pSet = App.g_kSetManager.GetSet("VhnoriHomeworld1")
	pVhnoriHomeworldC = App.ShipClass_GetObject(pSet, "The Vhnori Homeworld")

	if pVhnoriHomeworldC != None:
		pNeutralGroup.AddName("The Vhnori Homeworld")
		pVhnoriHomeworldC.SetAI(SelfDefenseAI.CreateAI(pVhnoriHomeworldC))
	if pVhnoriR != None:
		pNeutralGroup.AddName("The Vhnori Rings")
		pVhnoriR.SetAI(SelfDefenseAI.CreateAI(pVhnoriR))

