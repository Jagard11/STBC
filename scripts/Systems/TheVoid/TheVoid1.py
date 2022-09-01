import App
##import Systems.FoundationUtils

def Initialize():
	# Create the set ("TheVoid1")
	pSet = App.SetClass_Create()
	App.g_kSetManager.AddSet(pSet, "TheVoid1")

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.TheVoid.TheVoid1")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)


	# Load the placements and backdrops for this set.
	LoadPlacements("TheVoid1")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "TheVoid1_S.py" file with an Initialize function that creates them.
	try:
		import TheVoid1_S
		TheVoid1_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass

	# Done.

def GetSetName():
	return "TheVoid1"

def GetSet():
	return App.g_kSetManager.GetSet("TheVoid1")

def Terminate():
	App.g_kSetManager.DeleteSet("TheVoid1")

def LoadPlacements(sSetName):
##	placer = Systems.FoundationUtils.SystemPlacer(728.91, 3, 2)

	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(0.01, 0.01, 0.40, 0.05)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-0.044018, 0.572347, 0.029146)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.076971, 0.995795, 0.049676)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.006766, -0.050345, 0.998709)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(.1, .1, .4, .05)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.000000, 0.000000, 0.000000)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"

	# Position "Night Ship2"
	kThis = App.Waypoint_Create("Night Ship2 Location", sSetName, None)
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
	# End position "Night Ship2"

	# Position "Night Ship3"
	kThis = App.Waypoint_Create("Night Ship3 Location", sSetName, None)
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
	# End position "Night Ship3"

	# Position "Night Ship4"
	kThis = App.Waypoint_Create("Night Ship4 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(350.827942, -50.803833, -590.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(-1.000000, 0.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "Night Ship4"

	# Position "Night Ship5"
	kThis = App.Waypoint_Create("Night Ship5 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(400.827942, -650.803833, 860.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, 1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "Night Ship5"

	# Position "Night Ship6"
	kThis = App.Waypoint_Create("Night Ship6 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(200.827942, -250.803833, -60.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, -1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "Night Ship6"

	# Position "Night Ship7"
	kThis = App.Waypoint_Create("Night Ship7 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(10.827942, -20.803833, 360.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, -1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "Night Ship7"

	# Position "Night Ship8"
	kThis = App.Waypoint_Create("Night Ship8 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(400.827942, -550.803833, -260.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, -1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "Night Ship8"

	# Position "Night Ship9"
	kThis = App.Waypoint_Create("Night Ship9 Location", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(80.827942, -320.803833, 60.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.000000, -1.000000, 0.000000)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.000000, 0.000000, 1.000000)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(0.500000)
	kThis.Update(0)
	kThis = None
	# End position "Night Ship9"

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
	kThis.SetTextureFileName("data/JLSVoid.tga")
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