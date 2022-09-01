import App

def Initialize():
	# Create the set ("Unicomplex1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "Unicomplex1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.Unicomplex.Unicomplex1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("Unicomplex1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "Unicomplex1_S.py" file with an Initialize function that creates them.
	try:
		import Unicomplex1_S
		Unicomplex1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "Unicomplex1"

def GetSet():
	return App.g_kSetManager.GetSet("Unicomplex1")

def Terminate():
	App.g_kSetManager.DeleteSet("Unicomplex1")

def LoadPlacements(sSetName):
	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(1.000000, 1.000000, 1.000000, 0.100000)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(1.622276, -1.830812, -0.326898)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.099571, -0.962789, 0.251243)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.019077, 0.250604, 0.967902)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1.000000, 0.800000, 0.600000, 0.450000)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Position "TravelerWarpPlacement1"
	kThis = App.PlacementObject_Create("TravelerWarpPlacement1", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-4943.350586, -216.335266, 742.520020)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.000000, 0.000000, -0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.000000, 1.000000, 0.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.Update(0)
	kThis = None
	# End position "TravelerWarpPlacement1"

	# Light position "Light 2"
	kThis = App.LightPlacement_Create("Light 2", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-1192.286865, -3610.998047, 1584.271729)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.339386, 0.811272, -0.476083)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.158128, 0.449715, 0.879063)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(0.700000, 0.600000, 0.800000, 1.000000)
	kThis.Update(0)
	kThis = None
	# End position "Light 2"

	# Light position "Light 3"
	kThis = App.LightPlacement_Create("Light 3", sSetName, None)
	kThis.SetStatic(0)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-5512.178711, 72.293457, 135.650986)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.826873, -0.474868, -0.301300)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.012030, 0.520693, -0.853659)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(1.000000, 0.500000, 0.600000, 1.000000)
	kThis.Update(0)
	kThis = None
	# End position "Light 3"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(43.899635, -180.916016, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"

	# Position "Unicomplex Location"
	kThis = App.Waypoint_Create("Unicomplex Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(150.827942, 50.803833, 40.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Unicomplex Location"

	# Light position "Directional Light 2"
	kThis = App.LightPlacement_Create("Directional Light 2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-19.846134, -5.809788, -33.403244)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.155816, 0.140545, -0.977736)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.524738, -0.826833, -0.202478)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(0.800000, 0.800000, 0.500000, 0.300000)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light 2"

	# Light position "Light 1"
	kThis = App.LightPlacement_Create("Light 1", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(-1131.857666, -3533.488770, 1548.625000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.323417, 0.880718, -0.346029)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.119280, 0.324821, 0.938224)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(0.700000, 0.600000, 0.400000, 1.000000)
	kThis.Update(0)
	kThis = None
	# End position "Light 1"

	# Position "Borg2"
	kThis = App.Waypoint_Create("Borg2 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(50.827942, 2050.803833, -120.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, -1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "Borg2"

	# Position "Borg3"
	kThis = App.Waypoint_Create("Borg3 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(10.827942, -1550.803833, -260.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 0.000000, 1.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "Borg3"

	# Position "Borg4"
	kThis = App.Waypoint_Create("Borg4 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(50.827942, -500.803833, -590.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.000000, 0.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "Borg4"

	# Position "Borg5"
	kThis = App.Waypoint_Create("Borg5 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(4000.827942, -650.803833, 860.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "Borg5"

	# Position "Borg6"
	kThis = App.Waypoint_Create("Borg6 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(100.827942, -2500.803833, -60.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, -1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "Borg6"

	# Position "Borg7"
	kThis = App.Waypoint_Create("Borg7 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(1000.827942, -20.803833, 360.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, -1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "Borg7"

	# Position "Borg8"
	kThis = App.Waypoint_Create("Borg8 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(400.827942, -5500.803833, -260.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, -1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "Borg8"

	# Position "Borg9"
	kThis = App.Waypoint_Create("Borg9 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(800.827942, -3200.803833, 60.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, -1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "Borg9"

	# Position "Borg10"
	kThis = App.Waypoint_Create("Borg10 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(1200.827942, -1500.803833, 460.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, -1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "Borg10"



import App

def LoadBackdrops(pSet):

	#Draw order is implicit. First object gets drawn first

	# Star Sphere "Backdrop stars"
	kThis = App.StarSphere_Create()
	kThis.SetName("Backdrop stars")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.185766, 0.947862, -0.258938)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.049825, 0.254099, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/deltastars.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(22.000000)
	kThis.SetTextureVTile(11.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"

        # Backdrop Sphere
        kThis = App.BackdropSphere_Create()
        kThis.SetName("Backdrop Vandros01")
        kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
        kForward = App.TGPoint3()
        kForward.SetXYZ(1000.827942, -20.803833, 360.0)
        kUp = App.TGPoint3()
        kUp.SetXYZ(0.0, 0.0, 1.0)
        kThis.AlignToVectors(kForward, kUp)
        kThis.SetTextureFileName("data/backgrounds/JLSBorgU.tga")
        kThis.SetTargetPolyCount(256)
        kThis.SetHorizontalSpan(0.572500)
        kThis.SetVerticalSpan(0.895000)
        kThis.SetSphereRadius(300.000000)
        kThis.SetTextureHTile(1.000000)
        kThis.SetTextureVTile(1.000000)
        kThis.Rebuild()
        pSet.AddBackdropToSet(kThis,"Backdrop Vandros01")
        kThis.Update(0)
        kThis = None
        # End Backdrop Sphere

