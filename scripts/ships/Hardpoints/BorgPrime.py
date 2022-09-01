# C:\Program Files (x86)\Activision\Bridge Commander  KM v1 plus\scripts\ships\Hardpoints\BorgPrime.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
BorgPrime = App.ShipProperty_Create("BorgPrime")

BorgPrime.SetGenus(2)
BorgPrime.SetSpecies(145)
BorgPrime.SetMass(600000.000000)
BorgPrime.SetRotationalInertia(7000.000000)
BorgPrime.SetShipName("BorgPrime")
BorgPrime.SetModelFilename("data/models/bases/BorgPrime/BorgPrime.nif")
BorgPrime.SetDamageResolution(75.000000)
BorgPrime.SetAffiliation(0)
BorgPrime.SetStationary(0)
BorgPrime.SetAIString("StarbaseAttack")
BorgPrime.SetDeathExplosionSound("g_lsBigDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(BorgPrime)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(999999986991104.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(64.000000, 50.000000)
Hull.SetRepairComplexity(2.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(0.001000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(20000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(0)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, 0.000000)
ShieldGenerator.SetPosition2D(64.000000, 50.000000)
ShieldGenerator.SetRepairComplexity(1.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(0.000100)
ShieldGenerator.SetNormalPowerPerSecond(1000.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.203922, 0.631373, 1.000000, 0.466667)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 0.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 0.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(8000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, 0.000000, 4.200000)
SensorArray.SetPosition2D(64.000000, 15.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.000100)
SensorArray.SetNormalPowerPerSecond(1000.000000)
SensorArray.SetBaseSensorRange(20000.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
PowerPlant = App.PowerProperty_Create("Power Plant")

PowerPlant.SetMaxCondition(25000.000000)
PowerPlant.SetCritical(1)
PowerPlant.SetTargetable(1)
PowerPlant.SetPrimary(1)
PowerPlant.SetPosition(0.000000, 0.000000, -5.000000)
PowerPlant.SetPosition2D(64.000000, 100.000000)
PowerPlant.SetRepairComplexity(2.000000)
PowerPlant.SetDisabledPercentage(0.750000)
PowerPlant.SetRadius(0.000100)
PowerPlant.SetMainBatteryLimit(300000000.000000)
PowerPlant.SetBackupBatteryLimit(140000.000000)
PowerPlant.SetMainConduitCapacity(3000.000000)
PowerPlant.SetBackupConduitCapacity(1200.000000)
PowerPlant.SetPowerOutput(2500.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(PowerPlant)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")

Engineering.SetMaxCondition(10000.000000)
Engineering.SetCritical(0)
Engineering.SetTargetable(0)
Engineering.SetPrimary(1)
Engineering.SetPosition(0.000000, 0.000000, 0.000000)
Engineering.SetPosition2D(63.000000, 27.000000)
Engineering.SetRepairComplexity(2.000000)
Engineering.SetDisabledPercentage(0.100000)
Engineering.SetRadius(1.000000)
Engineering.SetNormalPowerPerSecond(1.000000)
Engineering.SetMaxRepairPoints(80.000000)
Engineering.SetNumRepairTeams(4)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
GravityGenerator = App.HullProperty_Create("Gravity Generator")

GravityGenerator.SetMaxCondition(100.000000)
GravityGenerator.SetCritical(0)
GravityGenerator.SetTargetable(0)
GravityGenerator.SetPrimary(0)
GravityGenerator.SetPosition(0.000000, 0.0, 0.0)
GravityGenerator.SetPosition2D(0.000000, 0.000000)
GravityGenerator.SetRepairComplexity(0.000000)
GravityGenerator.SetDisabledPercentage(0.01)
GravityGenerator.SetRadius(1.00000)
App.g_kModelPropertyManager.RegisterLocalTemplate(GravityGenerator)
#################################################
GravityGenerator1 = App.HullProperty_Create("Gravity Generator 1")

GravityGenerator1.SetMaxCondition(100.000000)
GravityGenerator1.SetCritical(0)
GravityGenerator1.SetTargetable(0)
GravityGenerator1.SetPrimary(0)
GravityGenerator1.SetPosition(0.000000, 0.0, 0.0)
GravityGenerator1.SetPosition2D(0.000000, 0.000000)
GravityGenerator1.SetRepairComplexity(0.000000)
GravityGenerator1.SetDisabledPercentage(0.01)
GravityGenerator1.SetRadius(1.00000)
App.g_kModelPropertyManager.RegisterLocalTemplate(GravityGenerator1)
#################################################
GravityGenerator2 = App.HullProperty_Create("Gravity Generator 2")

GravityGenerator2.SetMaxCondition(100.000000)
GravityGenerator2.SetCritical(0)
GravityGenerator2.SetTargetable(0)
GravityGenerator2.SetPrimary(0)
GravityGenerator2.SetPosition(0.000000, 0.0, 0.0)
GravityGenerator2.SetPosition2D(0.000000, 0.000000)
GravityGenerator2.SetRepairComplexity(0.000000)
GravityGenerator2.SetDisabledPercentage(0.01)
GravityGenerator2.SetRadius(1.00000)
App.g_kModelPropertyManager.RegisterLocalTemplate(GravityGenerator2)
#################################################
GravityGenerator3 = App.HullProperty_Create("Gravity Generator 3")

GravityGenerator3.SetMaxCondition(100.000000)
GravityGenerator3.SetCritical(0)
GravityGenerator3.SetTargetable(0)
GravityGenerator3.SetPrimary(0)
GravityGenerator3.SetPosition(0.000000, 0.0, 0.0)
GravityGenerator3.SetPosition2D(0.000000, 0.000000)
GravityGenerator3.SetRepairComplexity(0.000000)
GravityGenerator3.SetDisabledPercentage(0.01)
GravityGenerator3.SetRadius(1.00000)
App.g_kModelPropertyManager.RegisterLocalTemplate(GravityGenerator3)
#################################################
GravityGenerator4 = App.HullProperty_Create("Gravity Generator 4")

GravityGenerator4.SetMaxCondition(100.000000)
GravityGenerator4.SetCritical(0)
GravityGenerator4.SetTargetable(0)
GravityGenerator4.SetPrimary(0)
GravityGenerator4.SetPosition(0.000000, 0.0, 0.0)
GravityGenerator4.SetPosition2D(0.000000, 0.000000)
GravityGenerator4.SetRepairComplexity(0.000000)
GravityGenerator4.SetDisabledPercentage(0.01)
GravityGenerator4.SetRadius(1.00000)
App.g_kModelPropertyManager.RegisterLocalTemplate(GravityGenerator4)
#################################################
GravityGenerator5 = App.HullProperty_Create("Gravity Generator 5")

GravityGenerator5.SetMaxCondition(100.000000)
GravityGenerator5.SetCritical(0)
GravityGenerator5.SetTargetable(0)
GravityGenerator5.SetPrimary(0)
GravityGenerator5.SetPosition(0.000000, 0.0, 0.0)
GravityGenerator5.SetPosition2D(0.000000, 0.000000)
GravityGenerator5.SetRepairComplexity(0.000000)
GravityGenerator5.SetDisabledPercentage(0.01)
GravityGenerator5.SetRadius(1.00000)
App.g_kModelPropertyManager.RegisterLocalTemplate(GravityGenerator5)

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
	prop = App.g_kModelPropertyManager.FindByName("Power Plant", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("BorgPrime", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Gravity Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Gravity Generator 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Gravity Generator 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Gravity Generator 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Gravity Generator 4", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Gravity Generator 5", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
