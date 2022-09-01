# C:\Users\Admin\DQP Hps\BORG SHIPS\Borg Transwarp Hub\Data\Models\Bases\DQP\JLSBorgHub\JLSTranswarpHub.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(240000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(0)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, 0.000000)
ShieldGenerator.SetPosition2D(66.000000, 38.000000)
ShieldGenerator.SetRepairComplexity(3.000000)
ShieldGenerator.SetDisabledPercentage(0.250000)
ShieldGenerator.SetRadius(0.010000)
ShieldGenerator.SetNormalPowerPerSecond(50.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 1000000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 1000000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 1000000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 1000000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 1000000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 1000000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 900.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 900.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 900.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 900.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 900.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 900.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(2000000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(0)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, -0.020000, 0.000000)
Hull.SetPosition2D(66.000000, 38.000000)
Hull.SetRepairComplexity(3.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.160000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(200000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.093000, -0.005000)
SensorArray.SetPosition2D(66.000000, 7.000000)
SensorArray.SetRepairComplexity(3.000000)
SensorArray.SetDisabledPercentage(0.250000)
SensorArray.SetRadius(0.008000)
SensorArray.SetNormalPowerPerSecond(50.000000)
SensorArray.SetBaseSensorRange(5000000.000000)
SensorArray.SetMaxProbes(0)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(200100.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(0)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, -0.040000, 0.000000)
WarpCore.SetPosition2D(65.000000, 55.000000)
WarpCore.SetRepairComplexity(3.000000)
WarpCore.SetDisabledPercentage(0.250000)
WarpCore.SetRadius(0.005000)
WarpCore.SetMainBatteryLimit(800000.000000)
WarpCore.SetBackupBatteryLimit(100000.000000)
WarpCore.SetMainConduitCapacity(4700.000000)
WarpCore.SetBackupConduitCapacity(700.000000)
WarpCore.SetPowerOutput(400.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")

Engineering.SetMaxCondition(200000.000000)
Engineering.SetCritical(0)
Engineering.SetTargetable(0)
Engineering.SetPrimary(1)
Engineering.SetPosition(0.000000, 0.000000, 0.000000)
Engineering.SetPosition2D(64.000000, 80.000000)
Engineering.SetRepairComplexity(2.000000)
Engineering.SetDisabledPercentage(0.100000)
Engineering.SetRadius(0.000100)
Engineering.SetNormalPowerPerSecond(1.000000)
Engineering.SetMaxRepairPoints(20.000000)
Engineering.SetNumRepairTeams(5)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
JLSTranswarpHub = App.ShipProperty_Create("JLSTranswarpHub")

JLSTranswarpHub.SetGenus(2)
JLSTranswarpHub.SetSpecies(149)
JLSTranswarpHub.SetMass(500.000000)
JLSTranswarpHub.SetRotationalInertia(49999998976.000000)
JLSTranswarpHub.SetShipName("Transwarp Hub")
JLSTranswarpHub.SetModelFilename("data/Models/Bases/DQP/JLSTranswarpHub/TranswarpHub.nif")
JLSTranswarpHub.SetDamageResolution(15.000000)
JLSTranswarpHub.SetAffiliation(0)
JLSTranswarpHub.SetStationary(1)
JLSTranswarpHub.SetAIString("StarbaseAttack")
JLSTranswarpHub.SetDeathExplosionSound("g_lsBigDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(JLSTranswarpHub)
#################################################
ViewscreenForward = App.PositionOrientationProperty_Create("ViewscreenForward")

ViewscreenForwardForward = App.TGPoint3()
ViewscreenForwardForward.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenForwardUp = App.TGPoint3()
ViewscreenForwardUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenForwardRight = App.TGPoint3()
ViewscreenForwardRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenForward.SetOrientation(ViewscreenForwardForward, ViewscreenForwardUp, ViewscreenForwardRight)
ViewscreenForwardPosition = App.TGPoint3()
ViewscreenForwardPosition.SetXYZ(0.000000, -1000.000000, 0.000000)
ViewscreenForward.SetPosition(ViewscreenForwardPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenForward)
#################################################
ViewscreenBack = App.PositionOrientationProperty_Create("ViewscreenBack")

ViewscreenBackForward = App.TGPoint3()
ViewscreenBackForward.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenBackUp = App.TGPoint3()
ViewscreenBackUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenBackRight = App.TGPoint3()
ViewscreenBackRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenBack.SetOrientation(ViewscreenBackForward, ViewscreenBackUp, ViewscreenBackRight)
ViewscreenBackPosition = App.TGPoint3()
ViewscreenBackPosition.SetXYZ(0.000000, 1000.000000, 0.000000)
ViewscreenBack.SetPosition(ViewscreenBackPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenBack)
#################################################
ViewscreenLeft = App.PositionOrientationProperty_Create("ViewscreenLeft")

ViewscreenLeftForward = App.TGPoint3()
ViewscreenLeftForward.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenLeftUp = App.TGPoint3()
ViewscreenLeftUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenLeftRight = App.TGPoint3()
ViewscreenLeftRight.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenLeft.SetOrientation(ViewscreenLeftForward, ViewscreenLeftUp, ViewscreenLeftRight)
ViewscreenLeftPosition = App.TGPoint3()
ViewscreenLeftPosition.SetXYZ(0.000000, 0.000000, 0.000000)
ViewscreenLeft.SetPosition(ViewscreenLeftPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenLeft)
#################################################
ViewscreenRight = App.PositionOrientationProperty_Create("ViewscreenRight")

ViewscreenRightForward = App.TGPoint3()
ViewscreenRightForward.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenRightUp = App.TGPoint3()
ViewscreenRightUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenRightRight = App.TGPoint3()
ViewscreenRightRight.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenRight.SetOrientation(ViewscreenRightForward, ViewscreenRightUp, ViewscreenRightRight)
ViewscreenRightPosition = App.TGPoint3()
ViewscreenRightPosition.SetXYZ(0.000000, 0.000000, 0.000000)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
#################################################
ViewscreenUp = App.PositionOrientationProperty_Create("ViewscreenUp")

ViewscreenUpForward = App.TGPoint3()
ViewscreenUpForward.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenUpUp = App.TGPoint3()
ViewscreenUpUp.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenUpRight = App.TGPoint3()
ViewscreenUpRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenUp.SetOrientation(ViewscreenUpForward, ViewscreenUpUp, ViewscreenUpRight)
ViewscreenUpPosition = App.TGPoint3()
ViewscreenUpPosition.SetXYZ(0.000000, 0.000000, 0.000000)
ViewscreenUp.SetPosition(ViewscreenUpPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenUp)
#################################################
ViewscreenDown = App.PositionOrientationProperty_Create("ViewscreenDown")

ViewscreenDownForward = App.TGPoint3()
ViewscreenDownForward.SetXYZ(0.000000, 0.000000, -1.000000)
ViewscreenDownUp = App.TGPoint3()
ViewscreenDownUp.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenDownRight = App.TGPoint3()
ViewscreenDownRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenDown.SetOrientation(ViewscreenDownForward, ViewscreenDownUp, ViewscreenDownRight)
ViewscreenDownPosition = App.TGPoint3()
ViewscreenDownPosition.SetXYZ(0.000000, 0.000000, 0.000000)
ViewscreenDown.SetPosition(ViewscreenDownPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenDown)
#################################################
FirstPersonCamera = App.PositionOrientationProperty_Create("FirstPersonCamera")

FirstPersonCameraForward = App.TGPoint3()
FirstPersonCameraForward.SetXYZ(0.000000, 1.000000, 0.000000)
FirstPersonCameraUp = App.TGPoint3()
FirstPersonCameraUp.SetXYZ(0.000000, 0.000000, 1.000000)
FirstPersonCameraRight = App.TGPoint3()
FirstPersonCameraRight.SetXYZ(1.000000, 0.000000, 0.000000)
FirstPersonCamera.SetOrientation(FirstPersonCameraForward, FirstPersonCameraUp, FirstPersonCameraRight)
FirstPersonCameraPosition = App.TGPoint3()
FirstPersonCameraPosition.SetXYZ(0.000000, 0.920000, 0.000000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
Conduit1 = App.HullProperty_Create("Conduit 1")

Conduit1.SetMaxCondition(29006.000000)
Conduit1.SetCritical(0)
Conduit1.SetTargetable(1)
Conduit1.SetPrimary(0)
Conduit1.SetPosition(-220.949997, 0.000000, 1310.000000)
Conduit1.SetPosition2D(64.000000, 50.000000)
Conduit1.SetRepairComplexity(1.000000)
Conduit1.SetDisabledPercentage(0.250000)
Conduit1.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit1)
#################################################
Conduit2 = App.HullProperty_Create("Conduit 2")

Conduit2.SetMaxCondition(290006.000000)
Conduit2.SetCritical(0)
Conduit2.SetTargetable(1)
Conduit2.SetPrimary(0)
Conduit2.SetPosition(-150.000000, 0.000000, 650.000000)
Conduit2.SetPosition2D(64.000000, 50.000000)
Conduit2.SetRepairComplexity(1.000000)
Conduit2.SetDisabledPercentage(0.250000)
Conduit2.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit2)
#################################################
Conduit3 = App.HullProperty_Create("Conduit 3")

Conduit3.SetMaxCondition(29006.000000)
Conduit3.SetCritical(0)
Conduit3.SetTargetable(1)
Conduit3.SetPrimary(0)
Conduit3.SetPosition(-750.000000, 0.000000, 1000.000000)
Conduit3.SetPosition2D(64.000000, 50.000000)
Conduit3.SetRepairComplexity(1.000000)
Conduit3.SetDisabledPercentage(0.250000)
Conduit3.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit3)
#################################################
Conduit4 = App.HullProperty_Create("Conduit 4")

Conduit4.SetMaxCondition(200000.000000)
Conduit4.SetCritical(0)
Conduit4.SetTargetable(1)
Conduit4.SetPrimary(0)
Conduit4.SetPosition(500.000000, 0.000000, 1050.000000)
Conduit4.SetPosition2D(64.000000, 50.000000)
Conduit4.SetRepairComplexity(1.000000)
Conduit4.SetDisabledPercentage(0.250000)
Conduit4.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit4)
#################################################
Conduit5 = App.HullProperty_Create("Conduit 5")

Conduit5.SetMaxCondition(296000.000000)
Conduit5.SetCritical(0)
Conduit5.SetTargetable(1)
Conduit5.SetPrimary(0)
Conduit5.SetPosition(570.000000, 0.000000, 622.000000)
Conduit5.SetPosition2D(64.000000, 50.000000)
Conduit5.SetRepairComplexity(1.000000)
Conduit5.SetDisabledPercentage(0.250000)
Conduit5.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit5)
#################################################
Conduit6 = App.HullProperty_Create("Conduit 6")

