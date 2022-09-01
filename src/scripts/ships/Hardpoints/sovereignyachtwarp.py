# C:\J-Single-testing-KM1\scripts\ships\Hardpoints\sovereignyachtwarp.py
# This file was automatically generated - modify at your own risk.
#   checked systems,  uncritizled repair

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Torpedo1 = App.TorpedoTubeProperty_Create("Torpedo 1")

Torpedo1.SetMaxCondition(200.000000)
Torpedo1.SetCritical(0)
Torpedo1.SetTargetable(1)
Torpedo1.SetPrimary(1)
Torpedo1.SetPosition(0.002065, 0.123506, 0.014171)
Torpedo1.SetPosition2D(1.000000, 114.000000)
Torpedo1.SetRepairComplexity(2.000000)
Torpedo1.SetDisabledPercentage(0.500000)
Torpedo1.SetRadius(0.200000)
Torpedo1.SetDumbfire(1)
Torpedo1.SetWeaponID(8)
Torpedo1.SetGroups(1)
Torpedo1.SetDamageRadiusFactor(0.200000)
Torpedo1.SetIconNum(365)
Torpedo1.SetIconPositionX(82.000000)
Torpedo1.SetIconPositionY(60.000000)
Torpedo1.SetIconAboveShip(1)
Torpedo1.SetImmediateDelay(0.250000)
Torpedo1.SetReloadDelay(25.000000)
Torpedo1.SetMaxReady(1)
Torpedo1Direction = App.TGPoint3()
Torpedo1Direction.SetXYZ(0.000000, 1.000000, 0.000000)
Torpedo1.SetDirection(Torpedo1Direction)
Torpedo1Right = App.TGPoint3()
Torpedo1Right.SetXYZ(1.000000, 0.000000, 0.000000)
Torpedo1.SetRight(Torpedo1Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedo1)
#################################################
Torpedo2 = App.TorpedoTubeProperty_Create("Torpedo 2")

