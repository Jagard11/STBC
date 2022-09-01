import App

def Initialize():
	# Create the set ("FluidicSpace1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "FluidicSpace1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.FluidicSpace.FluidicSpace1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)

	# Load the placements and backdrops for this set.
	LoadPlacements("FluidicSpace1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "FluidicSpace1_S.py" file with an Initialize function that creates them.
	try:
		import FluidicSpace1_S
		FluidicSpace1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "FluidicSpace1"

def GetSet():
	return App.g_kSetManager.GetSet("FluidicSpace1")

def Terminate():
	App.g_kSetManager.DeleteSet("FluidicSpace1")

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
	kThis.ConfigAmbientLight(0.000000, 0.000000, 0.400000, 0.1)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(14.928001, 0.000001, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, -1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.141766, -0.114260, 0.983284)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.5, .9, .8, .8)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Light position "Directional Light2"
	kThis = App.LightPlacement_Create("Directional Light2", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(2.928001, 0.000001, 14.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-0.8, -0.2, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.141766, 0.114260, -0.983284)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.4, .6, .8, .3)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light2"

	# Position "Nebula Core"
	kThis = App.Waypoint_Create("Nebula Core", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(100.0, 2000.0, 800.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.1, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Nebula Core"


	# Position "8472 Bioship  Bioship 2"
	kThis = App.Waypoint_Create("8472 Bioship  Bioship 2 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(50.827942, 190.803833, -120.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, -1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "8472 Bioship  Bioship 2"

	# Position "8472 Bioship 3"
	kThis = App.Waypoint_Create("8472 Bioship 3 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(300.827942, 250.803833, -260.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 0.000000, 1.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "8472 Bioship 3"

	# Position "8472 Bioship 4"
	kThis = App.Waypoint_Create("8472 Bioship 4 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(800.827942, -50.803833, -590.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.000000, 0.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "8472 Bioship 4"

	# Position "8472 Bioship 5"
	kThis = App.Waypoint_Create("8472 Bioship 5 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(400.827942, -3050.803833, 860.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.000000, 0.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "8472 Bioship 5"

	# Position "8472 Bioship 6"
	kThis = App.Waypoint_Create("8472 Bioship 6 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(100.827942, -650.803833, -60.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, -1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "8472 Bioship 6"

	# Position "8472 Bioship 7"
	kThis = App.Waypoint_Create("8472 Bioship 7 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(100.827942, -220.803833, 360.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, -1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "8472 Bioship 7"

	# Position "8472 Bioship 8"
	kThis = App.Waypoint_Create("8472 Bioship 8 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(140.827942, -350.803833, -260.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "8472 Bioship 8"

	# Position "8472 Bioship 9"
	kThis = App.Waypoint_Create("8472 Bioship 9 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(100.827942, -320.803833, 60.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 0.000000, 1.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "8472 Bioship 9"

	# Position "8472 Bioship 10"
	kThis = App.Waypoint_Create("8472 Bioship 10 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(100.827942, 250.803833, 460.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, -1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "8472 Bioship 10"

	# Position "8472 Bioship 11"
	kThis = App.Waypoint_Create("8472 Bioship 11 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(160.827942, 350.803833, 60.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "8472 Bioship 11"

import App

def LoadBackdrops(pSet):

	#Draw order is implicit. First object gets drawn first

	# Star Sphere "Backdrop Fluid"
	kThis = App.StarSphere_Create()
	kThis.SetName("Backdrop Fluid")
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.185766, 0.947862, -0.258937)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.049823, 0.254099, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/Backgrounds/High/JLSFluidicS.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.000000)
	kThis.SetVerticalSpan(1.000000)
	kThis.SetSphereRadius(300.000000)
	kThis.SetTextureHTile(3.000000)
	kThis.SetTextureVTile(2.000000)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop Fluid")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop Fluid"
