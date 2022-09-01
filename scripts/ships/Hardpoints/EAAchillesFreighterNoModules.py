# C:\Program Files\Activision\AllStuff\Bridge Commander\scripts\ships\Hardpoints\EAAchillesFreighterNoModules.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
EAAchillesFreighterNoModules = App.ShipProperty_Create("EAAchillesFreighterNoModules")

EAAchillesFreighterNoModules.SetGenus(1)
EAAchillesFreighterNoModules.SetSpecies(106)
EAAchillesFreighterNoModules.SetMass(40.000000)
EAAchillesFreighterNoModules.SetRotationalInertia(10000.000000)
EAAchillesFreighterNoModules.SetShipName("EAAchillesFreighterNoModules")
EAAchillesFreighterNoModules.SetModelFilename("data/Models/Ships/EAAchillesFreighter/EAAchillesFreighterLeftModule.nif")
EAAchillesFreighterNoModules.SetDamageResolution(5.000000)
EAAchillesFreighterNoModules.SetAffiliation(0)
EAAchillesFreighterNoModules.SetStationary(0)
EAAchillesFreighterNoModules.SetAIString("NonFedAttack")
EAAchillesFreighterNoModules.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(EAAchillesFreighterNoModules)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(100.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(65.000000, 65.000000)
Hull.SetRepairComplexity(2.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(4.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
Bridge = App.HullProperty_Create("Bridge")

Bridge.SetMaxCondition(80.000000)
Bridge.SetCritical(0)
Bridge.SetTargetable(1)
Bridge.SetPrimary(0)
Bridge.SetPosition(0.000000, 5.012140, 0.136250)
Bridge.SetPosition2D(65.000000, 60.000000)
Bridge.SetRepairComplexity(1.000000)
Bridge.SetDisabledPercentage(0.500000)
Bridge.SetRadius(0.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Bridge)
#################################################
CargoModule1 = App.HullProperty_Create("Cargo Module 1")

CargoModule1.SetMaxCondition(100.000000)
CargoModule1.SetCritical(0)
CargoModule1.SetTargetable(1)
CargoModule1.SetPrimary(0)
CargoModule1.SetPosition(-1.000000, 2.000000, 0.000000)
CargoModule1.SetPosition2D(65.000000, 60.000000)
CargoModule1.SetRepairComplexity(1.000000)
CargoModule1.SetDisabledPercentage(0.500000)
CargoModule1.SetRadius(0.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CargoModule1)
#################################################
CargoModule2 = App.HullProperty_Create("Cargo Module 2")

CargoModule2.SetMaxCondition(100.000000)
CargoModule2.SetCritical(0)
CargoModule2.SetTargetable(1)
CargoModule2.SetPrimary(0)
CargoModule2.SetPosition(1.000000, 2.000000, 0.000000)
CargoModule2.SetPosition2D(65.000000, 60.000000)
CargoModule2.SetRepairComplexity(1.000000)
CargoModule2.SetDisabledPercentage(0.500000)
CargoModule2.SetRadius(0.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CargoModule2)
#################################################
CargoModule3 = App.HullProperty_Create("Cargo Module 3")

CargoModule3.SetMaxCondition(100.000000)
CargoModule3.SetCritical(0)
CargoModule3.SetTargetable(1)
CargoModule3.SetPrimary(0)
CargoModule3.SetPosition(-1.000000, 0.400000, 0.000000)
CargoModule3.SetPosition2D(65.000000, 60.000000)
CargoModule3.SetRepairComplexity(1.000000)
CargoModule3.SetDisabledPercentage(0.500000)
CargoModule3.SetRadius(0.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CargoModule3)
#################################################
CargoModule4 = App.HullProperty_Create("Cargo Module 4")

CargoModule4.SetMaxCondition(100.000000)
CargoModule4.SetCritical(0)
CargoModule4.SetTargetable(1)
CargoModule4.SetPrimary(0)
CargoModule4.SetPosition(1.000000, 0.400000, 0.000000)
CargoModule4.SetPosition2D(65.000000, 60.000000)
CargoModule4.SetRepairComplexity(1.000000)
CargoModule4.SetDisabledPercentage(0.500000)
CargoModule4.SetRadius(0.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CargoModule4)
#################################################
CargoModule5 = App.HullProperty_Create("Cargo Module 5")

CargoModule5.SetMaxCondition(100.000000)
CargoModule5.SetCritical(0)
CargoModule5.SetTargetable(1)
CargoModule5.SetPrimary(0)
CargoModule5.SetPosition(-1.000000, -1.412140, 0.000000)
CargoModule5.SetPosition2D(65.000000, 60.000000)
CargoModule5.SetRepairComplexity(1.000000)
CargoModule5.SetDisabledPercentage(0.500000)
CargoModule5.SetRadius(0.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CargoModule5)
#################################################
CargoModule6 = App.HullProperty_Create("Cargo Module 6")

CargoModule6.SetMaxCondition(100.000000)
CargoModule6.SetCritical(0)
CargoModule6.SetTargetable(1)
CargoModule6.SetPrimary(0)
CargoModule6.SetPosition(1.000000, -1.412140, 0.000000)
CargoModule6.SetPosition2D(65.000000, 60.000000)
CargoModule6.SetRepairComplexity(1.000000)
CargoModule6.SetDisabledPercentage(0.500000)
CargoModule6.SetRadius(0.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CargoModule6)
#################################################
CargoModule7 = App.HullProperty_Create("Cargo Module 7")

CargoModule7.SetMaxCondition(100.000000)
CargoModule7.SetCritical(0)
CargoModule7.SetTargetable(1)
CargoModule7.SetPrimary(0)
CargoModule7.SetPosition(-1.000000, -3.012140, 0.000000)
CargoModule7.SetPosition2D(65.000000, 60.000000)
CargoModule7.SetRepairComplexity(1.000000)
CargoModule7.SetDisabledPercentage(0.500000)
CargoModule7.SetRadius(0.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CargoModule7)
#################################################
CargoModule8 = App.HullProperty_Create("Cargo Module 8")

CargoModule8.SetMaxCondition(100.000000)
CargoModule8.SetCritical(0)
CargoModule8.SetTargetable(1)
CargoModule8.SetPrimary(0)
CargoModule8.SetPosition(1.000000, -3.012140, 0.000000)
CargoModule8.SetPosition2D(65.000000, 60.000000)
CargoModule8.SetRepairComplexity(1.000000)
CargoModule8.SetDisabledPercentage(0.500000)
CargoModule8.SetRadius(0.500000)
App.g_kModelPropertyManager.RegisterLocalTemplate(CargoModule8)
#################################################
PowerCore = App.PowerProperty_Create("Power Core")

PowerCore.SetMaxCondition(90.000000)
PowerCore.SetCritical(1)
PowerCore.SetTargetable(1)
PowerCore.SetPrimary(1)
PowerCore.SetPosition(0.000000, -3.426700, 0.000000)
PowerCore.SetPosition2D(65.000000, 90.000000)
PowerCore.SetRepairComplexity(1.000000)
PowerCore.SetDisabledPercentage(0.500000)
PowerCore.SetRadius(0.500000)
PowerCore.SetMainBatteryLimit(70000.000000)
PowerCore.SetBackupBatteryLimit(10000.000000)
PowerCore.SetMainConduitCapacity(20.000000)
PowerCore.SetBackupConduitCapacity(10.000000)
PowerCore.SetPowerOutput(35.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerCore)
#################################################
SublightDriveSys = App.ImpulseEngineProperty_Create("Sublight Drive Sys")

SublightDriveSys.SetMaxCondition(400.000000)
SublightDriveSys.SetCritical(0)
SublightDriveSys.SetTargetable(0)
SublightDriveSys.SetPrimary(1)
SublightDriveSys.SetPosition(0.000000, 0.000000, 0.000000)
SublightDriveSys.SetPosition2D(65.000000, 90.000000)
SublightDriveSys.SetRepairComplexity(1.000000)
SublightDriveSys.SetDisabledPercentage(0.500000)
SublightDriveSys.SetRadius(0.025000)
SublightDriveSys.SetNormalPowerPerSecond(5.000000)
SublightDriveSys.SetMaxAccel(0.250000)
SublightDriveSys.SetMaxAngularAccel(0.040000)
SublightDriveSys.SetMaxAngularVelocity(0.080000)
SublightDriveSys.SetMaxSpeed(7.500000)
SublightDriveSys.SetEngineSound("Klingon Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(SublightDriveSys)
#################################################
JumpEngineSys = App.WarpEngineProperty_Create("Jump Engine Sys")

JumpEngineSys.SetMaxCondition(400.000000)
JumpEngineSys.SetCritical(0)
JumpEngineSys.SetTargetable(0)
JumpEngineSys.SetPrimary(1)
JumpEngineSys.SetPosition(0.000000, 0.000000, 0.000000)
JumpEngineSys.SetPosition2D(65.000000, 80.000000)
JumpEngineSys.SetRepairComplexity(1.000000)
JumpEngineSys.SetDisabledPercentage(0.500000)
JumpEngineSys.SetRadius(0.025000)
JumpEngineSys.SetNormalPowerPerSecond(10.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(JumpEngineSys)
#################################################
SensorGrid = App.SensorProperty_Create("Sensor Grid")

SensorGrid.SetMaxCondition(400.000000)
SensorGrid.SetCritical(1)
SensorGrid.SetTargetable(1)
SensorGrid.SetPrimary(1)
SensorGrid.SetPosition(0.000000, 6.012140, -0.186250)
SensorGrid.SetPosition2D(65.000000, 50.000000)
SensorGrid.SetRepairComplexity(2.000000)
SensorGrid.SetDisabledPercentage(0.500000)
SensorGrid.SetRadius(0.025000)
SensorGrid.SetNormalPowerPerSecond(4.000000)
SensorGrid.SetBaseSensorRange(900.000000)
SensorGrid.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorGrid)
#################################################
DamageControl = App.RepairSubsystemProperty_Create("Damage Control")

DamageControl.SetMaxCondition(800.000000)
DamageControl.SetCritical(0)
DamageControl.SetTargetable(0)
DamageControl.SetPrimary(1)
DamageControl.SetPosition(0.000000, 0.000000, 0.000000)
DamageControl.SetPosition2D(65.000000, 70.000000)
DamageControl.SetRepairComplexity(1.000000)
DamageControl.SetDisabledPercentage(0.500000)
DamageControl.SetRadius(0.025000)
DamageControl.SetNormalPowerPerSecond(0.010000)
DamageControl.SetMaxRepairPoints(9.000000)
DamageControl.SetNumRepairTeams(3)
App.g_kModelPropertyManager.RegisterLocalTemplate(DamageControl)
#################################################
Engine1 = App.EngineProperty_Create("Engine 1")

Engine1.SetMaxCondition(80.000000)
Engine1.SetCritical(0)
Engine1.SetTargetable(1)
Engine1.SetPrimary(0)
Engine1.SetPosition(0.000000, -5.000000, 0.000000)
Engine1.SetPosition2D(60.000000, 100.000000)
Engine1.SetRepairComplexity(4.000000)
Engine1.SetDisabledPercentage(0.500000)
Engine1.SetRadius(0.500000)
Engine1.SetEngineType(Engine1.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engine1)
#################################################
JumpEngine1 = App.EngineProperty_Create("Jumpspace Drive 1")

JumpEngine1.SetMaxCondition(500.000000)
JumpEngine1.SetCritical(0)
JumpEngine1.SetTargetable(1)
JumpEngine1.SetPrimary(0)
JumpEngine1.SetPosition(0.000000, -4.770240, 0.000000)
JumpEngine1.SetPosition2D(65.000000, 65.000000)
JumpEngine1.SetRepairComplexity(1.000000)
JumpEngine1.SetDisabledPercentage(0.500000)
JumpEngine1.SetRadius(0.250000)
JumpEngine1.SetEngineType(JumpEngine1.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(JumpEngine1)
#################################################
JumpEngine2 = App.EngineProperty_Create("Jumpspace Drive 2")

JumpEngine2.SetMaxCondition(500.000000)
JumpEngine2.SetCritical(0)
JumpEngine2.SetTargetable(1)
JumpEngine2.SetPrimary(0)
JumpEngine2.SetPosition(0.000000, 2.042850, 0.000000)
JumpEngine2.SetPosition2D(65.000000, 75.000000)
JumpEngine2.SetRepairComplexity(1.000000)
JumpEngine2.SetDisabledPercentage(0.500000)
JumpEngine2.SetRadius(0.250000)
JumpEngine2.SetEngineType(JumpEngine2.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(JumpEngine2)
#################################################
DefenseGrid = App.ShieldProperty_Create("Defense Grid")

DefenseGrid.SetMaxCondition(50.000000)
DefenseGrid.SetCritical(0)
DefenseGrid.SetTargetable(1)
DefenseGrid.SetPrimary(1)
DefenseGrid.SetPosition(0.000000, 0.000000, 0.000000)
DefenseGrid.SetPosition2D(65.000000, 60.000000)
DefenseGrid.SetRepairComplexity(1.000000)
DefenseGrid.SetDisabledPercentage(0.500000)
DefenseGrid.SetRadius(0.250000)
DefenseGrid.SetNormalPowerPerSecond(0.000000)
DefenseGridShieldGlowColor = App.TGColorA()
DefenseGridShieldGlowColor.SetRGBA(0.00000, 0.000000, 0.000000, 0.000000)
DefenseGrid.SetShieldGlowColor(DefenseGridShieldGlowColor)
DefenseGrid.SetShieldGlowDecay(1.000000)
DefenseGrid.SetMaxShields(DefenseGrid.FRONT_SHIELDS, 16.000000)
DefenseGrid.SetMaxShields(DefenseGrid.REAR_SHIELDS, 16.000000)
DefenseGrid.SetMaxShields(DefenseGrid.TOP_SHIELDS, 16.000000)
DefenseGrid.SetMaxShields(DefenseGrid.BOTTOM_SHIELDS, 16.000000)
DefenseGrid.SetMaxShields(DefenseGrid.LEFT_SHIELDS, 16.000000)
DefenseGrid.SetMaxShields(DefenseGrid.RIGHT_SHIELDS, 16.000000)
DefenseGrid.SetShieldChargePerSecond(DefenseGrid.FRONT_SHIELDS, 1.000000)
DefenseGrid.SetShieldChargePerSecond(DefenseGrid.REAR_SHIELDS, 1.000000)
DefenseGrid.SetShieldChargePerSecond(DefenseGrid.TOP_SHIELDS, 1.000000)
DefenseGrid.SetShieldChargePerSecond(DefenseGrid.BOTTOM_SHIELDS, 1.000000)
DefenseGrid.SetShieldChargePerSecond(DefenseGrid.LEFT_SHIELDS, 1.000000)
DefenseGrid.SetShieldChargePerSecond(DefenseGrid.RIGHT_SHIELDS, 1.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(DefenseGrid)
#################################################
Eng1glow = App.BlinkingLightProperty_Create("Eng 1 glow")

Eng1glowForward = App.TGPoint3()
Eng1glowForward.SetXYZ(0.000000, 1.000000, 0.000000)
Eng1glowUp = App.TGPoint3()
Eng1glowUp.SetXYZ(0.000000, 0.000000, 1.000000)
Eng1glowRight = App.TGPoint3()
Eng1glowRight.SetXYZ(1.000000, 0.000000, 0.000000)
Eng1glow.SetOrientation(Eng1glowForward, Eng1glowUp, Eng1glowRight)
Eng1glowPosition = App.TGPoint3()
Eng1glowPosition.SetXYZ(0.000000, -0.870000, -0.001000)
Eng1glow.SetPosition(Eng1glowPosition)
Eng1glowLightColor = App.TGColorA()
Eng1glowLightColor.SetRGBA(1.000000, 1.000000, 1.000000, 1.000000)
Eng1glow.SetColor(Eng1glowLightColor)
Eng1glow.SetRadius(5.000000)
Eng1glow.SetPeriod(3.000000)
Eng1glow.SetDuration(0.000000)
Eng1glow.SetTextureName("scripts/Custom/NanoFXv2/SpecialFX/Gfx/Blinker/Blank.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(Eng1glow)
#################################################
ShuttleBay1OEP = App.ObjectEmitterProperty_Create("Shuttle Bay 1 OEP")

ShuttleBay1OEPForward = App.TGPoint3()
ShuttleBay1OEPForward.SetXYZ(0.000000, 1.000000, 0.000000)
ShuttleBay1OEPUp = App.TGPoint3()
ShuttleBay1OEPUp.SetXYZ(0.000000, 0.000000, 1.000000)
ShuttleBay1OEPRight = App.TGPoint3()
ShuttleBay1OEPRight.SetXYZ(0.000000, 5.580680, -0.250000)
ShuttleBay1OEP.SetOrientation(ShuttleBay1OEPForward, ShuttleBay1OEPUp, ShuttleBay1OEPRight)
ShuttleBay1OEPPosition = App.TGPoint3()
ShuttleBay1OEPPosition.SetXYZ(0.000000, 5.580680, -0.250000)
ShuttleBay1OEP.SetPosition(ShuttleBay1OEPPosition)
ShuttleBay1OEP.SetEmittedObjectType(ShuttleBay1OEP.OEP_SHUTTLE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay1OEP)
#################################################
ShuttleBay1 = App.HullProperty_Create("Shuttle Bay 1")

ShuttleBay1.SetMaxCondition(50.000000)
ShuttleBay1.SetCritical(0)
ShuttleBay1.SetTargetable(1)
ShuttleBay1.SetPrimary(0)
ShuttleBay1.SetPosition(0.000000, 5.580680, -0.250000)
ShuttleBay1.SetPosition2D(64.000000, 25.000000)
ShuttleBay1.SetRepairComplexity(14.500000)
ShuttleBay1.SetDisabledPercentage(0.000000)
ShuttleBay1.SetRadius(1.300000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShuttleBay1)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Power Core", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sublight Drive Sys", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Grid", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Damage Control", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engine 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Eng 1 glow", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Bridge", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Defense Grid", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("EAAchillesFreighterNoModules", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shuttle Bay 1 OEP", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)