Torpedo2.SetMaxCondition(200.000000)
Torpedo2.SetCritical(0)
Torpedo2.SetTargetable(1)
Torpedo2.SetPrimary(1)
Torpedo2.SetPosition(-0.003276, 0.123489, 0.014191)
Torpedo2.SetPosition2D(21.000000, 115.000000)
Torpedo2.SetRepairComplexity(2.000000)
Torpedo2.SetDisabledPercentage(0.500000)
Torpedo2.SetRadius(0.200000)
Torpedo2.SetDumbfire(1)
Torpedo2.SetWeaponID(19)
Torpedo2.SetGroups(1)
Torpedo2.SetDamageRadiusFactor(0.200000)
Torpedo2.SetIconNum(365)
Torpedo2.SetIconPositionX(71.000000)
Torpedo2.SetIconPositionY(60.000000)
Torpedo2.SetIconAboveShip(1)
Torpedo2.SetImmediateDelay(0.350000)
Torpedo2.SetReloadDelay(25.000000)
Torpedo2.SetMaxReady(1)
Torpedo2Direction = App.TGPoint3()
Torpedo2Direction.SetXYZ(0.000000, 1.000000, 0.000000)
Torpedo2.SetDirection(Torpedo2Direction)
Torpedo2Right = App.TGPoint3()
Torpedo2Right.SetXYZ(1.000000, 0.000000, 0.000000)
Torpedo2.SetRight(Torpedo2Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(Torpedo2)
#################################################
TorpedoSystem = App.TorpedoSystemProperty_Create("Torpedo System")

TorpedoSystem.SetMaxCondition(1000.000000)
TorpedoSystem.SetCritical(0)
TorpedoSystem.SetTargetable(0)
TorpedoSystem.SetPrimary(1)
TorpedoSystem.SetPosition(0.000000, 0.040000, 0.000000)
TorpedoSystem.SetPosition2D(0.000000, 0.000000)
TorpedoSystem.SetRepairComplexity(1.000000)
TorpedoSystem.SetDisabledPercentage(0.500000)
TorpedoSystem.SetRadius(0.010000)
TorpedoSystem.SetNormalPowerPerSecond(5.000000)
TorpedoSystem.SetWeaponSystemType(TorpedoSystem.WST_TORPEDO)
TorpedoSystem.SetSingleFire(1)
TorpedoSystem.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
TorpedoSystem.SetFiringChainString(kFiringChainString)
TorpedoSystem.SetMaxTorpedoes(0, 20)
TorpedoSystem.SetTorpedoScript(0, "Tactical.Projectiles.PhotonTorpedo3")
TorpedoSystem.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(TorpedoSystem)
#################################################
StarWarp = App.EngineProperty_Create("Star Warp")

StarWarp.SetMaxCondition(500.000000)
StarWarp.SetCritical(0)
StarWarp.SetTargetable(1)
StarWarp.SetPrimary(1)
StarWarp.SetPosition(0.093765, -0.099183, 0.020167)
StarWarp.SetPosition2D(135.000000, 101.000000)
StarWarp.SetRepairComplexity(1.000000)
StarWarp.SetDisabledPercentage(0.500000)
StarWarp.SetRadius(0.030000)
StarWarp.SetEngineType(StarWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarWarp)
#################################################
PortWarp = App.EngineProperty_Create("Port Warp")

PortWarp.SetMaxCondition(500.000000)
PortWarp.SetCritical(0)
PortWarp.SetTargetable(1)
PortWarp.SetPrimary(1)
PortWarp.SetPosition(-0.095399, -0.096733, 0.020195)
PortWarp.SetPosition2D(124.000000, 101.000000)
PortWarp.SetRepairComplexity(1.000000)
PortWarp.SetDisabledPercentage(0.500000)
PortWarp.SetRadius(0.020000)
PortWarp.SetEngineType(PortWarp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortWarp)
#################################################
ForPhaser1 = App.PhaserProperty_Create("For Phaser 1")

ForPhaser1.SetMaxCondition(500.000000)
ForPhaser1.SetCritical(0)
ForPhaser1.SetTargetable(1)
ForPhaser1.SetPrimary(1)
ForPhaser1.SetPosition(-0.023769, 0.121797, 0.009784)
ForPhaser1.SetPosition2D(-2.000000, 25.000000)
ForPhaser1.SetRepairComplexity(3.000000)
ForPhaser1.SetDisabledPercentage(0.500000)
ForPhaser1.SetRadius(0.030000)
ForPhaser1.SetDumbfire(0)
ForPhaser1.SetWeaponID(1)
ForPhaser1.SetGroups(1)
ForPhaser1.SetDamageRadiusFactor(0.100000)
ForPhaser1.SetIconNum(364)
ForPhaser1.SetIconPositionX(64.000000)
ForPhaser1.SetIconPositionY(43.000000)
ForPhaser1.SetIconAboveShip(1)
ForPhaser1.SetFireSound("FedBurst")
ForPhaser1.SetMaxCharge(1.000000)
ForPhaser1.SetMaxDamage(700.000000)
ForPhaser1.SetMaxDamageDistance(40.000000)
ForPhaser1.SetMinFiringCharge(1.000000)
ForPhaser1.SetNormalDischargeRate(1.000000)
ForPhaser1.SetRechargeRate(1.000000)
ForPhaser1.SetIndicatorIconNum(510)
ForPhaser1.SetIndicatorIconPositionX(58.000000)
ForPhaser1.SetIndicatorIconPositionY(34.000000)
ForPhaser1Forward = App.TGPoint3()
ForPhaser1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
ForPhaser1Up = App.TGPoint3()
ForPhaser1Up.SetXYZ(0.000000, 0.000000, 1.000000)
ForPhaser1.SetOrientation(ForPhaser1Forward, ForPhaser1Up)
ForPhaser1.SetWidth(0.012000)
ForPhaser1.SetLength(0.001000)
ForPhaser1.SetArcWidthAngles(-0.506145, 0.506145)
ForPhaser1.SetArcHeightAngles(-0.017453, 0.610865)
ForPhaser1.SetPhaserTextureStart(0)
ForPhaser1.SetPhaserTextureEnd(7)
ForPhaser1.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
ForPhaser1.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
ForPhaser1.SetInnerShellColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.000000, 1.000000)
ForPhaser1.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.501961, 1.000000)
ForPhaser1.SetInnerCoreColor(kColor)
ForPhaser1.SetNumSides(6)
ForPhaser1.SetMainRadius(0.009000)
ForPhaser1.SetTaperRadius(0.010000)
ForPhaser1.SetCoreScale(0.500000)
ForPhaser1.SetTaperRatio(0.250000)
ForPhaser1.SetTaperMinLength(5.000000)
ForPhaser1.SetTaperMaxLength(30.000000)
ForPhaser1.SetLengthTextureTilePerUnit(0.500000)
ForPhaser1.SetPerimeterTile(1.000000)
ForPhaser1.SetTextureSpeed(2.500000)
ForPhaser1.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForPhaser1)
#################################################
ForPhaser2 = App.PhaserProperty_Create("For Phaser 2")