Conduit6.SetMaxCondition(2000.000000)
Conduit6.SetCritical(0)
Conduit6.SetTargetable(1)
Conduit6.SetPrimary(0)
Conduit6.SetPosition(1630.000000, 0.000000, 700.000000)
Conduit6.SetPosition2D(64.000000, 50.000000)
Conduit6.SetRepairComplexity(1.000000)
Conduit6.SetDisabledPercentage(0.250000)
Conduit6.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit6)
#################################################
Conduit7 = App.HullProperty_Create("Conduit 7")

Conduit7.SetMaxCondition(296000.000000)
Conduit7.SetCritical(0)
Conduit7.SetTargetable(1)
Conduit7.SetPrimary(0)
Conduit7.SetPosition(-470.000000, 0.000000, 250.000000)
Conduit7.SetPosition2D(64.000000, 50.000000)
Conduit7.SetRepairComplexity(1.000000)
Conduit7.SetDisabledPercentage(0.250000)
Conduit7.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit7)
#################################################
Conduit8 = App.HullProperty_Create("Conduit 8")

Conduit8.SetMaxCondition(296000.000000)
Conduit8.SetCritical(0)
Conduit8.SetTargetable(1)
Conduit8.SetPrimary(0)
Conduit8.SetPosition(-1150.000000, 0.000000, 350.000000)
Conduit8.SetPosition2D(64.000000, 50.000000)
Conduit8.SetRepairComplexity(1.000000)
Conduit8.SetDisabledPercentage(0.250000)
Conduit8.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit8)
#################################################
Conduit9 = App.HullProperty_Create("Conduit 9")

