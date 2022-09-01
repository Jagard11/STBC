# C:\Program Files\Activision\Bridge Commander\scripts\ships\Hardpoints\Fighter.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(750.000000)
Hull.SetCritical(1)
Hull.SetTargetable(0)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(67.000000, 47.000000)
Hull.SetRepairComplexity(3.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.030000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
SublightEngines = App.ImpulseEngineProperty_Create("Sublight Engines")

SublightEngines.SetMaxCondition(100.000000)
SublightEngines.SetCritical(0)
SublightEngines.SetTargetable(0)
SublightEngines.SetPrimary(1)
SublightEngines.SetPosition(0.000000, 0.000000, 0.000000)
SublightEngines.SetPosition2D(51.000000, 48.000000)
SublightEngines.SetRepairComplexity(1.000000)
SublightEngines.SetDisabledPercentage(0.500000)
SublightEngines.SetRadius(0.003000)
SublightEngines.SetNormalPowerPerSecond(30.000000)
SublightEngines.SetMaxAccel(5.000000)
SublightEngines.SetMaxAngularAccel(3.800000)
SublightEngines.SetMaxAngularVelocity(0.950000)
SublightEngines.SetMaxSpeed(7.000000)
SublightEngines.SetEngineSound("SGDGEngine")
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightEngines)
#################################################
PowerUnit = App.PowerProperty_Create("Power Unit")

PowerUnit.SetMaxCondition(320.000000)
PowerUnit.SetCritical(1)
PowerUnit.SetTargetable(1)
PowerUnit.SetPrimary(1)
PowerUnit.SetPosition(0.000000, -0.045000, -0.007500)
PowerUnit.SetPosition2D(64, 66)
PowerUnit.SetRepairComplexity(2.000000)
PowerUnit.SetDisabledPercentage(0.500000)
PowerUnit.SetRadius(0.002000)
PowerUnit.SetMainBatteryLimit(50000.000000)
PowerUnit.SetBackupBatteryLimit(20000.000000)
PowerUnit.SetMainConduitCapacity(200.000000)
PowerUnit.SetBackupConduitCapacity(100.000000)
PowerUnit.SetPowerOutput(100.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerUnit)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(200.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.010000, -0.004908)
SensorArray.SetPosition2D(65, 34)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.750000)
SensorArray.SetRadius(0.004000)
SensorArray.SetNormalPowerPerSecond(30.000000)
SensorArray.SetBaseSensorRange(1000.000000)
SensorArray.SetMaxProbes(0)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(1.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(0)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, 0.000000)
ShieldGenerator.SetPosition2D(67.000000, 47.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.500000)
ShieldGenerator.SetRadius(0.002000)
ShieldGenerator.SetNormalPowerPerSecond(0.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
Fighter = App.ShipProperty_Create("Fighter")

Fighter.SetGenus(1)
Fighter.SetSpecies(714)
Fighter.SetMass(25.000000)
Fighter.SetRotationalInertia(2000.000000)
Fighter.SetShipName("Fighter")
Fighter.SetModelFilename("data/Models/Ships/OriWarship/Fighter.NIF")
Fighter.SetDamageResolution(0.000100)
Fighter.SetAffiliation(0)
Fighter.SetStationary(0)
Fighter.SetAIString("RomulanAttack")
Fighter.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Fighter)
#################################################
PortEngine = App.EngineProperty_Create("Port Engine")

PortEngine.SetMaxCondition(200.000000)
PortEngine.SetCritical(0)
PortEngine.SetTargetable(1)
PortEngine.SetPrimary(1)
PortEngine.SetPosition(-0.007000, -0.044000, -0.014500)
PortEngine.SetPosition2D(56, 74)
PortEngine.SetRepairComplexity(2.000000)
PortEngine.SetDisabledPercentage(0.500000)
PortEngine.SetRadius(0.002000)
PortEngine.SetEngineType(PortEngine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortEngine)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 0.036000, 0.008000)
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
ViewscreenLeftPosition.SetXYZ(-0.027500, 0.000000, 0.000000)
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
ViewscreenRightPosition.SetXYZ(0.027500, 0.000000, 0.000000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.100000, 0.000000)
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
ViewscreenUpPosition.SetXYZ(0.000000, 0.000000, 0.025000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.000000, -0.020000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 0.036000, 0.008000)
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
Repair.SetMaxRepairPoints(2.000000)
Repair.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Repair)
#################################################
Canon1 = App.PulseWeaponProperty_Create("Canon 1")