ForPhaser2.SetMaxCondition(500.000000)
ForPhaser2.SetCritical(0)
ForPhaser2.SetTargetable(1)
ForPhaser2.SetPrimary(1)
ForPhaser2.SetPosition(0.022141, 0.121953, 0.009820)
ForPhaser2.SetPosition2D(9.000000, 25.000000)
ForPhaser2.SetRepairComplexity(3.000000)
ForPhaser2.SetDisabledPercentage(0.500000)
ForPhaser2.SetRadius(0.030000)
ForPhaser2.SetDumbfire(0)
ForPhaser2.SetWeaponID(1)
ForPhaser2.SetGroups(1)
ForPhaser2.SetDamageRadiusFactor(0.100000)
ForPhaser2.SetIconNum(364)
ForPhaser2.SetIconPositionX(64.000000)
ForPhaser2.SetIconPositionY(64.000000)
ForPhaser2.SetIconAboveShip(1)
ForPhaser2.SetFireSound("FedBurst")
ForPhaser2.SetMaxCharge(1.000000)
ForPhaser2.SetMaxDamage(700.000000)
ForPhaser2.SetMaxDamageDistance(40.000000)
ForPhaser2.SetMinFiringCharge(1.000000)
ForPhaser2.SetNormalDischargeRate(1.000000)
ForPhaser2.SetRechargeRate(1.000000)
ForPhaser2.SetIndicatorIconNum(510)
ForPhaser2.SetIndicatorIconPositionX(58.000000)
ForPhaser2.SetIndicatorIconPositionY(50.000000)
ForPhaser2Forward = App.TGPoint3()
ForPhaser2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
ForPhaser2Up = App.TGPoint3()
ForPhaser2Up.SetXYZ(0.000000, 0.000000, 1.000000)
ForPhaser2.SetOrientation(ForPhaser2Forward, ForPhaser2Up)
ForPhaser2.SetWidth(0.012000)
ForPhaser2.SetLength(0.001000)
ForPhaser2.SetArcWidthAngles(-0.506145, 0.506145)
ForPhaser2.SetArcHeightAngles(-0.017453, 0.610865)
ForPhaser2.SetPhaserTextureStart(0)
ForPhaser2.SetPhaserTextureEnd(7)
ForPhaser2.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
ForPhaser2.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
ForPhaser2.SetInnerShellColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.000000, 1.000000)
ForPhaser2.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.501961, 1.000000)
ForPhaser2.SetInnerCoreColor(kColor)
ForPhaser2.SetNumSides(6)
ForPhaser2.SetMainRadius(0.009000)
ForPhaser2.SetTaperRadius(0.010000)
ForPhaser2.SetCoreScale(0.500000)
ForPhaser2.SetTaperRatio(0.250000)
ForPhaser2.SetTaperMinLength(5.000000)
ForPhaser2.SetTaperMaxLength(30.000000)
ForPhaser2.SetLengthTextureTilePerUnit(0.500000)
ForPhaser2.SetPerimeterTile(1.000000)
ForPhaser2.SetTextureSpeed(2.500000)
ForPhaser2.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForPhaser2)
#################################################
PortAftPhaser = App.PhaserProperty_Create("Port Aft Phaser")

