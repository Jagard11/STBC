# C:\J-Single-testing-KM1\scripts\ships\Hardpoints\VentureScout.py
# This file was automatically generated - modify at your own risk.
# PulsePhaser in place as instructed

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(2900.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(61.000000, 52.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.085000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(1000.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, 0.000000, 0.000000)
ImpulseEngines.SetPosition2D(123.000000, 48.000000)
ImpulseEngines.SetRepairComplexity(2.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.003000)
ImpulseEngines.SetNormalPowerPerSecond(5.000000)
ImpulseEngines.SetMaxAccel(4.000000)
ImpulseEngines.SetMaxAngularAccel(1.000000)
ImpulseEngines.SetMaxAngularVelocity(1.000000)
ImpulseEngines.SetMaxSpeed(9.500000)
ImpulseEngines.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(1000.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(-0.000795, -0.028776, 0.022000)
WarpCore.SetPosition2D(121.000000, 30.000000)
WarpCore.SetRepairComplexity(1.000000)
WarpCore.SetDisabledPercentage(0.500000)
WarpCore.SetRadius(0.010000)
WarpCore.SetMainBatteryLimit(50000.000000)
WarpCore.SetBackupBatteryLimit(200000.000000)
WarpCore.SetMainConduitCapacity(900.000000)
WarpCore.SetBackupConduitCapacity(100.000000)
WarpCore.SetPowerOutput(800.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")

RepairSystem.SetMaxCondition(200.000000)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(1)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(0.000000, 0.000000, 0.000000)
RepairSystem.SetPosition2D(0.000000, 0.000000)
RepairSystem.SetRepairComplexity(1.000000)
RepairSystem.SetDisabledPercentage(0.500000)
RepairSystem.SetRadius(0.250000)
RepairSystem.SetNormalPowerPerSecond(1.000000)
RepairSystem.SetMaxRepairPoints(15.000000)
RepairSystem.SetNumRepairTeams(3)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(1400.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.097389, 0.000564)
SensorArray.SetPosition2D(122.000000, -1.000000)
SensorArray.SetRepairComplexity(0.400000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.003000)
SensorArray.SetNormalPowerPerSecond(5.000000)
SensorArray.SetBaseSensorRange(3000.000000)
SensorArray.SetMaxProbes(4)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(2600.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(-0.000306, 0.026120, 0.025224)
ShieldGenerator.SetPosition2D(99.000000, 7.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.003000)
ShieldGenerator.SetNormalPowerPerSecond(10.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.203922, 0.631373, 1.000000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 3500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 3500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 3500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 3500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 3500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 3500.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 10.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 10.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 10.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 10.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 10.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 10.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
Phasers = App.WeaponSystemProperty_Create("Phasers")

Phasers.SetMaxCondition(800.000000)
Phasers.SetCritical(0)
Phasers.SetTargetable(0)
Phasers.SetPrimary(1)
Phasers.SetPosition(0.000175, 0.015236, -0.000475)
Phasers.SetPosition2D(-1.000000, 19.000000)
Phasers.SetRepairComplexity(3.000000)
Phasers.SetDisabledPercentage(0.750000)
Phasers.SetRadius(0.002500)
Phasers.SetNormalPowerPerSecond(10.000000)
Phasers.SetWeaponSystemType(Phasers.WST_PHASER)
Phasers.SetSingleFire(0)
Phasers.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Phasers.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Phasers)
#################################################
PortPhaser = App.PhaserProperty_Create("Port Phaser")

PortPhaser.SetMaxCondition(800.000000)
PortPhaser.SetCritical(0)
PortPhaser.SetTargetable(1)
PortPhaser.SetPrimary(1)
PortPhaser.SetPosition(-0.007939, 0.119809, -0.003680)
PortPhaser.SetPosition2D(5.000000, 30.000000)
PortPhaser.SetRepairComplexity(3.000000)
PortPhaser.SetDisabledPercentage(0.750000)
PortPhaser.SetRadius(0.034000)
PortPhaser.SetDumbfire(0)
PortPhaser.SetWeaponID(1)
PortPhaser.SetGroups(1)
PortPhaser.SetDamageRadiusFactor(0.100000)
PortPhaser.SetIconNum(364)
PortPhaser.SetIconPositionX(42.000000)
PortPhaser.SetIconPositionY(45.000000)
PortPhaser.SetIconAboveShip(1)
PortPhaser.SetFireSound("FedLight")
PortPhaser.SetMaxCharge(3.000000)
PortPhaser.SetMaxDamage(700.000000)
PortPhaser.SetMaxDamageDistance(65.000000)
PortPhaser.SetMinFiringCharge(1.000000)
PortPhaser.SetNormalDischargeRate(1.000000)
PortPhaser.SetRechargeRate(1.000000)
PortPhaser.SetIndicatorIconNum(510)
PortPhaser.SetIndicatorIconPositionX(36.000000)
PortPhaser.SetIndicatorIconPositionY(41.000000)
PortPhaserForward = App.TGPoint3()
PortPhaserForward.SetXYZ(0.000000, 1.000000, 0.000000)
PortPhaserUp = App.TGPoint3()
PortPhaserUp.SetXYZ(0.000000, 0.000000, 1.000000)
PortPhaser.SetOrientation(PortPhaserForward, PortPhaserUp)
PortPhaser.SetWidth(0.001000)
PortPhaser.SetLength(0.001000)
PortPhaser.SetArcWidthAngles(-0.214676, 0.698132)
PortPhaser.SetArcHeightAngles(-0.523599, 0.523599)
PortPhaser.SetPhaserTextureStart(0)
PortPhaser.SetPhaserTextureEnd(7)
PortPhaser.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
PortPhaser.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
PortPhaser.SetInnerShellColor(kColor)
kColor.SetRGBA(0.992157, 0.831373, 0.639216, 1.000000)
PortPhaser.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.992157, 0.901961, 0.858824, 1.000000)
PortPhaser.SetInnerCoreColor(kColor)
PortPhaser.SetNumSides(6)
PortPhaser.SetMainRadius(0.020000)
PortPhaser.SetTaperRadius(0.001000)
PortPhaser.SetCoreScale(0.500000)
PortPhaser.SetTaperRatio(0.250000)
PortPhaser.SetTaperMinLength(5.000000)
PortPhaser.SetTaperMaxLength(30.000000)
PortPhaser.SetLengthTextureTilePerUnit(0.500000)
PortPhaser.SetPerimeterTile(1.000000)
PortPhaser.SetTextureSpeed(2.500000)
PortPhaser.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortPhaser)
#################################################
PortImpulse = App.EngineProperty_Create("Port Impulse")

PortImpulse.SetMaxCondition(1100.000000)
PortImpulse.SetCritical(0)
PortImpulse.SetTargetable(1)
PortImpulse.SetPrimary(1)
PortImpulse.SetPosition(-0.015556, -0.109293, 0.006246)
PortImpulse.SetPosition2D(115.000000, 58.000000)
PortImpulse.SetRepairComplexity(1.000000)
PortImpulse.SetDisabledPercentage(0.500000)
PortImpulse.SetRadius(0.004000)
PortImpulse.SetEngineType(PortImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortImpulse)
#################################################
StarImpulse = App.EngineProperty_Create("Star Impulse")

StarImpulse.SetMaxCondition(1100.000000)
StarImpulse.SetCritical(0)
StarImpulse.SetTargetable(1)
StarImpulse.SetPrimary(1)
StarImpulse.SetPosition(0.017037, -0.109145, 0.006269)
StarImpulse.SetPosition2D(131.000000, 58.000000)
StarImpulse.SetRepairComplexity(1.000000)
StarImpulse.SetDisabledPercentage(0.500000)
StarImpulse.SetRadius(0.004000)
StarImpulse.SetEngineType(StarImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarImpulse)
#################################################
VentureScout = App.ShipProperty_Create("VentureScout")

VentureScout.SetGenus(1)
VentureScout.SetSpecies(139)
VentureScout.SetMass(15.000000)
VentureScout.SetRotationalInertia(2000.000000)
VentureScout.SetShipName("VentureScout")
VentureScout.SetModelFilename("data/Models/Ships/VentureScout.nif")
VentureScout.SetDamageResolution(1.000000)
VentureScout.SetAffiliation(10)
VentureScout.SetStationary(0)
VentureScout.SetAIString("FedAttack")
VentureScout.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(VentureScout)
#################################################
Repair = App.RepairSubsystemProperty_Create("Repair")

Repair.SetMaxCondition(200.000000)
Repair.SetCritical(0)
Repair.SetTargetable(0)
Repair.SetPrimary(1)
Repair.SetPosition(0.000000, -0.018206, -0.023286)
Repair.SetPosition2D(96.000000, 29.000000)
Repair.SetRepairComplexity(4.000000)
Repair.SetDisabledPercentage(0.100000)
Repair.SetRadius(0.010000)
Repair.SetNormalPowerPerSecond(1.000000)
Repair.SetMaxRepairPoints(2.000000)
Repair.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Repair)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(1600.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.000000, 0.000000, -0.020000)
WarpEngines.SetPosition2D(126.000000, 87.000000)
WarpEngines.SetRepairComplexity(1.000000)
WarpEngines.SetDisabledPercentage(0.500000)
WarpEngines.SetRadius(0.010000)
WarpEngines.SetNormalPowerPerSecond(1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
PortWarp = App.EngineProperty_Create("Port Warp")

PortWarp.SetMaxCondition(800.000000)
PortWarp.SetCritical(0)
PortWarp.SetTargetable(1)
PortWarp.SetPrimary(1)
PortWarp.SetPosition(-0.041465, -0.082729, -0.006779)
PortWarp.SetPosition2D(120.000000, 101.000000)
PortWarp.SetRepairComplexity(1.000000)
PortWarp.SetDisabledPercentage(0.500000)
PortWarp.SetRadius(0.004000)
PortWarp.SetEngineType(PortWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortWarp)
#################################################
StarWarp = App.EngineProperty_Create("Star Warp")

StarWarp.SetMaxCondition(800.000000)
StarWarp.SetCritical(0)
StarWarp.SetTargetable(1)
StarWarp.SetPrimary(1)
StarWarp.SetPosition(0.041409, -0.082937, -0.006334)
StarWarp.SetPosition2D(132.000000, 100.000000)
StarWarp.SetRepairComplexity(1.000000)
StarWarp.SetDisabledPercentage(0.500000)
StarWarp.SetRadius(0.004000)
StarWarp.SetEngineType(StarWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 0.110000, 0.020000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.120000, 0.020000)
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
ViewscreenLeftPosition.SetXYZ(-0.060000, 0.060000, 0.020000)
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
ViewscreenRightPosition.SetXYZ(0.060000, 0.060000, 0.020000)
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
ViewscreenUpPosition.SetXYZ(0.000000, 0.080000, 0.040000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.080000, -0.030000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 0.110000, 0.020000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
StarPhaser = App.PhaserProperty_Create("Star Phaser")

StarPhaser.SetMaxCondition(800.000000)
StarPhaser.SetCritical(0)
StarPhaser.SetTargetable(1)
StarPhaser.SetPrimary(1)
StarPhaser.SetPosition(0.008178, 0.119830, -0.003583)
StarPhaser.SetPosition2D(10.000000, 30.000000)
StarPhaser.SetRepairComplexity(3.000000)
StarPhaser.SetDisabledPercentage(0.750000)
StarPhaser.SetRadius(0.034000)
StarPhaser.SetDumbfire(0)
StarPhaser.SetWeaponID(1)
StarPhaser.SetGroups(1)
StarPhaser.SetDamageRadiusFactor(0.100000)
StarPhaser.SetIconNum(364)
StarPhaser.SetIconPositionX(82.000000)
StarPhaser.SetIconPositionY(45.000000)
StarPhaser.SetIconAboveShip(1)
StarPhaser.SetFireSound("FedLight")
StarPhaser.SetMaxCharge(3.000000)
StarPhaser.SetMaxDamage(700.000000)
StarPhaser.SetMaxDamageDistance(65.000000)
StarPhaser.SetMinFiringCharge(1.000000)
StarPhaser.SetNormalDischargeRate(1.000000)
StarPhaser.SetRechargeRate(1.000000)
StarPhaser.SetIndicatorIconNum(510)
StarPhaser.SetIndicatorIconPositionX(76.000000)
StarPhaser.SetIndicatorIconPositionY(41.000000)
StarPhaserForward = App.TGPoint3()
StarPhaserForward.SetXYZ(0.000000, 1.000000, 0.000000)
StarPhaserUp = App.TGPoint3()
StarPhaserUp.SetXYZ(0.000000, 0.000000, 1.000000)
StarPhaser.SetOrientation(StarPhaserForward, StarPhaserUp)
StarPhaser.SetWidth(0.001000)
StarPhaser.SetLength(0.001000)
StarPhaser.SetArcWidthAngles(-0.698132, 0.212930)
StarPhaser.SetArcHeightAngles(-0.523599, 0.523599)
StarPhaser.SetPhaserTextureStart(0)
StarPhaser.SetPhaserTextureEnd(7)
StarPhaser.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
StarPhaser.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
StarPhaser.SetInnerShellColor(kColor)
kColor.SetRGBA(0.992157, 0.831373, 0.639216, 1.000000)
StarPhaser.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.992157, 0.901961, 0.858824, 1.000000)
StarPhaser.SetInnerCoreColor(kColor)
StarPhaser.SetNumSides(6)
StarPhaser.SetMainRadius(0.020000)
StarPhaser.SetTaperRadius(0.001000)
StarPhaser.SetCoreScale(0.500000)
StarPhaser.SetTaperRatio(0.250000)
StarPhaser.SetTaperMinLength(5.000000)
StarPhaser.SetTaperMaxLength(30.000000)
StarPhaser.SetLengthTextureTilePerUnit(0.500000)
StarPhaser.SetPerimeterTile(1.000000)
StarPhaser.SetTextureSpeed(2.500000)
StarPhaser.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarPhaser)
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")

Torpedoes.SetMaxCondition(1000.000000)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(0)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.000000, 0.000000, 0.000000)
Torpedoes.SetPosition2D(5.000000, 103.000000)
Torpedoes.SetRepairComplexity(1.000000)
Torpedoes.SetDisabledPercentage(0.500000)
Torpedoes.SetRadius(0.010000)
Torpedoes.SetNormalPowerPerSecond(5.000000)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(1)
Torpedoes.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 10)
Torpedoes.SetTorpedoScript(0, "Tactical.Projectiles.PhotonTorpedo")
Torpedoes.SetMaxTorpedoes(1, 5)
Torpedoes.SetTorpedoScript(1, "Tactical.Projectiles.CATachyon")
Torpedoes.SetNumAmmoTypes(2)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
#################################################
StarTorpedo = App.TorpedoTubeProperty_Create("Star Torpedo")