Canon1.SetMaxCondition(200.000000)
Canon1.SetCritical(0)
Canon1.SetTargetable(1)
Canon1.SetPrimary(1)
Canon1.SetPosition(-0.037300, 0.000000, -0.011000)
Canon1.SetPosition2D(29, 50)
Canon1.SetRepairComplexity(1.000000)
Canon1.SetDisabledPercentage(0.500000)
Canon1.SetRadius(0.002000)
Canon1.SetDumbfire(1)
Canon1.SetWeaponID(0)
Canon1.SetGroups(0)
Canon1.SetDamageRadiusFactor(0.300000)
Canon1.SetIconNum(365)
Canon1.SetIconPositionX(50)
Canon1.SetIconPositionY(73)
Canon1.SetIconAboveShip(1)
Canon1.SetFireSound("")
Canon1.SetMaxCharge(20.000000)
Canon1.SetMaxDamage(1.000000)
Canon1.SetMaxDamageDistance(100.000000)
Canon1.SetMinFiringCharge(3.000000)
Canon1.SetNormalDischargeRate(1.000000)
Canon1.SetRechargeRate(0.650000)
Canon1.SetIndicatorIconNum(510)
Canon1.SetIndicatorIconPositionX(31)
Canon1.SetIndicatorIconPositionY(70)
Canon1Forward = App.TGPoint3()
Canon1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Canon1Up = App.TGPoint3()
Canon1Up.SetXYZ(0.000000, 0.000000, 1.000000)
Canon1.SetOrientation(Canon1Forward, Canon1Up)
Canon1.SetArcWidthAngles(-0.349066, 0.349066)
Canon1.SetArcHeightAngles(-0.349066, 0.349066)
Canon1.SetCooldownTime(0.300000)
Canon1.SetModuleName("Tactical.Projectiles.OriCanon")
App.g_kModelPropertyManager.RegisterLocalTemplate(Canon1)
#################################################
WeaponsSystem = App.WeaponSystemProperty_Create("Weapons System")

WeaponsSystem.SetMaxCondition(2000.000000)
WeaponsSystem.SetCritical(0)
WeaponsSystem.SetTargetable(0)
WeaponsSystem.SetPrimary(1)
WeaponsSystem.SetPosition(0.000000, 0.000000, 0.000000)
WeaponsSystem.SetPosition2D(15.000000, 15.000000)
WeaponsSystem.SetRepairComplexity(1.000000)
WeaponsSystem.SetDisabledPercentage(0.500000)
WeaponsSystem.SetRadius(0.010000)
WeaponsSystem.SetNormalPowerPerSecond(5.000000)
WeaponsSystem.SetWeaponSystemType(WeaponsSystem.WST_PULSE)
WeaponsSystem.SetSingleFire(0)
WeaponsSystem.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
WeaponsSystem.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(WeaponsSystem)
#################################################
Canon2 = App.PulseWeaponProperty_Create("Canon 2")

Canon2.SetMaxCondition(200.000000)
Canon2.SetCritical(0)
Canon2.SetTargetable(1)
Canon2.SetPrimary(1)
Canon2.SetPosition(0.037300, 0.000000, -0.011000)
Canon2.SetPosition2D(95, 50)
Canon2.SetRepairComplexity(1.000000)
Canon2.SetDisabledPercentage(0.500000)
Canon2.SetRadius(0.002000)
Canon2.SetDumbfire(1)
Canon2.SetWeaponID(0)
Canon2.SetGroups(0)
Canon2.SetDamageRadiusFactor(0.300000)
Canon2.SetIconNum(365)
Canon2.SetIconPositionX(103)
Canon2.SetIconPositionY(73)
Canon2.SetIconAboveShip(1)
Canon2.SetFireSound("")
Canon2.SetMaxCharge(20.000000)
Canon2.SetMaxDamage(1.000000)
Canon2.SetMaxDamageDistance(100.000000)
Canon2.SetMinFiringCharge(3.000000)
Canon2.SetNormalDischargeRate(1.000000)
Canon2.SetRechargeRate(0.650000)
Canon2.SetIndicatorIconNum(510)
Canon2.SetIndicatorIconPositionX(85)
Canon2.SetIndicatorIconPositionY(70)
Canon2Forward = App.TGPoint3()
Canon2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Canon2Up = App.TGPoint3()
Canon2Up.SetXYZ(0.000000, 0.000000, 1.000000)
Canon2.SetOrientation(Canon2Forward, Canon2Up)
Canon2.SetArcWidthAngles(-0.349066, 0.349066)
Canon2.SetArcHeightAngles(-0.349066, 0.349066)
Canon2.SetCooldownTime(0.300000)
Canon2.SetModuleName("Tactical.Projectiles.OriCanon")
App.g_kModelPropertyManager.RegisterLocalTemplate(Canon2)
#################################################
Cockpit = App.HullProperty_Create("Cockpit")

