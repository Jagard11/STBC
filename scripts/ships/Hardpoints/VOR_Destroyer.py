#####  Created by:
#####  Bridge Commander Universal Tool
# C:\Program Files\Activision\Bridge Commander\scripts\ships\Hardpoints\VOR_Fighter.py


import App
import GlobalPropertyTemplates

# Local Templates
#################################################
BioOrganicHull = App.HullProperty_Create("Bio Organic Hull")

BioOrganicHull.SetMaxCondition(4000.000000)
BioOrganicHull.SetCritical(1)
BioOrganicHull.SetTargetable(1)
BioOrganicHull.SetPrimary(1)
BioOrganicHull.SetPosition(0.009189, 0.237915, 0.118693)
BioOrganicHull.SetPosition2D(64.000000, 50.000000)
BioOrganicHull.SetRepairComplexity(1.500000)
BioOrganicHull.SetDisabledPercentage(0.000000)
BioOrganicHull.SetRadius(0.550000)
App.g_kModelPropertyManager.RegisterLocalTemplate(BioOrganicHull)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(5000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(0)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.009189, 0.237915, 0.118693)
ShieldGenerator.SetPosition2D(64.000000, 50.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.000000)
ShieldGenerator.SetRadius(0.180000)
ShieldGenerator.SetNormalPowerPerSecond(1.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 0.999993, 0.200000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 600.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 600.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 600.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 600.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 600.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 600.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 600.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 300.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 400.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 400.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 400.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 400.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(2100.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.003716, 0.535871, -0.194414)
SensorArray.SetPosition2D(64.000000, 10.000000)
SensorArray.SetRepairComplexity(0.500000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.170000)
SensorArray.SetNormalPowerPerSecond(150.000000)
SensorArray.SetBaseSensorRange(3500.000000)
SensorArray.SetMaxProbes(15)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(3000.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.009189, 0.237915, 0.118693)
WarpCore.SetPosition2D(64.000000, 30.000000)
WarpCore.SetRepairComplexity(2.000000)
WarpCore.SetDisabledPercentage(0.750000)
WarpCore.SetRadius(0.200000)
WarpCore.SetMainBatteryLimit(1500000.000000)
WarpCore.SetBackupBatteryLimit(50000.000000)
WarpCore.SetMainConduitCapacity(9000.000000)
WarpCore.SetBackupConduitCapacity(1000.000000)
WarpCore.SetPowerOutput(400.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(3900.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, -3.440000, 0.000000)
ImpulseEngines.SetPosition2D(0.000000, 0.000000)
ImpulseEngines.SetRepairComplexity(3.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.250000)
ImpulseEngines.SetNormalPowerPerSecond(50.000000)
ImpulseEngines.SetMaxAccel(4.000000)
ImpulseEngines.SetMaxAngularAccel(1.000000)
ImpulseEngines.SetMaxAngularVelocity(1.500000)
ImpulseEngines.SetMaxSpeed(10.000000)
ImpulseEngines.SetEngineSound("VOR_SmallEngines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
RegenerationSystem = App.RepairSubsystemProperty_Create("Regeneration System")

RegenerationSystem.SetMaxCondition(5000.000000)
RegenerationSystem.SetCritical(0)
RegenerationSystem.SetTargetable(0)
RegenerationSystem.SetPrimary(1)
RegenerationSystem.SetPosition(-0.008684, -0.140950, 0.114832)
RegenerationSystem.SetPosition2D(64.000000, 40.000000)
RegenerationSystem.SetRepairComplexity(4.000000)
RegenerationSystem.SetDisabledPercentage(0.100000)
RegenerationSystem.SetRadius(0.250000)
RegenerationSystem.SetNormalPowerPerSecond(1.000000)
RegenerationSystem.SetMaxRepairPoints(400.000000)
RegenerationSystem.SetNumRepairTeams(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(RegenerationSystem)
#################################################
Torpedoes = App.TorpedoSystemProperty_Create("Torpedoes")

Torpedoes.SetMaxCondition(1000.000000)
Torpedoes.SetCritical(0)
Torpedoes.SetTargetable(0)
Torpedoes.SetPrimary(1)
Torpedoes.SetPosition(0.015140, 0.981951, 0.062888)
Torpedoes.SetPosition2D(82.000000, 64.000000)
Torpedoes.SetRepairComplexity(2.000000)
Torpedoes.SetDisabledPercentage(0.750000)
Torpedoes.SetRadius(0.300000)
Torpedoes.SetNormalPowerPerSecond(1.000000)
Torpedoes.SetWeaponSystemType(Torpedoes.WST_TORPEDO)
Torpedoes.SetSingleFire(0)
Torpedoes.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Torpedoes.SetFiringChainString(kFiringChainString)
Torpedoes.SetMaxTorpedoes(0, 50)
Torpedoes.SetTorpedoScript(0, "Tactical.Projectiles.Vorlonweapon")
Torpedoes.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedoes)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 3.000000, 0.100000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.700000, 0.100000)
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
ViewscreenLeftPosition.SetXYZ(0.000000, 3.000000, 0.100000)
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
ViewscreenRightPosition.SetXYZ(0.000000, 3.000000, 0.000000)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
#################################################
ViewscreenUp = App.PositionOrientationProperty_Create("ViewscreenUp")

ViewscreenUpForward = App.TGPoint3()
ViewscreenUpForward.SetXYZ(0.000000, 0.000000, 0.000000)
ViewscreenUpUp = App.TGPoint3()
ViewscreenUpUp.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenUpRight = App.TGPoint3()
ViewscreenUpRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenUp.SetOrientation(ViewscreenUpForward, ViewscreenUpUp, ViewscreenUpRight)
ViewscreenUpPosition = App.TGPoint3()
ViewscreenUpPosition.SetXYZ(0.000000, 3.000000, 0.100000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 3.000000, -0.100000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 2.200000, 0.100000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
GraviticEngine = App.EngineProperty_Create("Gravitic Engine")

GraviticEngine.SetMaxCondition(1500.000000)
GraviticEngine.SetCritical(0)
GraviticEngine.SetTargetable(1)
GraviticEngine.SetPrimary(1)
GraviticEngine.SetPosition(0.000000, -3.535871, -0.190000)
GraviticEngine.SetPosition2D(32.000000, 40.000000)
GraviticEngine.SetRepairComplexity(3.000000)
GraviticEngine.SetDisabledPercentage(0.500000)
GraviticEngine.SetRadius(0.070000)
GraviticEngine.SetEngineType(GraviticEngine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(GraviticEngine)
#################################################
GraviticEngine2 = App.EngineProperty_Create("Backup Gravitic Engine")

GraviticEngine2.SetMaxCondition(1500.000000)
GraviticEngine2.SetCritical(0)
GraviticEngine2.SetTargetable(1)
GraviticEngine2.SetPrimary(1)
GraviticEngine2.SetPosition(0.000000, 2.501430, 0.000000)
GraviticEngine2.SetPosition2D(32.000000, 40.000000)
GraviticEngine2.SetRepairComplexity(3.000000)
GraviticEngine2.SetDisabledPercentage(0.500000)
GraviticEngine2.SetRadius(0.070000)
GraviticEngine2.SetEngineType(GraviticEngine2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(GraviticEngine2)
#################################################
VOR_Destroyer = App.ShipProperty_Create("VOR_Destroyer")

VOR_Destroyer.SetGenus(1)
VOR_Destroyer.SetSpecies(101)
VOR_Destroyer.SetMass(750.000000)
VOR_Destroyer.SetRotationalInertia(3000.000000)
VOR_Destroyer.SetShipName("VOR_Destroyer")
VOR_Destroyer.SetModelFilename("data/Models/Ships/VOR_Destroyer/VOR_Destroyer.nif")
VOR_Destroyer.SetDamageResolution(8.000000)
VOR_Destroyer.SetAffiliation(0)
VOR_Destroyer.SetStationary(0)
VOR_Destroyer.SetAIString("FedAttack")
VOR_Destroyer.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(VOR_Destroyer)
#################################################
VorlonBeam = App.WeaponSystemProperty_Create("Vorlon Beam")

VorlonBeam.SetMaxCondition(2400.000000)
VorlonBeam.SetCritical(0)
VorlonBeam.SetTargetable(0)
VorlonBeam.SetPrimary(1)
VorlonBeam.SetPosition(0.000000, 0.000000, 0.000000)
VorlonBeam.SetPosition2D(46.000000, 64.000000)
VorlonBeam.SetRepairComplexity(4.000000)
VorlonBeam.SetDisabledPercentage(0.500000)
VorlonBeam.SetRadius(0.300000)
VorlonBeam.SetNormalPowerPerSecond(200.000000)
VorlonBeam.SetWeaponSystemType(VorlonBeam.WST_PHASER)
VorlonBeam.SetSingleFire(0)
VorlonBeam.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
VorlonBeam.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(VorlonBeam)
#################################################
BiobeamEmitter = App.PhaserProperty_Create("Biobeam Emitter")

BiobeamEmitter.SetMaxCondition(2000.000000)
BiobeamEmitter.SetCritical(0)
BiobeamEmitter.SetTargetable(0)
BiobeamEmitter.SetPrimary(1)
BiobeamEmitter.SetPosition(0.000000, 3.440000, 0.000000)
BiobeamEmitter.SetPosition2D(65.000000, 5.000000)
BiobeamEmitter.SetRepairComplexity(2.000000)
BiobeamEmitter.SetDisabledPercentage(0.500000)
BiobeamEmitter.SetRadius(0.250000)
BiobeamEmitter.SetDumbfire(0)
BiobeamEmitter.SetWeaponID(0)
BiobeamEmitter.SetGroups(31)
BiobeamEmitter.SetDamageRadiusFactor(0.150000)
BiobeamEmitter.SetIconNum(364)
BiobeamEmitter.SetIconPositionX(65.000000)
BiobeamEmitter.SetIconPositionY(50.000000)
BiobeamEmitter.SetIconAboveShip(1)
BiobeamEmitter.SetFireSound("VOR_LG")
BiobeamEmitter.SetMaxCharge(10.000000)
BiobeamEmitter.SetMaxDamage(2500.000000)
BiobeamEmitter.SetMaxDamageDistance(80.000000)
BiobeamEmitter.SetMinFiringCharge(5.000000)
BiobeamEmitter.SetNormalDischargeRate(3.000000)
BiobeamEmitter.SetRechargeRate(1.000000)
BiobeamEmitter.SetIndicatorIconNum(364)
BiobeamEmitter.SetIndicatorIconPositionX(65.000000)
BiobeamEmitter.SetIndicatorIconPositionY(55.000000)
BiobeamEmitterForward = App.TGPoint3()
BiobeamEmitterForward.SetXYZ(0.000000, 1.000000, 0.000000)
BiobeamEmitterUp = App.TGPoint3()
BiobeamEmitterUp.SetXYZ(0.000000, 0.000000, 1.000000)
BiobeamEmitter.SetOrientation(BiobeamEmitterForward, BiobeamEmitterUp)
BiobeamEmitter.SetWidth(0.100000)
BiobeamEmitter.SetLength(0.100000)
BiobeamEmitter.SetArcWidthAngles(-0.139626, 0.139626)
BiobeamEmitter.SetArcHeightAngles(-0.385398, 0.385398)
BiobeamEmitter.SetPhaserTextureStart(0)
BiobeamEmitter.SetPhaserTextureEnd(7)
BiobeamEmitter.SetPhaserWidth(0.900000)
kColor = App.TGColorA()
kColor.SetRGBA(0.70000, 1.000000, 0.300000, 1.000000)
BiobeamEmitter.SetOuterShellColor(kColor)
kColor.SetRGBA(0.40000, 1.000000, 0.100000, 0.500000)
BiobeamEmitter.SetInnerShellColor(kColor)
kColor.SetRGBA(0.10000, 1.000000, 0.100000, 0.80000)
BiobeamEmitter.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.10000, 1.000000, 0.100000, 0.100000)
BiobeamEmitter.SetInnerCoreColor(kColor)
BiobeamEmitter.SetNumSides(6)
BiobeamEmitter.SetMainRadius(0.200000)
BiobeamEmitter.SetTaperRadius(0.200000)
BiobeamEmitter.SetCoreScale(0.750000)
BiobeamEmitter.SetTaperRatio(0.750000)
BiobeamEmitter.SetTaperMinLength(5.000000)
BiobeamEmitter.SetTaperMaxLength(30.000000)
BiobeamEmitter.SetLengthTextureTilePerUnit(0.500000)
BiobeamEmitter.SetPerimeterTile(1.000000)
BiobeamEmitter.SetTextureSpeed(4.000000)
BiobeamEmitter.SetTextureName("data/VORLON_Lightning.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(BiobeamEmitter)
#################################################
CutterDecoration = App.PhaserProperty_Create("PulseDefenseBeam")

CutterDecoration.SetMaxCondition(2000.000000)
CutterDecoration.SetCritical(0)
CutterDecoration.SetTargetable(0)
CutterDecoration.SetPrimary(0)
CutterDecoration.SetPosition(0.000000, 3.440000, 0.000000)
CutterDecoration.SetPosition2D(65.000000, 5.000000)
CutterDecoration.SetRepairComplexity(2.000000)
CutterDecoration.SetDisabledPercentage(0.500000)
CutterDecoration.SetRadius(0.250000)
CutterDecoration.SetDumbfire(0)
CutterDecoration.SetWeaponID(0)
CutterDecoration.SetGroups(31)
CutterDecoration.SetDamageRadiusFactor(0.150000)
CutterDecoration.SetIconNum(0)
CutterDecoration.SetIconPositionX(0.000000)
CutterDecoration.SetIconPositionY(0.000000)
CutterDecoration.SetIconAboveShip(1)
CutterDecoration.SetFireSound("")
CutterDecoration.SetMaxCharge(0.050000)
CutterDecoration.SetMaxDamage(1.000000)
CutterDecoration.SetMaxDamageDistance(80.000000)
CutterDecoration.SetMinFiringCharge(0.010000)
CutterDecoration.SetNormalDischargeRate(1.000000)
CutterDecoration.SetRechargeRate(5.000000)
CutterDecoration.SetIndicatorIconNum(0)
CutterDecoration.SetIndicatorIconPositionX(0.000000)
CutterDecoration.SetIndicatorIconPositionY(0.000000)
CutterDecorationForward = App.TGPoint3()
CutterDecorationForward.SetXYZ(0.000000, 1.000000, 0.000000)
CutterDecorationUp = App.TGPoint3()
CutterDecorationUp.SetXYZ(0.000000, 0.000000, 1.000000)
CutterDecoration.SetOrientation(CutterDecorationForward, CutterDecorationUp)
CutterDecoration.SetWidth(0.100000)
CutterDecoration.SetLength(0.100000)
CutterDecoration.SetArcWidthAngles(-0.139626, 0.139626)
CutterDecoration.SetArcHeightAngles(-0.385398, 0.385398)
CutterDecoration.SetPhaserTextureStart(0)
CutterDecoration.SetPhaserTextureEnd(7)
CutterDecoration.SetPhaserWidth(0.350000)
kColor = App.TGColorA()
kColor.SetRGBA(0.30000, 1.000000, 0.300000, 1.000000)
CutterDecoration.SetOuterShellColor(kColor)
kColor.SetRGBA(0.00000, 1.000000, 0.100000, 0.500000)
CutterDecoration.SetInnerShellColor(kColor)
kColor.SetRGBA(0.10000, 1.000000, 0.100000, 0.80000)
CutterDecoration.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.10000, 1.000000, 0.100000, 0.100000)
CutterDecoration.SetInnerCoreColor(kColor)
CutterDecoration.SetNumSides(6)
CutterDecoration.SetMainRadius(0.070000)
CutterDecoration.SetTaperRadius(0.500000)
CutterDecoration.SetCoreScale(0.500000)
CutterDecoration.SetTaperRatio(0.250000)
CutterDecoration.SetTaperMinLength(10.000000)
CutterDecoration.SetTaperMaxLength(40.000000)
CutterDecoration.SetLengthTextureTilePerUnit(0.010000)
CutterDecoration.SetPerimeterTile(1.000000)
CutterDecoration.SetTextureSpeed(0.000001)
CutterDecoration.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(CutterDecoration)
#################################################
JumpspaceDriveA = App.HullProperty_Create("Jumpspace Drive 1")

JumpspaceDriveA.SetMaxCondition(800.000000)
JumpspaceDriveA.SetCritical(0)
JumpspaceDriveA.SetTargetable(1)
JumpspaceDriveA.SetPrimary(0)
JumpspaceDriveA.SetPosition(0.000000, -3.000000, 0.000000)
JumpspaceDriveA.SetPosition2D(75.000000, 40.000000)
JumpspaceDriveA.SetRepairComplexity(3.000000)
JumpspaceDriveA.SetDisabledPercentage(0.750000)
JumpspaceDriveA.SetRadius(0.200000)
App.g_kModelPropertyManager.RegisterLocalTemplate(JumpspaceDriveA)
#################################################
Tractors = App.WeaponSystemProperty_Create("Tractors")

Tractors.SetMaxCondition(3500.000000)
Tractors.SetCritical(0)
Tractors.SetTargetable(0)
Tractors.SetPrimary(1)
Tractors.SetPosition(-0.500000, 2.440000, 0.100000)
Tractors.SetPosition2D(120.000000, 120.000000)
Tractors.SetRepairComplexity(1.000000)
Tractors.SetDisabledPercentage(0.750000)
Tractors.SetRadius(0.250000)
Tractors.SetNormalPowerPerSecond(100.000000)
Tractors.SetWeaponSystemType(Tractors.WST_TRACTOR)
Tractors.SetSingleFire(1)
Tractors.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Tractors.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Tractors)
#################################################
ForwardTractor = App.TractorBeamProperty_Create("Forward Tractor")

ForwardTractor.SetMaxCondition(3500.000000)
ForwardTractor.SetCritical(0)
ForwardTractor.SetTargetable(1)
ForwardTractor.SetPrimary(1)
ForwardTractor.SetPosition(0.000000, 3.000000, 0.000000)
ForwardTractor.SetPosition2D(64.000000, 54.000000)
ForwardTractor.SetRepairComplexity(2.000000)
ForwardTractor.SetDisabledPercentage(0.750000)
ForwardTractor.SetRadius(0.200000)
ForwardTractor.SetDumbfire(0)
ForwardTractor.SetWeaponID(1)
ForwardTractor.SetGroups(0)
ForwardTractor.SetDamageRadiusFactor(0.900000)
ForwardTractor.SetIconNum(0)
ForwardTractor.SetIconPositionX(0.000000)
ForwardTractor.SetIconPositionY(0.000000)
ForwardTractor.SetIconAboveShip(1)
ForwardTractor.SetFireSound("Tractor Beam")
ForwardTractor.SetMaxCharge(5.000000)
ForwardTractor.SetMaxDamage(7000.000000)
ForwardTractor.SetMaxDamageDistance(100.000000)
ForwardTractor.SetMinFiringCharge(3.000000)
ForwardTractor.SetNormalDischargeRate(1.000000)
ForwardTractor.SetRechargeRate(0.300000)
ForwardTractor.SetIndicatorIconNum(0)
ForwardTractor.SetIndicatorIconPositionX(0.000000)
ForwardTractor.SetIndicatorIconPositionY(0.000000)
ForwardTractorForward = App.TGPoint3()
ForwardTractorForward.SetXYZ(0.000000, 1.000000, 0.000000)
ForwardTractorUp = App.TGPoint3()
ForwardTractorUp.SetXYZ(0.000000, 0.000000, 1.000000)
ForwardTractor.SetOrientation(ForwardTractorForward, ForwardTractorUp)
ForwardTractor.SetArcWidthAngles(-0.872665, 0.872665)
ForwardTractor.SetArcHeightAngles(-0.872665, 0.000000)
ForwardTractor.SetTractorBeamWidth(0.300000)
ForwardTractor.SetTextureStart(0)
ForwardTractor.SetTextureEnd(0)
ForwardTractor.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.400000, 1.000000, 0.800000, 1.000000)
ForwardTractor.SetOuterShellColor(kColor)
kColor.SetRGBA(0.400000, 1.000000, 0.800000, 1.000000)
ForwardTractor.SetInnerShellColor(kColor)
kColor.SetRGBA(0.400000, 1.000000, 0.800000, 1.000000)
ForwardTractor.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.400000, 1.000000, 0.800000, 1.000000)
ForwardTractor.SetInnerCoreColor(kColor)
ForwardTractor.SetNumSides(12)
ForwardTractor.SetMainRadius(0.075000)
ForwardTractor.SetTaperRadius(0.000000)
ForwardTractor.SetCoreScale(0.450000)
ForwardTractor.SetTaperRatio(0.200000)
ForwardTractor.SetTaperMinLength(1.000000)
ForwardTractor.SetTaperMaxLength(5.000000)
ForwardTractor.SetLengthTextureTilePerUnit(0.250000)
ForwardTractor.SetPerimeterTile(1.000000)
ForwardTractor.SetTextureSpeed(0.200000)
ForwardTractor.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForwardTractor)
#################################################
AftTractor = App.TractorBeamProperty_Create("Aft Tractor")

