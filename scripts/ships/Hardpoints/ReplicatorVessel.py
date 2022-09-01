# C:\Program Files\Activision\Bridge Commander\scripts\ships\Hardpoints\ReplicatorVessel.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
SublightEngine = App.EngineProperty_Create("Sublight Engine")

SublightEngine.SetMaxCondition(10000.000000)
SublightEngine.SetCritical(0)
SublightEngine.SetTargetable(1)
SublightEngine.SetPrimary(1)
SublightEngine.SetPosition(0.000000, -2.450000, 0.000000)
SublightEngine.SetPosition2D(60, 86)
SublightEngine.SetRepairComplexity(3.000000)
SublightEngine.SetDisabledPercentage(0.500000)
SublightEngine.SetRadius(0.250000)
SublightEngine.SetEngineType(SublightEngine.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightEngine)
#################################################
ReplicatorVessel = App.ShipProperty_Create("ReplicatorVessel")

ReplicatorVessel.SetGenus(1)
ReplicatorVessel.SetSpecies(781)
ReplicatorVessel.SetMass(3000.000000)
ReplicatorVessel.SetRotationalInertia(300.000000)
ReplicatorVessel.SetShipName("ReplicatorVessel")
ReplicatorVessel.SetModelFilename("data/Models/Ships/ReplicatorVessel/ReplicatorVessel.nif")
ReplicatorVessel.SetDamageResolution(0.000100)
ReplicatorVessel.SetAffiliation(0)
ReplicatorVessel.SetStationary(0)
ReplicatorVessel.SetAIString("FedAttack")
ReplicatorVessel.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(ReplicatorVessel)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(22000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.700000, 0.100000)
ShieldGenerator.SetPosition2D(65, 39)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.400000)
ShieldGenerator.SetNormalPowerPerSecond(1200.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.223529, 0.749020, 0.968628, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 65000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 65000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 65000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 65000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 65000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 65000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 40.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 40.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 40.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 40.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 40.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 40.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(40000.000000)
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

SensorArray.SetMaxCondition(8000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 3.750000, 0.350000)
SensorArray.SetPosition2D(65, 25)
SensorArray.SetRepairComplexity(2.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.250000)
SensorArray.SetNormalPowerPerSecond(100.000000)
SensorArray.SetBaseSensorRange(900.000000)
SensorArray.SetMaxProbes(6)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
PowerGenerator = App.PowerProperty_Create("Power Generator")

PowerGenerator.SetMaxCondition(18500.000000)
PowerGenerator.SetCritical(1)
PowerGenerator.SetTargetable(1)
PowerGenerator.SetPrimary(1)
PowerGenerator.SetPosition(0.000000, -1.200000, 0.000000)
PowerGenerator.SetPosition2D(65, 71)
PowerGenerator.SetRepairComplexity(3.000000)
PowerGenerator.SetDisabledPercentage(0.500000)
PowerGenerator.SetRadius(0.300000)
PowerGenerator.SetMainBatteryLimit(2000000.000000)
PowerGenerator.SetBackupBatteryLimit(100000.000000)
PowerGenerator.SetMainConduitCapacity(2500.000000)
PowerGenerator.SetBackupConduitCapacity(500.000000)
PowerGenerator.SetPowerOutput(2500.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerGenerator)
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
SublightEngines.SetMaxAccel(5.000000)
SublightEngines.SetMaxAngularAccel(0.400000)
SublightEngines.SetMaxAngularVelocity(0.400000)
SublightEngines.SetMaxSpeed(6.000000)
SublightEngines.SetEngineSound("RepEngine")
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightEngines)
#################################################
Hyperdrive1 = App.HullProperty_Create("Hyperdrive 1")

