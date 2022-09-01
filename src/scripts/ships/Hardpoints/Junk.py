# C:\Users\Owner\Documents\FinalHP_Changes_Other\Junk.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(15000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(64.000000, 60.000000)
Hull.SetRepairComplexity(3.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(7.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(8500.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(1)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, -2.000000, 0.000000)
ImpulseEngines.SetPosition2D(0.000000, 0.000000)
ImpulseEngines.SetRepairComplexity(4.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.700000)
ImpulseEngines.SetNormalPowerPerSecond(100.000000)
ImpulseEngines.SetMaxAccel(5.000000)
ImpulseEngines.SetMaxAngularAccel(0.050000)
ImpulseEngines.SetMaxAngularVelocity(0.090000)
ImpulseEngines.SetMaxSpeed(6.000000)
ImpulseEngines.SetEngineSound("Klingon Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(7500.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, -1.000000, 0.000000)
WarpCore.SetPosition2D(64.000000, 75.000000)
WarpCore.SetRepairComplexity(2.000000)
WarpCore.SetDisabledPercentage(0.500000)
WarpCore.SetRadius(0.500000)
WarpCore.SetMainBatteryLimit(10000.000000)
WarpCore.SetBackupBatteryLimit(10000.000000)
WarpCore.SetMainConduitCapacity(700.000000)
WarpCore.SetBackupConduitCapacity(150.000000)
WarpCore.SetPowerOutput(750.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")

RepairSystem.SetMaxCondition(32000.000000)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(0)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(0.000000, 0.000000, 0.000000)
RepairSystem.SetPosition2D(44.000000, 70.000000)
RepairSystem.SetRepairComplexity(10.000000)
RepairSystem.SetDisabledPercentage(0.100000)
RepairSystem.SetRadius(0.100000)
RepairSystem.SetNormalPowerPerSecond(1.000000)
RepairSystem.SetMaxRepairPoints(5.000000)
RepairSystem.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(8000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 4.000000, 0.000000)
SensorArray.SetPosition2D(64.000000, 25.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.750000)
SensorArray.SetRadius(0.300000)
SensorArray.SetNormalPowerPerSecond(100.000000)
SensorArray.SetBaseSensorRange(5800.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(8250.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, -1.500000, -1.500000)
ShieldGenerator.SetPosition2D(64.000000, 60.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.600000)
ShieldGenerator.SetRadius(0.500000)
ShieldGenerator.SetNormalPowerPerSecond(250.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.203922, 0.756863, 0.784314, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 4500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 4500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 4500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 4500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 4500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 4500.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 5.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 5.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 5.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 5.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 5.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 5.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(8000.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(1)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.000000, 1.000000, 0.300000)
WarpEngines.SetPosition2D(0.000000, 0.000000)
WarpEngines.SetRepairComplexity(3.000000)
WarpEngines.SetDisabledPercentage(0.750000)
WarpEngines.SetRadius(0.300000)
WarpEngines.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")

Torpedoes.SetMaxCondition(22000.000000)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(1)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.000000, 2.000000, -0.300000)
Torpedoes.SetPosition2D(57.000000, 13.000000)
Torpedoes.SetRepairComplexity(3.000000)
Torpedoes.SetDisabledPercentage(0.750000)
Torpedoes.SetRadius(0.300000)
Torpedoes.SetNormalPowerPerSecond(150.000000)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(0)
Torpedoes.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 50)
Torpedoes.SetTorpedoScript(0, "Tactical.Projectiles.CAJunkTorpedo")
Torpedoes.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
#################################################
FwdTorpedo1 = App.TorpedoTubeProperty_Create("Fwd Torpedo 1")

FwdTorpedo1.SetMaxCondition(12500.000000)
FwdTorpedo1.SetCritical(0)
FwdTorpedo1.SetTargetable(1)
FwdTorpedo1.SetPrimary(0)
FwdTorpedo1.SetPosition(0.000000, 4.700000, 0.200000)
FwdTorpedo1.SetPosition2D(57.000000, 13.000000)
FwdTorpedo1.SetRepairComplexity(3.000000)
FwdTorpedo1.SetDisabledPercentage(0.750000)
FwdTorpedo1.SetRadius(0.100000)
FwdTorpedo1.SetDumbfire(1)
FwdTorpedo1.SetWeaponID(0)
FwdTorpedo1.SetGroups(1)
FwdTorpedo1.SetDamageRadiusFactor(0.200000)
FwdTorpedo1.SetIconNum(370)
FwdTorpedo1.SetIconPositionX(70.000000)
FwdTorpedo1.SetIconPositionY(35.000000)
FwdTorpedo1.SetIconAboveShip(1)
FwdTorpedo1.SetImmediateDelay(0.000000)
FwdTorpedo1.SetReloadDelay(30.000000)
FwdTorpedo1.SetMaxReady(2)
FwdTorpedo1Direction = App.TGPoint3()
FwdTorpedo1Direction.SetXYZ(0.000000, 1.000000, 0.000000)
FwdTorpedo1.SetDirection(FwdTorpedo1Direction)
FwdTorpedo1Right = App.TGPoint3()
FwdTorpedo1Right.SetXYZ(1.000000, 0.000000, 0.000000)
FwdTorpedo1.SetRight(FwdTorpedo1Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(FwdTorpedo1)
#################################################
PortImpulse = App.EngineProperty_Create("Port Impulse")

PortImpulse.SetMaxCondition(8500.000000)
PortImpulse.SetCritical(0)
PortImpulse.SetTargetable(1)
PortImpulse.SetPrimary(1)
PortImpulse.SetPosition(-0.460386, -0.171841, -0.005482)
PortImpulse.SetPosition2D(34.000000, 84.000000)
PortImpulse.SetRepairComplexity(3.000000)
PortImpulse.SetDisabledPercentage(0.500000)
PortImpulse.SetRadius(0.040000)
PortImpulse.SetEngineType(PortImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortImpulse)
#################################################
StarImpulse = App.EngineProperty_Create("Star Impulse")

StarImpulse.SetMaxCondition(8500.000000)
StarImpulse.SetCritical(0)
StarImpulse.SetTargetable(1)
StarImpulse.SetPrimary(1)
StarImpulse.SetPosition(0.462742, -0.174617, -0.006518)
StarImpulse.SetPosition2D(92.000000, 84.000000)
StarImpulse.SetRepairComplexity(3.000000)
StarImpulse.SetDisabledPercentage(0.500000)
StarImpulse.SetRadius(0.040000)
StarImpulse.SetEngineType(StarImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarImpulse)
#################################################
PortWarp = App.EngineProperty_Create("Port Warp")

PortWarp.SetMaxCondition(6250.000000)
PortWarp.SetCritical(0)
PortWarp.SetTargetable(1)
PortWarp.SetPrimary(0)
PortWarp.SetPosition(-5.000000, -1.000000, 1.000000)
PortWarp.SetPosition2D(7.000000, 100.000000)
PortWarp.SetRepairComplexity(3.000000)
PortWarp.SetDisabledPercentage(0.750000)
PortWarp.SetRadius(0.500000)
PortWarp.SetEngineType(PortWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortWarp)
#################################################
StarWarp = App.EngineProperty_Create("Star Warp")

StarWarp.SetMaxCondition(6250.000000)
StarWarp.SetCritical(0)
StarWarp.SetTargetable(1)
StarWarp.SetPrimary(0)
StarWarp.SetPosition(5.000000, -1.000000, 1.000000)
StarWarp.SetPosition2D(121.000000, 100.000000)
StarWarp.SetRepairComplexity(3.000000)
StarWarp.SetDisabledPercentage(0.750000)
StarWarp.SetRadius(0.500000)
StarWarp.SetEngineType(StarWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp)
#################################################
Junk = App.ShipProperty_Create("Junk")

Junk.SetGenus(1)
Junk.SetSpecies(918)
Junk.SetMass(250.000000)
Junk.SetRotationalInertia(15000.000000)
Junk.SetShipName("Junk")
Junk.SetModelFilename("data/Models/Ships/Junk.nif")
Junk.SetDamageResolution(10.000000)
Junk.SetAffiliation(0)
Junk.SetStationary(0)
Junk.SetAIString("NonFedAttack")
Junk.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Junk)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 0.200000, 0.120000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.500000, 0.120000)
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
ViewscreenLeftPosition.SetXYZ(0.000000, 0.200000, 0.120000)
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
ViewscreenRightPosition.SetXYZ(0.000000, 0.200000, 0.120000)
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
ViewscreenUpPosition.SetXYZ(0.000000, 0.200000, 0.120000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.200000, -0.120000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 0.200000, 0.120000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
Phasers = App.WeaponSystemProperty_Create("Phasers")

Phasers.SetMaxCondition(15000.000000)
Phasers.SetCritical(0)
Phasers.SetTargetable(1)
Phasers.SetPrimary(1)
Phasers.SetPosition(0.000000, 3.800000, -2.000000)
Phasers.SetPosition2D(0.000000, 0.000000)
Phasers.SetRepairComplexity(1.000000)
Phasers.SetDisabledPercentage(0.500000)
Phasers.SetRadius(0.200000)
Phasers.SetNormalPowerPerSecond(1.000000)
Phasers.SetWeaponSystemType(Phasers.WST_PHASER)
Phasers.SetSingleFire(0)
Phasers.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Phasers.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Phasers)
#################################################
PortPhaser1 = App.PhaserProperty_Create("Port Phaser 1")

PortPhaser1.SetMaxCondition(22000.000000)
PortPhaser1.SetCritical(0)
PortPhaser1.SetTargetable(1)
PortPhaser1.SetPrimary(1)
PortPhaser1.SetPosition(-0.461296, 0.218942, -0.000767)
PortPhaser1.SetPosition2D(0.000000, 0.000000)
PortPhaser1.SetRepairComplexity(1.000000)
PortPhaser1.SetDisabledPercentage(0.500000)
PortPhaser1.SetRadius(0.250000)
PortPhaser1.SetDumbfire(0)
PortPhaser1.SetWeaponID(0)
PortPhaser1.SetGroups(0)
PortPhaser1.SetDamageRadiusFactor(0.250000)
PortPhaser1.SetIconNum(364)
PortPhaser1.SetIconPositionX(35.000000)
PortPhaser1.SetIconPositionY(40.000000)
PortPhaser1.SetIconAboveShip(1)
PortPhaser1.SetFireSound("Junk Phaser")
PortPhaser1.SetMaxCharge(3.000000)
PortPhaser1.SetMaxDamage(450.000000)
PortPhaser1.SetMaxDamageDistance(100.000000)
PortPhaser1.SetMinFiringCharge(1.000000)
PortPhaser1.SetNormalDischargeRate(1.000000)
PortPhaser1.SetRechargeRate(1.000000)
PortPhaser1.SetIndicatorIconNum(510)
PortPhaser1.SetIndicatorIconPositionX(29.000000)
PortPhaser1.SetIndicatorIconPositionY(35.000000)
PortPhaser1Forward = App.TGPoint3()
PortPhaser1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
PortPhaser1Up = App.TGPoint3()
PortPhaser1Up.SetXYZ(0.000000, 0.000000, 1.000000)
PortPhaser1.SetOrientation(PortPhaser1Forward, PortPhaser1Up)
PortPhaser1.SetWidth(0.010000)
PortPhaser1.SetLength(0.010000)
PortPhaser1.SetArcWidthAngles(0.785398, -0.209440)
PortPhaser1.SetArcHeightAngles(-0.349066, 0.785398)
PortPhaser1.SetPhaserTextureStart(0)
PortPhaser1.SetPhaserTextureEnd(0)
PortPhaser1.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.501961, 0.000000, 0.501961, 1.000000)
PortPhaser1.SetOuterShellColor(kColor)
kColor.SetRGBA(0.501961, 0.501961, 1.000000, 1.000000)
PortPhaser1.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 0.000000, 1.000000)
PortPhaser1.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.501961, 0.000000, 0.501961, 1.000000)
PortPhaser1.SetInnerCoreColor(kColor)
PortPhaser1.SetNumSides(6)
PortPhaser1.SetMainRadius(0.050000)
PortPhaser1.SetTaperRadius(0.010000)
PortPhaser1.SetCoreScale(0.200000)
PortPhaser1.SetTaperRatio(0.550000)
PortPhaser1.SetTaperMinLength(5.000000)
PortPhaser1.SetTaperMaxLength(30.000000)
PortPhaser1.SetLengthTextureTilePerUnit(0.010000)
PortPhaser1.SetPerimeterTile(1.000000)
PortPhaser1.SetTextureSpeed(2.000000)
PortPhaser1.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortPhaser1)
#################################################
StarPhaser1 = App.PhaserProperty_Create("Star Phaser 1")

