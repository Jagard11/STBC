# C:\Users\Owner\Documents\FinalHP_Changes_Other\escapepod.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(700.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(67.000000, 47.000000)
Hull.SetRepairComplexity(3.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.030000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(300.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, 0.000000, 0.000000)
ImpulseEngines.SetPosition2D(51.000000, 48.000000)
ImpulseEngines.SetRepairComplexity(1.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.003000)
ImpulseEngines.SetNormalPowerPerSecond(10.000000)
ImpulseEngines.SetMaxAccel(0.500000)
ImpulseEngines.SetMaxAngularAccel(0.300000)
ImpulseEngines.SetMaxAngularVelocity(0.700000)
ImpulseEngines.SetMaxSpeed(2.000000)
ImpulseEngines.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
PowerPlant = App.PowerProperty_Create("Power Plant")

PowerPlant.SetMaxCondition(700.000000)
PowerPlant.SetCritical(1)
PowerPlant.SetTargetable(1)
PowerPlant.SetPrimary(1)
PowerPlant.SetPosition(0.000000, 0.000000, 0.005000)
PowerPlant.SetPosition2D(73.000000, 67.000000)
PowerPlant.SetRepairComplexity(2.000000)
PowerPlant.SetDisabledPercentage(0.500000)
PowerPlant.SetRadius(0.020000)
PowerPlant.SetMainBatteryLimit(50000.000000)
PowerPlant.SetBackupBatteryLimit(20000.000000)
PowerPlant.SetMainConduitCapacity(200.000000)
PowerPlant.SetBackupConduitCapacity(100.000000)
PowerPlant.SetPowerOutput(100.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(400.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.006460, -0.009075)
SensorArray.SetPosition2D(63.000000, 22.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.750000)
SensorArray.SetRadius(0.004000)
SensorArray.SetNormalPowerPerSecond(30.000000)
SensorArray.SetBaseSensorRange(1000.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(400.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(-0.000513, 0.013900, -0.017119)
ShieldGenerator.SetPosition2D(67.000000, 47.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.500000)
ShieldGenerator.SetRadius(0.002000)
ShieldGenerator.SetNormalPowerPerSecond(1.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.203922, 0.631373, 1.000000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 10.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 10.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 10.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 10.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 10.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 10.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 1.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
EscapePod = App.ShipProperty_Create("Escape Pod")

EscapePod.SetGenus(1)
EscapePod.SetSpecies(714)
EscapePod.SetMass(0.200000)
EscapePod.SetRotationalInertia(2000.000000)
EscapePod.SetShipName("Escape Pod")
EscapePod.SetModelFilename("data/Models/Ships/shuttle.nif")
EscapePod.SetDamageResolution(6.000000)
EscapePod.SetAffiliation(0)
EscapePod.SetStationary(0)
EscapePod.SetAIString("FedAttack")
EscapePod.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(EscapePod)
#################################################
PortImpulse = App.EngineProperty_Create("Port Impulse")

PortImpulse.SetMaxCondition(400.000000)
PortImpulse.SetCritical(0)
PortImpulse.SetTargetable(1)
PortImpulse.SetPrimary(1)
PortImpulse.SetPosition(-0.037000, -0.025000, -0.030000)
PortImpulse.SetPosition2D(31.000000, 39.000000)
PortImpulse.SetRepairComplexity(2.000000)
PortImpulse.SetDisabledPercentage(0.500000)
PortImpulse.SetRadius(0.020000)
PortImpulse.SetEngineType(PortImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortImpulse)
#################################################
StarImpulse = App.EngineProperty_Create("Star Impulse")

StarImpulse.SetMaxCondition(400.000000)
StarImpulse.SetCritical(0)
StarImpulse.SetTargetable(1)
StarImpulse.SetPrimary(1)
StarImpulse.SetPosition(0.037000, -0.025000, -0.030000)
StarImpulse.SetPosition2D(99.000000, 31.000000)
StarImpulse.SetRepairComplexity(2.000000)
StarImpulse.SetDisabledPercentage(0.500000)
StarImpulse.SetRadius(0.020000)
StarImpulse.SetEngineType(StarImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarImpulse)
#################################################
CenterImpulse = App.EngineProperty_Create("Center Impulse")

CenterImpulse.SetMaxCondition(400.000000)
CenterImpulse.SetCritical(0)
CenterImpulse.SetTargetable(1)
CenterImpulse.SetPrimary(1)
CenterImpulse.SetPosition(0.000000, 0.040000, -0.030000)
CenterImpulse.SetPosition2D(99.000000, 31.000000)
CenterImpulse.SetRepairComplexity(2.000000)
CenterImpulse.SetDisabledPercentage(0.500000)
CenterImpulse.SetRadius(0.020000)
CenterImpulse.SetEngineType(CenterImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(CenterImpulse)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 2.900000, 0.500000)
ViewscreenForward.SetPosition(ViewscreenForwardPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenForward)
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
ViewscreenLeftPosition.SetXYZ(-2.200000, 2.000000, 0.500000)
ViewscreenLeft.SetPosition(ViewscreenLeftPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenLeft)
#################################################
ViewscreenRight = App.PositionOrientationProperty_Create("ViewscreenRight")

ViewscreenRightForward = App.TGPoint3()
ViewscreenRightForward.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenRightUp = App.TGPoint3()
ViewscreenRightUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenRightRight = App.TGPoint3()
ViewscreenRightRight.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenRight.SetOrientation(ViewscreenRightForward, ViewscreenRightUp, ViewscreenRightRight)
ViewscreenRightPosition = App.TGPoint3()
ViewscreenRightPosition.SetXYZ(2.200000, 2.000000, 0.500000)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
#################################################
ViewscreenBack = App.PositionOrientationProperty_Create("ViewscreenBack")

ViewscreenBackForward = App.TGPoint3()
ViewscreenBackForward.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenBackUp = App.TGPoint3()
ViewscreenBackUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenBackRight = App.TGPoint3()
ViewscreenBackRight.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenBack.SetOrientation(ViewscreenBackForward, ViewscreenBackUp, ViewscreenBackRight)
ViewscreenBackPosition = App.TGPoint3()
ViewscreenBackPosition.SetXYZ(0.000000, 0.000000, 0.560000)
ViewscreenBack.SetPosition(ViewscreenBackPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenBack)
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
ViewscreenUpPosition.SetXYZ(0.000000, 2.000000, 0.700000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 2.000000, 0.000000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 0.100000, 0.100000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
Repair = App.RepairSubsystemProperty_Create("Repair")

Repair.SetMaxCondition(200.000000)
Repair.SetCritical(0)
Repair.SetTargetable(0)
Repair.SetPrimary(1)
Repair.SetPosition(0.000000, 0.000000, 0.000000)
Repair.SetPosition2D(0.000000, 0.000000)
Repair.SetRepairComplexity(1.000000)
Repair.SetDisabledPercentage(0.500000)
Repair.SetRadius(0.060000)
Repair.SetNormalPowerPerSecond(1.000000)
Repair.SetMaxRepairPoints(20.000000)
Repair.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Repair)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Plant", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Escape Pod", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Center Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenForward", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenLeft", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenRight", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenBack", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Repair", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
