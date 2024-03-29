# C:\J-Single-testing-KM1\scripts\ships\Hardpoints\Freighter.py
# This file was automatically generated - modify at your own risk.
# tiqhud 2009.07.17

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(4000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.600000, 0.100000)
Hull.SetPosition2D(64.000000, 60.000000)
Hull.SetRepairComplexity(3.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.600000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ImpulseEngines = App.ImpulseEngineProperty_Create("Impulse Engines")

ImpulseEngines.SetMaxCondition(2000.000000)
ImpulseEngines.SetCritical(0)
ImpulseEngines.SetTargetable(0)
ImpulseEngines.SetPrimary(1)
ImpulseEngines.SetPosition(0.005503, -0.729128, 0.226805)
ImpulseEngines.SetPosition2D(0.000000, 0.000000)
ImpulseEngines.SetRepairComplexity(2.000000)
ImpulseEngines.SetDisabledPercentage(0.500000)
ImpulseEngines.SetRadius(0.030000)
ImpulseEngines.SetNormalPowerPerSecond(100.000000)
ImpulseEngines.SetMaxAccel(2.500000)
ImpulseEngines.SetMaxAngularAccel(0.200000)
ImpulseEngines.SetMaxAngularVelocity(0.200000)
ImpulseEngines.SetMaxSpeed(6.000000)
ImpulseEngines.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulseEngines)
#################################################
WarpCore = App.PowerProperty_Create("Warp Core")

WarpCore.SetMaxCondition(1200.000000)
WarpCore.SetCritical(1)
WarpCore.SetTargetable(1)
WarpCore.SetPrimary(1)
WarpCore.SetPosition(0.000000, -0.100000, 0.200000)
WarpCore.SetPosition2D(123.000000, 32.000000)
WarpCore.SetRepairComplexity(2.000000)
WarpCore.SetDisabledPercentage(0.750000)
WarpCore.SetRadius(0.030000)
WarpCore.SetMainBatteryLimit(70000.000000)
WarpCore.SetBackupBatteryLimit(40000.000000)
WarpCore.SetMainConduitCapacity(650.000000)
WarpCore.SetBackupConduitCapacity(400.000000)
WarpCore.SetPowerOutput(250.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpCore)
#################################################
RepairSystem = App.RepairSubsystemProperty_Create("Repair System")

