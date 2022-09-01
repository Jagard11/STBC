# C:\Program Files\Activision\AllStuff\Bridge Commander\scripts\ships\Hardpoints\B5ZephyrRaider.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(15.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, -0.030744, 0.000000)
Hull.SetPosition2D(65.000000, 55.000000)
Hull.SetRepairComplexity(15.000000)
Hull.SetDisabledPercentage(0.500000)
Hull.SetRadius(0.075000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
PowerPlant = App.PowerProperty_Create("Power Plant")

PowerPlant.SetMaxCondition(15.000000)
PowerPlant.SetCritical(1)
PowerPlant.SetTargetable(1)
PowerPlant.SetPrimary(1)
PowerPlant.SetPosition(0.000000, 0.000000, 0.000000)
PowerPlant.SetPosition2D(65.000000, 65.000000)
PowerPlant.SetRepairComplexity(1.000000)
PowerPlant.SetDisabledPercentage(0.500000)
PowerPlant.SetRadius(0.005000)
PowerPlant.SetMainBatteryLimit(70000.000000)
PowerPlant.SetBackupBatteryLimit(10000.000000)
PowerPlant.SetMainConduitCapacity(18.000000)
PowerPlant.SetBackupConduitCapacity(7.000000)
PowerPlant.SetPowerOutput(20.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)
#################################################
FuealTank1 = App.HullProperty_Create("Fuel Tank 1")

FuealTank1.SetMaxCondition(12.000000)
FuealTank1.SetCritical(1)
FuealTank1.SetTargetable(1)
FuealTank1.SetPrimary(0)
FuealTank1.SetPosition(0.400000, -0.060744, 0.000000)
FuealTank1.SetPosition2D(65.000000, 55.000000)
FuealTank1.SetRepairComplexity(15.000000)
FuealTank1.SetDisabledPercentage(0.500000)
FuealTank1.SetRadius(0.005000)
App.g_kModelPropertyManager.RegisterLocalTemplate(FuealTank1)
#################################################
FuealTank2 = App.HullProperty_Create("Fuel Tank 2")

FuealTank2.SetMaxCondition(12.000000)
FuealTank2.SetCritical(1)
FuealTank2.SetTargetable(1)
FuealTank2.SetPrimary(0)
FuealTank2.SetPosition(-0.400000, -0.060744, 0.000000)
FuealTank2.SetPosition2D(65.000000, 55.000000)
FuealTank2.SetRepairComplexity(15.000000)
FuealTank2.SetDisabledPercentage(0.500000)
FuealTank2.SetRadius(0.005000)
App.g_kModelPropertyManager.RegisterLocalTemplate(FuealTank2)
#################################################
Sensor = App.SensorProperty_Create("Sensor")

Sensor.SetMaxCondition(8.000000)
Sensor.SetCritical(0)
Sensor.SetTargetable(1)
Sensor.SetPrimary(1)
Sensor.SetPosition(0.000000, 0.000000, 0.000000)
Sensor.SetPosition2D(65.000000, 60.000000)
Sensor.SetRepairComplexity(1.000000)
Sensor.SetDisabledPercentage(0.500000)
Sensor.SetRadius(0.002500)
Sensor.SetNormalPowerPerSecond(5.000000)
Sensor.SetBaseSensorRange(1000.000000)
Sensor.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(Sensor)
#################################################
Shields = App.ShieldProperty_Create("Shields")

Shields.SetMaxCondition(5.000000)
Shields.SetCritical(0)
Shields.SetTargetable(1)
Shields.SetPrimary(1)
Shields.SetPosition(0.000000, 0.000000, 0.000000)
Shields.SetPosition2D(65.000000, 65.000000)
Shields.SetRepairComplexity(1.000000)
Shields.SetDisabledPercentage(0.500000)
Shields.SetRadius(0.005000)
Shields.SetNormalPowerPerSecond(0.000000)
ShieldsShieldGlowColor = App.TGColorA()
ShieldsShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
Shields.SetShieldGlowColor(ShieldsShieldGlowColor)
Shields.SetShieldGlowDecay(1.000000)
Shields.SetMaxShields(Shields.FRONT_SHIELDS, 0.000000)
Shields.SetMaxShields(Shields.REAR_SHIELDS, 0.000000)
Shields.SetMaxShields(Shields.TOP_SHIELDS, 0.000000)
Shields.SetMaxShields(Shields.BOTTOM_SHIELDS, 0.000000)
Shields.SetMaxShields(Shields.LEFT_SHIELDS, 0.000000)
Shields.SetMaxShields(Shields.RIGHT_SHIELDS, 0.000000)
Shields.SetShieldChargePerSecond(Shields.FRONT_SHIELDS, 0.001000)
Shields.SetShieldChargePerSecond(Shields.REAR_SHIELDS, 0.001000)
Shields.SetShieldChargePerSecond(Shields.TOP_SHIELDS, 0.001000)
Shields.SetShieldChargePerSecond(Shields.BOTTOM_SHIELDS, 0.001000)
Shields.SetShieldChargePerSecond(Shields.LEFT_SHIELDS, 0.001000)
Shields.SetShieldChargePerSecond(Shields.RIGHT_SHIELDS, 0.001000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Shields)
#################################################
SubLightSys = App.ImpulseEngineProperty_Create("Sub Light Sys")

SubLightSys.SetMaxCondition(10.000000)
SubLightSys.SetCritical(0)
SubLightSys.SetTargetable(0)
SubLightSys.SetPrimary(1)
SubLightSys.SetPosition(0.000000, 0.000000, 0.000000)
SubLightSys.SetPosition2D(65.000000, 60.000000)
SubLightSys.SetRepairComplexity(1.000000)
SubLightSys.SetDisabledPercentage(0.500000)
SubLightSys.SetRadius(0.002500)
SubLightSys.SetNormalPowerPerSecond(5.000000)
SubLightSys.SetMaxAccel(1.000000)
SubLightSys.SetMaxAngularAccel(6.000000)
SubLightSys.SetMaxAngularVelocity(1.250000)
SubLightSys.SetMaxSpeed(8.000000)
SubLightSys.SetEngineSound("EA_SF_Engine")
App.g_kModelPropertyManager.RegisterLocalTemplate(SubLightSys)
#################################################
JumpSys = App.WarpEngineProperty_Create("Jump Sys")

JumpSys.SetMaxCondition(4.000000)
JumpSys.SetCritical(0)
JumpSys.SetTargetable(0)
JumpSys.SetPrimary(1)
JumpSys.SetPosition(0.000000, 0.000000, 0.000000)
JumpSys.SetPosition2D(65.000000, 60.000000)
JumpSys.SetRepairComplexity(1.000000)
JumpSys.SetDisabledPercentage(0.500000)
JumpSys.SetRadius(0.002500)
JumpSys.SetNormalPowerPerSecond(0.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(JumpSys)
#################################################
RepairSys = App.RepairSubsystemProperty_Create("Repair Sys")

RepairSys.SetMaxCondition(10.000000)
RepairSys.SetCritical(0)
RepairSys.SetTargetable(0)
RepairSys.SetPrimary(1)
RepairSys.SetPosition(0.000000, 0.000000, 0.000000)
RepairSys.SetPosition2D(65.000000, 60.000000)
RepairSys.SetRepairComplexity(1.000000)
RepairSys.SetDisabledPercentage(0.500000)
RepairSys.SetRadius(0.002500)
RepairSys.SetNormalPowerPerSecond(0.500000)
RepairSys.SetMaxRepairPoints(2.000000)
RepairSys.SetNumRepairTeams(2)
App.g_kModelPropertyManager.RegisterLocalTemplate(RepairSys)
#################################################
EAStarfury = App.ShipProperty_Create("B5ZephyrRaider")

EAStarfury.SetGenus(1)
EAStarfury.SetSpecies(106)
EAStarfury.SetMass(90.000000)
EAStarfury.SetRotationalInertia(600.000000)
EAStarfury.SetShipName("B5ZephyrRaider")
EAStarfury.SetModelFilename("data/Models/Ships/B5ZephyrRaider/B5ZephyrRaider.nif")
EAStarfury.SetDamageResolution(15.000000)
EAStarfury.SetAffiliation(0)
EAStarfury.SetStationary(0)
EAStarfury.SetAIString("NonFedAttack")
EAStarfury.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(EAStarfury)
#################################################
PulseCannonSys = App.WeaponSystemProperty_Create("Pulse Cannon Sys")

PulseCannonSys.SetMaxCondition(9.000000)
PulseCannonSys.SetCritical(0)
PulseCannonSys.SetTargetable(0)
PulseCannonSys.SetPrimary(1)
PulseCannonSys.SetPosition(0.000000, 0.000000, 0.000000)
PulseCannonSys.SetPosition2D(10.000000, 10.000000)
PulseCannonSys.SetRepairComplexity(1.000000)
PulseCannonSys.SetDisabledPercentage(0.500000)
PulseCannonSys.SetRadius(0.002500)
PulseCannonSys.SetNormalPowerPerSecond(5.000000)
PulseCannonSys.SetWeaponSystemType(PulseCannonSys.WST_PULSE)
PulseCannonSys.SetSingleFire(0)
PulseCannonSys.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
PulseCannonSys.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(PulseCannonSys)
#################################################
Engine1 = App.EngineProperty_Create("Engine 1")

Engine1.SetMaxCondition(3.000000)
Engine1.SetCritical(0)
Engine1.SetTargetable(1)
Engine1.SetPrimary(0)
Engine1.SetPosition(-0.079342, -0.052331, 0.000000)
Engine1.SetPosition2D(50.000000, 85.000000)
Engine1.SetRepairComplexity(1.000000)
Engine1.SetDisabledPercentage(0.500000)
Engine1.SetRadius(0.015000)
Engine1.SetEngineType(Engine1.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine1)
#################################################
Engine2 = App.EngineProperty_Create("Engine 2")

Engine2.SetMaxCondition(3.000000)
Engine2.SetCritical(0)
Engine2.SetTargetable(1)
Engine2.SetPrimary(0)
Engine2.SetPosition(-0.080184, -0.052331, 0.000000)
Engine2.SetPosition2D(55.000000, 85.000000)
Engine2.SetRepairComplexity(1.000000)
Engine2.SetDisabledPercentage(0.500000)
Engine2.SetRadius(0.015000)
Engine2.SetEngineType(Engine2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine2)
#################################################
PulseCannon1 = App.PulseWeaponProperty_Create("Pulse Cannon 1")

PulseCannon1.SetMaxCondition(2.000000)
PulseCannon1.SetCritical(0)
PulseCannon1.SetTargetable(1)
PulseCannon1.SetPrimary(0)
PulseCannon1.SetPosition(0.087822, 0.215737, 0.000000)
PulseCannon1.SetPosition2D(0.000000, 0.000000)
PulseCannon1.SetRepairComplexity(1.000000)
PulseCannon1.SetDisabledPercentage(0.500000)
PulseCannon1.SetRadius(0.025000)
PulseCannon1.SetDumbfire(1)
PulseCannon1.SetWeaponID(0)
PulseCannon1.SetGroups(0)
PulseCannon1.SetDamageRadiusFactor(0.030000)
PulseCannon1.SetIconNum(370)
PulseCannon1.SetIconPositionX(65.000000)
PulseCannon1.SetIconPositionY(40.000000)
PulseCannon1.SetIconAboveShip(1)
PulseCannon1.SetFireSound("EAPulse2")
PulseCannon1.SetMaxCharge(4.000000)
PulseCannon1.SetMaxDamage(25.000000)
PulseCannon1.SetMaxDamageDistance(100.000000)
PulseCannon1.SetMinFiringCharge(3.000000)
PulseCannon1.SetNormalDischargeRate(1.000000)
PulseCannon1.SetRechargeRate(0.300000)
PulseCannon1.SetIndicatorIconNum(0)
PulseCannon1.SetIndicatorIconPositionX(0.000000)
PulseCannon1.SetIndicatorIconPositionY(0.000000)
PulseCannon1Forward = App.TGPoint3()
PulseCannon1Forward.SetXYZ(0.000000, 1.000000, 0.000000)
PulseCannon1Up = App.TGPoint3()
PulseCannon1Up.SetXYZ(0.000000, 0.000000, 1.000000)
PulseCannon1.SetOrientation(PulseCannon1Forward, PulseCannon1Up)
PulseCannon1.SetArcWidthAngles(-0.174533, 0.174533)
PulseCannon1.SetArcHeightAngles(-0.174533, 0.174533)
PulseCannon1.SetCooldownTime(0.300000)
PulseCannon1.SetModuleName("Tactical.Projectiles.ZephyrBolter")
App.g_kModelPropertyManager.RegisterLocalTemplate(PulseCannon1)
#################################################
PulseCannon2 = App.PulseWeaponProperty_Create("Pulse Cannon 2")

PulseCannon2.SetMaxCondition(2.000000)
PulseCannon2.SetCritical(0)
PulseCannon2.SetTargetable(1)
PulseCannon2.SetPrimary(0)
PulseCannon2.SetPosition(-0.087822, 0.215686, 0.000000)
PulseCannon2.SetPosition2D(0.000000, 0.000000)
PulseCannon2.SetRepairComplexity(1.000000)
PulseCannon2.SetDisabledPercentage(0.500000)
PulseCannon2.SetRadius(0.025000)
PulseCannon2.SetDumbfire(1)
PulseCannon2.SetWeaponID(1)
PulseCannon2.SetGroups(0)
PulseCannon2.SetDamageRadiusFactor(0.030000)
PulseCannon2.SetIconNum(370)
PulseCannon2.SetIconPositionX(80.000000)
PulseCannon2.SetIconPositionY(40.000000)
PulseCannon2.SetIconAboveShip(1)
PulseCannon2.SetFireSound("EAPulse2")
PulseCannon2.SetMaxCharge(4.000000)
PulseCannon2.SetMaxDamage(25.000000)
PulseCannon2.SetMaxDamageDistance(100.000000)
PulseCannon2.SetMinFiringCharge(3.000000)
PulseCannon2.SetNormalDischargeRate(1.000000)
PulseCannon2.SetRechargeRate(0.300000)
PulseCannon2.SetIndicatorIconNum(0)
PulseCannon2.SetIndicatorIconPositionX(0.000000)
PulseCannon2.SetIndicatorIconPositionY(0.000000)
PulseCannon2Forward = App.TGPoint3()
PulseCannon2Forward.SetXYZ(0.000000, 1.000000, 0.000000)
PulseCannon2Up = App.TGPoint3()
PulseCannon2Up.SetXYZ(0.000000, 0.000000, 1.000000)
PulseCannon2.SetOrientation(PulseCannon2Forward, PulseCannon2Up)
PulseCannon2.SetArcWidthAngles(-0.174533, 0.174533)
PulseCannon2.SetArcHeightAngles(-0.174533, 0.174533)
PulseCannon2.SetCooldownTime(0.300000)
PulseCannon2.SetModuleName("Tactical.Projectiles.ZephyrBolter")
App.g_kModelPropertyManager.RegisterLocalTemplate(PulseCannon2)
#################################################
TractorSys = App.WeaponSystemProperty_Create("Tractor Sys")

TractorSys.SetMaxCondition(3.000000)
TractorSys.SetCritical(0)
TractorSys.SetTargetable(0)
TractorSys.SetPrimary(1)
TractorSys.SetPosition(0.000000, 0.000000, 0.000000)
TractorSys.SetPosition2D(10.000000, 40.000000)
TractorSys.SetRepairComplexity(1.000000)
TractorSys.SetDisabledPercentage(0.500000)
TractorSys.SetRadius(0.002500)
TractorSys.SetNormalPowerPerSecond(0.500000)
TractorSys.SetWeaponSystemType(TractorSys.WST_TRACTOR)
TractorSys.SetSingleFire(1)
TractorSys.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
TractorSys.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(TractorSys)
#################################################
GraplingClaw = App.TractorBeamProperty_Create("Grapling Claw")

GraplingClaw.SetMaxCondition(4.000000)
GraplingClaw.SetCritical(0)
GraplingClaw.SetTargetable(1)
GraplingClaw.SetPrimary(0)
GraplingClaw.SetPosition(-0.000493, -0.014534, -0.021788)
GraplingClaw.SetPosition2D(75.000000, 60.000000)
GraplingClaw.SetRepairComplexity(1.000000)
GraplingClaw.SetDisabledPercentage(0.500000)
GraplingClaw.SetRadius(0.002500)
GraplingClaw.SetDumbfire(1)
GraplingClaw.SetWeaponID(7)
GraplingClaw.SetGroups(0)
GraplingClaw.SetDamageRadiusFactor(0.300000)
GraplingClaw.SetIconNum(0)
GraplingClaw.SetIconPositionX(0.000000)
GraplingClaw.SetIconPositionY(0.000000)
GraplingClaw.SetIconAboveShip(1)
GraplingClaw.SetFireSound("")
GraplingClaw.SetMaxCharge(1.000000)
GraplingClaw.SetMaxDamage(25.000000)
GraplingClaw.SetMaxDamageDistance(57.000000)
GraplingClaw.SetMinFiringCharge(1.000000)
GraplingClaw.SetNormalDischargeRate(1.000000)
GraplingClaw.SetRechargeRate(1.000000)
GraplingClaw.SetIndicatorIconNum(0)
GraplingClaw.SetIndicatorIconPositionX(0.000000)
GraplingClaw.SetIndicatorIconPositionY(0.000000)
GraplingClawForward = App.TGPoint3()
GraplingClawForward.SetXYZ(0.000000, 1.000000, 0.000000)
GraplingClawUp = App.TGPoint3()
GraplingClawUp.SetXYZ(0.000000, 0.000000, 1.000000)
GraplingClaw.SetOrientation(GraplingClawForward, GraplingClawUp)
GraplingClaw.SetArcWidthAngles(-0.174533, 0.174533)
GraplingClaw.SetArcHeightAngles(-0.087266, 3.228859)
GraplingClaw.SetTractorBeamWidth(0.300000)
GraplingClaw.SetTextureStart(0)
GraplingClaw.SetTextureEnd(0)
GraplingClaw.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
kColor = App.TGColorA()
kColor.SetRGBA(0.000000, 0.000000, 0.000000, 1.000000)
GraplingClaw.SetOuterShellColor(kColor)
kColor.SetRGBA(0.000000, 0.000000, 0.000000, 1.000000)
GraplingClaw.SetInnerShellColor(kColor)
kColor.SetRGBA(0.000000, 0.000000, 0.000000, 1.000000)
GraplingClaw.SetOuterCoreColor(kColor)
kColor.SetRGBA(0.000000, 0.000000, 0.000000, 1.000000)
GraplingClaw.SetInnerCoreColor(kColor)
GraplingClaw.SetNumSides(12)
GraplingClaw.SetMainRadius(0.007500)
GraplingClaw.SetTaperRadius(0.000000)
GraplingClaw.SetCoreScale(0.450000)
GraplingClaw.SetTaperRatio(0.200000)
GraplingClaw.SetTaperMinLength(1.000000)
GraplingClaw.SetTaperMaxLength(5.000000)
GraplingClaw.SetLengthTextureTilePerUnit(0.250000)
GraplingClaw.SetPerimeterTile(1.000000)
GraplingClaw.SetTextureSpeed(0.200000)
GraplingClaw.SetTextureName("data/Textures/Tactical/TractorBeam.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(GraplingClaw)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fuel Tank 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fuel Tank 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Plant", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shields", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sub Light Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Jump Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("B5ZephyrRaider", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Pulse Cannon Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Pulse Cannon 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Pulse Cannon 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Tractor Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Grapling Claw", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)