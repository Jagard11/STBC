# C:\Program Files (x86)\Activision\Bridge Commander  KM v1 plus\scripts\ships\Hardpoints\JLSAeon.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(2400.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.003069, -0.049843, 0.019847)
ShieldGenerator.SetPosition2D(66.000000, 38.000000)
ShieldGenerator.SetRepairComplexity(3.000000)
ShieldGenerator.SetDisabledPercentage(0.250000)
ShieldGenerator.SetRadius(0.010000)
ShieldGenerator.SetNormalPowerPerSecond(50.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.509804, 0.749020, 1.000000, 1.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 100000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 100000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 100000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 100000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 100000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 100000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 90.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 90.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 90.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 90.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 90.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 90.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(2000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, -0.020000, 0.000000)
Hull.SetPosition2D(66.000000, 38.000000)
Hull.SetRepairComplexity(3.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.160000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(2000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.093000, -0.005000)
SensorArray.SetPosition2D(66.000000, 7.000000)
SensorArray.SetRepairComplexity(3.000000)
SensorArray.SetDisabledPercentage(0.250000)
SensorArray.SetRadius(0.008000)
SensorArray.SetNormalPowerPerSecond(50.000000)
SensorArray.SetBaseSensorRange(500000.000000)
SensorArray.SetMaxProbes(0)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(2100.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, -0.040000, 0.000000)
WarpCore.SetPosition2D(65.000000, 55.000000)
WarpCore.SetRepairComplexity(3.000000)
WarpCore.SetDisabledPercentage(0.250000)
WarpCore.SetRadius(0.005000)
WarpCore.SetMainBatteryLimit(80000.000000)
WarpCore.SetBackupBatteryLimit(100000.000000)
WarpCore.SetMainConduitCapacity(470.000000)
WarpCore.SetBackupConduitCapacity(70.000000)
WarpCore.SetPowerOutput(400.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(7000.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, 0.000000, 0.000000)
ImpulseEngines.SetPosition2D(64.000000, 104.000000)
ImpulseEngines.SetRepairComplexity(3.000000)
ImpulseEngines.SetDisabledPercentage(0.250000)
ImpulseEngines.SetRadius(0.012000)
ImpulseEngines.SetNormalPowerPerSecond(50.000000)
ImpulseEngines.SetMaxAccel(4.000000)
ImpulseEngines.SetMaxAngularAccel(1.000000)
ImpulseEngines.SetMaxAngularVelocity(1.300000)
ImpulseEngines.SetMaxSpeed(13.000000)
ImpulseEngines.SetEngineSound("Aeon Engine")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(8000.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.000000, -0.070000, 0.000000)
WarpEngines.SetPosition2D(64.000000, 104.000000)
WarpEngines.SetRepairComplexity(2.000000)
WarpEngines.SetDisabledPercentage(0.250000)
WarpEngines.SetRadius(0.030000)
WarpEngines.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
PortWarp = App.EngineProperty_Create("Port Warp")

PortWarp.SetMaxCondition(1000.000000)
PortWarp.SetCritical(0)
PortWarp.SetTargetable(1)
PortWarp.SetPrimary(1)
PortWarp.SetPosition(-0.068497, -0.050553, 0.000000)
PortWarp.SetPosition2D(46.000000, 78.000000)
PortWarp.SetRepairComplexity(2.000000)
PortWarp.SetDisabledPercentage(0.250000)
PortWarp.SetRadius(0.010000)
PortWarp.SetEngineType(PortWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortWarp)
#################################################
StarWarp = App.EngineProperty_Create("Star Warp")

StarWarp.SetMaxCondition(1000.000000)
StarWarp.SetCritical(0)
StarWarp.SetTargetable(1)
StarWarp.SetPrimary(1)
StarWarp.SetPosition(0.068497, -0.050553, 0.000000)
StarWarp.SetPosition2D(82.000000, 78.000000)
StarWarp.SetRepairComplexity(2.000000)
StarWarp.SetDisabledPercentage(0.250000)
StarWarp.SetRadius(0.010000)
StarWarp.SetEngineType(StarWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")

Engineering.SetMaxCondition(2000.000000)
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
Engineering.SetNumRepairTeams(2)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
Aeon = App.ShipProperty_Create("Aeon")

Aeon.SetGenus(1)
Aeon.SetSpecies(401)
Aeon.SetMass(45.000000)
Aeon.SetRotationalInertia(2000.000000)
Aeon.SetShipName("Bird of Prey")
Aeon.SetModelFilename("data/Models/Ships/DQP/JLSAeon/Aeon.NIF")
Aeon.SetDamageResolution(1.000000)
Aeon.SetAffiliation(0)
Aeon.SetStationary(0)
Aeon.SetAIString("NonFedAttack")
Aeon.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Aeon)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 0.000000, 0.000000)
ViewscreenForward.SetPosition(ViewscreenForwardPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenForward)
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
ViewscreenBackPosition.SetXYZ(0.000000, 0.000000, 0.000000)
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
StarImpulse = App.EngineProperty_Create("Star Impulse")

StarImpulse.SetMaxCondition(1200.000000)
StarImpulse.SetCritical(0)
StarImpulse.SetTargetable(1)
StarImpulse.SetPrimary(1)
StarImpulse.SetPosition(0.034774, -0.065436, 0.000000)
StarImpulse.SetPosition2D(64.000000, 85.000000)
StarImpulse.SetRepairComplexity(3.000000)
StarImpulse.SetDisabledPercentage(0.250000)
StarImpulse.SetRadius(0.030000)
StarImpulse.SetEngineType(StarImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarImpulse)
#################################################
PortImpulse = App.EngineProperty_Create("Port Impulse")

PortImpulse.SetMaxCondition(1200.000000)
PortImpulse.SetCritical(0)
PortImpulse.SetTargetable(1)
PortImpulse.SetPrimary(1)
PortImpulse.SetPosition(-0.034774, -0.065436, 0.000000)
PortImpulse.SetPosition2D(64.000000, 85.000000)
PortImpulse.SetRepairComplexity(3.000000)
PortImpulse.SetDisabledPercentage(0.250000)
PortImpulse.SetRadius(0.030000)
PortImpulse.SetEngineType(PortImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortImpulse)
#################################################
Phaser = App.WeaponSystemProperty_Create("Phaser")

Phaser.SetMaxCondition(2000.000000)
Phaser.SetCritical(0)
Phaser.SetTargetable(1)
Phaser.SetPrimary(1)
Phaser.SetPosition(0.000000, 0.000000, 0.000000)
Phaser.SetPosition2D(0.000000, 0.000000)
Phaser.SetRepairComplexity(3.000000)
Phaser.SetDisabledPercentage(0.200000)
Phaser.SetRadius(0.010000)
Phaser.SetNormalPowerPerSecond(50.000000)
Phaser.SetWeaponSystemType(Phaser.WST_PHASER)
Phaser.SetSingleFire(1)
Phaser.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Phaser.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Phaser)
#################################################
SubatomicDisruptor = App.PhaserProperty_Create("Subatomic Disruptor")

SubatomicDisruptor.SetMaxCondition(2000.000000)
SubatomicDisruptor.SetCritical(0)
SubatomicDisruptor.SetTargetable(1)
SubatomicDisruptor.SetPrimary(1)
SubatomicDisruptor.SetPosition(0.000000, 0.110000, -0.001000)
SubatomicDisruptor.SetPosition2D(0.000000, 0.000000)
SubatomicDisruptor.SetRepairComplexity(1.000000)
SubatomicDisruptor.SetDisabledPercentage(0.200000)
SubatomicDisruptor.SetRadius(0.040000)
SubatomicDisruptor.SetDumbfire(0)
SubatomicDisruptor.SetWeaponID(0)
SubatomicDisruptor.SetGroups(0)
SubatomicDisruptor.SetDamageRadiusFactor(0.100000)
SubatomicDisruptor.SetIconNum(364)
SubatomicDisruptor.SetIconPositionX(63.000000)
SubatomicDisruptor.SetIconPositionY(20.000000)
SubatomicDisruptor.SetIconAboveShip(1)
SubatomicDisruptor.SetFireSound("Burst")
SubatomicDisruptor.SetMaxCharge(4.500000)
SubatomicDisruptor.SetMaxDamage(9800.000000)
SubatomicDisruptor.SetMaxDamageDistance(100.000000)
SubatomicDisruptor.SetMinFiringCharge(1.000000)
SubatomicDisruptor.SetNormalDischargeRate(40.500000)
SubatomicDisruptor.SetRechargeRate(0.200000)
SubatomicDisruptor.SetIndicatorIconNum(510)
SubatomicDisruptor.SetIndicatorIconPositionX(57.000000)
SubatomicDisruptor.SetIndicatorIconPositionY(15.000000)
SubatomicDisruptorForward = App.TGPoint3()
SubatomicDisruptorForward.SetXYZ(-0.047340, 0.973019, 0.225817)
SubatomicDisruptorUp = App.TGPoint3()
SubatomicDisruptorUp.SetXYZ(0.033474, -0.224399, 0.973922)
SubatomicDisruptor.SetOrientation(SubatomicDisruptorForward, SubatomicDisruptorUp)
SubatomicDisruptor.SetWidth(0.000000)
SubatomicDisruptor.SetLength(0.010000)
SubatomicDisruptor.SetArcWidthAngles(-0.872665, 0.872665)
SubatomicDisruptor.SetArcHeightAngles(-0.872665, 0.872665)
SubatomicDisruptor.SetPhaserTextureStart(0)
SubatomicDisruptor.SetPhaserTextureEnd(0)
SubatomicDisruptor.SetPhaserWidth(0.500000)
kColor = App.TGColorA()
kColor.SetRGBA(0.874510, 0.439216, 0.000000, 1.000000)
SubatomicDisruptor.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.647059, 0.286275, 1.000000)
SubatomicDisruptor.SetInnerShellColor(kColor)
kColor.SetRGBA(0.768628, 0.768628, 0.000000, 1.000000)
SubatomicDisruptor.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.501961, 1.000000)
SubatomicDisruptor.SetInnerCoreColor(kColor)
SubatomicDisruptor.SetNumSides(6)
SubatomicDisruptor.SetMainRadius(0.010000)
SubatomicDisruptor.SetTaperRadius(0.010000)
SubatomicDisruptor.SetCoreScale(0.500000)
SubatomicDisruptor.SetTaperRatio(0.250000)
SubatomicDisruptor.SetTaperMinLength(5.000000)
SubatomicDisruptor.SetTaperMaxLength(30.000000)
SubatomicDisruptor.SetLengthTextureTilePerUnit(0.500000)
SubatomicDisruptor.SetPerimeterTile(1.000000)
SubatomicDisruptor.SetTextureSpeed(2.500000)
SubatomicDisruptor.SetTextureName("data/JLSAeon.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(SubatomicDisruptor)
#################################################
LifeSupport = App.HullProperty_Create("Life Support")

LifeSupport.SetMaxCondition(29520.000000)
LifeSupport.SetCritical(0)
LifeSupport.SetTargetable(1)
LifeSupport.SetPrimary(0)
LifeSupport.SetPosition(0.000000, 0.000000, 0.000000)
LifeSupport.SetPosition2D(0.000000, 0.000000)
LifeSupport.SetRepairComplexity(1.000000)
LifeSupport.SetDisabledPercentage(0.100000)
LifeSupport.SetRadius(0.250000)
App.g_kModelPropertyManager.RegisterLocalTemplate(LifeSupport)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Life Support", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Star Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Aeon", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Phaser", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Subatomic Disruptor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
