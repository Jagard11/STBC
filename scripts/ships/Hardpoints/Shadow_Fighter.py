# C:\Programme\Activision\Babylon 5 Bridge Commander\scripts\ships\Hardpoints\Shadow_Scout.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Engine = App.EngineProperty_Create("Engine")

Engine.SetMaxCondition(300.000000)
Engine.SetCritical(0)
Engine.SetTargetable(1)
Engine.SetPrimary(1)
Engine.SetPosition(0.000000, 0.000000, 0.000000)
Engine.SetPosition2D(0.000000, 0.000000)
Engine.SetRepairComplexity(1.000000)
Engine.SetDisabledPercentage(0.500000)
Engine.SetRadius(1.000000)
Engine.SetEngineType(Engine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine)
#################################################
BioOrganicHull = App.HullProperty_Create("Bio Organic Hull")

BioOrganicHull.SetMaxCondition(350.000000)
BioOrganicHull.SetCritical(1)
BioOrganicHull.SetTargetable(1)
BioOrganicHull.SetPrimary(1)
BioOrganicHull.SetPosition(0.000000, 0.000000, 0.000000)
BioOrganicHull.SetPosition2D(0.000000, 0.000000)
BioOrganicHull.SetRepairComplexity(26.000000)
BioOrganicHull.SetDisabledPercentage(0.000000)
BioOrganicHull.SetRadius(9.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(BioOrganicHull)
#################################################
HyperspaceTap = App.PowerProperty_Create("Hyperspace Tap")

HyperspaceTap.SetMaxCondition(300.000000)
HyperspaceTap.SetCritical(1)
HyperspaceTap.SetTargetable(0)
HyperspaceTap.SetPrimary(1)
HyperspaceTap.SetPosition(0.000000, 0.000000, 0.000000)
HyperspaceTap.SetPosition2D(0.000000, 0.000000)
HyperspaceTap.SetRepairComplexity(1.000000)
HyperspaceTap.SetDisabledPercentage(0.500000)
HyperspaceTap.SetRadius(1.000000)
HyperspaceTap.SetMainBatteryLimit(150000.000000)
HyperspaceTap.SetBackupBatteryLimit(100000.000000)
HyperspaceTap.SetMainConduitCapacity(30.000000)
HyperspaceTap.SetBackupConduitCapacity(30.000000)
HyperspaceTap.SetPowerOutput(30.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(HyperspaceTap)
#################################################
Sensor = App.SensorProperty_Create("Sensor")

Sensor.SetMaxCondition(300.000000)
Sensor.SetCritical(0)
Sensor.SetTargetable(0)
Sensor.SetPrimary(1)
Sensor.SetPosition(0.000000, 0.000000, 0.000000)
Sensor.SetPosition2D(0.000000, 0.000000)
Sensor.SetRepairComplexity(1.000000)
Sensor.SetDisabledPercentage(0.500000)
Sensor.SetRadius(0.060000)
Sensor.SetNormalPowerPerSecond(1.000000)
Sensor.SetBaseSensorRange(1200.000000)
Sensor.SetMaxProbes(0)
App.g_kModelPropertyManager.RegisterLocalTemplate(Sensor)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")

RepairSystem.SetMaxCondition(300.000000)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(0)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(0.000000, 0.000000, 0.000000)
RepairSystem.SetPosition2D(0.000000, 0.000000)
RepairSystem.SetRepairComplexity(1.000000)
RepairSystem.SetDisabledPercentage(0.500000)
RepairSystem.SetRadius(0.030000)
RepairSystem.SetNormalPowerPerSecond(1.000000)
RepairSystem.SetMaxRepairPoints(500.000000)
RepairSystem.SetNumRepairTeams(3)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
ShadowShields = App.ShieldProperty_Create("Shadow Shields")

ShadowShields.SetMaxCondition(300.000000)
ShadowShields.SetCritical(0)
ShadowShields.SetTargetable(0)
ShadowShields.SetPrimary(1)
ShadowShields.SetPosition(0.000000, 0.000000, 0.000000)
ShadowShields.SetPosition2D(0.000000, 0.000000)
ShadowShields.SetRepairComplexity(1.000000)
ShadowShields.SetDisabledPercentage(0.500000)
ShadowShields.SetRadius(0.010000)
ShadowShields.SetNormalPowerPerSecond(1.000000)
ShadowShieldsShieldGlowColor = App.TGColorA()
ShadowShieldsShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
ShadowShields.SetShieldGlowColor(ShadowShieldsShieldGlowColor)
ShadowShields.SetShieldGlowDecay(1.000000)
ShadowShields.SetMaxShields(ShadowShields.FRONT_SHIELDS, 100.000000)
ShadowShields.SetMaxShields(ShadowShields.REAR_SHIELDS, 50.000000)
ShadowShields.SetMaxShields(ShadowShields.TOP_SHIELDS, 50.000000)
ShadowShields.SetMaxShields(ShadowShields.BOTTOM_SHIELDS, 50.000000)
ShadowShields.SetMaxShields(ShadowShields.LEFT_SHIELDS, 50.000000)
ShadowShields.SetMaxShields(ShadowShields.RIGHT_SHIELDS, 50.000000)
ShadowShields.SetShieldChargePerSecond(ShadowShields.FRONT_SHIELDS, 165.000000)
ShadowShields.SetShieldChargePerSecond(ShadowShields.REAR_SHIELDS, 165.000000)
ShadowShields.SetShieldChargePerSecond(ShadowShields.TOP_SHIELDS, 165.000000)
ShadowShields.SetShieldChargePerSecond(ShadowShields.BOTTOM_SHIELDS, 165.000000)
ShadowShields.SetShieldChargePerSecond(ShadowShields.LEFT_SHIELDS, 165.000000)
ShadowShields.SetShieldChargePerSecond(ShadowShields.RIGHT_SHIELDS, 165.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShadowShields)
#################################################
ShadowBattlecrab = App.ShipProperty_Create("Shadow Fighter")

ShadowBattlecrab.SetGenus(0)
ShadowBattlecrab.SetSpecies(401)
ShadowBattlecrab.SetMass(30.000000)
ShadowBattlecrab.SetRotationalInertia(500.000000)
ShadowBattlecrab.SetShipName("Shadow Fighter")
ShadowBattlecrab.SetModelFilename("data/Models/Ships/Shadow_Fighter/Shadow_Fighter.nif")
ShadowBattlecrab.SetDamageResolution(0.000010)
ShadowBattlecrab.SetAffiliation(0)
ShadowBattlecrab.SetStationary(0)
ShadowBattlecrab.SetAIString("NonFedAttack")
ShadowBattlecrab.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(ShadowBattlecrab)
#################################################
Cockpit = App.TorpedoSystemProperty_Create("Cockpit")

Cockpit.SetMaxCondition(300.000000)
Cockpit.SetCritical(1)
Cockpit.SetTargetable(0)
Cockpit.SetPrimary(1)
Cockpit.SetPosition(0.000000, 0.000000, 0.000000)
Cockpit.SetPosition2D(0.000000, 0.000000)
Cockpit.SetRepairComplexity(1.000000)
Cockpit.SetDisabledPercentage(0.500000)
Cockpit.SetRadius(0.080000)
Cockpit.SetNormalPowerPerSecond(1.000000)
Cockpit.SetWeaponSystemType(Cockpit.WST_TORPEDO)
Cockpit.SetSingleFire(0)
Cockpit.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Cockpit.SetFiringChainString(kFiringChainString)
Cockpit.SetMaxTorpedoes(0, 100)
Cockpit.SetTorpedoScript(0, "Tactical.Projectiles.ShadHipDis")
Cockpit.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Cockpit)
#################################################
AftTorpedo = App.TorpedoTubeProperty_Create("Aft Torpedo")

AftTorpedo.SetMaxCondition(350.000000)
AftTorpedo.SetCritical(0)
AftTorpedo.SetTargetable(0)
AftTorpedo.SetPrimary(1)
AftTorpedo.SetPosition(0.000000, -0.100000, 0.000000)
AftTorpedo.SetPosition2D(0.000000, 0.000000)
AftTorpedo.SetRepairComplexity(3.000000)
AftTorpedo.SetDisabledPercentage(0.750000)
AftTorpedo.SetRadius(0.150000)
AftTorpedo.SetDumbfire(0)
AftTorpedo.SetWeaponID(2)
AftTorpedo.SetGroups(2)
AftTorpedo.SetDamageRadiusFactor(0.999999)
AftTorpedo.SetIconNum(370)
AftTorpedo.SetIconPositionX(76.000000)
AftTorpedo.SetIconPositionY(100.000000)
AftTorpedo.SetIconAboveShip(1)
AftTorpedo.SetImmediateDelay(0.500000)
AftTorpedo.SetReloadDelay(600.000000)
AftTorpedo.SetMaxReady(1)
AftTorpedoDirection = App.TGPoint3()
AftTorpedoDirection.SetXYZ(0.000000, -1.000000, 0.000000)
AftTorpedo.SetDirection(AftTorpedoDirection)
AftTorpedoRight = App.TGPoint3()
AftTorpedoRight.SetXYZ(-1.000000, 0.000000, 0.000000)
AftTorpedo.SetRight(AftTorpedoRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(AftTorpedo)
#################################################
LaserEmiter = App.WeaponSystemProperty_Create("Laser Emiter")

LaserEmiter.SetMaxCondition(300.000000)
LaserEmiter.SetCritical(0)
LaserEmiter.SetTargetable(0)
LaserEmiter.SetPrimary(1)
LaserEmiter.SetPosition(0.000000, 0.000000, 0.000000)
LaserEmiter.SetPosition2D(0.000000, 0.000000)
LaserEmiter.SetRepairComplexity(1.000000)
LaserEmiter.SetDisabledPercentage(0.500000)
LaserEmiter.SetRadius(0.050000)
LaserEmiter.SetNormalPowerPerSecond(10.000000)
LaserEmiter.SetWeaponSystemType(LaserEmiter.WST_PHASER)
LaserEmiter.SetSingleFire(0)
LaserEmiter.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
LaserEmiter.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(LaserEmiter)
#################################################
ShadowEngine = App.ImpulseEngineProperty_Create("Shadow Engine")

ShadowEngine.SetMaxCondition(300.000000)
ShadowEngine.SetCritical(0)
ShadowEngine.SetTargetable(0)
ShadowEngine.SetPrimary(1)
ShadowEngine.SetPosition(0.000000, 0.000000, 0.000000)
ShadowEngine.SetPosition2D(0.000000, 0.000000)
ShadowEngine.SetRepairComplexity(1.000000)
ShadowEngine.SetDisabledPercentage(0.500000)
ShadowEngine.SetRadius(1.000000)
ShadowEngine.SetNormalPowerPerSecond(2.000000)
ShadowEngine.SetMaxAccel(5.000000)
ShadowEngine.SetMaxAngularAccel(2.600000)
ShadowEngine.SetMaxAngularVelocity(2.400000)
ShadowEngine.SetMaxSpeed(27.000000)
ShadowEngine.SetEngineSound("shadowengine")
App.g_kModelPropertyManager.RegisterLocalTemplate(ShadowEngine)
#################################################
HyperspaceEngine = App.EngineProperty_Create("Hyperspace Engine")

HyperspaceEngine.SetMaxCondition(300.000000)
HyperspaceEngine.SetCritical(0)
HyperspaceEngine.SetTargetable(0)
HyperspaceEngine.SetPrimary(1)
HyperspaceEngine.SetPosition(0.000000, 0.000000, 0.000000)
HyperspaceEngine.SetPosition2D(0.000000, 0.000000)
HyperspaceEngine.SetRepairComplexity(1.000000)
HyperspaceEngine.SetDisabledPercentage(0.500000)
HyperspaceEngine.SetRadius(1.000000)
HyperspaceEngine.SetEngineType(HyperspaceEngine.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(HyperspaceEngine)
#################################################
hyperback = App.WarpEngineProperty_Create("hyper back")

hyperback.SetMaxCondition(300.000000)
hyperback.SetCritical(0)
hyperback.SetTargetable(0)
hyperback.SetPrimary(1)
hyperback.SetPosition(0.000000, 0.000000, 0.000000)
hyperback.SetPosition2D(0.000000, 0.000000)
hyperback.SetRepairComplexity(1.000000)
hyperback.SetDisabledPercentage(0.500000)
hyperback.SetRadius(1.000000)
hyperback.SetNormalPowerPerSecond(1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(hyperback)
#################################################
DeathRay = App.PhaserProperty_Create("Death Ray")

DeathRay.SetMaxCondition(300.000000)
DeathRay.SetCritical(0)
DeathRay.SetTargetable(0)
DeathRay.SetPrimary(1)
DeathRay.SetPosition(0.000000, 0.500000, 0.000000)
DeathRay.SetPosition2D(0.000000, 0.000000)
DeathRay.SetRepairComplexity(1.000000)
DeathRay.SetDisabledPercentage(0.500000)
DeathRay.SetRadius(3.050000)
DeathRay.SetDumbfire(1)
DeathRay.SetWeaponID(0)
DeathRay.SetGroups(1)
DeathRay.SetDamageRadiusFactor(9.999999)
DeathRay.SetIconNum(510)
DeathRay.SetIconPositionX(60.000000)
DeathRay.SetIconPositionY(70.000000)
DeathRay.SetIconAboveShip(1)
DeathRay.SetFireSound("shadowbeam")
DeathRay.SetMaxCharge(1.000000)
DeathRay.SetMaxDamage(250.000000)
DeathRay.SetMaxDamageDistance(80.000000)
DeathRay.SetMinFiringCharge(0.500000)
DeathRay.SetNormalDischargeRate(2.000000)
DeathRay.SetRechargeRate(0.500000)
DeathRay.SetIndicatorIconNum(0)
DeathRay.SetIndicatorIconPositionX(0.000000)
DeathRay.SetIndicatorIconPositionY(0.000000)
DeathRayForward = App.TGPoint3()
DeathRayForward.SetXYZ(0.000000, 1.000000, 0.000000)
DeathRayUp = App.TGPoint3()
DeathRayUp.SetXYZ(0.000000, 0.000000, 1.000000)
DeathRay.SetOrientation(DeathRayForward, DeathRayUp)
DeathRay.SetWidth(0.010000)
DeathRay.SetLength(0.010000)
DeathRay.SetArcWidthAngles(-0.401426, 0.401426)
DeathRay.SetArcHeightAngles(-0.453786, 0.453786)
DeathRay.SetPhaserTextureStart(5)
DeathRay.SetPhaserTextureEnd(20)
DeathRay.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.576471, 0.156863, 1.000000, 1.000000)
DeathRay.SetOuterShellColor(kColor)
kColor.SetRGBA(0.576471, 0.156863, 1.000000, 1.000000)
DeathRay.SetInnerShellColor(kColor)
kColor.SetRGBA(1.000000, 0.200000, 0.400000, 1.000000)
DeathRay.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 0.200000, 0.400000, 1.000000)
DeathRay.SetInnerCoreColor(kColor)
DeathRay.SetNumSides(6)
DeathRay.SetMainRadius(0.200000)
DeathRay.SetTaperRadius(0.020000)
DeathRay.SetCoreScale(0.300000)
DeathRay.SetTaperRatio(0.050000)
DeathRay.SetTaperMinLength(5.000000)
DeathRay.SetTaperMaxLength(20.000000)
DeathRay.SetLengthTextureTilePerUnit(0.300000)
DeathRay.SetPerimeterTile(1.000000)
DeathRay.SetTextureSpeed(0.000100)
DeathRay.SetTextureName("data/b5shadow.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(DeathRay)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 4.500000, 0.000000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -3.500000, 0.500000)
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
ViewscreenLeftPosition.SetXYZ(-9.000000, -2.000000, 0.000000)
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
ViewscreenRightPosition.SetXYZ(9.000000, -2.000000, 0.000000)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
#################################################
ViewscreenUp = App.PositionOrientationProperty_Create("ViewscreenUp")

ViewscreenUpForward = App.TGPoint3()
ViewscreenUpForward.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenUpUp = App.TGPoint3()
ViewscreenUpUp.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenUpRight = App.TGPoint3()
ViewscreenUpRight.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenUp.SetOrientation(ViewscreenUpForward, ViewscreenUpUp, ViewscreenUpRight)
ViewscreenUpPosition = App.TGPoint3()
ViewscreenUpPosition.SetXYZ(0.000000, -2.000000, 2.000000)
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
ViewscreenDownPosition.SetXYZ(0.000000, -2.000000, -2.000000)
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
FirstPersonCameraPosition.SetXYZ(-0.057000, 1.000000, 0.000000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
ShadowSceam = App.WeaponSystemProperty_Create("ShadowSceam")

ShadowSceam.SetMaxCondition(310.000000)
ShadowSceam.SetCritical(0)
ShadowSceam.SetTargetable(0)
ShadowSceam.SetPrimary(1)
ShadowSceam.SetPosition(0.000000, 0.000000, 0.000000)
ShadowSceam.SetPosition2D(0.000000, 0.000000)
ShadowSceam.SetRepairComplexity(1.000000)
ShadowSceam.SetDisabledPercentage(0.500000)
ShadowSceam.SetRadius(0.250000)
ShadowSceam.SetNormalPowerPerSecond(1.000000)
ShadowSceam.SetWeaponSystemType(ShadowSceam.WST_PULSE)
ShadowSceam.SetSingleFire(0)
ShadowSceam.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
ShadowSceam.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShadowSceam)
#################################################
Scream = App.PulseWeaponProperty_Create("Scream")

Scream.SetMaxCondition(310.000000)
Scream.SetCritical(0)
Scream.SetTargetable(0)
Scream.SetPrimary(1)
Scream.SetPosition(0.000000, 0.250000, 0.000000)
Scream.SetPosition2D(0.000000, 0.000000)
Scream.SetRepairComplexity(1.000000)
Scream.SetDisabledPercentage(0.500000)
Scream.SetRadius(0.250000)
Scream.SetDumbfire(1)
Scream.SetWeaponID(0)
Scream.SetGroups(0)
Scream.SetDamageRadiusFactor(9.999999)
Scream.SetIconNum(0)
Scream.SetIconPositionX(0.000000)
Scream.SetIconPositionY(0.000000)
Scream.SetIconAboveShip(1)
Scream.SetFireSound("shadowscream")
Scream.SetMaxCharge(1.000000)
Scream.SetMaxDamage(25.000000)
Scream.SetMaxDamageDistance(170.000000)
Scream.SetMinFiringCharge(1.000000)
Scream.SetNormalDischargeRate(1.000000)
Scream.SetRechargeRate(0.000500)
Scream.SetIndicatorIconNum(0)
Scream.SetIndicatorIconPositionX(0.000000)
Scream.SetIndicatorIconPositionY(0.000000)
ScreamForward = App.TGPoint3()
ScreamForward.SetXYZ(0.000000, 1.000000, 0.000000)
ScreamUp = App.TGPoint3()
ScreamUp.SetXYZ(0.000000, 0.000000, 1.000000)
Scream.SetOrientation(ScreamForward, ScreamUp)
Scream.SetArcWidthAngles(-2.094395, 2.094395)
Scream.SetArcHeightAngles(-2.094395, 2.094395)
Scream.SetCooldownTime(0.001000)
Scream.SetModuleName("Tactical.Projectiles.shadowscream")
App.g_kModelPropertyManager.RegisterLocalTemplate(Scream)
#################################################
Spit = App.PulseWeaponProperty_Create("Spit")

Spit.SetMaxCondition(310.000000)
Spit.SetCritical(0)
Spit.SetTargetable(0)
Spit.SetPrimary(1)
Spit.SetPosition(0.000000, 0.000000, 0.000000)
Spit.SetPosition2D(0.000000, 0.000000)
Spit.SetRepairComplexity(1.000000)
Spit.SetDisabledPercentage(0.500000)
Spit.SetRadius(0.250000)
Spit.SetDumbfire(1)
Spit.SetWeaponID(0)
Spit.SetGroups(0)
Spit.SetDamageRadiusFactor(9.999999)
Spit.SetIconNum(0)
Spit.SetIconPositionX(0.000000)
Spit.SetIconPositionY(0.000000)
Spit.SetIconAboveShip(1)
Spit.SetFireSound("shadowSpit")
Spit.SetMaxCharge(1.000000)
Spit.SetMaxDamage(265.000000)
Spit.SetMaxDamageDistance(170.000000)
Spit.SetMinFiringCharge(1.000000)
Spit.SetNormalDischargeRate(1.000000)
Spit.SetRechargeRate(0.800000)
Spit.SetIndicatorIconNum(0)
Spit.SetIndicatorIconPositionX(0.000000)
Spit.SetIndicatorIconPositionY(0.000000)
SpitForward = App.TGPoint3()
SpitForward.SetXYZ(0.000000, 1.000000, 0.000000)
SpitUp = App.TGPoint3()
SpitUp.SetXYZ(0.000000, 0.000000, 1.000000)
Spit.SetOrientation(SpitForward, SpitUp)
Spit.SetArcWidthAngles(-2.094395, 2.094395)
Spit.SetArcHeightAngles(-2.094395, 2.094395)
Spit.SetCooldownTime(0.001000)
Spit.SetModuleName("Tactical.Projectiles.shadowSpit")
App.g_kModelPropertyManager.RegisterLocalTemplate(Spit)
#################################################
PhaseCloak = App.CloakingSubsystemProperty_Create("Hyperspace Cloak")

PhaseCloak.SetMaxCondition(310.000000)
PhaseCloak.SetCritical(0)
PhaseCloak.SetTargetable(0)
PhaseCloak.SetPrimary(1)
PhaseCloak.SetPosition(0.000000, 0.000000, 0.000000)
PhaseCloak.SetPosition2D(0.000000, 0.000000)
PhaseCloak.SetRepairComplexity(1.000000)
PhaseCloak.SetDisabledPercentage(0.500000)
PhaseCloak.SetRadius(0.250000)
PhaseCloak.SetNormalPowerPerSecond(0.000001)
PhaseCloak.SetCloakStrength(7.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PhaseCloak)
#################################################
JumpspaceDrive = App.HullProperty_Create("Jumpspace Drive 1")

JumpspaceDrive.SetMaxCondition(310.000000)
JumpspaceDrive.SetCritical(0)
JumpspaceDrive.SetTargetable(0)
JumpspaceDrive.SetPrimary(0)
JumpspaceDrive.SetPosition(0.000000, 0.000000, 0.000000)
JumpspaceDrive.SetPosition2D(0.000000, 0.000000)
JumpspaceDrive.SetRepairComplexity(1.000000)
JumpspaceDrive.SetDisabledPercentage(0.500000)
JumpspaceDrive.SetRadius(7.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(JumpspaceDrive)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Bio Organic Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hyperspace Tap", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shadow Fighter", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shadow Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hyperspace Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("hyper back", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shadow Shields", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("ShadowSceam", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Scream", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Spit", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hyperspace Cloak", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Jumpspace Drive 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