Cockpit.SetMaxCondition(500.000000)
Cockpit.SetCritical(1)
Cockpit.SetTargetable(1)
Cockpit.SetPrimary(0)
Cockpit.SetPosition(0.000000, 0.017500, 0.008000)
Cockpit.SetPosition2D(64, 47)
Cockpit.SetRepairComplexity(3.000000)
Cockpit.SetDisabledPercentage(0.000000)
Cockpit.SetRadius(0.015000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Cockpit)
#################################################
MissileControl = App.TorpedoSystemProperty_Create("Missile Control")

MissileControl.SetMaxCondition(1000.000000)
MissileControl.SetCritical(0)
MissileControl.SetTargetable(0)
MissileControl.SetPrimary(1)
MissileControl.SetPosition(0.000000, 0.000000, 0.000000)
MissileControl.SetPosition2D(0.000000, 0.000000)
MissileControl.SetRepairComplexity(1.000000)
MissileControl.SetDisabledPercentage(0.500000)
MissileControl.SetRadius(0.010000)
MissileControl.SetNormalPowerPerSecond(10.000000)
MissileControl.SetWeaponSystemType(MissileControl.WST_TORPEDO)
MissileControl.SetSingleFire(1)
MissileControl.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
MissileControl.SetFiringChainString(kFiringChainString)
MissileControl.SetMaxTorpedoes(0, 200)
MissileControl.SetTorpedoScript(0, "Tactical.Projectiles.A2AMissiles2")
MissileControl.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(MissileControl)
#################################################
Missile1 = App.TorpedoTubeProperty_Create("Missile 1")

Missile1.SetMaxCondition(100.000000)
Missile1.SetCritical(0)
Missile1.SetTargetable(0)
Missile1.SetPrimary(1)
Missile1.SetPosition(-0.024000, 0.020000, -0.002000)
Missile1.SetPosition2D(30, 50)
Missile1.SetRepairComplexity(1.000000)
Missile1.SetDisabledPercentage(0.500000)
Missile1.SetRadius(0.003000)
Missile1.SetDumbfire(1)
Missile1.SetWeaponID(0)
Missile1.SetGroups(1)
Missile1.SetDamageRadiusFactor(0.600000)
Missile1.SetIconNum(370)
Missile1.SetIconPositionX(51)
Missile1.SetIconPositionY(73)
Missile1.SetIconAboveShip(1)
Missile1.SetImmediateDelay(0.000000)
Missile1.SetReloadDelay(20.000000)
Missile1.SetMaxReady(5)
Missile1Direction = App.TGPoint3()
Missile1Direction.SetXYZ(0.000000, 1.000000, 0.000000)
Missile1.SetDirection(Missile1Direction)
Missile1Right = App.TGPoint3()
Missile1Right.SetXYZ(1.000000, 0.000000, 0.000000)
Missile1.SetRight(Missile1Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(Missile1)
#################################################
Missile2 = App.TorpedoTubeProperty_Create("Missile 2")

Missile2.SetMaxCondition(100.000000)
Missile2.SetCritical(0)
Missile2.SetTargetable(0)
Missile2.SetPrimary(1)
Missile2.SetPosition(0.024000, 0.020000, -0.002000)
Missile2.SetPosition2D(95, 50)
Missile2.SetRepairComplexity(1.000000)
Missile2.SetDisabledPercentage(0.500000)
Missile2.SetRadius(0.003000)
Missile2.SetDumbfire(1)
Missile2.SetWeaponID(1)
Missile2.SetGroups(1)
Missile2.SetDamageRadiusFactor(0.600000)
Missile2.SetIconNum(370)
Missile2.SetIconPositionX(103)
Missile2.SetIconPositionY(73)
Missile2.SetIconAboveShip(1)
Missile2.SetImmediateDelay(0.000000)
Missile2.SetReloadDelay(20.000000)
Missile2.SetMaxReady(5)
Missile2Direction = App.TGPoint3()
Missile2Direction.SetXYZ(0.000000, 1.000000, 0.000000)
Missile2.SetDirection(Missile2Direction)
Missile2Right = App.TGPoint3()
Missile2Right.SetXYZ(1.000000, 0.000000, 0.000000)
Missile2.SetRight(Missile2Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(Missile2)
#################################################
StarEngine = App.EngineProperty_Create("Star Engine")

StarEngine.SetMaxCondition(200.000000)
StarEngine.SetCritical(0)
StarEngine.SetTargetable(1)
StarEngine.SetPrimary(1)
StarEngine.SetPosition(0.007000, -0.044000, -0.014500)
StarEngine.SetPosition2D(71, 74)
StarEngine.SetRepairComplexity(2.000000)
StarEngine.SetDisabledPercentage(0.500000)
StarEngine.SetRadius(0.002000)
StarEngine.SetEngineType(StarEngine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarEngine)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Cockpit", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Unit", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Missile Control", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Missile 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Missile 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Fighter", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Weapons System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Canon 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Canon 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