StarPhaser1.SetMaxCondition(22000.000000)
StarPhaser1.SetCritical(0)
StarPhaser1.SetTargetable(1)
StarPhaser1.SetPrimary(1)
StarPhaser1.SetPosition(0.463353, 0.218880, -0.000665)
StarPhaser1.SetPosition2D(0.000000, 0.000000)
StarPhaser1.SetRepairComplexity(1.000000)
StarPhaser1.SetDisabledPercentage(0.500000)
StarPhaser1.SetRadius(0.250000)
StarPhaser1.SetDumbfire(0)
StarPhaser1.SetWeaponID(0)
StarPhaser1.SetGroups(0)
StarPhaser1.SetDamageRadiusFactor(0.250000)
StarPhaser1.SetIconNum(364)
StarPhaser1.SetIconPositionX(92.000000)
StarPhaser1.SetIconPositionY(40.000000)
StarPhaser1.SetIconAboveShip(1)
StarPhaser1.SetFireSound("Junk Phaser")
StarPhaser1.SetMaxCharge(3.000000)
StarPhaser1.SetMaxDamage(450.000000)
StarPhaser1.SetMaxDamageDistance(100.000000)
StarPhaser1.SetMinFiringCharge(1.000000)
StarPhaser1.SetNormalDischargeRate(1.000000)
StarPhaser1.SetRechargeRate(1.000000)
StarPhaser1.SetIndicatorIconNum(510)
StarPhaser1.SetIndicatorIconPositionX(86.000000)
StarPhaser1.SetIndicatorIconPositionY(35.000000)
StarPhaser1Forward = App.TGPoint3()
StarPhaser1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
StarPhaser1Up = App.TGPoint3()
StarPhaser1Up.SetXYZ(0.000000, 0.000000, 1.000000)
StarPhaser1.SetOrientation(StarPhaser1Forward, StarPhaser1Up)
StarPhaser1.SetWidth(0.010000)
StarPhaser1.SetLength(0.010000)
StarPhaser1.SetArcWidthAngles(-0.785398, 0.209440)
StarPhaser1.SetArcHeightAngles(-0.349066, 0.785398)
StarPhaser1.SetPhaserTextureStart(0)
StarPhaser1.SetPhaserTextureEnd(0)
StarPhaser1.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.501961, 0.000000, 0.501961, 1.000000)
StarPhaser1.SetOuterShellColor(kColor)
kColor.SetRGBA(0.501961, 0.501961, 1.000000, 1.000000)
StarPhaser1.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 0.000000, 1.000000)
StarPhaser1.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.501961, 0.000000, 0.501961, 1.000000)
StarPhaser1.SetInnerCoreColor(kColor)
StarPhaser1.SetNumSides(6)
StarPhaser1.SetMainRadius(0.050000)
StarPhaser1.SetTaperRadius(0.010000)
StarPhaser1.SetCoreScale(0.200000)
StarPhaser1.SetTaperRatio(0.550000)
StarPhaser1.SetTaperMinLength(5.000000)
StarPhaser1.SetTaperMaxLength(30.000000)
StarPhaser1.SetLengthTextureTilePerUnit(0.010000)
StarPhaser1.SetPerimeterTile(1.000000)
StarPhaser1.SetTextureSpeed(2.000000)
StarPhaser1.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarPhaser1)
#################################################
PortPhaser2 = App.PhaserProperty_Create("Port Phaser 2")

