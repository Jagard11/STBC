###############################################################################
#	Filename:	FluidicSpace1_S.py
#	
#	Confidential and Proprietary, Copyright 2001 by Totally Games/Ben Howard
#	
#	Creates Fluid 1 static objects.  Called by Fluid1.py when region is created
#	
#	Created:	09/17/00 
###############################################################################
import App
import loadspacehelper
import Tactical.LensFlares
import MissionLib
import SelfDefenseAI

def Initialize(pSet):

	# MetaNebula_Create params are:
	# r, g, b : (floats [0.0 , 1.0]) 
	# visibility distance inside the nebula (float in world units)
	# sensor density of nebula(value to scale sensor range by)
    	# name of internal texture (needs alpha)
	# name of external texture (no need for alpha)
	
	pNebula = App.MetaNebula_Create(140.0 / 255.0, 240.0 / 255.0, 65.0  / 255.0, 40.0, 6.0, "data/Backgrounds/High/JLSFluidicS.tga", "data/Backgrounds/High/JLSFluidicS.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula.SetupDamage(1.0, 1.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula.AddNebulaSphere(1000.0, 6000.0, 3000.0, 7800.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula, "Nebula1")
	
	pNebula2 = App.MetaNebula_Create(40.0 / 255.0, 240.0 / 255.0, 165.0  / 255.0, 40.0, 6.0, "data/Backgrounds/High/JLSFluidicS.tga", "data/Backgrounds/High/JLSFluidicS.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula2.SetupDamage(1.0, 1.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula2.AddNebulaSphere(3500.0, -7800.0, -2000.0, 7800.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula2, "Nebula2")
	
	pNebula3 = App.MetaNebula_Create(40.0 / 255.0, 140.0 / 255.0, 45.0  / 255.0, 40.0, 6.0, "data/Backgrounds/High/JLSFluidicS.tga", "data/Backgrounds/High/JLSFluidicS.tga")
	# Set nebula damage/sec to Hull/Shields.
	pNebula3.SetupDamage(1.0, 1.0)
	# Adds a fuzzy sphere at x, y, z (in world coord) of specified size (1000.0 in this case)
	pNebula3.AddNebulaSphere(-6500.0, -4800.0, 0.0, 7800.0)
	# Puts the nebula in the set
	pSet.AddObjectToSet(pNebula3, "Nebula3")


	if (App.g_kUtopiaModule.IsHost ()) or not (App.g_kUtopiaModule.IsMultiplayer()):

		#Create More Ships
                #Bioship
                pBioship2       = loadspacehelper.CreateShip("JLS8472", pSet, "8472 Bioship 1", "8472 Bioship 2 Location")

                #Bioship
                pBioship3      = loadspacehelper.CreateShip("JLS8472", pSet, "8472 Bioship 2", "8472 Bioship 3 Location")

                #Bioship
                pBioship4       = loadspacehelper.CreateShip("JLS8472", pSet, "8472 Bioship 3", "8472 Bioship 4 Location")

                #Bioship
                pBioship5       = loadspacehelper.CreateShip("JLS8472", pSet, "8472 Bioship 4", "8472 Bioship 5 Location")

                #Bioship
                pBioship6       = loadspacehelper.CreateShip("JLS8472", pSet, "8472 Bioship 5", "8472 Bioship 6 Location")

                #Bioship
                pBioship7      = loadspacehelper.CreateShip("JLS8472", pSet, "8472 Bioship 6", "8472 Bioship 7 Location")

                #Bioship
                pBioship8       = loadspacehelper.CreateShip("JLS8472", pSet, "8472 Bioship 7", "8472 Bioship 8 Location")

                #Bioship
                pBioship9       = loadspacehelper.CreateShip("JLS8472", pSet, "8472 Bioship 8", "8472 Bioship 9 Location")

                #Bioship
                pBioship10       = loadspacehelper.CreateShip("JLS8472", pSet, "8472 Bioship 9", "8472 Bioship 10 Location")

                #Bioship
                pBioship11       = loadspacehelper.CreateShip("JLS8472", pSet, "8472 Bioship 10", "8472 Bioship 11 Location")

	if (App.g_kUtopiaModule.IsMultiplayer()):
		pMission = MissionLib.GetMission ()
		SetupEventHandlers(pMission)

	else:
                pBioship2.SetAI(SelfDefenseAI.CreateAI(pBioship2))    
                pBioship3.SetAI(SelfDefenseAI.CreateAI(pBioship3))
                pBioship4.SetAI(SelfDefenseAI.CreateAI(pBioship4))    
                pBioship5.SetAI(SelfDefenseAI.CreateAI(pBioship5))
                pBioship6.SetAI(SelfDefenseAI.CreateAI(pBioship6))
                pBioship7.SetAI(SelfDefenseAI.CreateAI(pBioship7))
                pBioship8.SetAI(SelfDefenseAI.CreateAI(pBioship8))    
                pBioship9.SetAI(SelfDefenseAI.CreateAI(pBioship9))
                pBioship10.SetAI(SelfDefenseAI.CreateAI(pBioship10))
                pBioship11.SetAI(SelfDefenseAI.CreateAI(pBioship11))


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


	pSet = App.g_kSetManager.GetSet("FluidicSpace1")
        pBioship2 = App.ShipClass_GetObject(pSet, "8472 Bioship 1")
        pBioship3 = App.ShipClass_GetObject(pSet, "8472 Bioship 2")
        pBioship4 = App.ShipClass_GetObject(pSet, "8472 Bioship 3")
        pBioship5 = App.ShipClass_GetObject(pSet, "8472 Bioship 4")
        pBioship6 = App.ShipClass_GetObject(pSet, "8472 Bioship 5")
        pBioship7 = App.ShipClass_GetObject(pSet, "8472 Bioship 6")
        pBioship8 = App.ShipClass_GetObject(pSet, "8472 Bioship 7")
        pBioship9 = App.ShipClass_GetObject(pSet, "8472 Bioship 8")
        pBioship10 = App.ShipClass_GetObject(pSet, "8472 Bioship 9")
        pBioship11 = App.ShipClass_GetObject(pSet, "8472 Bioship 10")
        if pBioship2 != None:   
                  pBioship2.SetAI(SelfDefenseAI.CreateAI(pBioship2))   
        if pBioship3 != None:   
                  pBioship1.SetAI(SelfDefenseAI.CreateAI(pBioship3))
        if pBioship4 != None:   
                  pBioship2.SetAI(SelfDefenseAI.CreateAI(pBioship4))    
        if pBioship5 != None:   
                  pBioship1.SetAI(SelfDefenseAI.CreateAI(pBioship5))
        if pBioship6 != None:   
                  pBioship1.SetAI(SelfDefenseAI.CreateAI(pBioship6))
        if pBioship7 != None:   
                  pBioship1.SetAI(SelfDefenseAI.CreateAI(pBioship7))
        if pBioship8 != None:   
                  pBioship2.SetAI(SelfDefenseAI.CreateAI(pBioship8))    
        if pBioship9 != None:   
                  pBioship1.SetAI(SelfDefenseAI.CreateAI(pBioship9))
        if pBioship10 != None:   
                  pBioship1.SetAI(SelfDefenseAI.CreateAI(pBioship10))
        if pBioship11 != None:   
                  pBioship1.SetAI(SelfDefenseAI.CreateAI(pBioship11))