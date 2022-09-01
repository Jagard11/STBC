# C:\Program Files\Activision\Bridge Commander\scripts\ships\Hardpoints\ReplicatorBeliskner.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
PortEngine = App.EngineProperty_Create("Port Engine")

PortEngine.SetMaxCondition(4000.000000)
PortEngine.SetCritical(0)
PortEngine.SetTargetable(1)
PortEngine.SetPrimary(1)
PortEngine.SetPosition(-0.420000, -3.250000, -0.150000)
PortEngine.SetPosition2D(55, 95)
PortEngine.SetRepairComplexity(3.000000)
PortEngine.SetDisabledPercentage(0.500000)
PortEngine.SetRadius(0.170000)
PortEngine.SetEngineType(PortEngine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortEngine)
#################################################
Beliskner = App.ShipProperty_Create("Beliskner")

Beliskner.SetGenus(1)
Beliskner.SetSpecies(767)
Beliskner.SetMass(20000.000000)
Beliskner.SetRotationalInertia(300.000000)
Beliskner.SetShipName("Beliskner")
Beliskner.SetModelFilename("data/Models/Ships/Beliskner/Beliskner.nif")
Beliskner.SetDamageResolution(0.000100)
Beliskner.SetAffiliation(0)
Beliskner.SetStationary(0)
Beliskner.SetAIString("NonFedAttack")
Beliskner.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Beliskner)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(7000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.950000, 0.000000)
ShieldGenerator.SetPosition2D(65, 57)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.300000)
ShieldGenerator.SetNormalPowerPerSecond(1200.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(1.000000, 0.647059, 0.192157, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 75000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 75000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 75000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 75000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 75000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 75000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 30.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 30.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 30.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 30.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 30.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 30.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(20000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(0)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(3.000000, 4.000000)
Hull.SetRepairComplexity(3.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.050000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(5000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 2.500000, -0.050000)
SensorArray.SetPosition2D(65, 12)
SensorArray.SetRepairComplexity(2.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.200000)
SensorArray.SetNormalPowerPerSecond(100.000000)
SensorArray.SetBaseSensorRange(900.000000)
SensorArray.SetMaxProbes(6)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
PowerGenerators = App.PowerProperty_Create("Power Generators")

PowerGenerators.SetMaxCondition(18500.000000)
PowerGenerators.SetCritical(1)
PowerGenerators.SetTargetable(1)
PowerGenerators.SetPrimary(1)
PowerGenerators.SetPosition(0.000000, -0.350000, -0.200000)
PowerGenerators.SetPosition2D(65, 43)
PowerGenerators.SetRepairComplexity(3.000000)
PowerGenerators.SetDisabledPercentage(0.500000)
PowerGenerators.SetRadius(0.300000)
PowerGenerators.SetMainBatteryLimit(2000000.000000)
PowerGenerators.SetBackupBatteryLimit(100000.000000)
PowerGenerators.SetMainConduitCapacity(2500.000000)
PowerGenerators.SetBackupConduitCapacity(500.000000)
PowerGenerators.SetPowerOutput(2000.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerGenerators)
#################################################
SublightEngines = App.ImpulseEngineProperty_Create("Sublight Engines")

SublightEngines.SetMaxCondition(10000.000000)
SublightEngines.SetCritical(0)
SublightEngines.SetTargetable(0)
SublightEngines.SetPrimary(1)
SublightEngines.SetPosition(0.000000, 0.000000, 0.000000)
SublightEngines.SetPosition2D(64.000000, 104.000000)
SublightEngines.SetRepairComplexity(4.000000)
SublightEngines.SetDisabledPercentage(0.500000)
SublightEngines.SetRadius(0.100000)
SublightEngines.SetNormalPowerPerSecond(300.000000)
SublightEngines.SetMaxAccel(5.600000)
SublightEngines.SetMaxAngularAccel(0.500000)
SublightEngines.SetMaxAngularVelocity(0.500000)
SublightEngines.SetMaxSpeed(6.000000)
SublightEngines.SetEngineSound("Klingon Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightEngines)
#################################################
Hyperdrive1 = App.HullProperty_Create("Hyperdrive 1")

Hyperdrive1.SetMaxCondition(5000.000000)
Hyperdrive1.SetCritical(0)
Hyperdrive1.SetTargetable(1)
Hyperdrive1.SetPrimary(0)
Hyperdrive1.SetPosition(-0.420000, -3.250000, -0.150000)
Hyperdrive1.SetPosition2D(60, 85)
Hyperdrive1.SetRepairComplexity(1.000000)
Hyperdrive1.SetDisabledPercentage(0.000000)
Hyperdrive1.SetRadius(0.025000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hyperdrive1)
#################################################
Hyperdrive2 = App.HullProperty_Create("Hyperdrive 2")

Hyperdrive2.SetMaxCondition(5000.000000)
Hyperdrive2.SetCritical(0)
Hyperdrive2.SetTargetable(1)
Hyperdrive2.SetPrimary(0)
Hyperdrive2.SetPosition(0.420000, -3.250000, -0.150000)
Hyperdrive2.SetPosition2D(70, 85)
Hyperdrive2.SetRepairComplexity(1.000000)
Hyperdrive2.SetDisabledPercentage(0.000000)
Hyperdrive2.SetRadius(0.025000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hyperdrive2)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")

Engineering.SetMaxCondition(15400.000000)
Engineering.SetCritical(0)
Engineering.SetTargetable(0)
Engineering.SetPrimary(1)
Engineering.SetPosition(-0.004850, -0.289657, -0.038300)
Engineering.SetPosition2D(64.000000, 80.000000)
Engineering.SetRepairComplexity(4.000000)
Engineering.SetDisabledPercentage(0.100000)
Engineering.SetRadius(0.150000)
Engineering.SetNormalPowerPerSecond(1.000000)
Engineering.SetMaxRepairPoints(7.000000)
Engineering.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 3.650000, 0.100000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -2.650000, 1.000000)
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
ViewscreenLeftPosition.SetXYZ(-1.000000, 0.000000, 0.000000)
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
ViewscreenRightPosition.SetXYZ(1.000000, 0.000000, 0.000000)
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
ViewscreenUpPosition.SetXYZ(0.000000, 0.400000, 0.600000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.200000, -0.600000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 3.650000, 0.100000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
Bridge = App.HullProperty_Create("Bridge")

Bridge.SetMaxCondition(8000.000000)
Bridge.SetCritical(1)
Bridge.SetTargetable(1)
Bridge.SetPrimary(0)
Bridge.SetPosition(0.000000, -2.550000, 0.800000)
Bridge.SetPosition2D(65, 71)
Bridge.SetRepairComplexity(2.000000)
Bridge.SetDisabledPercentage(0.500000)
Bridge.SetRadius(0.100000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Bridge)
#################################################
Cannon1 = App.TorpedoTubeProperty_Create("Cannon 1")

Cannon1.SetMaxCondition(5000.000000)
Cannon1.SetCritical(0)
Cannon1.SetTargetable(1)
Cannon1.SetPrimary(1)
Cannon1.SetPosition(0.000000, 3.500000, -0.035000)
Cannon1.SetPosition2D(65, 1)
Cannon1.SetRepairComplexity(3.000000)
Cannon1.SetDisabledPercentage(0.600000)
Cannon1.SetRadius(0.020000)
Cannon1.SetDumbfire(1)
Cannon1.SetWeaponID(1)
Cannon1.SetGroups(1)
Cannon1.SetDamageRadiusFactor(0.050000)
Cannon1.SetIconNum(370)
Cannon1.SetIconPositionX(76)
Cannon1.SetIconPositionY(40)
Cannon1.SetIconAboveShip(1)
Cannon1.SetImmediateDelay(0.100000)
Cannon1.SetReloadDelay(4.000000)
Cannon1.SetMaxReady(2)
Cannon1Direction = App.TGPoint3()
Cannon1Direction.SetXYZ(0.000000, 1.000000, 0.000000)
Cannon1.SetDirection(Cannon1Direction)
Cannon1Right = App.TGPoint3()
Cannon1Right.SetXYZ(0.000000, 0.000000, 1.000000)
Cannon1.SetRight(Cannon1Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(Cannon1)
#################################################
IonCannons = App.TorpedoSystemProperty_Create("Ion Cannons")

IonCannons.SetMaxCondition(16500.000000)
IonCannons.SetCritical(0)
IonCannons.SetTargetable(0)
IonCannons.SetPrimary(1)
IonCannons.SetPosition(0.000000, 0.000000, 0.000000)
IonCannons.SetPosition2D(64.000000, 10.000000)
IonCannons.SetRepairComplexity(3.000000)
IonCannons.SetDisabledPercentage(0.600000)
IonCannons.SetRadius(0.100000)
IonCannons.SetNormalPowerPerSecond(200.000000)
IonCannons.SetWeaponSystemType(IonCannons.WST_TORPEDO)
IonCannons.SetSingleFire(1)
IonCannons.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
IonCannons.SetFiringChainString(kFiringChainString)
IonCannons.SetMaxTorpedoes(0, 300)
IonCannons.SetTorpedoScript(0, "Tactical.Projectiles.IonCannon4")
IonCannons.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(IonCannons)
#################################################
IonPulses = App.WeaponSystemProperty_Create("Ion Pulses")

IonPulses.SetMaxCondition(2000.000000)
IonPulses.SetCritical(0)
IonPulses.SetTargetable(0)
IonPulses.SetPrimary(1)
IonPulses.SetPosition(0.000000, 0.000000, 0.000000)
IonPulses.SetPosition2D(0.000000, 0.000000)
IonPulses.SetRepairComplexity(1.000000)
IonPulses.SetDisabledPercentage(0.500000)
IonPulses.SetRadius(0.250000)
IonPulses.SetNormalPowerPerSecond(400.000000)
IonPulses.SetWeaponSystemType(IonPulses.WST_PULSE)
IonPulses.SetSingleFire(1)
IonPulses.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
IonPulses.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(IonPulses)
#################################################
PortPulse1 = App.PulseWeaponProperty_Create("Port Pulse 1")

PortPulse1.SetMaxCondition(2000.000000)
PortPulse1.SetCritical(0)
PortPulse1.SetTargetable(1)
PortPulse1.SetPrimary(1)
PortPulse1.SetPosition(-1.330000, 2.500000, -0.040000)
PortPulse1.SetPosition2D(47, 12)
PortPulse1.SetRepairComplexity(1.000000)
PortPulse1.SetDisabledPercentage(0.500000)
PortPulse1.SetRadius(0.050000)
PortPulse1.SetDumbfire(1)
PortPulse1.SetWeaponID(0)
PortPulse1.SetGroups(0)
PortPulse1.SetDamageRadiusFactor(0.300000)
PortPulse1.SetIconNum(365)
PortPulse1.SetIconPositionX(60)
PortPulse1.SetIconPositionY(52)
PortPulse1.SetIconAboveShip(1)
PortPulse1.SetFireSound("")
PortPulse1.SetMaxCharge(5.000000)
PortPulse1.SetMaxDamage(1.000000)
PortPulse1.SetMaxDamageDistance(100.000000)
PortPulse1.SetMinFiringCharge(3.000000)
PortPulse1.SetNormalDischargeRate(1.000000)
PortPulse1.SetRechargeRate(0.700000)
PortPulse1.SetIndicatorIconNum(0)
PortPulse1.SetIndicatorIconPositionX(15)
PortPulse1.SetIndicatorIconPositionY(15)
PortPulse1Forward = App.TGPoint3()
PortPulse1Forward.SetXYZ(-1.000000, 0.000000, 0.000000)
PortPulse1Up = App.TGPoint3()
PortPulse1Up.SetXYZ(0.000000, 0.000000, 1.000000)
PortPulse1.SetOrientation(PortPulse1Forward, PortPulse1Up)
PortPulse1.SetArcWidthAngles(-1.134464, 1.134464)
PortPulse1.SetArcHeightAngles(-0.523599, 0.523599)
PortPulse1.SetCooldownTime(0.000100)
PortPulse1.SetModuleName("Tactical.Projectiles.IonPulse4")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortPulse1)
#################################################
StarPulse1 = App.PulseWeaponProperty_Create("Star Pulse 1")

StarPulse1.SetMaxCondition(2000.000000)
StarPulse1.SetCritical(0)
StarPulse1.SetTargetable(1)
StarPulse1.SetPrimary(1)
StarPulse1.SetPosition(1.330000, 2.500000, -0.040000)
StarPulse1.SetPosition2D(81, 12)
StarPulse1.SetRepairComplexity(1.000000)
StarPulse1.SetDisabledPercentage(0.500000)
StarPulse1.SetRadius(0.050000)
StarPulse1.SetDumbfire(1)
StarPulse1.SetWeaponID(0)
StarPulse1.SetGroups(0)
StarPulse1.SetDamageRadiusFactor(0.300000)
StarPulse1.SetIconNum(365)
StarPulse1.SetIconPositionX(90)
StarPulse1.SetIconPositionY(52)
StarPulse1.SetIconAboveShip(1)
StarPulse1.SetFireSound("")
StarPulse1.SetMaxCharge(5.000000)
StarPulse1.SetMaxDamage(1.000000)
StarPulse1.SetMaxDamageDistance(100.000000)
StarPulse1.SetMinFiringCharge(3.000000)
StarPulse1.SetNormalDischargeRate(1.000000)
StarPulse1.SetRechargeRate(0.700000)
StarPulse1.SetIndicatorIconNum(0)
StarPulse1.SetIndicatorIconPositionX(15)
StarPulse1.SetIndicatorIconPositionY(15)
StarPulse1Forward = App.TGPoint3()
StarPulse1Forward.SetXYZ(1.000000, 0.000000, 0.000000)
StarPulse1Up = App.TGPoint3()
StarPulse1Up.SetXYZ(0.000000, 0.000000, 1.000000)
StarPulse1.SetOrientation(StarPulse1Forward, StarPulse1Up)
StarPulse1.SetArcWidthAngles(-1.134464, 1.134464)
StarPulse1.SetArcHeightAngles(-0.523599, 0.523599)
StarPulse1.SetCooldownTime(0.000100)
StarPulse1.SetModuleName("Tactical.Projectiles.IonPulse4")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarPulse1)
#################################################
VentralPulse1 = App.PulseWeaponProperty_Create("Ventral Pulse 1")

VentralPulse1.SetMaxCondition(2000.000000)
VentralPulse1.SetCritical(0)
VentralPulse1.SetTargetable(1)
VentralPulse1.SetPrimary(1)
VentralPulse1.SetPosition(-1.025000, -2.200000, -1.350000)
VentralPulse1.SetPosition2D(55, 74)
VentralPulse1.SetRepairComplexity(1.000000)
VentralPulse1.SetDisabledPercentage(0.500000)
VentralPulse1.SetRadius(0.050000)
VentralPulse1.SetDumbfire(1)
VentralPulse1.SetWeaponID(0)
VentralPulse1.SetGroups(0)
VentralPulse1.SetDamageRadiusFactor(0.300000)
VentralPulse1.SetIconNum(365)
VentralPulse1.SetIconPositionX(68)
VentralPulse1.SetIconPositionY(80)
VentralPulse1.SetIconAboveShip(1)
VentralPulse1.SetFireSound("")
VentralPulse1.SetMaxCharge(5.000000)
VentralPulse1.SetMaxDamage(1.000000)
VentralPulse1.SetMaxDamageDistance(100.000000)
VentralPulse1.SetMinFiringCharge(3.000000)
VentralPulse1.SetNormalDischargeRate(1.000000)
VentralPulse1.SetRechargeRate(0.700000)
VentralPulse1.SetIndicatorIconNum(0)
VentralPulse1.SetIndicatorIconPositionX(15)
VentralPulse1.SetIndicatorIconPositionY(15)
VentralPulse1Forward = App.TGPoint3()
VentralPulse1Forward.SetXYZ(0.000000, 0.000000, -1.000000)
VentralPulse1Up = App.TGPoint3()
VentralPulse1Up.SetXYZ(0.000000, 1.000000, 0.000000)
VentralPulse1.SetOrientation(VentralPulse1Forward, VentralPulse1Up)
VentralPulse1.SetArcWidthAngles(-1.047198, 1.047198)
VentralPulse1.SetArcHeightAngles(1.047198, -1.047198)
VentralPulse1.SetCooldownTime(0.300000)
VentralPulse1.SetModuleName("Tactical.Projectiles.IonPulse4")
App.g_kModelPropertyManager.RegisterLocalTemplate(VentralPulse1)
#################################################
VentralPulse2 = App.PulseWeaponProperty_Create("Ventral Pulse 2")

VentralPulse2.SetMaxCondition(2000.000000)
VentralPulse2.SetCritical(0)
VentralPulse2.SetTargetable(1)
VentralPulse2.SetPrimary(1)
VentralPulse2.SetPosition(1.025000, -2.200000, -1.350000)
VentralPulse2.SetPosition2D(74, 74)
VentralPulse2.SetRepairComplexity(1.000000)
VentralPulse2.SetDisabledPercentage(0.500000)
VentralPulse2.SetRadius(0.050000)
VentralPulse2.SetDumbfire(1)
VentralPulse2.SetWeaponID(0)
VentralPulse2.SetGroups(0)
VentralPulse2.SetDamageRadiusFactor(0.300000)
VentralPulse2.SetIconNum(365)
VentralPulse2.SetIconPositionX(83)
VentralPulse2.SetIconPositionY(80)
VentralPulse2.SetIconAboveShip(1)
VentralPulse2.SetFireSound("")
VentralPulse2.SetMaxCharge(5.000000)
VentralPulse2.SetMaxDamage(1.000000)
VentralPulse2.SetMaxDamageDistance(100.000000)
VentralPulse2.SetMinFiringCharge(3.000000)
VentralPulse2.SetNormalDischargeRate(1.000000)
VentralPulse2.SetRechargeRate(0.700000)
VentralPulse2.SetIndicatorIconNum(0)
VentralPulse2.SetIndicatorIconPositionX(15)
VentralPulse2.SetIndicatorIconPositionY(15)
VentralPulse2Forward = App.TGPoint3()
VentralPulse2Forward.SetXYZ(0.000000, 0.000000, -1.000000)
VentralPulse2Up = App.TGPoint3()
VentralPulse2Up.SetXYZ(0.000000, 1.000000, 0.000000)
VentralPulse2.SetOrientation(VentralPulse2Forward, VentralPulse2Up)
VentralPulse2.SetArcWidthAngles(-1.047198, 1.047198)
VentralPulse2.SetArcHeightAngles(1.047198, -1.047198)
VentralPulse2.SetCooldownTime(0.300000)
VentralPulse2.SetModuleName("Tactical.Projectiles.IonPulse4")
App.g_kModelPropertyManager.RegisterLocalTemplate(VentralPulse2)
#################################################
DorsalPulse1 = App.PulseWeaponProperty_Create("Dorsal Pulse 1")

DorsalPulse1.SetMaxCondition(2000.000000)
DorsalPulse1.SetCritical(0)
DorsalPulse1.SetTargetable(1)
DorsalPulse1.SetPrimary(1)
DorsalPulse1.SetPosition(-1.050000, -2.350000, 1.250000)
DorsalPulse1.SetPosition2D(50, 65)
DorsalPulse1.SetRepairComplexity(1.000000)
DorsalPulse1.SetDisabledPercentage(0.500000)
DorsalPulse1.SetRadius(0.050000)
DorsalPulse1.SetDumbfire(1)
DorsalPulse1.SetWeaponID(0)
DorsalPulse1.SetGroups(0)
DorsalPulse1.SetDamageRadiusFactor(0.300000)
DorsalPulse1.SetIconNum(365)
DorsalPulse1.SetIconPositionX(58)
DorsalPulse1.SetIconPositionY(90)
DorsalPulse1.SetIconAboveShip(1)
DorsalPulse1.SetFireSound("")
DorsalPulse1.SetMaxCharge(5.000000)
DorsalPulse1.SetMaxDamage(1.000000)
DorsalPulse1.SetMaxDamageDistance(100.000000)
DorsalPulse1.SetMinFiringCharge(3.000000)
DorsalPulse1.SetNormalDischargeRate(1.000000)
DorsalPulse1.SetRechargeRate(0.700000)
DorsalPulse1.SetIndicatorIconNum(0)
DorsalPulse1.SetIndicatorIconPositionX(15)
DorsalPulse1.SetIndicatorIconPositionY(15)
DorsalPulse1Forward = App.TGPoint3()
DorsalPulse1Forward.SetXYZ(0.000000, 0.000000, 1.000000)
DorsalPulse1Up = App.TGPoint3()
DorsalPulse1Up.SetXYZ(0.000000, 1.000000, 0.000000)
DorsalPulse1.SetOrientation(DorsalPulse1Forward, DorsalPulse1Up)
DorsalPulse1.SetArcWidthAngles(-1.047198, 1.047198)
DorsalPulse1.SetArcHeightAngles(-1.047198, 1.047198)
DorsalPulse1.SetCooldownTime(0.300000)
DorsalPulse1.SetModuleName("Tactical.Projectiles.IonPulse4")
App.g_kModelPropertyManager.RegisterLocalTemplate(DorsalPulse1)
#################################################
DorsalPulse2 = App.PulseWeaponProperty_Create("Dorsal Pulse 2")

DorsalPulse2.SetMaxCondition(2000.000000)
DorsalPulse2.SetCritical(0)
DorsalPulse2.SetTargetable(1)
DorsalPulse2.SetPrimary(1)
DorsalPulse2.SetPosition(1.050000, -2.350000, 1.250000)
DorsalPulse2.SetPosition2D(79, 65)
DorsalPulse2.SetRepairComplexity(1.000000)
DorsalPulse2.SetDisabledPercentage(0.500000)
DorsalPulse2.SetRadius(0.050000)
DorsalPulse2.SetDumbfire(1)
DorsalPulse2.SetWeaponID(0)
DorsalPulse2.SetGroups(0)
DorsalPulse2.SetDamageRadiusFactor(0.300000)
DorsalPulse2.SetIconNum(365)
DorsalPulse2.SetIconPositionX(90)
DorsalPulse2.SetIconPositionY(90)
DorsalPulse2.SetIconAboveShip(1)
DorsalPulse2.SetFireSound("")
DorsalPulse2.SetMaxCharge(5.000000)
DorsalPulse2.SetMaxDamage(1.000000)
DorsalPulse2.SetMaxDamageDistance(100.000000)
DorsalPulse2.SetMinFiringCharge(3.000000)
DorsalPulse2.SetNormalDischargeRate(1.000000)
DorsalPulse2.SetRechargeRate(0.700000)
DorsalPulse2.SetIndicatorIconNum(0)
DorsalPulse2.SetIndicatorIconPositionX(15)
DorsalPulse2.SetIndicatorIconPositionY(15)
DorsalPulse2Forward = App.TGPoint3()
DorsalPulse2Forward.SetXYZ(0.000000, 0.000000, 1.000000)
DorsalPulse2Up = App.TGPoint3()
DorsalPulse2Up.SetXYZ(0.000000, 1.000000, 0.000000)
DorsalPulse2.SetOrientation(DorsalPulse2Forward, DorsalPulse2Up)
DorsalPulse2.SetArcWidthAngles(-1.047198, 1.047198)
DorsalPulse2.SetArcHeightAngles(-1.047198, 1.047198)
DorsalPulse2.SetCooldownTime(0.300000)
DorsalPulse2.SetModuleName("Tactical.Projectiles.IonPulse4")
App.g_kModelPropertyManager.RegisterLocalTemplate(DorsalPulse2)
#################################################
AftPulse1 = App.PulseWeaponProperty_Create("Aft Pulse 1")

AftPulse1.SetMaxCondition(2000.000000)
AftPulse1.SetCritical(0)
AftPulse1.SetTargetable(1)
AftPulse1.SetPrimary(1)
AftPulse1.SetPosition(-1.100000, -3.150000, -0.150000)
AftPulse1.SetPosition2D(56, 108)
AftPulse1.SetRepairComplexity(1.000000)
AftPulse1.SetDisabledPercentage(0.500000)
AftPulse1.SetRadius(0.050000)
AftPulse1.SetDumbfire(1)
AftPulse1.SetWeaponID(0)
AftPulse1.SetGroups(0)
AftPulse1.SetDamageRadiusFactor(0.300000)
AftPulse1.SetIconNum(366)
AftPulse1.SetIconPositionX(62)
AftPulse1.SetIconPositionY(115)
AftPulse1.SetIconAboveShip(1)
AftPulse1.SetFireSound("")
AftPulse1.SetMaxCharge(5.000000)
AftPulse1.SetMaxDamage(1.000000)
AftPulse1.SetMaxDamageDistance(100.000000)
AftPulse1.SetMinFiringCharge(3.000000)
AftPulse1.SetNormalDischargeRate(1.000000)
AftPulse1.SetRechargeRate(0.700000)
AftPulse1.SetIndicatorIconNum(0)
AftPulse1.SetIndicatorIconPositionX(15)
AftPulse1.SetIndicatorIconPositionY(15)
AftPulse1Forward = App.TGPoint3()
AftPulse1Forward.SetXYZ(0.000000, -1.000000, 0.000000)
AftPulse1Up = App.TGPoint3()
AftPulse1Up.SetXYZ(0.000000, 0.000000, 1.000000)
AftPulse1.SetOrientation(AftPulse1Forward, AftPulse1Up)
AftPulse1.SetArcWidthAngles(-0.698132, 0.698132)
AftPulse1.SetArcHeightAngles(-0.959931, 0.959931)
AftPulse1.SetCooldownTime(0.300000)
AftPulse1.SetModuleName("Tactical.Projectiles.IonPulse4")
App.g_kModelPropertyManager.RegisterLocalTemplate(AftPulse1)
#################################################
AftPulse2 = App.PulseWeaponProperty_Create("Aft Pulse 2")

AftPulse2.SetMaxCondition(2000.000000)
AftPulse2.SetCritical(0)
AftPulse2.SetTargetable(1)
AftPulse2.SetPrimary(1)
AftPulse2.SetPosition(1.100000, -3.150000, -0.150000)
AftPulse2.SetPosition2D(73, 108)
AftPulse2.SetRepairComplexity(1.000000)
AftPulse2.SetDisabledPercentage(0.500000)
AftPulse2.SetRadius(0.050000)
AftPulse2.SetDumbfire(1)
AftPulse2.SetWeaponID(0)
AftPulse2.SetGroups(0)
AftPulse2.SetDamageRadiusFactor(0.300000)
AftPulse2.SetIconNum(366)
AftPulse2.SetIconPositionX(86)
AftPulse2.SetIconPositionY(115)
AftPulse2.SetIconAboveShip(1)
AftPulse2.SetFireSound("")
AftPulse2.SetMaxCharge(5.000000)
AftPulse2.SetMaxDamage(1.000000)
AftPulse2.SetMaxDamageDistance(100.000000)
AftPulse2.SetMinFiringCharge(3.000000)
AftPulse2.SetNormalDischargeRate(1.000000)
AftPulse2.SetRechargeRate(0.700000)
AftPulse2.SetIndicatorIconNum(0)
AftPulse2.SetIndicatorIconPositionX(15)
AftPulse2.SetIndicatorIconPositionY(15)
AftPulse2Forward = App.TGPoint3()
AftPulse2Forward.SetXYZ(0.000000, -1.000000, 0.000000)
AftPulse2Up = App.TGPoint3()
AftPulse2Up.SetXYZ(0.000000, 0.000000, 1.000000)
AftPulse2.SetOrientation(AftPulse2Forward, AftPulse2Up)
AftPulse2.SetArcWidthAngles(-0.698132, 0.698132)
AftPulse2.SetArcHeightAngles(-0.959931, 0.959931)
AftPulse2.SetCooldownTime(0.300000)
AftPulse2.SetModuleName("Tactical.Projectiles.IonPulse4")
App.g_kModelPropertyManager.RegisterLocalTemplate(AftPulse2)
#################################################
Cloak = App.CloakingSubsystemProperty_Create("Cloak")

Cloak.SetMaxCondition(2000.000000)
Cloak.SetCritical(0)
Cloak.SetTargetable(1)
Cloak.SetPrimary(1)
Cloak.SetPosition(0.000000, 0.100000, 0.000000)
Cloak.SetPosition2D(65, 27)
Cloak.SetRepairComplexity(1.000000)
Cloak.SetDisabledPercentage(0.500000)
Cloak.SetRadius(0.250000)
Cloak.SetNormalPowerPerSecond(150.000000)
Cloak.SetCloakStrength(300.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Cloak)
#################################################
StarEngine = App.EngineProperty_Create("Star Engine")

StarEngine.SetMaxCondition(4000.000000)
StarEngine.SetCritical(0)
StarEngine.SetTargetable(1)
StarEngine.SetPrimary(1)
StarEngine.SetPosition(0.420000, -3.250000, -0.150000)
StarEngine.SetPosition2D(75, 95)
StarEngine.SetRepairComplexity(3.000000)
StarEngine.SetDisabledPercentage(0.500000)
StarEngine.SetRadius(0.170000)
StarEngine.SetEngineType(StarEngine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarEngine)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Beliskner", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Bridge", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engineering", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Generators", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hyperdrive 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hyperdrive 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Ion Cannons", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Cannon 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Ion Pulses", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Pulse 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Pulse 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Dorsal Pulse 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Dorsal Pulse 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Ventral Pulse 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Ventral Pulse 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Aft Pulse 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Aft Pulse 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Cloak", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