PortPhaser2.SetMaxCondition(22000.000000)
PortPhaser2.SetCritical(0)
PortPhaser2.SetTargetable(1)
PortPhaser2.SetPrimary(1)
PortPhaser2.SetPosition(-0.462062, 0.219129, -0.042917)
PortPhaser2.SetPosition2D(0.000000, 0.000000)
PortPhaser2.SetRepairComplexity(1.000000)
PortPhaser2.SetDisabledPercentage(0.500000)
PortPhaser2.SetRadius(0.250000)
PortPhaser2.SetDumbfire(0)
PortPhaser2.SetWeaponID(0)
PortPhaser2.SetGroups(0)
PortPhaser2.SetDamageRadiusFactor(0.250000)
PortPhaser2.SetIconNum(364)
PortPhaser2.SetIconPositionX(45.000000)
PortPhaser2.SetIconPositionY(20.000000)
PortPhaser2.SetIconAboveShip(1)
PortPhaser2.SetFireSound("Junk Phaser")
PortPhaser2.SetMaxCharge(3.000000)
PortPhaser2.SetMaxDamage(450.000000)
PortPhaser2.SetMaxDamageDistance(100.000000)
PortPhaser2.SetMinFiringCharge(1.000000)
PortPhaser2.SetNormalDischargeRate(1.000000)
PortPhaser2.SetRechargeRate(1.000000)
PortPhaser2.SetIndicatorIconNum(510)
PortPhaser2.SetIndicatorIconPositionX(39.000000)
PortPhaser2.SetIndicatorIconPositionY(15.000000)
PortPhaser2Forward = App.TGPoint3()
PortPhaser2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
PortPhaser2Up = App.TGPoint3()
PortPhaser2Up.SetXYZ(0.000000, 0.000000, 1.000000)
PortPhaser2.SetOrientation(PortPhaser2Forward, PortPhaser2Up)
PortPhaser2.SetWidth(0.010000)
PortPhaser2.SetLength(0.010000)
PortPhaser2.SetArcWidthAngles(0.698132, -0.366519)
PortPhaser2.SetArcHeightAngles(-0.785398, 0.349066)
PortPhaser2.SetPhaserTextureStart(0)
PortPhaser2.SetPhaserTextureEnd(0)
PortPhaser2.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.501961, 0.000000, 0.501961, 1.000000)
PortPhaser2.SetOuterShellColor(kColor)
kColor.SetRGBA(0.501961, 0.501961, 1.000000, 1.000000)
PortPhaser2.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 0.000000, 1.000000)
PortPhaser2.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.501961, 0.000000, 0.501961, 1.000000)
PortPhaser2.SetInnerCoreColor(kColor)
PortPhaser2.SetNumSides(6)
PortPhaser2.SetMainRadius(0.050000)
PortPhaser2.SetTaperRadius(0.010000)
PortPhaser2.SetCoreScale(0.200000)
PortPhaser2.SetTaperRatio(0.550000)
PortPhaser2.SetTaperMinLength(5.000000)
PortPhaser2.SetTaperMaxLength(30.000000)
PortPhaser2.SetLengthTextureTilePerUnit(0.010000)
PortPhaser2.SetPerimeterTile(1.000000)
PortPhaser2.SetTextureSpeed(2.000000)
PortPhaser2.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortPhaser2)
#################################################
StarPhaser2 = App.PhaserProperty_Create("Star Phaser 2")