Hyperdrive1.SetMaxCondition(6000.000000)
Hyperdrive1.SetCritical(0)
Hyperdrive1.SetTargetable(1)
Hyperdrive1.SetPrimary(0)
Hyperdrive1.SetPosition(0.000000, -2.400000, 0.000000)
Hyperdrive1.SetPosition2D(70, 86)
Hyperdrive1.SetRepairComplexity(1.000000)
Hyperdrive1.SetDisabledPercentage(0.000000)
Hyperdrive1.SetRadius(0.025000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hyperdrive1)
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
Engineering.SetMaxRepairPoints(70.000000)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 4.600000, 0.275000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -1.650000, 1.200000)
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
ViewscreenLeftPosition.SetXYZ(-0.450000, 0.000000, 1.000000)
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
ViewscreenRightPosition.SetXYZ(0.450000, 0.000000, 1.000000)
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
ViewscreenUpPosition.SetXYZ(0.000000, 0.000000, 3.100000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.000000, -4.100000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 0.000000, 0.000000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
MainWeapons = App.WeaponSystemProperty_Create("Main Weapons")

MainWeapons.SetMaxCondition(15000.000000)
MainWeapons.SetCritical(0)
MainWeapons.SetTargetable(0)
MainWeapons.SetPrimary(1)
MainWeapons.SetPosition(0.000000, 0.000000, 0.000000)
MainWeapons.SetPosition2D(0.000000, 0.000000)
MainWeapons.SetRepairComplexity(1.000000)
MainWeapons.SetDisabledPercentage(0.500000)
MainWeapons.SetRadius(0.250000)
MainWeapons.SetNormalPowerPerSecond(150.000000)
MainWeapons.SetWeaponSystemType(MainWeapons.WST_PHASER)
MainWeapons.SetSingleFire(1)
MainWeapons.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
MainWeapons.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(MainWeapons)
#################################################
Beam1 = App.PhaserProperty_Create("Beam 1")

Beam1.SetMaxCondition(7000.000000)
Beam1.SetCritical(0)
Beam1.SetTargetable(1)
Beam1.SetPrimary(1)
Beam1.SetPosition(0.000000, 1.250000, 2.262500)
Beam1.SetPosition2D(65, 11)
Beam1.SetRepairComplexity(1.000000)
Beam1.SetDisabledPercentage(0.500000)
Beam1.SetRadius(0.250000)
Beam1.SetDumbfire(0)
Beam1.SetWeaponID(0)
Beam1.SetGroups(0)
Beam1.SetDamageRadiusFactor(0.250000)
Beam1.SetIconNum(364)
Beam1.SetIconPositionX(64)
Beam1.SetIconPositionY(39)
Beam1.SetIconAboveShip(1)
Beam1.SetFireSound("RepBeam")
Beam1.SetMaxCharge(0.750000)
Beam1.SetMaxDamage(10000.000000)
Beam1.SetMaxDamageDistance(100.000000)
Beam1.SetMinFiringCharge(0.750000)
Beam1.SetNormalDischargeRate(1.000000)
Beam1.SetRechargeRate(0.750000)
Beam1.SetIndicatorIconNum(510)
Beam1.SetIndicatorIconPositionX(58)
Beam1.SetIndicatorIconPositionY(34)
Beam1Forward = App.TGPoint3()
Beam1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Beam1Up = App.TGPoint3()
Beam1Up.SetXYZ(0.000000, 0.000000, 1.000000)
Beam1.SetOrientation(Beam1Forward, Beam1Up)
Beam1.SetWidth(0.001000)
Beam1.SetLength(0.001000)
Beam1.SetArcWidthAngles(-0.872665, 0.872665)
Beam1.SetArcHeightAngles(-0.349066, 1.221731)
Beam1.SetPhaserTextureStart(0)
Beam1.SetPhaserTextureEnd(1)
Beam1.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.501961, 1.000000, 0.329412)
Beam1.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 0.501961, 0.749020, 0.419608)
Beam1.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 1.000000, 0.749020)
Beam1.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.501961, 1.000000, 1.000000, 0.784314)
Beam1.SetInnerCoreColor(kColor)
Beam1.SetNumSides(6)
Beam1.SetMainRadius(0.150000)
Beam1.SetTaperRadius(0.010000)
Beam1.SetCoreScale(0.500000)
Beam1.SetTaperRatio(0.250000)
Beam1.SetTaperMinLength(5.000000)
Beam1.SetTaperMaxLength(30.000000)
Beam1.SetLengthTextureTilePerUnit(0.500000)
Beam1.SetPerimeterTile(1.000000)
Beam1.SetTextureSpeed(2.500000)
Beam1.SetTextureName("data/textures/tactical/ZZ_ENT4sPhaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Beam1)
#################################################
Beam2 = App.PhaserProperty_Create("Beam 2")

Beam2.SetMaxCondition(7000.000000)
Beam2.SetCritical(0)
Beam2.SetTargetable(1)
Beam2.SetPrimary(1)
Beam2.SetPosition(0.000000, 2.000000, -2.750000)
Beam2.SetPosition2D(65, 53)
Beam2.SetRepairComplexity(1.000000)
Beam2.SetDisabledPercentage(0.500000)
Beam2.SetRadius(0.250000)
Beam2.SetDumbfire(0)
Beam2.SetWeaponID(0)
Beam2.SetGroups(0)
Beam2.SetDamageRadiusFactor(0.250000)
Beam2.SetIconNum(364)
Beam2.SetIconPositionX(64)
Beam2.SetIconPositionY(61)
Beam2.SetIconAboveShip(1)
Beam2.SetFireSound("RepBeam")
Beam2.SetMaxCharge(0.750000)
Beam2.SetMaxDamage(10000.000000)
Beam2.SetMaxDamageDistance(100.000000)
Beam2.SetMinFiringCharge(0.750000)
Beam2.SetNormalDischargeRate(1.000000)
Beam2.SetRechargeRate(0.750000)
Beam2.SetIndicatorIconNum(510)
Beam2.SetIndicatorIconPositionX(58)
Beam2.SetIndicatorIconPositionY(57)
Beam2Forward = App.TGPoint3()
Beam2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Beam2Up = App.TGPoint3()
Beam2Up.SetXYZ(0.000000, 0.000000, 1.000000)
Beam2.SetOrientation(Beam2Forward, Beam2Up)
Beam2.SetWidth(0.001000)
Beam2.SetLength(0.001000)
Beam2.SetArcWidthAngles(-0.872665, 0.872665)
Beam2.SetArcHeightAngles(-1.221731, 0.436332)
Beam2.SetPhaserTextureStart(0)
Beam2.SetPhaserTextureEnd(1)
Beam2.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.501961, 1.000000, 0.329412)
Beam2.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 0.501961, 0.749020, 0.419608)
Beam2.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 1.000000, 0.749020)
Beam2.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.501961, 1.000000, 1.000000, 0.784314)
Beam2.SetInnerCoreColor(kColor)
Beam2.SetNumSides(6)
Beam2.SetMainRadius(0.150000)
Beam2.SetTaperRadius(0.010000)
Beam2.SetCoreScale(0.500000)
Beam2.SetTaperRatio(0.250000)
Beam2.SetTaperMinLength(5.000000)
Beam2.SetTaperMaxLength(30.000000)
Beam2.SetLengthTextureTilePerUnit(0.500000)
Beam2.SetPerimeterTile(1.000000)
Beam2.SetTextureSpeed(2.500000)
Beam2.SetTextureName("data/textures/tactical/ZZ_ENT4sPhaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Beam2)
#################################################
Beam3 = App.PhaserProperty_Create("Beam 3")

Beam3.SetMaxCondition(7000.000000)
Beam3.SetCritical(0)
Beam3.SetTargetable(1)
Beam3.SetPrimary(1)
Beam3.SetPosition(-4.535000, 2.150000, -1.025000)
Beam3.SetPosition2D(14, 40)
Beam3.SetRepairComplexity(1.000000)
Beam3.SetDisabledPercentage(0.500000)
Beam3.SetRadius(0.250000)
Beam3.SetDumbfire(0)
Beam3.SetWeaponID(0)
Beam3.SetGroups(0)
Beam3.SetDamageRadiusFactor(0.250000)
Beam3.SetIconNum(364)
Beam3.SetIconPositionX(27)
Beam3.SetIconPositionY(50)
Beam3.SetIconAboveShip(1)
Beam3.SetFireSound("RepBeam")
Beam3.SetMaxCharge(0.750000)
Beam3.SetMaxDamage(10000.000000)
Beam3.SetMaxDamageDistance(100.000000)
Beam3.SetMinFiringCharge(0.750000)
Beam3.SetNormalDischargeRate(1.000000)
Beam3.SetRechargeRate(0.750000)
Beam3.SetIndicatorIconNum(510)
Beam3.SetIndicatorIconPositionX(21)
Beam3.SetIndicatorIconPositionY(46)
Beam3Forward = App.TGPoint3()
Beam3Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Beam3Up = App.TGPoint3()
Beam3Up.SetXYZ(0.000000, 0.000000, 1.000000)
Beam3.SetOrientation(Beam3Forward, Beam3Up)
Beam3.SetWidth(0.001000)
Beam3.SetLength(0.001000)
Beam3.SetArcWidthAngles(-1.047198, 1.047198)
Beam3.SetArcHeightAngles(-0.872665, 0.872665)
Beam3.SetPhaserTextureStart(0)
Beam3.SetPhaserTextureEnd(1)
Beam3.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.501961, 1.000000, 0.329412)
Beam3.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 0.501961, 0.749020, 0.419608)
Beam3.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 1.000000, 0.749020)
Beam3.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.501961, 1.000000, 1.000000, 0.784314)
Beam3.SetInnerCoreColor(kColor)
Beam3.SetNumSides(6)
Beam3.SetMainRadius(0.150000)
Beam3.SetTaperRadius(0.010000)
Beam3.SetCoreScale(0.500000)
Beam3.SetTaperRatio(0.250000)
Beam3.SetTaperMinLength(5.000000)
Beam3.SetTaperMaxLength(30.000000)
Beam3.SetLengthTextureTilePerUnit(0.500000)
Beam3.SetPerimeterTile(1.000000)
Beam3.SetTextureSpeed(2.500000)
Beam3.SetTextureName("data/textures/tactical/ZZ_ENT4sPhaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Beam3)
#################################################
Beam4 = App.PhaserProperty_Create("Beam 4")

Beam4.SetMaxCondition(7000.000000)
Beam4.SetCritical(0)
Beam4.SetTargetable(1)
Beam4.SetPrimary(1)
Beam4.SetPosition(4.535000, 2.150000, -1.025000)
Beam4.SetPosition2D(118, 40)
Beam4.SetRepairComplexity(1.000000)
Beam4.SetDisabledPercentage(0.500000)
Beam4.SetRadius(0.250000)
Beam4.SetDumbfire(0)
Beam4.SetWeaponID(0)
Beam4.SetGroups(0)
Beam4.SetDamageRadiusFactor(0.250000)
Beam4.SetIconNum(364)
Beam4.SetIconPositionX(102)
Beam4.SetIconPositionY(50)
Beam4.SetIconAboveShip(1)
Beam4.SetFireSound("RepBeam")
Beam4.SetMaxCharge(0.750000)
Beam4.SetMaxDamage(10000.000000)
Beam4.SetMaxDamageDistance(100.000000)
Beam4.SetMinFiringCharge(0.750000)
Beam4.SetNormalDischargeRate(1.000000)
Beam4.SetRechargeRate(0.750000)
Beam4.SetIndicatorIconNum(510)
Beam4.SetIndicatorIconPositionX(96)
Beam4.SetIndicatorIconPositionY(46)
Beam4Forward = App.TGPoint3()
Beam4Forward.SetXYZ(0.000000, 1.000000, 0.000000)
Beam4Up = App.TGPoint3()
Beam4Up.SetXYZ(0.000000, 0.000000, 1.000000)
Beam4.SetOrientation(Beam4Forward, Beam4Up)
Beam4.SetWidth(0.001000)
Beam4.SetLength(0.001000)
Beam4.SetArcWidthAngles(-1.047198, 1.047198)
Beam4.SetArcHeightAngles(-0.872665, 0.872665)
Beam4.SetPhaserTextureStart(0)
Beam4.SetPhaserTextureEnd(1)
Beam4.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.501961, 1.000000, 0.329412)
Beam4.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 0.501961, 0.749020, 0.419608)
Beam4.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 1.000000, 0.749020)
Beam4.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.501961, 1.000000, 1.000000, 0.784314)
Beam4.SetInnerCoreColor(kColor)
Beam4.SetNumSides(6)
Beam4.SetMainRadius(0.150000)
Beam4.SetTaperRadius(0.010000)
Beam4.SetCoreScale(0.500000)
Beam4.SetTaperRatio(0.250000)
Beam4.SetTaperMinLength(5.000000)
Beam4.SetTaperMaxLength(30.000000)
Beam4.SetLengthTextureTilePerUnit(0.500000)
Beam4.SetPerimeterTile(1.000000)
Beam4.SetTextureSpeed(2.500000)
Beam4.SetTextureName("data/textures/tactical/ZZ_ENT4sPhaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Beam4)
#################################################
Beam5 = App.PhaserProperty_Create("Beam 5")

Beam5.SetMaxCondition(7000.000000)
Beam5.SetCritical(0)
Beam5.SetTargetable(1)
Beam5.SetPrimary(1)
Beam5.SetPosition(0.000000, -2.850000, -1.400000)
Beam5.SetPosition2D(65, 101)
Beam5.SetRepairComplexity(1.000000)
Beam5.SetDisabledPercentage(0.500000)
Beam5.SetRadius(0.250000)
Beam5.SetDumbfire(0)
Beam5.SetWeaponID(0)
Beam5.SetGroups(0)
Beam5.SetDamageRadiusFactor(0.250000)
Beam5.SetIconNum(363)
Beam5.SetIconPositionX(64)
Beam5.SetIconPositionY(106)
Beam5.SetIconAboveShip(1)
Beam5.SetFireSound("RepBeam")
Beam5.SetMaxCharge(0.750000)
Beam5.SetMaxDamage(10000.000000)
Beam5.SetMaxDamageDistance(100.000000)
Beam5.SetMinFiringCharge(0.750000)
Beam5.SetNormalDischargeRate(1.000000)
Beam5.SetRechargeRate(0.750000)
Beam5.SetIndicatorIconNum(511)
Beam5.SetIndicatorIconPositionX(58)
Beam5.SetIndicatorIconPositionY(101)
Beam5Forward = App.TGPoint3()
Beam5Forward.SetXYZ(0.000000, -1.000000, 0.000000)
Beam5Up = App.TGPoint3()
Beam5Up.SetXYZ(0.000000, 0.000000, 1.000000)
Beam5.SetOrientation(Beam5Forward, Beam5Up)
Beam5.SetWidth(0.001000)
Beam5.SetLength(0.001000)
Beam5.SetArcWidthAngles(-0.872665, 0.872665)
Beam5.SetArcHeightAngles(-0.698132, 0.698132)
Beam5.SetPhaserTextureStart(0)
Beam5.SetPhaserTextureEnd(1)
Beam5.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.501961, 1.000000, 0.329412)
Beam5.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 0.501961, 0.749020, 0.419608)
Beam5.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 1.000000, 0.749020)
Beam5.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.501961, 1.000000, 1.000000, 0.784314)
Beam5.SetInnerCoreColor(kColor)
Beam5.SetNumSides(6)
Beam5.SetMainRadius(0.150000)
Beam5.SetTaperRadius(0.010000)
Beam5.SetCoreScale(0.500000)
Beam5.SetTaperRatio(0.250000)
Beam5.SetTaperMinLength(5.000000)
Beam5.SetTaperMaxLength(30.000000)
Beam5.SetLengthTextureTilePerUnit(0.500000)
Beam5.SetPerimeterTile(1.000000)
Beam5.SetTextureSpeed(2.500000)
Beam5.SetTextureName("data/textures/tactical/ZZ_ENT4sPhaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Beam5)
#################################################
Beam6 = App.PhaserProperty_Create("Beam 6")

Beam6.SetMaxCondition(7000.000000)
Beam6.SetCritical(0)
Beam6.SetTargetable(1)
Beam6.SetPrimary(1)
Beam6.SetPosition(-1.685000, -3.375000, -0.270000)
Beam6.SetPosition2D(43, 77)
Beam6.SetRepairComplexity(1.000000)
Beam6.SetDisabledPercentage(0.500000)
Beam6.SetRadius(0.250000)
Beam6.SetDumbfire(0)
Beam6.SetWeaponID(0)
Beam6.SetGroups(0)
Beam6.SetDamageRadiusFactor(0.250000)
Beam6.SetIconNum(363)
Beam6.SetIconPositionX(39)
Beam6.SetIconPositionY(91)
Beam6.SetIconAboveShip(1)
Beam6.SetFireSound("RepBeam")
Beam6.SetMaxCharge(0.750000)
Beam6.SetMaxDamage(10000.000000)
Beam6.SetMaxDamageDistance(100.000000)
Beam6.SetMinFiringCharge(0.750000)
Beam6.SetNormalDischargeRate(1.000000)
Beam6.SetRechargeRate(0.750000)
Beam6.SetIndicatorIconNum(511)
Beam6.SetIndicatorIconPositionX(33)
Beam6.SetIndicatorIconPositionY(85)
Beam6Forward = App.TGPoint3()
Beam6Forward.SetXYZ(0.000000, -1.000000, 0.000000)
Beam6Up = App.TGPoint3()
Beam6Up.SetXYZ(0.000000, 0.000000, 1.000000)
Beam6.SetOrientation(Beam6Forward, Beam6Up)
Beam6.SetWidth(0.001000)
Beam6.SetLength(0.001000)
Beam6.SetArcWidthAngles(-0.872665, 0.872665)
Beam6.SetArcHeightAngles(-0.872665, 0.872665)
Beam6.SetPhaserTextureStart(0)
Beam6.SetPhaserTextureEnd(1)
Beam6.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.501961, 1.000000, 0.329412)
Beam6.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 0.501961, 0.749020, 0.419608)
Beam6.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 1.000000, 0.749020)
Beam6.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.501961, 1.000000, 1.000000, 0.784314)
Beam6.SetInnerCoreColor(kColor)
Beam6.SetNumSides(6)
Beam6.SetMainRadius(0.150000)
Beam6.SetTaperRadius(0.010000)
Beam6.SetCoreScale(0.500000)
Beam6.SetTaperRatio(0.250000)
Beam6.SetTaperMinLength(5.000000)
Beam6.SetTaperMaxLength(30.000000)
Beam6.SetLengthTextureTilePerUnit(0.500000)
Beam6.SetPerimeterTile(1.000000)
Beam6.SetTextureSpeed(2.500000)
Beam6.SetTextureName("data/textures/tactical/ZZ_ENT4sPhaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Beam6)
#################################################
Beam7 = App.PhaserProperty_Create("Beam 7")

Beam7.SetMaxCondition(7000.000000)
Beam7.SetCritical(0)
Beam7.SetTargetable(1)
Beam7.SetPrimary(1)
Beam7.SetPosition(1.685000, -3.375000, -0.270000)
Beam7.SetPosition2D(88, 77)
Beam7.SetRepairComplexity(1.000000)
Beam7.SetDisabledPercentage(0.500000)
Beam7.SetRadius(0.250000)
Beam7.SetDumbfire(0)
Beam7.SetWeaponID(0)
Beam7.SetGroups(0)
Beam7.SetDamageRadiusFactor(0.250000)
Beam7.SetIconNum(363)
Beam7.SetIconPositionX(89)
Beam7.SetIconPositionY(91)
Beam7.SetIconAboveShip(1)
Beam7.SetFireSound("RepBeam")
Beam7.SetMaxCharge(0.750000)
Beam7.SetMaxDamage(10000.000000)
Beam7.SetMaxDamageDistance(100.000000)
Beam7.SetMinFiringCharge(0.750000)
Beam7.SetNormalDischargeRate(1.000000)
Beam7.SetRechargeRate(0.750000)
Beam7.SetIndicatorIconNum(511)
Beam7.SetIndicatorIconPositionX(83)
Beam7.SetIndicatorIconPositionY(85)
Beam7Forward = App.TGPoint3()
Beam7Forward.SetXYZ(0.000000, -1.000000, 0.000000)
Beam7Up = App.TGPoint3()
Beam7Up.SetXYZ(0.000000, 0.000000, 1.000000)
Beam7.SetOrientation(Beam7Forward, Beam7Up)
Beam7.SetWidth(0.001000)
Beam7.SetLength(0.001000)
Beam7.SetArcWidthAngles(-0.872665, 0.872665)
Beam7.SetArcHeightAngles(-0.872665, 0.872665)
Beam7.SetPhaserTextureStart(0)
Beam7.SetPhaserTextureEnd(1)
Beam7.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.501961, 1.000000, 0.329412)
Beam7.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 0.501961, 0.749020, 0.419608)
Beam7.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 1.000000, 1.000000, 0.749020)
Beam7.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.501961, 1.000000, 1.000000, 0.784314)
Beam7.SetInnerCoreColor(kColor)
Beam7.SetNumSides(6)
Beam7.SetMainRadius(0.150000)
Beam7.SetTaperRadius(0.010000)
Beam7.SetCoreScale(0.500000)
Beam7.SetTaperRatio(0.250000)
Beam7.SetTaperMinLength(5.000000)
Beam7.SetTaperMaxLength(30.000000)
Beam7.SetLengthTextureTilePerUnit(0.500000)
Beam7.SetPerimeterTile(1.000000)
Beam7.SetTextureSpeed(2.500000)
Beam7.SetTextureName("data/textures/tactical/ZZ_ENT4sPhaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Beam7)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Power Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hyperdrive 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("ReplicatorVessel", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Main Weapons", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Beam 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Beam 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Beam 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Beam 4", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Beam 5", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Beam 6", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Beam 7", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