RepairSystem.SetMaxCondition(200.000000)
RepairSystem.SetCritical(0)
RepairSystem.SetTargetable(0)
RepairSystem.SetPrimary(1)
RepairSystem.SetPosition(-0.007569, -0.223323, 0.345946)
RepairSystem.SetPosition2D(0.000000, 0.000000)
RepairSystem.SetRepairComplexity(1.000000)
RepairSystem.SetDisabledPercentage(0.500000)
RepairSystem.SetRadius(0.100000)
RepairSystem.SetNormalPowerPerSecond(1.000000)
RepairSystem.SetMaxRepairPoints(8.000000)
RepairSystem.SetNumRepairTeams(2)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(1200.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(-0.001312, 1.471400, 0.219329)
SensorArray.SetPosition2D(128.000000, 7.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.100000)
SensorArray.SetNormalPowerPerSecond(20.000000)
SensorArray.SetBaseSensorRange(2500.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(2400.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.003811, 0.008754, 0.345946)
ShieldGenerator.SetPosition2D(102.000000, 9.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.020000)
ShieldGenerator.SetNormalPowerPerSecond(100.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 0.501961, 0.356863, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 9000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 9000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 9000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 7200.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 9000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 9000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 8.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 8.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 8.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 8.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 8.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 8.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
WarpEngines = App.WarpEngineProperty_Create("Warp Engines")

WarpEngines.SetMaxCondition(2200.000000)
WarpEngines.SetCritical(0)
WarpEngines.SetTargetable(1)
WarpEngines.SetPrimary(1)
WarpEngines.SetPosition(0.005503, -0.729128, 0.226805)
WarpEngines.SetPosition2D(129.000000, 53.000000)
WarpEngines.SetRepairComplexity(1.000000)
WarpEngines.SetDisabledPercentage(0.500000)
WarpEngines.SetRadius(0.030000)
WarpEngines.SetNormalPowerPerSecond(10.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngines)
#################################################
Tractors = App.WeaponSystemProperty_Create("Tractors")

Tractors.SetMaxCondition(1500.000000)
Tractors.SetCritical(0)
Tractors.SetTargetable(1)
Tractors.SetPrimary(1)
Tractors.SetPosition(0.009568, 0.117886, 0.345946)
Tractors.SetPosition2D(85.000000, 119.000000)
Tractors.SetRepairComplexity(1.000000)
Tractors.SetDisabledPercentage(0.750000)
Tractors.SetRadius(0.050000)
Tractors.SetNormalPowerPerSecond(10.000000)
Tractors.SetWeaponSystemType(Tractors.WST_TRACTOR)
Tractors.SetSingleFire(1)
Tractors.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Tractors.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Tractors)
#################################################
PortImpulse = App.EngineProperty_Create("Port Impulse")

PortImpulse.SetMaxCondition(2000.000000)
PortImpulse.SetCritical(0)
PortImpulse.SetTargetable(1)
PortImpulse.SetPrimary(1)
PortImpulse.SetPosition(-0.147301, -1.574540, 0.108598)
PortImpulse.SetPosition2D(118.000000, 88.000000)
PortImpulse.SetRepairComplexity(2.000000)
PortImpulse.SetDisabledPercentage(0.500000)
PortImpulse.SetRadius(0.080000)
PortImpulse.SetEngineType(PortImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortImpulse)
#################################################
StarImpulse = App.EngineProperty_Create("Star Impulse")

StarImpulse.SetMaxCondition(2000.000000)
StarImpulse.SetCritical(0)
StarImpulse.SetTargetable(1)
StarImpulse.SetPrimary(1)
StarImpulse.SetPosition(0.148595, -1.574560, 0.105821)
StarImpulse.SetPosition2D(133.000000, 88.000000)
StarImpulse.SetRepairComplexity(2.000000)
StarImpulse.SetDisabledPercentage(0.500000)
StarImpulse.SetRadius(0.080000)
StarImpulse.SetEngineType(StarImpulse.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarImpulse)
#################################################
TractorBeam = App.TractorBeamProperty_Create("Tractor Beam")

TractorBeam.SetMaxCondition(1500.000000)
TractorBeam.SetCritical(0)
TractorBeam.SetTargetable(1)
TractorBeam.SetPrimary(1)
TractorBeam.SetPosition(0.002379, -0.577442, -0.372652)
TractorBeam.SetPosition2D(92.000000, 119.000000)
TractorBeam.SetRepairComplexity(5.000000)
TractorBeam.SetDisabledPercentage(0.750000)
TractorBeam.SetRadius(0.300000)
TractorBeam.SetDumbfire(0)
TractorBeam.SetWeaponID(0)
TractorBeam.SetGroups(0)
TractorBeam.SetDamageRadiusFactor(0.300000)
TractorBeam.SetIconNum(0)
TractorBeam.SetIconPositionX(0.000000)
TractorBeam.SetIconPositionY(0.000000)
TractorBeam.SetIconAboveShip(1)
TractorBeam.SetFireSound("Tractor Beam")
TractorBeam.SetMaxCharge(5.000000)
TractorBeam.SetMaxDamage(100.000000)
TractorBeam.SetMaxDamageDistance(100.000000)
TractorBeam.SetMinFiringCharge(3.000000)
TractorBeam.SetNormalDischargeRate(1.000000)
TractorBeam.SetRechargeRate(0.300000)
TractorBeam.SetIndicatorIconNum(0)
TractorBeam.SetIndicatorIconPositionX(0.000000)
TractorBeam.SetIndicatorIconPositionY(0.000000)
TractorBeamForward = App.TGPoint3()
TractorBeamForward.SetXYZ(0.000000, 1.000000, 0.000000)
TractorBeamUp = App.TGPoint3()
TractorBeamUp.SetXYZ(0.000000, 0.000000, 1.000000)
TractorBeam.SetOrientation(TractorBeamForward, TractorBeamUp)
TractorBeam.SetArcWidthAngles(-1.963495, 1.963495)
TractorBeam.SetArcHeightAngles(-0.872665, 1.553343)
TractorBeam.SetTractorBeamWidth(0.300000)
TractorBeam.SetTextureStart(0)
TractorBeam.SetTextureEnd(0)
TractorBeam.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
TractorBeam.SetOuterShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
TractorBeam.SetInnerShellColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
TractorBeam.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.400000, 0.400000, 1.000000, 1.000000)
TractorBeam.SetInnerCoreColor(kColor)
TractorBeam.SetNumSides(12)
TractorBeam.SetMainRadius(0.075000)
TractorBeam.SetTaperRadius(0.000000)
TractorBeam.SetCoreScale(0.450000)
TractorBeam.SetTaperRatio(0.200000)
TractorBeam.SetTaperMinLength(1.000000)
TractorBeam.SetTaperMaxLength(5.000000)
TractorBeam.SetLengthTextureTilePerUnit(0.250000)
TractorBeam.SetPerimeterTile(1.000000)
TractorBeam.SetTextureSpeed(0.200000)
TractorBeam.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(TractorBeam)
#################################################
WarpEngine = App.EngineProperty_Create("Warp Engine")

WarpEngine.SetMaxCondition(2200.000000)
WarpEngine.SetCritical(0)
WarpEngine.SetTargetable(1)
WarpEngine.SetPrimary(1)
WarpEngine.SetPosition(0.002389, -1.574610, 0.105394)
WarpEngine.SetPosition2D(129.000000, 70.000000)
WarpEngine.SetRepairComplexity(3.000000)
WarpEngine.SetDisabledPercentage(0.750000)
WarpEngine.SetRadius(0.100000)
WarpEngine.SetEngineType(WarpEngine.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(WarpEngine)
#################################################
Freighter = App.ShipProperty_Create("Freighter")

Freighter.SetGenus(1)
Freighter.SetSpecies(108)
Freighter.SetMass(80.000000)
Freighter.SetRotationalInertia(10000.000000)
Freighter.SetShipName("Freighter")
Freighter.SetModelFilename("data/Models/Ships/Freighter.nif")
Freighter.SetDamageResolution(10.000000)
Freighter.SetAffiliation(0)
Freighter.SetStationary(0)
Freighter.SetAIString("NonFedAttack")
Freighter.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Freighter)
#################################################
Phasers = App.WeaponSystemProperty_Create("Phasers")

Phasers.SetMaxCondition(1000.000000)
Phasers.SetCritical(0)
Phasers.SetTargetable(1)
Phasers.SetPrimary(1)
Phasers.SetPosition(-0.004763, 1.573310, -0.178319)
Phasers.SetPosition2D(0.000000, 10.000000)
Phasers.SetRepairComplexity(1.000000)
Phasers.SetDisabledPercentage(0.750000)
Phasers.SetRadius(0.030000)
Phasers.SetNormalPowerPerSecond(1.000000)
Phasers.SetWeaponSystemType(Phasers.WST_PHASER)
Phasers.SetSingleFire(1)
Phasers.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Phasers.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(Phasers)
#################################################
ForeDorsalPhaser = App.PhaserProperty_Create("Fore Dorsal Phaser")

ForeDorsalPhaser.SetMaxCondition(800.000000)
ForeDorsalPhaser.SetCritical(0)
ForeDorsalPhaser.SetTargetable(1)
ForeDorsalPhaser.SetPrimary(1)
ForeDorsalPhaser.SetPosition(-0.000595, 1.468520, 0.221820)
ForeDorsalPhaser.SetPosition2D(-7.000000, 15.000000)
ForeDorsalPhaser.SetRepairComplexity(1.000000)
ForeDorsalPhaser.SetDisabledPercentage(0.750000)
ForeDorsalPhaser.SetRadius(0.250000)
ForeDorsalPhaser.SetDumbfire(1)
ForeDorsalPhaser.SetWeaponID(4)
ForeDorsalPhaser.SetGroups(0)
ForeDorsalPhaser.SetDamageRadiusFactor(0.080000)
ForeDorsalPhaser.SetIconNum(364)
ForeDorsalPhaser.SetIconPositionX(62.000000)
ForeDorsalPhaser.SetIconPositionY(32.000000)
ForeDorsalPhaser.SetIconAboveShip(1)
ForeDorsalPhaser.SetFireSound("Akira Phaser")
ForeDorsalPhaser.SetMaxCharge(5.500000)
ForeDorsalPhaser.SetMaxDamage(500.000000)
ForeDorsalPhaser.SetMaxDamageDistance(50.000000)
ForeDorsalPhaser.SetMinFiringCharge(3.000000)
ForeDorsalPhaser.SetNormalDischargeRate(1.000000)
ForeDorsalPhaser.SetRechargeRate(0.100000)
ForeDorsalPhaser.SetIndicatorIconNum(510)
ForeDorsalPhaser.SetIndicatorIconPositionX(58.000000)
ForeDorsalPhaser.SetIndicatorIconPositionY(27.000000)
ForeDorsalPhaserForward = App.TGPoint3()
ForeDorsalPhaserForward.SetXYZ(0.000000, 1.000000, 0.000000)
ForeDorsalPhaserUp = App.TGPoint3()
ForeDorsalPhaserUp.SetXYZ(0.000000, 0.000000, 1.000000)
ForeDorsalPhaser.SetOrientation(ForeDorsalPhaserForward, ForeDorsalPhaserUp)
ForeDorsalPhaser.SetWidth(0.010000)
ForeDorsalPhaser.SetLength(0.010000)
ForeDorsalPhaser.SetArcWidthAngles(-0.523599, 0.523599)
ForeDorsalPhaser.SetArcHeightAngles(-0.523599, 0.523599)
ForeDorsalPhaser.SetPhaserTextureStart(8)
ForeDorsalPhaser.SetPhaserTextureEnd(15)
ForeDorsalPhaser.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.839216, 0.129412, 0.003922, 1.000000)
ForeDorsalPhaser.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
ForeDorsalPhaser.SetInnerShellColor(kColor)
kColor.SetRGBA(0.639216, 0.639216, 0.000000, 1.000000)
ForeDorsalPhaser.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.800000, 0.800000, 0.000000, 1.000000)
ForeDorsalPhaser.SetInnerCoreColor(kColor)
ForeDorsalPhaser.SetNumSides(6)
ForeDorsalPhaser.SetMainRadius(0.050000)
ForeDorsalPhaser.SetTaperRadius(0.010000)
ForeDorsalPhaser.SetCoreScale(0.200000)
ForeDorsalPhaser.SetTaperRatio(0.550000)
ForeDorsalPhaser.SetTaperMinLength(0.100000)
ForeDorsalPhaser.SetTaperMaxLength(30.000000)
ForeDorsalPhaser.SetLengthTextureTilePerUnit(0.010000)
ForeDorsalPhaser.SetPerimeterTile(1.000000)
ForeDorsalPhaser.SetTextureSpeed(20.000000)
ForeDorsalPhaser.SetTextureName("data/phaser27b.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForeDorsalPhaser)
#################################################
ForeVentPhaser = App.PhaserProperty_Create("Fore Vent Phaser")

ForeVentPhaser.SetMaxCondition(800.000000)
ForeVentPhaser.SetCritical(0)
ForeVentPhaser.SetTargetable(1)
ForeVentPhaser.SetPrimary(1)
ForeVentPhaser.SetPosition(-0.006244, 1.557460, -0.179042)
ForeVentPhaser.SetPosition2D(13.000000, 15.000000)
ForeVentPhaser.SetRepairComplexity(1.000000)
ForeVentPhaser.SetDisabledPercentage(0.750000)
ForeVentPhaser.SetRadius(0.250000)
ForeVentPhaser.SetDumbfire(1)
ForeVentPhaser.SetWeaponID(4)
ForeVentPhaser.SetGroups(0)
ForeVentPhaser.SetDamageRadiusFactor(0.080000)
ForeVentPhaser.SetIconNum(364)
ForeVentPhaser.SetIconPositionX(62.000000)
ForeVentPhaser.SetIconPositionY(46.000000)
ForeVentPhaser.SetIconAboveShip(0)
ForeVentPhaser.SetFireSound("Akira Phaser")
ForeVentPhaser.SetMaxCharge(5.500000)
ForeVentPhaser.SetMaxDamage(500.000000)
ForeVentPhaser.SetMaxDamageDistance(50.000000)
ForeVentPhaser.SetMinFiringCharge(3.000000)
ForeVentPhaser.SetNormalDischargeRate(1.000000)
ForeVentPhaser.SetRechargeRate(0.100000)
ForeVentPhaser.SetIndicatorIconNum(510)
ForeVentPhaser.SetIndicatorIconPositionX(58.000000)
ForeVentPhaser.SetIndicatorIconPositionY(41.000000)
ForeVentPhaserForward = App.TGPoint3()
ForeVentPhaserForward.SetXYZ(0.000000, 1.000000, 0.000000)
ForeVentPhaserUp = App.TGPoint3()
ForeVentPhaserUp.SetXYZ(0.000000, 0.000000, 1.000000)
ForeVentPhaser.SetOrientation(ForeVentPhaserForward, ForeVentPhaserUp)
ForeVentPhaser.SetWidth(0.010000)
ForeVentPhaser.SetLength(0.010000)
ForeVentPhaser.SetArcWidthAngles(-0.523599, 0.523599)
ForeVentPhaser.SetArcHeightAngles(-1.483530, 0.034907)
ForeVentPhaser.SetPhaserTextureStart(8)
ForeVentPhaser.SetPhaserTextureEnd(15)
ForeVentPhaser.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.839216, 0.129412, 0.003922, 1.000000)
ForeVentPhaser.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.164706, 0.003922, 1.000000)
ForeVentPhaser.SetInnerShellColor(kColor)
kColor.SetRGBA(0.639216, 0.639216, 0.000000, 1.000000)
ForeVentPhaser.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.800000, 0.800000, 0.000000, 1.000000)
ForeVentPhaser.SetInnerCoreColor(kColor)
ForeVentPhaser.SetNumSides(6)
ForeVentPhaser.SetMainRadius(0.050000)
ForeVentPhaser.SetTaperRadius(0.010000)
ForeVentPhaser.SetCoreScale(0.200000)
ForeVentPhaser.SetTaperRatio(0.550000)
ForeVentPhaser.SetTaperMinLength(0.100000)
ForeVentPhaser.SetTaperMaxLength(30.000000)
ForeVentPhaser.SetLengthTextureTilePerUnit(0.010000)
ForeVentPhaser.SetPerimeterTile(1.000000)
ForeVentPhaser.SetTextureSpeed(20.000000)
ForeVentPhaser.SetTextureName("data/phaser27b.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(ForeVentPhaser)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractors", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractor Beam", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Impulse", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp Engine", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Freighter", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Phasers", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Torpedo System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fore Dorsal Phaser", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fore Vent Phaser", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