StarPhaser2.SetMaxCondition(22000.000000)
StarPhaser2.SetCritical(0)
StarPhaser2.SetTargetable(1)
StarPhaser2.SetPrimary(1)
StarPhaser2.SetPosition(0.457760, 0.219210, -0.036448)
StarPhaser2.SetPosition2D(0.000000, 0.000000)
StarPhaser2.SetRepairComplexity(1.000000)
StarPhaser2.SetDisabledPercentage(0.500000)
StarPhaser2.SetRadius(0.250000)
StarPhaser2.SetDumbfire(0)
StarPhaser2.SetWeaponID(0)
StarPhaser2.SetGroups(0)
StarPhaser2.SetDamageRadiusFactor(0.250000)
StarPhaser2.SetIconNum(364)
StarPhaser2.SetIconPositionX(82.000000)
StarPhaser2.SetIconPositionY(20.000000)
StarPhaser2.SetIconAboveShip(1)
StarPhaser2.SetFireSound("Junk Phaser")
StarPhaser2.SetMaxCharge(3.000000)
StarPhaser2.SetMaxDamage(450.000000)
StarPhaser2.SetMaxDamageDistance(100.000000)
StarPhaser2.SetMinFiringCharge(1.000000)
StarPhaser2.SetNormalDischargeRate(1.000000)
StarPhaser2.SetRechargeRate(1.000000)
StarPhaser2.SetIndicatorIconNum(510)
StarPhaser2.SetIndicatorIconPositionX(76.000000)
StarPhaser2.SetIndicatorIconPositionY(15.000000)
StarPhaser2Forward = App.TGPoint3()
StarPhaser2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
StarPhaser2Up = App.TGPoint3()
StarPhaser2Up.SetXYZ(0.000000, 0.000000, 1.000000)
StarPhaser2.SetOrientation(StarPhaser2Forward, StarPhaser2Up)
StarPhaser2.SetWidth(0.010000)
StarPhaser2.SetLength(0.010000)
StarPhaser2.SetArcWidthAngles(0.349066, -0.698132)
StarPhaser2.SetArcHeightAngles(-0.785398, 0.349066)
StarPhaser2.SetPhaserTextureStart(0)
StarPhaser2.SetPhaserTextureEnd(0)
StarPhaser2.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.501961, 0.000000, 0.501961, 1.000000)
StarPhaser2.SetOuterShellColor(kColor)
kColor.SetRGBA(0.501961, 0.501961, 1.000000, 1.000000)
StarPhaser2.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 0.000000, 1.000000)
StarPhaser2.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.501961, 0.000000, 0.501961, 1.000000)
StarPhaser2.SetInnerCoreColor(kColor)
StarPhaser2.SetNumSides(6)
StarPhaser2.SetMainRadius(0.050000)
StarPhaser2.SetTaperRadius(0.010000)
StarPhaser2.SetCoreScale(0.200000)
StarPhaser2.SetTaperRatio(0.550000)
StarPhaser2.SetTaperMinLength(5.000000)
StarPhaser2.SetTaperMaxLength(30.000000)
StarPhaser2.SetLengthTextureTilePerUnit(0.010000)
StarPhaser2.SetPerimeterTile(1.000000)
StarPhaser2.SetTextureSpeed(2.000000)
StarPhaser2.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarPhaser2)
#################################################
FwdTorpedo2 = App.TorpedoTubeProperty_Create("Fwd Torpedo 2")