StarTorpedo.SetMaxCondition(700.000000)
StarTorpedo.SetCritical(0)
StarTorpedo.SetTargetable(1)
StarTorpedo.SetPrimary(1)
StarTorpedo.SetPosition(0.034338, 0.049125, -0.004533)
StarTorpedo.SetPosition2D(17.000000, 117.000000)
StarTorpedo.SetRepairComplexity(1.000000)
StarTorpedo.SetDisabledPercentage(0.700000)
StarTorpedo.SetRadius(0.250000)
StarTorpedo.SetDumbfire(1)
StarTorpedo.SetWeaponID(0)
StarTorpedo.SetGroups(1)
StarTorpedo.SetDamageRadiusFactor(0.600000)
StarTorpedo.SetIconNum(370)
StarTorpedo.SetIconPositionX(83.000000)
StarTorpedo.SetIconPositionY(40.000000)
StarTorpedo.SetIconAboveShip(1)
StarTorpedo.SetImmediateDelay(0.250000)
StarTorpedo.SetReloadDelay(5.000000)
StarTorpedo.SetMaxReady(1)
StarTorpedoDirection = App.TGPoint3()
StarTorpedoDirection.SetXYZ(0.000000, 1.000000, 0.000000)
StarTorpedo.SetDirection(StarTorpedoDirection)
StarTorpedoRight = App.TGPoint3()
StarTorpedoRight.SetXYZ(1.000000, 0.000000, 0.000000)
StarTorpedo.SetRight(StarTorpedoRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarTorpedo)
#################################################
PortTorpedo = App.TorpedoTubeProperty_Create("Port Torpedo")

