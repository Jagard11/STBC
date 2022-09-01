import App
import MissionLib
import Tactical.LensFlares
import loadspacehelper
import SelfDefenseAI
import StarbaseMPAI
import AttackAI

def Initialize(pSet):

	# Add a sun, far far away
	pSun = App.Sun_Create(5000.0, 5000.0, 500, "data/Textures/SunBlueWhite.tga", "data/Textures/Effects/SunFlaresBlue.tga")
	pSet.AddObjectToSet(pSun, "Sun")
        
	# Place the object at the specified location.
	pSun.PlaceObjectByName( "Sun" )
	pSun.UpdateNodeOnly()

	# Builds a Yellow lens flare, attached to the sun
	Tactical.LensFlares.YellowLensFlare(pSet, pSun)


	if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):
		# Create ship
		pVeloceS	= loadspacehelper.CreateShip("Veloce", pSet, "Veloce", "Veloce Location")

		pVeloceS.SetInvincible(1)
		pVeloceS.SetHurtable(0)
		pVeloceS.SetTargetable(1)
		pVeloceS.SetCollisionsOn(1)
		pVeloceS.SetScale(38.0)
		vCurVelocity = App.TGPoint3()
		vCurVelocity.SetXYZ(0, 0, -195.01)
		pVeloceS.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		MissionLib.HideSubsystems(pVeloceS)

		from Custom.Autoload import PlanetShipAddon
		PlanetShipAddon.SetPlanetShipGlowSize(pVeloceS, 60)
		PlanetShipAddon.SetPlanetShipGlowColor(pVeloceS, 0.509804, 0.509804, 1.000000, 0.32)
		PlanetShipAddon.SetPlanetShipAtmosphereScript(pVeloceS, "AtmosphereUn")
		PlanetShipAddon.SetPlanetShipAtmosphereScaleBonus(pVeloceS, 0.001)
		PlanetShipAddon.SetPlanetShipAtmosphereAngularVelocity(pVeloceS, 0, 0, -195.01)


		pTractorp	= loadspacehelper.CreateShip("JLSTractor", pSet, "Tractor", "Tractor Location")

		pTractorp.SetInvincible(1)
		pTractorp.SetHurtable(0)
		pTractorp.SetTargetable(0)
		pTractorp.SetCollisionsOn(0)
		pTractorp.SetScale(32.0)


		MissionLib.HideSubsystems(pTractorp)

	if (App.g_kUtopiaModule.IsMultiplayer()):
		pMission = MissionLib.GetMission ()
		SetupEventHandlers(pMission)

	else:

                pGame = App.Game_GetCurrentGame() 
                pEpisode = pGame.GetCurrentEpisode() 
                pMission = pEpisode.GetCurrentMission()
                pNeutrals = pMission.GetNeutralGroup()
                if not pNeutrals.GetNameTuple():
                        pNeutrals.AddName("This ship probably wont exist 1")
                pEnemies = MissionLib.GetEnemyGroup()
                pEnemies.AddName("Tractor")


                import AttackAI
                pTractorp.SetAI(AttackAI.CreateAI(pTractorp))

		pVeloceS.SetAI(SelfDefenseAI.CreateAI(pVeloceS)) 

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


	pSet = App.g_kSetManager.GetSet("Veloce1")
	pVeloceS = App.ShipClass_GetObject(pSet, "Veloce")
	pTractorp = App.ShipClass_GetObject(pSet, "Tractor")
	if pVeloceS != None:
		pVeloceS.SetAI(SelfDefenseAI.CreateAI(pVeloceS))

	if pTractorp != None:
		pEnemyGroup.AddName("Tractor")
		pTractorp.SetAI(StarbaseMPAI.CreateAI(pTractorp))