FwdTorpedo2.SetMaxCondition(12500.000000)
FwdTorpedo2.SetCritical(0)
FwdTorpedo2.SetTargetable(1)
FwdTorpedo2.SetPrimary(0)
FwdTorpedo2.SetPosition(0.000000, 4.700000, 0.200000)
FwdTorpedo2.SetPosition2D(57.000000, 13.000000)
FwdTorpedo2.SetRepairComplexity(3.000000)
FwdTorpedo2.SetDisabledPercentage(0.750000)
FwdTorpedo2.SetRadius(0.100000)
FwdTorpedo2.SetDumbfire(1)
FwdTorpedo2.SetWeaponID(0)
FwdTorpedo2.SetGroups(1)
FwdTorpedo2.SetDamageRadiusFactor(0.200000)
FwdTorpedo2.SetIconNum(370)
FwdTorpedo2.SetIconPositionX(81.000000)
FwdTorpedo2.SetIconPositionY(35.000000)
FwdTorpedo2.SetIconAboveShip(1)
FwdTorpedo2.SetImmediateDelay(0.000000)
FwdTorpedo2.SetReloadDelay(30.000000)
FwdTorpedo2.SetMaxReady(1)
FwdTorpedo2Direction = App.TGPoint3()
FwdTorpedo2Direction.SetXYZ(0.000000, 1.000000, 0.000000)
FwdTorpedo2.SetDirection(FwdTorpedo2Direction)
FwdTorpedo2Right = App.TGPoint3()
FwdTorpedo2Right.SetXYZ(1.000000, 0.000000, 0.000000)
FwdTorpedo2.SetRight(FwdTorpedo2Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(FwdTorpedo2)
#################################################
AftPhaser = App.PhaserProperty_Create("Aft Phaser")

AftPhaser.SetMaxCondition(22000.000000)
AftPhaser.SetCritical(0)
AftPhaser.SetTargetable(1)
AftPhaser.SetPrimary(1)
AftPhaser.SetPosition(-0.000283, -0.494453, 0.038488)
AftPhaser.SetPosition2D(0.000000, 0.000000)
AftPhaser.SetRepairComplexity(1.000000)
AftPhaser.SetDisabledPercentage(0.500000)
AftPhaser.SetRadius(0.250000)
AftPhaser.SetDumbfire(0)
AftPhaser.SetWeaponID(0)
AftPhaser.SetGroups(0)
AftPhaser.SetDamageRadiusFactor(0.250000)
AftPhaser.SetIconNum(363)
AftPhaser.SetIconPositionX(63.000000)
AftPhaser.SetIconPositionY(118.000000)
AftPhaser.SetIconAboveShip(1)
AftPhaser.SetFireSound("Junk Phaser")
AftPhaser.SetMaxCharge(3.000000)
AftPhaser.SetMaxDamage(450.000000)
AftPhaser.SetMaxDamageDistance(100.000000)
AftPhaser.SetMinFiringCharge(1.000000)
AftPhaser.SetNormalDischargeRate(1.000000)
AftPhaser.SetRechargeRate(1.000000)
AftPhaser.SetIndicatorIconNum(511)
AftPhaser.SetIndicatorIconPositionX(58.000000)
AftPhaser.SetIndicatorIconPositionY(118.000000)
AftPhaserForward = App.TGPoint3()
AftPhaserForward.SetXYZ(-0.085724, -0.950244, -0.299479)
AftPhaserUp = App.TGPoint3()
AftPhaserUp.SetXYZ(0.000000, 0.000000, 1.000000)
AftPhaser.SetOrientation(AftPhaserForward, AftPhaserUp)
AftPhaser.SetWidth(0.010000)
AftPhaser.SetLength(0.010000)
AftPhaser.SetArcWidthAngles(1.396263, -1.396263)
AftPhaser.SetArcHeightAngles(0.349066, 1.745329)
AftPhaser.SetPhaserTextureStart(0)
AftPhaser.SetPhaserTextureEnd(0)
AftPhaser.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.501961, 0.000000, 0.501961, 1.000000)
AftPhaser.SetOuterShellColor(kColor)
kColor.SetRGBA(0.501961, 0.501961, 1.000000, 1.000000)
AftPhaser.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 0.000000, 1.000000)
AftPhaser.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.501961, 0.000000, 0.501961, 1.000000)
AftPhaser.SetInnerCoreColor(kColor)
AftPhaser.SetNumSides(6)
AftPhaser.SetMainRadius(0.050000)
AftPhaser.SetTaperRadius(0.010000)
AftPhaser.SetCoreScale(0.200000)
AftPhaser.SetTaperRatio(0.550000)
AftPhaser.SetTaperMinLength(5.000000)
AftPhaser.SetTaperMaxLength(30.000000)
AftPhaser.SetLengthTextureTilePerUnit(0.010000)
AftPhaser.SetPerimeterTile(1.000000)
AftPhaser.SetTextureSpeed(2.000000)
AftPhaser.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(AftPhaser)
#################################################
Engine1 = App.EngineProperty_Create("Engine 1")

