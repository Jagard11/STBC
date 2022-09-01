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
		pVaadwaurHomeworld2	= loadspacehelper.CreateShip("VaadwaurHomeworld", pSet, "Vaadwaur Homeworld2", "Vaadwaur Homeworld Location")

		pVaadwaurHomeworld2.SetInvincible(1)
		pVaadwaurHomeworld2.SetHurtable(0)
		pVaadwaurHomeworld2.SetTargetable(1)
		pVaadwaurHomeworld2.SetCollisionsOn(1)
		pVaadwaurHomeworld2.SetScale(30.0)
		vCurVelocity = App.TGPoint3()
		vCurVelocity.SetXYZ(0, 0, -0.01)
		pVaadwaurHomeworld2.SetAngularVelocity(vCurVelocity, App.PhysicsObjectClass.DIRECTION_MODEL_SPACE)

		from Custom.Autoload import PlanetShipAddon
		PlanetShipAddon.SetPlanetShipGlowSize(pVaadwaurHomeworld2, 55)
		PlanetShipAddon.SetPlanetShipGlowColor(pVaadwaurHomeworld2, 0.992157, 0.756863, 0.215686, 0.32)
		PlanetShipAddon.SetPlanetShipAtmosphereScript(pVaadwaurHomeworld2, "AtmosphereO")
		PlanetShipAddon.SetPlanetShipAtmosphereScaleBonus(pVaadwaurHomeworld2, 0.001)
		PlanetShipAddon.SetPlanetShipAtmosphereAngularVelocity(pVaadwaurHomeworld2, 0, 0, -0.015)

		MissionLib.HideSubsystems(pVaadwaurHomeworld2)

		
		#Create More Ships

		#VaadwaurFighter
                pVaadwaurFighter2       = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 1", "VaadwaurFighter2 Location")

                #VaadwaurFighter
                pVaadwaurFighter3      = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 2", "VaadwaurFighter3 Location")

                #VaadwaurFighter
                pVaadwaurFighter4       = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 3", "VaadwaurFighter4 Location")

                #VaadwaurFighter
                pVaadwaurFighter5       = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 4", "VaadwaurFighter5 Location")

                #VaadwaurFighter
                pVaadwaurFighter6       = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 5", "VaadwaurFighter6 Location")

                #VaadwaurFighter
                pVaadwaurFighter7      = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 6", "VaadwaurFighter7 Location")

                #VaadwaurFighter
                pVaadwaurFighter8       = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 7", "VaadwaurFighter8 Location")

                #VaadwaurFighter
                pVaadwaurFighter9       = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 8", "VaadwaurFighter9 Location")

                #VaadwaurFighter
                pVaadwaurFighter10       = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 9", "VaadwaurFighter10 Location")

                #VaadwaurFighter
                pVaadwaurFighter11       = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 10", "VaadwaurFighter11 Location")

		#VaadwaurFighter
                pVaadwaurFighter12       = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 11", "VaadwaurFighter12 Location")

                #VaadwaurFighter
                pVaadwaurFighter13      = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 12", "VaadwaurFighter13 Location")

                #VaadwaurFighter
                pVaadwaurFighter14       = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 13", "VaadwaurFighter14 Location")

                #VaadwaurFighter
                pVaadwaurFighter15       = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 14", "VaadwaurFighter15 Location")

                #VaadwaurFighter
                pVaadwaurFighter16       = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 15", "VaadwaurFighter16 Location")

                #VaadwaurFighter
                pVaadwaurFighter17      = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 16", "VaadwaurFighter17 Location")

                #VaadwaurFighter
                pVaadwaurFighter18       = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 17", "VaadwaurFighter18 Location")

                #VaadwaurFighter
                pVaadwaurFighter19       = loadspacehelper.CreateShip("JLSVaadwaurFighter", pSet, "VaadwaurFighter 18", "VaadwaurFighter19 Location")





	if (App.g_kUtopiaModule.IsMultiplayer()):
		pMission = MissionLib.GetMission ()
		SetupEventHandlers(pMission)

	else:
		pVaadwaurHomeworld2.SetAI(SelfDefenseAI.CreateAI(pVaadwaurHomeworld2))
                pVaadwaurFighter2.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter2))    
                pVaadwaurFighter3.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter3))
                pVaadwaurFighter4.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter4))    
                pVaadwaurFighter5.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter5))
                pVaadwaurFighter6.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter6))
                pVaadwaurFighter7.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter7))
                pVaadwaurFighter8.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter8))    
                pVaadwaurFighter9.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter9))
                pVaadwaurFighter10.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter10))
                pVaadwaurFighter12.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter12))    
                pVaadwaurFighter13.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter13))
                pVaadwaurFighter14.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter14))    
                pVaadwaurFighter15.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter15))
                pVaadwaurFighter16.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter16))
                pVaadwaurFighter17.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter17))
                pVaadwaurFighter18.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter18))    
                pVaadwaurFighter19.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter19))
                pVaadwaurFighter11.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter11))


 


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


	pSet = App.g_kSetManager.GetSet("VaadwaurHomeworld1")
	pVaadwaurHomeworld2 = App.ShipClass_GetObject(pSet, "VaadwaurHomeworld")

        pVaadwaurFighter2 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 1")
        pVaadwaurFighter3 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 2")
        pVaadwaurFighter4 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 3")
        pVaadwaurFighter5 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 4")
        pVaadwaurFighter6 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 5")
        pVaadwaurFighter7 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 6")
        pVaadwaurFighter8 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 7")
        pVaadwaurFighter9 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 8")
        pVaadwaurFighter10 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 9")
        pVaadwaurFighter11 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 10")
        pVaadwaurFighter12 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 11")
        pVaadwaurFighter13 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 12")
        pVaadwaurFighter14 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 13")
        pVaadwaurFighter15 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 14")
        pVaadwaurFighter16 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 15")
        pVaadwaurFighter17 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 16")
        pVaadwaurFighter18 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 17")
        pVaadwaurFighter19 = App.ShipClass_GetObject(pSet, "VaadwaurFighter 18")


	if pVaadwaurHomeworld2 != None:
		pNeutralGroup.AddName("Vaadwaur1")
		pVaadwaurHomeworld2.SetAI(SelfDefenseAI.CreateAI(pVaadwaurHomeworld2))
                if pVaadwaurFighter2 != None:   
                        pVaadwaurFighter2.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter2))    
                if pVaadwaurFighter3 != None:
                        pVaadwaurFighter3.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter3))
                if pVaadwaurFighter4 != None:   
                        pVaadwaurFighter4.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter4))    
                if pVaadwaurFighter5 != None:   
                        pVaadwaurFighter5.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter5))
                if pVaadwaurFighter6 != None:  
                        pVaadwaurFighter6.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter6))
                if pVaadwaurFighter7 != None: 
                        pVaadwaurFighter7.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter7))
                if pVaadwaurFighter8 != None:   
                        pVaadwaurFighter8.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter8))    
                if pVaadwaurFighter9 != None:   
                        pVaadwaurFighter9.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter9))
                if pVaadwaurFighter10 != None:   
                        pVaadwaurFighter10.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter10))
                if pVaadwaurFighter11 != None:   
                        pVaadwaurFighter11.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter11))
                if pVaadwaurFighter12 != None:   
                        pVaadwaurFighter12.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter12))    
                if pVaadwaurFighter13 != None:
                        pVaadwaurFighter13.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter13))
                if pVaadwaurFighter14 != None:   
                        pVaadwaurFighter14.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter14))    
                if pVaadwaurFighter15 != None:   
                        pVaadwaurFighter15.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter15))
                if pVaadwaurFighter16 != None:  
                        pVaadwaurFighter16.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter16))
                if pVaadwaurFighter17 != None: 
                        pVaadwaurFighter17.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter17))
                if pVaadwaurFighter18 != None:   
                        pVaadwaurFighter18.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter18))    
                if pVaadwaurFighter19 != None:   
                        pVaadwaurFighter19.SetAI(SelfDefenseAI.CreateAI(pVaadwaurFighter19))