Conduit9.SetMaxCondition(296000.000000)
Conduit9.SetCritical(0)
Conduit9.SetTargetable(1)
Conduit9.SetPrimary(0)
Conduit9.SetPosition(-500.000000, 0.000000, -60.000000)
Conduit9.SetPosition2D(64.000000, 50.000000)
Conduit9.SetRepairComplexity(1.000000)
Conduit9.SetDisabledPercentage(0.250000)
Conduit9.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit9)
#################################################
Conduit10 = App.HullProperty_Create("Conduit 10")

Conduit10.SetMaxCondition(296000.000000)
Conduit10.SetCritical(0)
Conduit10.SetTargetable(1)
Conduit10.SetPrimary(0)
Conduit10.SetPosition(-50.000000, 0.000000, -460.000000)
Conduit10.SetPosition2D(64.000000, 50.000000)
Conduit10.SetRepairComplexity(1.000000)
Conduit10.SetDisabledPercentage(0.250000)
Conduit10.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit10)
#################################################
Conduit11 = App.HullProperty_Create("Conduit 11")

Conduit11.SetMaxCondition(2000.000000)
Conduit11.SetCritical(0)
Conduit11.SetTargetable(1)
Conduit11.SetPrimary(0)
Conduit11.SetPosition(640.000000, 0.000000, -360.000000)
Conduit11.SetPosition2D(64.000000, 50.000000)
Conduit11.SetRepairComplexity(1.000000)
Conduit11.SetDisabledPercentage(0.250000)
Conduit11.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit11)
#################################################
Conduit12 = App.HullProperty_Create("Conduit 12")