Engine1.SetMaxCondition(8500.000000)
Engine1.SetCritical(0)
Engine1.SetTargetable(1)
Engine1.SetPrimary(1)
Engine1.SetPosition(-2.700000, -3.000000, 1.000000)
Engine1.SetPosition2D(34.000000, 84.000000)
Engine1.SetRepairComplexity(3.000000)
Engine1.SetDisabledPercentage(0.500000)
Engine1.SetRadius(0.500000)
Engine1.SetEngineType(Engine1.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine1)
#################################################
Engine2 = App.EngineProperty_Create("Engine 2")

Engine2.SetMaxCondition(8500.000000)
Engine2.SetCritical(0)
Engine2.SetTargetable(1)
Engine2.SetPrimary(1)
Engine2.SetPosition(-0.800000, -3.000000, 1.000000)
Engine2.SetPosition2D(34.000000, 84.000000)
Engine2.SetRepairComplexity(3.000000)
Engine2.SetDisabledPercentage(0.500000)
Engine2.SetRadius(0.500000)
Engine2.SetEngineType(Engine2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine2)
#################################################
Engine3 = App.EngineProperty_Create("Engine 3")

Engine3.SetMaxCondition(8500.000000)
Engine3.SetCritical(0)
Engine3.SetTargetable(1)
Engine3.SetPrimary(1)
Engine3.SetPosition(0.800000, -3.000000, 1.000000)
Engine3.SetPosition2D(34.000000, 84.000000)
Engine3.SetRepairComplexity(3.000000)
Engine3.SetDisabledPercentage(0.500000)
Engine3.SetRadius(0.500000)
Engine3.SetEngineType(Engine3.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine3)
#################################################
Engine4 = App.EngineProperty_Create("Engine 4")

Engine4.SetMaxCondition(8500.000000)
Engine4.SetCritical(0)
Engine4.SetTargetable(1)
Engine4.SetPrimary(1)
Engine4.SetPosition(2.700000, -3.000000, 1.000000)
Engine4.SetPosition2D(34.000000, 84.000000)
Engine4.SetRepairComplexity(3.000000)
Engine4.SetDisabledPercentage(0.500000)
Engine4.SetRadius(0.500000)
Engine4.SetEngineType(Engine4.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine4)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fwd Torpedo 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Repair System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Junk", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Phasers", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Phaser 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Phaser 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Phaser 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Phaser 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fwd Torpedo 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Aft Phaser", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 4", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