PortTorpedo.SetMaxCondition(700.000000)
PortTorpedo.SetCritical(0)
PortTorpedo.SetTargetable(1)
PortTorpedo.SetPrimary(1)
PortTorpedo.SetPosition(-0.034338, 0.049125, -0.004533)
PortTorpedo.SetPosition2D(-4.000000, 117.000000)
PortTorpedo.SetRepairComplexity(1.000000)
PortTorpedo.SetDisabledPercentage(0.700000)
PortTorpedo.SetRadius(0.250000)
PortTorpedo.SetDumbfire(1)
PortTorpedo.SetWeaponID(0)
PortTorpedo.SetGroups(1)
PortTorpedo.SetDamageRadiusFactor(0.600000)
PortTorpedo.SetIconNum(370)
PortTorpedo.SetIconPositionX(67.000000)
PortTorpedo.SetIconPositionY(40.000000)
PortTorpedo.SetIconAboveShip(1)
PortTorpedo.SetImmediateDelay(0.250000)
PortTorpedo.SetReloadDelay(5.000000)
PortTorpedo.SetMaxReady(1)
PortTorpedoDirection = App.TGPoint3()
PortTorpedoDirection.SetXYZ(0.000000, 1.000000, 0.000000)
PortTorpedo.SetDirection(PortTorpedoDirection)
PortTorpedoRight = App.TGPoint3()
PortTorpedoRight.SetXYZ(1.000000, 0.000000, 0.000000)
PortTorpedo.SetRight(PortTorpedoRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortTorpedo)
#################################################
portimpulse2 = App.EngineProperty_Create("port impulse 2")

