# C:\Program Files\Activision\Bridge Commander\src\edited hps\FedConstOpen.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(4000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 3.000000, 0.000000)
Hull.SetPosition2D(64.000000, 60.000000)
Hull.SetRepairComplexity(3.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(400.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.000000, 0.000000, 0.000000)
ImpulseEngines.SetPosition2D(0.000000, 0.000000)
ImpulseEngines.SetRepairComplexity(4.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.250000)
ImpulseEngines.SetNormalPowerPerSecond(100.000000)
ImpulseEngines.SetMaxAccel(0.000000)
ImpulseEngines.SetMaxAngularAccel(0.000000)
ImpulseEngines.SetMaxAngularVelocity(0.020000)
ImpulseEngines.SetMaxSpeed(0.000000)
ImpulseEngines.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(2000.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, 2.000000, 0.000000)
WarpCore.SetPosition2D(64.000000, 80.000000)
WarpCore.SetRepairComplexity(2.000000)
WarpCore.SetDisabledPercentage(0.750000)
WarpCore.SetRadius(0.300000)
WarpCore.SetMainBatteryLimit(120000.000000)
WarpCore.SetBackupBatteryLimit(50000.000000)
WarpCore.SetMainConduitCapacity(800.000000)
WarpCore.SetBackupConduitCapacity(100.000000)
WarpCore.SetPowerOutput(700.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")

RepairSystem.SetMaxCondition(200.000000)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(0)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(0.000000, 0.000000, 0.000000)
RepairSystem.SetPosition2D(0.000000, 0.000000)
RepairSystem.SetRepairComplexity(1.000000)
RepairSystem.SetDisabledPercentage(0.500000)
RepairSystem.SetRadius(0.250000)
RepairSystem.SetNormalPowerPerSecond(1.000000)
RepairSystem.SetMaxRepairPoints(16.000000)
RepairSystem.SetNumRepairTeams(2)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(1200.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 2.500000, -0.300000)
SensorArray.SetPosition2D(64.000000, 10.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.100000)
SensorArray.SetNormalPowerPerSecond(100.000000)
SensorArray.SetBaseSensorRange(1000.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(1600.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 2.000000, 0.230000)
ShieldGenerator.SetPosition2D(64.000000, 60.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.200000)
ShieldGenerator.SetNormalPowerPerSecond(200.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.313726, 0.392157, 0.858824, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 2200.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 2200.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 2200.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 2200.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 2200.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 2200.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 4.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 4.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 4.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 4.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 4.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 4.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
Tractors = App.WeaponSystemProperty_Create("Tractors")

Tractors.SetMaxCondition(3600.000000)
Tractors.SetCritical(0)
Tractors.SetTargetable(0)
Tractors.SetPrimary(1)
Tractors.SetPosition(0.000000, 0.000000, 0.000000)
Tractors.SetPosition2D(64.000000, 0.000000)
Tractors.SetRepairComplexity(7.000000)
Tractors.SetDisabledPercentage(0.750000)
Tractors.SetRadius(0.250000)
Tractors.SetNormalPowerPerSecond(500.000000)
Tractors.SetWeaponSystemType(Tractors.WST_TRACTOR)
Tractors.SetSingleFire(1)
Tractors.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Tractors.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Tractors)
#################################################
AftTractor = App.TractorBeamProperty_Create("Aft Tractor")

AftTractor.SetMaxCondition(1200.000000)
AftTractor.SetCritical(0)
AftTractor.SetTargetable(1)
AftTractor.SetPrimary(1)
AftTractor.SetPosition(0.000000, 2.000000, -0.300000)
AftTractor.SetPosition2D(64.000000, 90.000000)
AftTractor.SetRepairComplexity(7.000000)
AftTractor.SetDisabledPercentage(0.750000)
AftTractor.SetRadius(0.250000)
AftTractor.SetDumbfire(0)
AftTractor.SetWeaponID(7)
AftTractor.SetGroups(0)
AftTractor.SetDamageRadiusFactor(0.300000)
AftTractor.SetIconNum(0)
AftTractor.SetIconPositionX(0.000000)
AftTractor.SetIconPositionY(0.000000)
AftTractor.SetIconAboveShip(1)
AftTractor.SetFireSound("Tractor Beam")
AftTractor.SetMaxCharge(5.000000)
AftTractor.SetMaxDamage(600.000000)
AftTractor.SetMaxDamageDistance(120.000000)
AftTractor.SetMinFiringCharge(3.000000)
AftTractor.SetNormalDischargeRate(1.000000)
AftTractor.SetRechargeRate(0.300000)
AftTractor.SetIndicatorIconNum(0)
AftTractor.SetIndicatorIconPositionX(0.000000)
AftTractor.SetIndicatorIconPositionY(0.000000)
AftTractorForward = App.TGPoint3()
AftTractorForward.SetXYZ(0.000000, -1.000000, 0.000000)
AftTractorUp = App.TGPoint3()
AftTractorUp.SetXYZ(0.000000, 0.894427, 0.447214)
AftTractor.SetOrientation(AftTractorForward, AftTractorUp)
AftTractor.SetArcWidthAngles(-1.047198, 1.047198)
AftTractor.SetArcHeightAngles(0.034907, -1.396263)
AftTractor.SetTractorBeamWidth(0.300000)
AftTractor.SetTextureStart(0)
AftTractor.SetTextureEnd(0)
AftTractor.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor.SetOuterShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor.SetInnerShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
AftTractor.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
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
PortImpulse = App.EngineProperty_Create("Port Impulse")

PortImpulse.SetMaxCondition(1000.000000)
PortImpulse.SetCritical(0)
PortImpulse.SetTargetable(1)
PortImpulse.SetPrimary(1)
PortImpulse.SetPosition(-0.580000, 1.900000, 0.000000)
PortImpulse.SetPosition2D(54.000000, 110.000000)
PortImpulse.SetRepairComplexity(3.000000)
PortImpulse.SetDisabledPercentage(0.500000)
PortImpulse.SetRadius(0.150000)
PortImpulse.SetEngineType(PortImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortImpulse)
#################################################
StarImpulse = App.EngineProperty_Create("Star Impulse")

StarImpulse.SetMaxCondition(1000.000000)
StarImpulse.SetCritical(0)
StarImpulse.SetTargetable(1)
StarImpulse.SetPrimary(1)
StarImpulse.SetPosition(0.580000, 1.900000, 0.000000)
StarImpulse.SetPosition2D(75.000000, 110.000000)
StarImpulse.SetRepairComplexity(3.000000)
StarImpulse.SetDisabledPercentage(0.500000)
StarImpulse.SetRadius(0.150000)
StarImpulse.SetEngineType(StarImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarImpulse)
#################################################
Phasers = App.WeaponSystemProperty_Create("Phasers")

Phasers.SetMaxCondition(2000.000000)
Phasers.SetCritical(0)
Phasers.SetTargetable(0)
Phasers.SetPrimary(1)
Phasers.SetPosition(0.000000, 0.000000, 0.000000)
Phasers.SetPosition2D(0.000000, 0.000000)
Phasers.SetRepairComplexity(7.000000)
Phasers.SetDisabledPercentage(0.750000)
Phasers.SetRadius(0.250000)
Phasers.SetNormalPowerPerSecond(200.000000)
Phasers.SetWeaponSystemType(Phasers.WST_PHASER)
Phasers.SetSingleFire(1)
Phasers.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Phasers.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Phasers)
#################################################
DorsalPhaser = App.PhaserProperty_Create("Dorsal Phaser")

DorsalPhaser.SetMaxCondition(800.000000)
DorsalPhaser.SetCritical(0)
DorsalPhaser.SetTargetable(1)
DorsalPhaser.SetPrimary(1)
DorsalPhaser.SetPosition(0.000000, 2.700000, 0.300000)
DorsalPhaser.SetPosition2D(64.000000, 10.000000)
DorsalPhaser.SetRepairComplexity(7.000000)
DorsalPhaser.SetDisabledPercentage(0.750000)
DorsalPhaser.SetRadius(0.250000)
DorsalPhaser.SetDumbfire(0)
DorsalPhaser.SetWeaponID(1)
DorsalPhaser.SetGroups(0)
DorsalPhaser.SetDamageRadiusFactor(0.150000)
DorsalPhaser.SetIconNum(364)
DorsalPhaser.SetIconPositionX(64.000000)
DorsalPhaser.SetIconPositionY(20.000000)
DorsalPhaser.SetIconAboveShip(1)
DorsalPhaser.SetFireSound("Galaxy Phaser")
DorsalPhaser.SetMaxCharge(8.000000)
DorsalPhaser.SetMaxDamage(300.000000)
DorsalPhaser.SetMaxDamageDistance(45.000000)
DorsalPhaser.SetMinFiringCharge(3.000000)
DorsalPhaser.SetNormalDischargeRate(1.000000)
DorsalPhaser.SetRechargeRate(0.300000)
DorsalPhaser.SetIndicatorIconNum(510)
DorsalPhaser.SetIndicatorIconPositionX(58.000000)
DorsalPhaser.SetIndicatorIconPositionY(16.000000)
DorsalPhaserForward = App.TGPoint3()
DorsalPhaserForward.SetXYZ(0.000000, 1.000000, 0.000000)
DorsalPhaserUp = App.TGPoint3()
DorsalPhaserUp.SetXYZ(0.000000, 0.000000, 1.000000)
DorsalPhaser.SetOrientation(DorsalPhaserForward, DorsalPhaserUp)
DorsalPhaser.SetWidth(0.470000)
DorsalPhaser.SetLength(0.670000)
DorsalPhaser.SetArcWidthAngles(-2.094395, 2.094395)
DorsalPhaser.SetArcHeightAngles(-0.087266, 1.221731)
DorsalPhaser.SetPhaserTextureStart(0)
DorsalPhaser.SetPhaserTextureEnd(7)
DorsalPhaser.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
DorsalPhaser.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
DorsalPhaser.SetInnerShellColor(kColor)
kColor.SetRGBA(0.992157, 0.831373, 0.639216, 1.000000)
DorsalPhaser.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.992157, 0.901961, 0.858824, 1.000000)
DorsalPhaser.SetInnerCoreColor(kColor)
DorsalPhaser.SetNumSides(6)
DorsalPhaser.SetMainRadius(0.150000)
DorsalPhaser.SetTaperRadius(0.010000)
DorsalPhaser.SetCoreScale(0.500000)
DorsalPhaser.SetTaperRatio(0.250000)
DorsalPhaser.SetTaperMinLength(5.000000)
DorsalPhaser.SetTaperMaxLength(30.000000)
DorsalPhaser.SetLengthTextureTilePerUnit(0.500000)
DorsalPhaser.SetPerimeterTile(1.000000)
DorsalPhaser.SetTextureSpeed(2.500000)
DorsalPhaser.SetTextureName("data/phaser.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(DorsalPhaser)
#################################################
FedConst = App.ShipProperty_Create("FedConst")

FedConst.SetGenus(1)
FedConst.SetSpecies(141)
FedConst.SetMass(500.000000)
FedConst.SetRotationalInertia(7000.000000)
FedConst.SetShipName("FedConst")
FedConst.SetModelFilename("data/Models/Ships/FedConst.nif")
FedConst.SetDamageResolution(10.000000)
FedConst.SetAffiliation(0)
FedConst.SetStationary(0)
FedConst.SetAIString("NonFedAttack")
FedConst.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(FedConst)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 3.000000, 0.400000)
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
ViewscreenBackPosition.SetXYZ(0.000000, 2.000000, 0.400000)
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
ViewscreenLeftPosition.SetXYZ(-0.390000, 1.000000, 0.300000)
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
ViewscreenRightPosition.SetXYZ(0.390000, 1.000000, 0.300000)
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
ViewscreenUpPosition.SetXYZ(0.000000, 3.300000, 0.100000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 3.300000, 0.100000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 3.300000, 0.100000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
CargoHolds = App.HullProperty_Create("Cargo Holds")

CargoHolds.SetMaxCondition(4500.000000)
CargoHolds.SetCritical(0)
CargoHolds.SetTargetable(1)
CargoHolds.SetPrimary(0)
CargoHolds.SetPosition(0.000000, -1.300000, 0.000000)
CargoHolds.SetPosition2D(64.000000, 60.000000)
CargoHolds.SetRepairComplexity(3.000000)
CargoHolds.SetDisabledPercentage(0.000000)
CargoHolds.SetRadius(0.600000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CargoHolds)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractors", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Aft Tractor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Phasers", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Dorsal Phaser", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("FedConst", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Cargo Holds", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