PortAftPhaser.SetMaxCondition(500.000000)
PortAftPhaser.SetCritical(0)
PortAftPhaser.SetTargetable(1)
PortAftPhaser.SetPrimary(1)
PortAftPhaser.SetPosition(-0.041235, -0.092327, 0.010561)
PortAftPhaser.SetPosition2D(-2.000000, 45.000000)
PortAftPhaser.SetRepairComplexity(3.000000)
PortAftPhaser.SetDisabledPercentage(0.500000)
PortAftPhaser.SetRadius(0.030000)
PortAftPhaser.SetDumbfire(0)
PortAftPhaser.SetWeaponID(1)
PortAftPhaser.SetGroups(1)
PortAftPhaser.SetDamageRadiusFactor(0.100000)
PortAftPhaser.SetIconNum(361)
PortAftPhaser.SetIconPositionX(44.000000)
PortAftPhaser.SetIconPositionY(90.000000)
PortAftPhaser.SetIconAboveShip(1)
PortAftPhaser.SetFireSound("FedBurst")
PortAftPhaser.SetMaxCharge(1.000000)
PortAftPhaser.SetMaxDamage(700.000000)
PortAftPhaser.SetMaxDamageDistance(40.000000)
PortAftPhaser.SetMinFiringCharge(1.000000)
PortAftPhaser.SetNormalDischargeRate(1.000000)
PortAftPhaser.SetRechargeRate(1.000000)
PortAftPhaser.SetIndicatorIconNum(508)
PortAftPhaser.SetIndicatorIconPositionX(33.000000)
PortAftPhaser.SetIndicatorIconPositionY(90.000000)
PortAftPhaserForward = App.TGPoint3()
PortAftPhaserForward.SetXYZ(-0.970148, -0.016934, 0.241922)
PortAftPhaserUp = App.TGPoint3()
PortAftPhaserUp.SetXYZ(0.241885, 0.004222, 0.970296)
PortAftPhaser.SetOrientation(PortAftPhaserForward, PortAftPhaserUp)
PortAftPhaser.SetWidth(0.005000)
PortAftPhaser.SetLength(0.001000)
PortAftPhaser.SetArcWidthAngles(-0.698132, 1.047198)
PortAftPhaser.SetArcHeightAngles(-0.034907, 1.047198)
PortAftPhaser.SetPhaserTextureStart(0)
PortAftPhaser.SetPhaserTextureEnd(7)
PortAftPhaser.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
PortAftPhaser.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
PortAftPhaser.SetInnerShellColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.000000, 1.000000)
PortAftPhaser.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.501961, 1.000000)
PortAftPhaser.SetInnerCoreColor(kColor)
PortAftPhaser.SetNumSides(6)
PortAftPhaser.SetMainRadius(0.009000)
PortAftPhaser.SetTaperRadius(0.010000)
PortAftPhaser.SetCoreScale(0.500000)
PortAftPhaser.SetTaperRatio(0.250000)
PortAftPhaser.SetTaperMinLength(5.000000)
PortAftPhaser.SetTaperMaxLength(30.000000)
PortAftPhaser.SetLengthTextureTilePerUnit(0.500000)
PortAftPhaser.SetPerimeterTile(1.000000)
PortAftPhaser.SetTextureSpeed(2.500000)
PortAftPhaser.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(PortAftPhaser)
#################################################
StarImpulse = App.EngineProperty_Create("Star Impulse")

StarImpulse.SetMaxCondition(600.000000)
StarImpulse.SetCritical(0)
StarImpulse.SetTargetable(1)
StarImpulse.SetPrimary(1)
StarImpulse.SetPosition(0.023781, -0.110358, 0.014258)
StarImpulse.SetPosition2D(137.000000, 54.000000)
StarImpulse.SetRepairComplexity(1.000000)
StarImpulse.SetDisabledPercentage(0.500000)
StarImpulse.SetRadius(0.005000)
StarImpulse.SetEngineType(StarImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarImpulse)
#################################################
PortImpulse = App.EngineProperty_Create("Port Impulse")