Conduit12.SetMaxCondition(209600.000000)
Conduit12.SetCritical(0)
Conduit12.SetTargetable(1)
Conduit12.SetPrimary(0)
Conduit12.SetPosition(1200.000000, 0.000000, 50.000000)
Conduit12.SetPosition2D(64.000000, 50.000000)
Conduit12.SetRepairComplexity(1.000000)
Conduit12.SetDisabledPercentage(0.250000)
Conduit12.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit12)
#################################################
Conduit13 = App.HullProperty_Create("Conduit 13")

Conduit13.SetMaxCondition(296000.000000)
Conduit13.SetCritical(0)
Conduit13.SetTargetable(1)
Conduit13.SetPrimary(0)
Conduit13.SetPosition(1250.000000, 0.000000, -410.000000)
Conduit13.SetPosition2D(64.000000, 50.000000)
Conduit13.SetRepairComplexity(1.000000)
Conduit13.SetDisabledPercentage(0.250000)
Conduit13.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit13)
#################################################
Conduit14 = App.HullProperty_Create("Conduit 14")

Conduit14.SetMaxCondition(296000.000000)
Conduit14.SetCritical(0)
Conduit14.SetTargetable(1)
Conduit14.SetPrimary(0)
Conduit14.SetPosition(930.000000, 0.000000, -960.000000)
Conduit14.SetPosition2D(64.000000, 50.000000)
Conduit14.SetRepairComplexity(1.000000)
Conduit14.SetDisabledPercentage(0.250000)
Conduit14.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit14)
#################################################
Conduit15 = App.HullProperty_Create("Conduit 15")

Conduit15.SetMaxCondition(2000.000000)
Conduit15.SetCritical(0)
Conduit15.SetTargetable(1)
Conduit15.SetPrimary(0)
Conduit15.SetPosition(-190.000000, 0.000000, -990.000000)
Conduit15.SetPosition2D(64.000000, 50.000000)
Conduit15.SetRepairComplexity(1.000000)
Conduit15.SetDisabledPercentage(0.250000)
Conduit15.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit15)
#################################################
Conduit16 = App.HullProperty_Create("Conduit 16")

Conduit16.SetMaxCondition(296000.000000)
Conduit16.SetCritical(0)
Conduit16.SetTargetable(1)
Conduit16.SetPrimary(0)
Conduit16.SetPosition(-500.000000, 0.000000, -900.000000)
Conduit16.SetPosition2D(64.000000, 50.000000)
Conduit16.SetRepairComplexity(1.000000)
Conduit16.SetDisabledPercentage(0.250000)
Conduit16.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit16)
#################################################
Conduit17 = App.HullProperty_Create("Conduit 17")

Conduit17.SetMaxCondition(296000.000000)
Conduit17.SetCritical(0)
Conduit17.SetTargetable(1)
Conduit17.SetPrimary(0)
Conduit17.SetPosition(-1060.000000, 0.000000, -780.000000)
Conduit17.SetPosition2D(64.000000, 50.000000)
Conduit17.SetRepairComplexity(1.000000)
Conduit17.SetDisabledPercentage(0.250000)
Conduit17.SetRadius(100.050003)
App.g_kModelPropertyManager.RegisterLocalTemplate(Conduit17)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 4", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 5", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 6", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 7", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 8", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 9", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 10", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 11", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 12", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 13", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 14", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 15", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 16", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Conduit 17", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engineering", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenForward", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenBack", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenLeft", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenRight", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenUp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenDown", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FirstPersonCamera", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("JLSTranswarpHub", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
