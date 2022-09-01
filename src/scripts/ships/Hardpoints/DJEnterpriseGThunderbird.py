#####  Created by:
#####  Tactical Display Icon Editor



import App
import GlobalPropertyTemplates

# Local Templates
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(15000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(-7.000000, 115.000000)
Hull.SetRepairComplexity(2.500000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(3500.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, 0.000000, 0.000000)
WarpCore.SetPosition2D(-4.000000, 94.000000)
WarpCore.SetRepairComplexity(2.250000)
WarpCore.SetDisabledPercentage(0.400000)
WarpCore.SetRadius(0.050000)
WarpCore.SetMainBatteryLimit(100000.000000)
WarpCore.SetBackupBatteryLimit(200000.000000)
WarpCore.SetMainConduitCapacity(3500.000000)
WarpCore.SetBackupConduitCapacity(500.000000)
WarpCore.SetPowerOutput(3000.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(12000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.155000, -0.051000)
SensorArray.SetPosition2D(64.000000, 85.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.350000)
SensorArray.SetRadius(0.050000)
SensorArray.SetNormalPowerPerSecond(200.000000)
SensorArray.SetBaseSensorRange(8000.000000)
SensorArray.SetMaxProbes(100)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
DJEnterpriseG = App.ShipProperty_Create("DJEnterpriseG")

DJEnterpriseG.SetGenus(1)
DJEnterpriseG.SetSpecies(162)
DJEnterpriseG.SetMass(700.000000)
DJEnterpriseG.SetRotationalInertia(1000.000000)
DJEnterpriseG.SetShipName("DJEnterpriseGThunderbird")
DJEnterpriseG.SetModelFilename("data/Models/Ships/DJEnterpriseGThunderbird.nif")
DJEnterpriseG.SetDamageResolution(15.000000)
DJEnterpriseG.SetAffiliation(0)
DJEnterpriseG.SetStationary(0)
DJEnterpriseG.SetAIString("FedAttack")
DJEnterpriseG.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(DJEnterpriseG)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(13000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.200000, 0.020000)
ShieldGenerator.SetPosition2D(66.000000, 113.000000)
ShieldGenerator.SetRepairComplexity(2.750000)
ShieldGenerator.SetDisabledPercentage(0.300000)
ShieldGenerator.SetRadius(0.100000)
ShieldGenerator.SetNormalPowerPerSecond(1100.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.784314, 0.784314, 1.000000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 13500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 13500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 13500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 13500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 13500.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 13500.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 25.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 25.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 25.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 25.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 25.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 25.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpDrive = App.WarpEngineProperty_Create("Warp Drive")

WarpDrive.SetMaxCondition(9500.000000)
WarpDrive.SetCritical(0)
WarpDrive.SetTargetable(0)
WarpDrive.SetPrimary(1)
WarpDrive.SetPosition(0.000000, 0.000000, 0.000000)
WarpDrive.SetPosition2D(0.000000, 0.000000)
WarpDrive.SetRepairComplexity(5.000000)
WarpDrive.SetDisabledPercentage(0.500000)
WarpDrive.SetRadius(0.050000)
WarpDrive.SetNormalPowerPerSecond(1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpDrive)
#################################################
PortNacelle = App.EngineProperty_Create("Port Nacelle")

PortNacelle.SetMaxCondition(5000.000000)
PortNacelle.SetCritical(0)
PortNacelle.SetTargetable(1)
PortNacelle.SetPrimary(1)
PortNacelle.SetPosition(-0.400000, -0.100000, -0.025000)
PortNacelle.SetPosition2D(13.000000, 69.000000)
PortNacelle.SetRepairComplexity(5.000000)
PortNacelle.SetDisabledPercentage(0.500000)
PortNacelle.SetRadius(0.250000)
PortNacelle.SetEngineType(PortNacelle.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortNacelle)
#################################################
StarboardNacelle = App.EngineProperty_Create("Starboard Nacelle")

StarboardNacelle.SetMaxCondition(5000.000000)
StarboardNacelle.SetCritical(0)
StarboardNacelle.SetTargetable(1)
StarboardNacelle.SetPrimary(1)
StarboardNacelle.SetPosition(0.400000, -0.100000, -0.025000)
StarboardNacelle.SetPosition2D(113.000000, 69.000000)
StarboardNacelle.SetRepairComplexity(5.000000)
StarboardNacelle.SetDisabledPercentage(0.500000)
StarboardNacelle.SetRadius(0.250000)
StarboardNacelle.SetEngineType(StarboardNacelle.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarboardNacelle)
#################################################
ImpulseDrive = App.ImpulseEngineProperty_Create("Impulse Drive")

ImpulseDrive.SetMaxCondition(3500.000000)
ImpulseDrive.SetCritical(0)
ImpulseDrive.SetTargetable(0)
ImpulseDrive.SetPrimary(1)
ImpulseDrive.SetPosition(0.000000, 0.000000, 0.000000)
ImpulseDrive.SetPosition2D(0.000000, 0.000000)
ImpulseDrive.SetRepairComplexity(1.000000)
ImpulseDrive.SetDisabledPercentage(0.500000)
ImpulseDrive.SetRadius(0.250000)
ImpulseDrive.SetNormalPowerPerSecond(350.000000)
ImpulseDrive.SetMaxAccel(5.000000)
ImpulseDrive.SetMaxAngularAccel(1.500000)
ImpulseDrive.SetMaxAngularVelocity(1.500000)
ImpulseDrive.SetMaxSpeed(17.000000)
ImpulseDrive.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseDrive)
#################################################
PortImpulse = App.EngineProperty_Create("Port Impulse")

PortImpulse.SetMaxCondition(1500.000000)
PortImpulse.SetCritical(0)
PortImpulse.SetTargetable(1)
PortImpulse.SetPrimary(1)
PortImpulse.SetPosition(-0.037000, -0.200000, 0.030000)
PortImpulse.SetPosition2D(47.000000, 91.000000)
PortImpulse.SetRepairComplexity(2.000000)
PortImpulse.SetDisabledPercentage(0.500000)
PortImpulse.SetRadius(0.050000)
PortImpulse.SetEngineType(PortImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortImpulse)
#################################################
StarboardImpulse = App.EngineProperty_Create("Starboard Impulse")

StarboardImpulse.SetMaxCondition(1500.000000)
StarboardImpulse.SetCritical(0)
StarboardImpulse.SetTargetable(1)
StarboardImpulse.SetPrimary(1)
StarboardImpulse.SetPosition(0.037000, -0.200000, 0.030000)
StarboardImpulse.SetPosition2D(80.000000, 91.000000)
StarboardImpulse.SetRepairComplexity(2.000000)
StarboardImpulse.SetDisabledPercentage(0.500000)
StarboardImpulse.SetRadius(0.050000)
StarboardImpulse.SetEngineType(StarboardImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarboardImpulse)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenForward.SetPosition(ViewscreenForwardPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenForward)
#################################################
ViewscreenBack = App.PositionOrientationProperty_Create("ViewscreenBack")

ViewscreenBackForward = App.TGPoint3()
ViewscreenBackForward.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenBackUp = App.TGPoint3()
ViewscreenBackUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenBackRight = App.TGPoint3()
ViewscreenBackRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenBack.SetOrientation(ViewscreenBackForward, ViewscreenBackUp, ViewscreenBackRight)
ViewscreenBackPosition = App.TGPoint3()
ViewscreenBackPosition.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenBack.SetPosition(ViewscreenBackPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenBack)
#################################################
ViewscreenLeft = App.PositionOrientationProperty_Create("ViewscreenLeft")

ViewscreenLeftForward = App.TGPoint3()
ViewscreenLeftForward.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenLeftUp = App.TGPoint3()
ViewscreenLeftUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenLeftRight = App.TGPoint3()
ViewscreenLeftRight.SetXYZ(-1.000000, 0.000000, 0.000000)
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
ViewscreenRightRight.SetXYZ(1.000000, 0.000000, 0.000000)
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
ViewscreenUpUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenUpRight = App.TGPoint3()
ViewscreenUpRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenUp.SetOrientation(ViewscreenUpForward, ViewscreenUpUp, ViewscreenUpRight)
ViewscreenUpPosition = App.TGPoint3()
ViewscreenUpPosition.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenUp.SetPosition(ViewscreenUpPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenUp)
#################################################
ViewscreenDown = App.PositionOrientationProperty_Create("ViewscreenDown")

ViewscreenDownForward = App.TGPoint3()
ViewscreenDownForward.SetXYZ(0.000000, 0.000000, -1.000000)
ViewscreenDownUp = App.TGPoint3()
ViewscreenDownUp.SetXYZ(0.000000, 0.000000, -1.000000)
ViewscreenDownRight = App.TGPoint3()
ViewscreenDownRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenDown.SetOrientation(ViewscreenDownForward, ViewscreenDownUp, ViewscreenDownRight)
ViewscreenDownPosition = App.TGPoint3()
ViewscreenDownPosition.SetXYZ(0.000000, 0.000000, -1.000000)
ViewscreenDown.SetPosition(ViewscreenDownPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenDown)
#################################################
FirstPerson = App.PositionOrientationProperty_Create("FirstPerson")

FirstPersonForward = App.TGPoint3()
FirstPersonForward.SetXYZ(0.000000, 1.000000, 0.000000)
FirstPersonUp = App.TGPoint3()
FirstPersonUp.SetXYZ(0.000000, 0.000000, 1.000000)
FirstPersonRight = App.TGPoint3()
FirstPersonRight.SetXYZ(1.000000, 0.000000, 0.000000)
FirstPerson.SetOrientation(FirstPersonForward, FirstPersonUp, FirstPersonRight)
FirstPersonPosition = App.TGPoint3()
FirstPersonPosition.SetXYZ(0.000000, 1.000000, 0.000000)
FirstPerson.SetPosition(FirstPersonPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPerson)
#################################################
Repair = App.RepairSubsystemProperty_Create("Repair")

Repair.SetMaxCondition(1200.000000)
Repair.SetCritical(0)
Repair.SetTargetable(0)
Repair.SetPrimary(1)
Repair.SetPosition(0.000000, 0.000000, 0.000000)
Repair.SetPosition2D(0.000000, 0.000000)
Repair.SetRepairComplexity(1.000000)
Repair.SetDisabledPercentage(0.010000)
Repair.SetRadius(0.010000)
Repair.SetNormalPowerPerSecond(1.000000)
Repair.SetMaxRepairPoints(150.000000)
Repair.SetNumRepairTeams(2)
App.g_kModelPropertyManager.RegisterLocalTemplate(Repair)
#################################################
Phasers = App.WeaponSystemProperty_Create("Phasers")

Phasers.SetMaxCondition(8000.000000)
Phasers.SetCritical(0)
Phasers.SetTargetable(0)
Phasers.SetPrimary(1)
Phasers.SetPosition(0.000000, 0.000000, 0.000000)
Phasers.SetPosition2D(0.000000, 0.000000)
Phasers.SetRepairComplexity(1.000000)
Phasers.SetDisabledPercentage(0.350000)
Phasers.SetRadius(0.250000)
Phasers.SetNormalPowerPerSecond(750.000000)
Phasers.SetWeaponSystemType(Phasers.WST_PHASER)
Phasers.SetSingleFire(0)
Phasers.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Phasers.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Phasers)
#################################################
QuantumTorpedoes = App.WeaponSystemProperty_Create("Quantum Torpedoes")

QuantumTorpedoes.SetMaxCondition(2500.000000)
QuantumTorpedoes.SetCritical(0)
QuantumTorpedoes.SetTargetable(0)
QuantumTorpedoes.SetPrimary(1)
QuantumTorpedoes.SetPosition(0.000000, 0.000000, 0.000000)
QuantumTorpedoes.SetPosition2D(0.000000, 0.000000)
QuantumTorpedoes.SetRepairComplexity(2.000000)
QuantumTorpedoes.SetDisabledPercentage(0.350000)
QuantumTorpedoes.SetRadius(0.250000)
QuantumTorpedoes.SetNormalPowerPerSecond(500.000000)
QuantumTorpedoes.SetWeaponSystemType(QuantumTorpedoes.WST_PULSE)
QuantumTorpedoes.SetSingleFire(1)
QuantumTorpedoes.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
QuantumTorpedoes.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(QuantumTorpedoes)
#################################################
Launcher1 = App.PulseWeaponProperty_Create("Launcher 1")

Launcher1.SetMaxCondition(2000.000000)
Launcher1.SetCritical(0)
Launcher1.SetTargetable(1)
Launcher1.SetPrimary(1)
Launcher1.SetPosition(-0.017000, 0.350000, -0.055000)
Launcher1.SetPosition2D(61.000000, 21.000000)
Launcher1.SetRepairComplexity(1.500000)
Launcher1.SetDisabledPercentage(0.350000)
Launcher1.SetRadius(0.250000)
Launcher1.SetDumbfire(1)
Launcher1.SetWeaponID(8)
Launcher1.SetGroups(0)
Launcher1.SetDamageRadiusFactor(0.300000)
Launcher1.SetIconNum(365)
Launcher1.SetIconPositionX(70.000000)
Launcher1.SetIconPositionY(30.000000)
Launcher1.SetIconAboveShip(1)
Launcher1.SetFireSound("DJQuantum")
Launcher1.SetMaxCharge(50.000000)
Launcher1.SetMaxDamage(1500.000000)
Launcher1.SetMaxDamageDistance(2000.000000)
Launcher1.SetMinFiringCharge(1.000000)
Launcher1.SetNormalDischargeRate(1.000000)
Launcher1.SetRechargeRate(0.000000)
Launcher1.SetIndicatorIconNum(0)
Launcher1.SetIndicatorIconPositionX(15.000000)
Launcher1.SetIndicatorIconPositionY(15.000000)
Launcher1Forward = App.TGPoint3()
Launcher1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Launcher1Up = App.TGPoint3()
Launcher1Up.SetXYZ(0.000000, 0.000000, 1.000000)
Launcher1.SetOrientation(Launcher1Forward, Launcher1Up)
Launcher1.SetArcWidthAngles(-0.261799, 0.261799)
Launcher1.SetArcHeightAngles(0.087266, -0.349066)
Launcher1.SetCooldownTime(15.000000)
Launcher1.SetModuleName("Tactical.Projectiles.RapidQuantum")
App.g_kModelPropertyManager.RegisterLocalTemplate(Launcher1)
#################################################
Launcher2 = App.PulseWeaponProperty_Create("Launcher 2")

Launcher2.SetMaxCondition(2000.000000)
Launcher2.SetCritical(0)
Launcher2.SetTargetable(1)
Launcher2.SetPrimary(1)
Launcher2.SetPosition(0.017000, 0.350000, -0.055000)
Launcher2.SetPosition2D(0.000000, 0.000000)
Launcher2.SetRepairComplexity(1.500000)
Launcher2.SetDisabledPercentage(0.350000)
Launcher2.SetRadius(0.250000)
Launcher2.SetDumbfire(1)
Launcher2.SetWeaponID(8)
Launcher2.SetGroups(0)
Launcher2.SetDamageRadiusFactor(0.300000)
Launcher2.SetIconNum(365)
Launcher2.SetIconPositionX(78.000000)
Launcher2.SetIconPositionY(30.000000)
Launcher2.SetIconAboveShip(1)
Launcher2.SetFireSound("DJQuantum")
Launcher2.SetMaxCharge(50.000000)
Launcher2.SetMaxDamage(1500.000000)
Launcher2.SetMaxDamageDistance(2000.000000)
Launcher2.SetMinFiringCharge(1.000000)
Launcher2.SetNormalDischargeRate(1.000000)
Launcher2.SetRechargeRate(0.000000)
Launcher2.SetIndicatorIconNum(0)
Launcher2.SetIndicatorIconPositionX(15.000000)
Launcher2.SetIndicatorIconPositionY(15.000000)
Launcher2Forward = App.TGPoint3()
Launcher2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Launcher2Up = App.TGPoint3()
Launcher2Up.SetXYZ(0.000000, 0.000000, 1.000000)
Launcher2.SetOrientation(Launcher2Forward, Launcher2Up)
Launcher2.SetArcWidthAngles(-0.261799, 0.261799)
Launcher2.SetArcHeightAngles(0.087266, -0.349066)
Launcher2.SetCooldownTime(15.000000)
Launcher2.SetModuleName("Tactical.Projectiles.RapidQuantum")
App.g_kModelPropertyManager.RegisterLocalTemplate(Launcher2)
#################################################
TorpedoLaunchers = App.TorpedoSystemProperty_Create("Torpedo Launchers")

TorpedoLaunchers.SetMaxCondition(200.000000)
TorpedoLaunchers.SetCritical(0)
TorpedoLaunchers.SetTargetable(0)
TorpedoLaunchers.SetPrimary(1)
TorpedoLaunchers.SetPosition(0.000000, 0.000000, 0.000000)
TorpedoLaunchers.SetPosition2D(0.000000, 0.000000)
TorpedoLaunchers.SetRepairComplexity(1.000000)
TorpedoLaunchers.SetDisabledPercentage(0.500000)
TorpedoLaunchers.SetRadius(0.250000)
TorpedoLaunchers.SetNormalPowerPerSecond(500.000000)
TorpedoLaunchers.SetWeaponSystemType(TorpedoLaunchers.WST_TORPEDO)
TorpedoLaunchers.SetSingleFire(0)
TorpedoLaunchers.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("0;Single;12;Dual;5;Quad")
TorpedoLaunchers.SetFiringChainString(kFiringChainString)
TorpedoLaunchers.SetMaxTorpedoes(0, 0)
TorpedoLaunchers.SetTorpedoScript(0, "")
TorpedoLaunchers.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(TorpedoLaunchers)
#################################################
ForPhaser1 = App.PhaserProperty_Create("For Phaser 1")

ForPhaser1.SetMaxCondition(2000.000000)
ForPhaser1.SetCritical(0)
ForPhaser1.SetTargetable(1)
ForPhaser1.SetPrimary(1)
ForPhaser1.SetPosition(-0.260000, 0.340000, 0.000000)
ForPhaser1.SetPosition2D(46.000000, 24.000000)
ForPhaser1.SetRepairComplexity(1.000000)
ForPhaser1.SetDisabledPercentage(0.400000)
ForPhaser1.SetRadius(0.250000)
ForPhaser1.SetDumbfire(0)
ForPhaser1.SetWeaponID(1)
ForPhaser1.SetGroups(0)
ForPhaser1.SetDamageRadiusFactor(0.250000)
ForPhaser1.SetIconNum(364)
ForPhaser1.SetIconPositionX(40.000000)
ForPhaser1.SetIconPositionY(50.000000)
ForPhaser1.SetIconAboveShip(1)
ForPhaser1.SetFireSound("DJPhaser")
ForPhaser1.SetMaxCharge(1.500000)
ForPhaser1.SetMaxDamage(2700.000000)
ForPhaser1.SetMaxDamageDistance(100.000000)
ForPhaser1.SetMinFiringCharge(1.500000)
ForPhaser1.SetNormalDischargeRate(2.500000)
ForPhaser1.SetRechargeRate(1.000000)
ForPhaser1.SetIndicatorIconNum(510)
ForPhaser1.SetIndicatorIconPositionX(36.000000)
ForPhaser1.SetIndicatorIconPositionY(45.000000)
ForPhaser1Forward = App.TGPoint3()
ForPhaser1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
ForPhaser1Up = App.TGPoint3()
ForPhaser1Up.SetXYZ(0.000000, 0.000000, 1.000000)
ForPhaser1.SetOrientation(ForPhaser1Forward, ForPhaser1Up)
ForPhaser1.SetWidth(0.001000)
ForPhaser1.SetLength(0.001000)
ForPhaser1.SetArcWidthAngles(-0.523599, 0.523599)
ForPhaser1.SetArcHeightAngles(-0.523599, 0.523599)
ForPhaser1.SetPhaserTextureStart(0)
ForPhaser1.SetPhaserTextureEnd(0)
ForPhaser1.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.000000, 0.000000, 1.000000)
ForPhaser1.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.501961, 1.000000)
ForPhaser1.SetInnerShellColor(kColor)
kColor.SetRGBA(0.976471, 0.792157, 0.674510, 1.000000)
ForPhaser1.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
ForPhaser1.SetInnerCoreColor(kColor)
ForPhaser1.SetNumSides(6)
ForPhaser1.SetMainRadius(0.140000)
ForPhaser1.SetTaperRadius(0.020000)
ForPhaser1.SetCoreScale(0.300000)
ForPhaser1.SetTaperRatio(0.250000)
ForPhaser1.SetTaperMinLength(30.000000)
ForPhaser1.SetTaperMaxLength(30.000000)
ForPhaser1.SetLengthTextureTilePerUnit(0.050000)
ForPhaser1.SetPerimeterTile(1.000000)
ForPhaser1.SetTextureSpeed(1.000000)
ForPhaser1.SetTextureName("data/DJPhaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForPhaser1)
#################################################
ForPhaser2 = App.PhaserProperty_Create("For Phaser 2")

ForPhaser2.SetMaxCondition(2000.000000)
ForPhaser2.SetCritical(0)
ForPhaser2.SetTargetable(1)
ForPhaser2.SetPrimary(1)
ForPhaser2.SetPosition(0.260000, 0.340000, 0.000000)
ForPhaser2.SetPosition2D(81.000000, 25.000000)
ForPhaser2.SetRepairComplexity(1.000000)
ForPhaser2.SetDisabledPercentage(0.400000)
ForPhaser2.SetRadius(0.250000)
ForPhaser2.SetDumbfire(0)
ForPhaser2.SetWeaponID(1)
ForPhaser2.SetGroups(0)
ForPhaser2.SetDamageRadiusFactor(0.250000)
ForPhaser2.SetIconNum(364)
ForPhaser2.SetIconPositionX(85.000000)
ForPhaser2.SetIconPositionY(51.000000)
ForPhaser2.SetIconAboveShip(1)
ForPhaser2.SetFireSound("DJPhaser")
ForPhaser2.SetMaxCharge(1.500000)
ForPhaser2.SetMaxDamage(2700.000000)
ForPhaser2.SetMaxDamageDistance(100.000000)
ForPhaser2.SetMinFiringCharge(1.500000)
ForPhaser2.SetNormalDischargeRate(2.500000)
ForPhaser2.SetRechargeRate(1.000000)
ForPhaser2.SetIndicatorIconNum(510)
ForPhaser2.SetIndicatorIconPositionX(81.000000)
ForPhaser2.SetIndicatorIconPositionY(46.000000)
ForPhaser2Forward = App.TGPoint3()
ForPhaser2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
ForPhaser2Up = App.TGPoint3()
ForPhaser2Up.SetXYZ(0.000000, 0.000000, 1.000000)
ForPhaser2.SetOrientation(ForPhaser2Forward, ForPhaser2Up)
ForPhaser2.SetWidth(0.001000)
ForPhaser2.SetLength(0.001000)
ForPhaser2.SetArcWidthAngles(-0.523599, 0.523599)
ForPhaser2.SetArcHeightAngles(-0.523599, 0.523599)
ForPhaser2.SetPhaserTextureStart(0)
ForPhaser2.SetPhaserTextureEnd(0)
ForPhaser2.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.000000, 0.000000, 1.000000)
ForPhaser2.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.501961, 1.000000)
ForPhaser2.SetInnerShellColor(kColor)
kColor.SetRGBA(0.976471, 0.792157, 0.674510, 1.000000)
ForPhaser2.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
ForPhaser2.SetInnerCoreColor(kColor)
ForPhaser2.SetNumSides(6)
ForPhaser2.SetMainRadius(0.140000)
ForPhaser2.SetTaperRadius(0.020000)
ForPhaser2.SetCoreScale(0.300000)
ForPhaser2.SetTaperRatio(0.250000)
ForPhaser2.SetTaperMinLength(30.000000)
ForPhaser2.SetTaperMaxLength(30.000000)
ForPhaser2.SetLengthTextureTilePerUnit(0.050000)
ForPhaser2.SetPerimeterTile(1.000000)
ForPhaser2.SetTextureSpeed(1.000000)
ForPhaser2.SetTextureName("data/DJPhaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForPhaser2)

# Property Set
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("DJEnterpriseG", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Drive", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Nacelle", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Starboard Nacelle", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Drive", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Starboard Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("FirstPerson", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Phasers", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Quantum Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Launcher 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Launcher 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("For Phaser 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("For Phaser 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)