portimpulse2.SetMaxCondition(1100.000000)
portimpulse2.SetCritical(0)
portimpulse2.SetTargetable(1)
portimpulse2.SetPrimary(1)
portimpulse2.SetPosition(-0.017704, -0.109553, -0.006381)
portimpulse2.SetPosition2D(115.000000, 74.000000)
portimpulse2.SetRepairComplexity(1.000000)
portimpulse2.SetDisabledPercentage(0.500000)
portimpulse2.SetRadius(0.004000)
portimpulse2.SetEngineType(portimpulse2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(portimpulse2)
#################################################
starimpulse2 = App.EngineProperty_Create("star impulse 2")

starimpulse2.SetMaxCondition(1100.000000)
starimpulse2.SetCritical(0)
starimpulse2.SetTargetable(1)
starimpulse2.SetPrimary(1)
starimpulse2.SetPosition(0.018106, -0.109855, -0.006289)
starimpulse2.SetPosition2D(131.000000, 74.000000)
starimpulse2.SetRepairComplexity(1.000000)
starimpulse2.SetDisabledPercentage(0.500000)
starimpulse2.SetRadius(0.004000)
starimpulse2.SetEngineType(starimpulse2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(starimpulse2)
#################################################
PulsePhasers = App.WeaponSystemProperty_Create("Pulse Phasers")

PulsePhasers.SetMaxCondition(3000.000000)
PulsePhasers.SetCritical(0)
PulsePhasers.SetTargetable(0)
PulsePhasers.SetPrimary(1)
PulsePhasers.SetPosition(-0.006878, 0.044448, 0.015922)
PulsePhasers.SetPosition2D(64.000000, 44.000000)
PulsePhasers.SetRepairComplexity(9.000000)
PulsePhasers.SetDisabledPercentage(0.750000)
PulsePhasers.SetRadius(0.003000)
PulsePhasers.SetNormalPowerPerSecond(80.000000)
PulsePhasers.SetWeaponSystemType(PulsePhasers.WST_PULSE)
PulsePhasers.SetSingleFire(0)
PulsePhasers.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
PulsePhasers.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(PulsePhasers)
#################################################
PortCannon1 = App.PulseWeaponProperty_Create("Port Cannon 1")

PortCannon1.SetMaxCondition(2000.000000)
PortCannon1.SetCritical(0)
PortCannon1.SetTargetable(1)
PortCannon1.SetPrimary(1)
PortCannon1.SetPosition(-0.046928, 0.003680, -0.013379)
PortCannon1.SetPosition2D(35.000000, 20.000000)
PortCannon1.SetRepairComplexity(4.000000)
PortCannon1.SetDisabledPercentage(0.750000)
PortCannon1.SetRadius(0.020000)
PortCannon1.SetDumbfire(1)
PortCannon1.SetWeaponID(2)
PortCannon1.SetGroups(1)
PortCannon1.SetDamageRadiusFactor(0.100000)
PortCannon1.SetIconNum(365)
PortCannon1.SetIconPositionX(54.000000)
PortCannon1.SetIconPositionY(55.000000)
PortCannon1.SetIconAboveShip(1)
PortCannon1.SetFireSound("Klingon Disruptor")
PortCannon1.SetMaxCharge(4.000000)
PortCannon1.SetMaxDamage(200.000000)
PortCannon1.SetMaxDamageDistance(150.000000)
PortCannon1.SetMinFiringCharge(3.000000)
PortCannon1.SetNormalDischargeRate(1.000000)
PortCannon1.SetRechargeRate(0.750000)
PortCannon1.SetIndicatorIconNum(365)
PortCannon1.SetIndicatorIconPositionX(54.000000)
PortCannon1.SetIndicatorIconPositionY(55.000000)
PortCannon1Forward = App.TGPoint3()
PortCannon1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
PortCannon1Up = App.TGPoint3()
PortCannon1Up.SetXYZ(0.000000, 0.000000, 1.000000)
PortCannon1.SetOrientation(PortCannon1Forward, PortCannon1Up)
PortCannon1.SetArcWidthAngles(-0.261799, 0.349066)
PortCannon1.SetArcHeightAngles(-0.261799, 0.314159)
PortCannon1.SetCooldownTime(0.000100)
PortCannon1.SetModuleName("Tactical.Projectiles.PulsePhaser")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortCannon1)
#################################################
StarCannon2 = App.PulseWeaponProperty_Create("Star Cannon 2")

StarCannon2.SetMaxCondition(2000.000000)
StarCannon2.SetCritical(0)
StarCannon2.SetTargetable(1)
StarCannon2.SetPrimary(1)
StarCannon2.SetPosition(0.047337, 0.003408, -0.013413)
StarCannon2.SetPosition2D(110.000000, 40.000000)
StarCannon2.SetRepairComplexity(4.000000)
StarCannon2.SetDisabledPercentage(0.750000)
StarCannon2.SetRadius(0.020000)
StarCannon2.SetDumbfire(1)
StarCannon2.SetWeaponID(2)
StarCannon2.SetGroups(1)
StarCannon2.SetDamageRadiusFactor(0.100000)
StarCannon2.SetIconNum(365)
StarCannon2.SetIconPositionX(95.000000)
StarCannon2.SetIconPositionY(55.000000)
StarCannon2.SetIconAboveShip(1)
StarCannon2.SetFireSound("Klingon Disruptor")
StarCannon2.SetMaxCharge(4.000000)
StarCannon2.SetMaxDamage(200.000000)
StarCannon2.SetMaxDamageDistance(150.000000)
StarCannon2.SetMinFiringCharge(3.000000)
StarCannon2.SetNormalDischargeRate(1.000000)
StarCannon2.SetRechargeRate(0.750000)
StarCannon2.SetIndicatorIconNum(365)
StarCannon2.SetIndicatorIconPositionX(95.000000)
StarCannon2.SetIndicatorIconPositionY(55.000000)
StarCannon2Forward = App.TGPoint3()
StarCannon2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
StarCannon2Up = App.TGPoint3()
StarCannon2Up.SetXYZ(0.000000, 0.000000, 1.000000)
StarCannon2.SetOrientation(StarCannon2Forward, StarCannon2Up)
StarCannon2.SetArcWidthAngles(-0.436332, 0.349066)
StarCannon2.SetArcHeightAngles(-0.436332, 0.314159)
StarCannon2.SetCooldownTime(0.000100)
StarCannon2.SetModuleName("Tactical.Projectiles.PulsePhaser")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarCannon2)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Phasers", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Port Phaser", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Phaser", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("VentureScout", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Torpedo", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Torpedo", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("port impulse 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("star impulse 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Pulse Phasers", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Cannon 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Cannon 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)