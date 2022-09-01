import App

def Initialize():
	# Create the set ("Cardassia8")
	pSet = App.SetClass_Create()

	# Save the name of the region file that's creating the set.
	pSet.SetRegionModule("Systems.Cardassia.Cardassia8")

	App.g_kSetManager.AddSet(pSet, "Cardassia8")

	# Activate the proximity manager for our set.
	pSet.SetProximityManagerActive(1)


	# Load the placements and backdrops for this set.
	LoadPlacements("Cardassia8")
	LoadBackdrops(pSet)

	#Load and place the grid.
	pGrid = App.GridClass_Create()
	pSet.AddObjectToSet(pGrid, "grid")
	pGrid.SetHidden(1)

	# Create static objects for this set:
	# If you want to create static objects for this region, make a
	# "Cardassia8_S.py" file with an Initialize function that creates them.
	try:
		import Cardassia8_S
		Cardassia8_S.Initialize(pSet)
	except ImportError:
		# Couldn't find the file.  That's ok.  Do nothing...
		pass
	# Done.

def GetSetName():
	return "Cardassia8"

def GetSet():
	return App.g_kSetManager.GetSet("Cardassia8")

def Terminate():
	App.g_kSetManager.DeleteSet("Cardassia8")

def LoadPlacements(sSetName):
	# Light position "Ambient Light"
	kThis = App.LightPlacement_Create("Ambient Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigAmbientLight(1.0, 0.7, 0.7, 0.13)
	kThis.Update(0)
	kThis = None
	# End position "Ambient Light"

	# Light position "Directional Light"
	kThis = App.LightPlacement_Create("Directional Light", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(1.0, 0.0, 0.01)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.ConfigDirectionalLight(1, 0.75, 0.6, 0.45)
	kThis.Update(0)
	kThis = None
	# End position "Directional Light"

	# Position "Cardassia-8"
	kThis = App.Waypoint_Create("Cardassia-8", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-100.00, 20000.00, 0.00)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.999996, 0.002645, 0.000035)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.05, -0.05, 0.9)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.000000)
	kThis.Update(0)
	kThis = None
	# End position "Cardassia-8"

	# Position "Player Start"
	kThis = App.Waypoint_Create("Player Start", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(0)
	kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Player Start"

	# Position "Sun"
	kThis = App.Waypoint_Create("Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetTranslateXYZ(-128571428.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "Sun"
	
	# Position "The Sun"
	kThis = App.Waypoint_Create("The Sun", sSetName, None)
	kThis.SetStatic(1)
	kThis.SetNavPoint(1)
	kThis.SetTranslateXYZ(-128331000.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.0, 1.0, 0.0)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.0, 0.0, 1.0)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetSpeed(25.0)
	kThis.Update(0)
	kThis = None
	# End position "The Sun"	

import App

def LoadBackdrops(pSet):

	#Draw order is implicit. First object gets drawn first

	# Star Sphere "Backdrop stars"
	kThis = App.StarSphere_Create()
	kThis.SetName("Backdrop stars")
	kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.185766, 0.947862, -0.258937)
	kUp = App.TGPoint3()
	kUp.SetXYZ(0.049814, 0.254101, 0.965894)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/stars.tga")
	kThis.SetTargetPolyCount(256)
	kThis.SetHorizontalSpan(1.0)
	kThis.SetVerticalSpan(1.0)
	kThis.SetSphereRadius(300.0)
	kThis.SetTextureHTile(22.0)
	kThis.SetTextureVTile(11.0)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Backdrop stars")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Backdrop stars"

	# Backdrop Sphere "Nebula"
	kThis = App.BackdropSphere_Create()
	kThis.SetName("Nebula")
	kThis.SetTranslateXYZ(0.0, 0.0, 0.0)
	kForward = App.TGPoint3()
	kForward.SetXYZ(0.860219, -0.122382, 0.495021)
	kUp = App.TGPoint3()
	kUp.SetXYZ(-0.490086, 0.069723, 0.868881)
	kThis.AlignToVectors(kForward, kUp)
	kThis.SetTextureFileName("data/Backgrounds/treknebula.tga")
	kThis.SetTargetPolyCount(512)
	kThis.SetHorizontalSpan(0.07)
	kThis.SetVerticalSpan(0.12)
	kThis.SetSphereRadius(300.0)
	kThis.SetTextureHTile(1.0)
	kThis.SetTextureVTile(1.0)
	kThis.Rebuild()
	pSet.AddBackdropToSet(kThis,"Nebula")
	kThis.Update(0)
	kThis = None
	# End Backdrop Sphere "Nebula"