PortImpulse.SetMaxCondition(600.000000)
PortImpulse.SetCritical(0)
PortImpulse.SetTargetable(1)
PortImpulse.SetPrimary(1)
PortImpulse.SetPosition(-0.026065, -0.109924, 0.014683)
PortImpulse.SetPosition2D(126.000000, 54.000000)
PortImpulse.SetRepairComplexity(1.000000)
PortImpulse.SetDisabledPercentage(0.500000)
PortImpulse.SetRadius(0.005000)
PortImpulse.SetEngineType(PortImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortImpulse)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(1000.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, -0.050000, 0.000000)
ImpulseEngines.SetPosition2D(52.000000, 59.000000)
ImpulseEngines.SetRepairComplexity(2.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.010000)
ImpulseEngines.SetNormalPowerPerSecond(5.000000)
ImpulseEngines.SetMaxAccel(6.500000)
ImpulseEngines.SetMaxAngularAccel(0.900000)
ImpulseEngines.SetMaxAngularVelocity(0.900000)
ImpulseEngines.SetMaxSpeed(9.400000)
ImpulseEngines.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(1600.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(0)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.000000, -0.020000, 0.000000)
WarpEngines.SetPosition2D(79.000000, 59.000000)
WarpEngines.SetRepairComplexity(1.000000)
WarpEngines.SetDisabledPercentage(0.500000)
WarpEngines.SetRadius(0.015000)
WarpEngines.SetNormalPowerPerSecond(5.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")

RepairSystem.SetMaxCondition(800.000000)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(0)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(-0.000850, 0.060526, 0.000000)
RepairSystem.SetPosition2D(52.000000, 59.000000)
RepairSystem.SetRepairComplexity(4.000000)
RepairSystem.SetDisabledPercentage(0.500000)
RepairSystem.SetRadius(0.003000)
RepairSystem.SetNormalPowerPerSecond(5.000000)
RepairSystem.SetMaxRepairPoints(10.000000)
RepairSystem.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(1000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(-0.001210, -0.021553, 0.038296)
SensorArray.SetPosition2D(128.000000, 0.000000)
SensorArray.SetRepairComplexity(0.400000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.010000)
SensorArray.SetNormalPowerPerSecond(5.000000)
SensorArray.SetBaseSensorRange(1000.000000)
SensorArray.SetMaxProbes(2)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
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
ViewscreenRightPosition.SetXYZ(0.035175, -0.103602, 0.013142)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
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
ViewscreenLeftPosition.SetXYZ(-0.037095, -0.105353, 0.013614)
ViewscreenLeft.SetPosition(ViewscreenLeftPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenLeft)
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
ViewscreenBackPosition.SetXYZ(0.000131, -0.118370, 0.005947)
ViewscreenBack.SetPosition(ViewscreenBackPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenBack)
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
ViewscreenForwardPosition.SetXYZ(-0.000759, 0.149145, 0.008626)
ViewscreenForward.SetPosition(ViewscreenForwardPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenForward)
#################################################
ViewscreenUp = App.PositionOrientationProperty_Create("ViewscreenUp")

ViewscreenUpForward = App.TGPoint3()
ViewscreenUpForward.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenUpUp = App.TGPoint3()
ViewscreenUpUp.SetXYZ(0.000000, -1.000000, 0.000000)
ViewscreenUpRight = App.TGPoint3()
ViewscreenUpRight.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenUp.SetOrientation(ViewscreenUpForward, ViewscreenUpUp, ViewscreenUpRight)
ViewscreenUpPosition = App.TGPoint3()
ViewscreenUpPosition.SetXYZ(-0.001306, -0.021034, 0.038295)
ViewscreenUp.SetPosition(ViewscreenUpPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenUp)
#################################################
ViewscreenDown = App.PositionOrientationProperty_Create("ViewscreenDown")

ViewscreenDownForward = App.TGPoint3()
ViewscreenDownForward.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenDownUp = App.TGPoint3()
ViewscreenDownUp.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenDownRight = App.TGPoint3()
ViewscreenDownRight.SetXYZ(-1.000000, 0.000000, 0.000000)
ViewscreenDown.SetOrientation(ViewscreenDownForward, ViewscreenDownUp, ViewscreenDownRight)
ViewscreenDownPosition = App.TGPoint3()
ViewscreenDownPosition.SetXYZ(0.000043, -0.016264, -0.008485)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 0.400000, 0.000000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
sovereignyacht = App.ShipProperty_Create("sovereignyacht")

sovereignyacht.SetGenus(1)
sovereignyacht.SetSpecies(135)
sovereignyacht.SetMass(15.000000)
sovereignyacht.SetRotationalInertia(2000.000000)
sovereignyacht.SetShipName("Sovereign Yacht")
sovereignyacht.SetModelFilename("data/Models/Ships/sovereignyacht/sovereignyacht.nif")
sovereignyacht.SetDamageResolution(6.000000)
sovereignyacht.SetAffiliation(0)
sovereignyacht.SetStationary(0)
sovereignyacht.SetAIString("FedAttack")
sovereignyacht.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(sovereignyacht)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(1000.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(-0.001484, -0.054858, -0.008485)
WarpCore.SetPosition2D(119.000000, 22.000000)
WarpCore.SetRepairComplexity(1.000000)
WarpCore.SetDisabledPercentage(0.500000)
WarpCore.SetRadius(0.020000)
WarpCore.SetMainBatteryLimit(13000.000000)
WarpCore.SetBackupBatteryLimit(3000.000000)
WarpCore.SetMainConduitCapacity(200.000000)
WarpCore.SetBackupConduitCapacity(30.000000)
WarpCore.SetPowerOutput(160.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(1000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(-0.000052, -0.016000, -0.008485)
ShieldGenerator.SetPosition2D(107.000000, 3.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.010000)
ShieldGenerator.SetNormalPowerPerSecond(5.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 0.000000, 1.000000, 0.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 5000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 5000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 5000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 5000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 5000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 5000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 15.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 15.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 15.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 15.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 15.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 15.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(3500.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, -0.010000, 0.000000)
Hull.SetPosition2D(63.000000, 55.000000)
Hull.SetRepairComplexity(1.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.140000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
PhaserArray = App.WeaponSystemProperty_Create("Phaser Array")

PhaserArray.SetMaxCondition(1200.000000)
PhaserArray.SetCritical(0)
PhaserArray.SetTargetable(0)
PhaserArray.SetPrimary(1)
PhaserArray.SetPosition(0.000000, 0.000000, 0.000000)
PhaserArray.SetPosition2D(79.000000, 59.000000)
PhaserArray.SetRepairComplexity(1.000000)
PhaserArray.SetDisabledPercentage(0.500000)
PhaserArray.SetRadius(0.002500)
PhaserArray.SetNormalPowerPerSecond(5.000000)
PhaserArray.SetWeaponSystemType(PhaserArray.WST_PHASER)
PhaserArray.SetSingleFire(1)
PhaserArray.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
PhaserArray.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(PhaserArray)
#################################################
StarAftPhaser = App.PhaserProperty_Create("Star Aft Phaser")

StarAftPhaser.SetMaxCondition(500.000000)
StarAftPhaser.SetCritical(0)
StarAftPhaser.SetTargetable(1)
StarAftPhaser.SetPrimary(1)
StarAftPhaser.SetPosition(0.039175, -0.085743, 0.010697)
StarAftPhaser.SetPosition2D(8.000000, 45.000000)
StarAftPhaser.SetRepairComplexity(3.000000)
StarAftPhaser.SetDisabledPercentage(0.500000)
StarAftPhaser.SetRadius(0.030000)
StarAftPhaser.SetDumbfire(0)
StarAftPhaser.SetWeaponID(1)
StarAftPhaser.SetGroups(1)
StarAftPhaser.SetDamageRadiusFactor(0.100000)
StarAftPhaser.SetIconNum(362)
StarAftPhaser.SetIconPositionX(101.000000)
StarAftPhaser.SetIconPositionY(90.000000)
StarAftPhaser.SetIconAboveShip(1)
StarAftPhaser.SetFireSound("FedBurst")
StarAftPhaser.SetMaxCharge(1.000000)
StarAftPhaser.SetMaxDamage(700.000000)
StarAftPhaser.SetMaxDamageDistance(40.000000)
StarAftPhaser.SetMinFiringCharge(1.000000)
StarAftPhaser.SetNormalDischargeRate(1.000000)
StarAftPhaser.SetRechargeRate(1.000000)
StarAftPhaser.SetIndicatorIconNum(509)
StarAftPhaser.SetIndicatorIconPositionX(100.000000)
StarAftPhaser.SetIndicatorIconPositionY(90.000000)
StarAftPhaserForward = App.TGPoint3()
StarAftPhaserForward.SetXYZ(0.981022, 0.034727, 0.190759)
StarAftPhaserUp = App.TGPoint3()
StarAftPhaserUp.SetXYZ(-0.190759, -0.003344, 0.981631)
StarAftPhaser.SetOrientation(StarAftPhaserForward, StarAftPhaserUp)
StarAftPhaser.SetWidth(0.005000)
StarAftPhaser.SetLength(0.001000)
StarAftPhaser.SetArcWidthAngles(-0.698132, 1.047198)
StarAftPhaser.SetArcHeightAngles(-0.034907, 1.047198)
StarAftPhaser.SetPhaserTextureStart(0)
StarAftPhaser.SetPhaserTextureEnd(7)
StarAftPhaser.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
StarAftPhaser.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
StarAftPhaser.SetInnerShellColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.000000, 1.000000)
StarAftPhaser.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.501961, 1.000000)
StarAftPhaser.SetInnerCoreColor(kColor)
StarAftPhaser.SetNumSides(6)
StarAftPhaser.SetMainRadius(0.009000)
StarAftPhaser.SetTaperRadius(0.010000)
StarAftPhaser.SetCoreScale(0.500000)
StarAftPhaser.SetTaperRatio(0.250000)
StarAftPhaser.SetTaperMinLength(5.000000)
StarAftPhaser.SetTaperMaxLength(30.000000)
StarAftPhaser.SetLengthTextureTilePerUnit(0.500000)
StarAftPhaser.SetPerimeterTile(1.000000)
StarAftPhaser.SetTextureSpeed(2.500000)
StarAftPhaser.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(StarAftPhaser)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Torpedo 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Phaser Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("For Phaser 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Aft Phaser", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("For Phaser 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("sovereignyacht", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Aft Phaser", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
