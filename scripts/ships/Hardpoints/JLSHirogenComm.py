# C:\Users\Admin\BC Mods\bcsdk1_1\Tools\ModelPropertyEditor\H Com\JLSHirogenComm.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(20000.000000)
Hull.SetCritical(1)
Hull.SetTargetable(1)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 0.000000, 0.000000)
Hull.SetPosition2D(64.000000, 70.000000)
Hull.SetRepairComplexity(3.000000)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(2.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(10000.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(1)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.000000, -1.403780)
ShieldGenerator.SetPosition2D(96.000000, 60.000000)
ShieldGenerator.SetRepairComplexity(2.000000)
ShieldGenerator.SetDisabledPercentage(0.750000)
ShieldGenerator.SetRadius(1.000000)
ShieldGenerator.SetNormalPowerPerSecond(200.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 0.000000, 0.000000, 0.000000)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 110000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 110000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 110000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 110000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 110000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 110000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 34.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 34.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 34.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 34.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 34.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 34.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(4000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(1)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(-0.022029, 0.004683, 4.100000)
SensorArray.SetPosition2D(63.000000, 13.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.500000)
SensorArray.SetRadius(0.100000)
SensorArray.SetNormalPowerPerSecond(50.000000)
SensorArray.SetBaseSensorRange(5000.000000)
SensorArray.SetMaxProbes(10)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
ArtificialQuantumSingularity = App.PowerProperty_Create("Artificial Quantum Singularity")

ArtificialQuantumSingularity.SetMaxCondition(12000.000000)
ArtificialQuantumSingularity.SetCritical(1)
ArtificialQuantumSingularity.SetTargetable(1)
ArtificialQuantumSingularity.SetPrimary(1)
ArtificialQuantumSingularity.SetPosition(0.000000, 0.000000, 0.000000)
ArtificialQuantumSingularity.SetPosition2D(32.000000, 60.000000)
ArtificialQuantumSingularity.SetRepairComplexity(4.000000)
ArtificialQuantumSingularity.SetDisabledPercentage(0.500000)
ArtificialQuantumSingularity.SetRadius(2.000000)
ArtificialQuantumSingularity.SetMainBatteryLimit(300000.000000)
ArtificialQuantumSingularity.SetBackupBatteryLimit(100000.000000)
ArtificialQuantumSingularity.SetMainConduitCapacity(20000.000000)
ArtificialQuantumSingularity.SetBackupConduitCapacity(1000.000000)
ArtificialQuantumSingularity.SetPowerOutput(15000.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ArtificialQuantumSingularity)
#################################################
Engineering = App.RepairSubsystemProperty_Create("Engineering")

Engineering.SetMaxCondition(6000.000000)
Engineering.SetCritical(0)
Engineering.SetTargetable(0)
Engineering.SetPrimary(1)
Engineering.SetPosition(0.000000, 0.000000, 0.000000)
Engineering.SetPosition2D(63.000000, 27.000000)
Engineering.SetRepairComplexity(2.000000)
Engineering.SetDisabledPercentage(0.100000)
Engineering.SetRadius(1.000000)
Engineering.SetNormalPowerPerSecond(10.000000)
Engineering.SetMaxRepairPoints(40.000000)
Engineering.SetNumRepairTeams(4)
App.g_kModelPropertyManager.RegisterLocalTemplate(Engineering)
#################################################
HirogenComm = App.ShipProperty_Create("Hirogen Comm")

HirogenComm.SetGenus(2)
HirogenComm.SetSpecies(706)
HirogenComm.SetMass(300.000000)
HirogenComm.SetRotationalInertia(50000.000000)
HirogenComm.SetShipName("HirogenComm")
HirogenComm.SetModelFilename("data/Models/Ships/DQP/JLSHirogenComm/HirogenComm.nif")
HirogenComm.SetDamageResolution(15.000000)
HirogenComm.SetAffiliation(0)
HirogenComm.SetStationary(1)
HirogenComm.SetAIString("StarbaseAttack")
HirogenComm.SetDeathExplosionSound("g_lsBigDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(HirogenComm)

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
	prop = App.g_kModelPropertyManager.FindByName("Artificial Quantum Singularity", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engineering", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Hirogen Comm", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