AftTractor.SetMaxCondition(3500.000000)
AftTractor.SetCritical(0)
AftTractor.SetTargetable(1)
AftTractor.SetPrimary(1)
AftTractor.SetPosition(0.003716, -3.535871, -0.194414)
AftTractor.SetPosition2D(64.000000, 59.000000)
AftTractor.SetRepairComplexity(2.000000)
AftTractor.SetDisabledPercentage(0.750000)
AftTractor.SetRadius(0.150000)
AftTractor.SetDumbfire(0)
AftTractor.SetWeaponID(1)
AftTractor.SetGroups(0)
AftTractor.SetDamageRadiusFactor(0.900000)
AftTractor.SetIconNum(0)
AftTractor.SetIconPositionX(0.000000)
AftTractor.SetIconPositionY(0.000000)
AftTractor.SetIconAboveShip(1)
AftTractor.SetFireSound("Tractor Beam")
AftTractor.SetMaxCharge(5.000000)
AftTractor.SetMaxDamage(7000.000000)
AftTractor.SetMaxDamageDistance(100.000000)
AftTractor.SetMinFiringCharge(3.000000)
AftTractor.SetNormalDischargeRate(1.000000)
AftTractor.SetRechargeRate(0.300000)
AftTractor.SetIndicatorIconNum(0)
AftTractor.SetIndicatorIconPositionX(0.000000)
AftTractor.SetIndicatorIconPositionY(0.000000)
AftTractorForward = App.TGPoint3()
AftTractorForward.SetXYZ(0.000000, -1.000000, 0.000000)
AftTractorUp = App.TGPoint3()
AftTractorUp.SetXYZ(0.000000, 0.000000, 1.000000)
AftTractor.SetOrientation(AftTractorForward, AftTractorUp)
AftTractor.SetArcWidthAngles(-0.698132, 0.698132)
AftTractor.SetArcHeightAngles(-0.698132, 0.000000)
AftTractor.SetTractorBeamWidth(0.300000)
AftTractor.SetTextureStart(0)
AftTractor.SetTextureEnd(0)
AftTractor.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.400000, 1.000000, 0.800000, 1.000000)
AftTractor.SetOuterShellColor(kColor)
kColor.SetRGBA(0.400000, 1.000000, 0.800000, 1.000000)
AftTractor.SetInnerShellColor(kColor)
kColor.SetRGBA(0.400000, 1.000000, 0.800000, 1.000000)
AftTractor.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.400000, 1.000000, 0.800000, 1.000000)
AftTractor.SetInnerCoreColor(kColor)
AftTractor.SetNumSides(12)
AftTractor.SetMainRadius(0.075000)
AftTractor.SetTaperRadius(0.000000)
AftTractor.SetCoreScale(0.450000)
AftTractor.SetTaperRatio(0.200000)
AftTractor.SetTaperMinLength(1.000000)
AftTractor.SetTaperMaxLength(5.000000)
AftTractor.SetLengthTextureTilePerUnit(0.250000)
AftTractor.SetPerimeterTile(1.000000)
AftTractor.SetTextureSpeed(0.200000)
AftTractor.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(AftTractor)
#################################################

# Property Set
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Bio Organic Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Jumpspace Drive 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Regeneration System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenForward", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("ViewscreenBack", App.TGModelPropertyManager.LOCAL_TEMPLATES)
        if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedoes", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Gravitic Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Backup Gravitic Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("VOR_Destroyer", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Vorlon Beam", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Biobeam Emitter", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("PulseDefenseBeam", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractors", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Forward Tractor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Aft Tractor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
