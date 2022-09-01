# C:\Program Files\Activision\Bridge Commander\scripts\ships\Hardpoints\F3022.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Shields = App.ShieldProperty_Create("Shields")

Shields.SetMaxCondition(400.000000)
Shields.SetCritical(0)
Shields.SetTargetable(0)
Shields.SetPrimary(1)
Shields.SetPosition(0.000000, 0.000000, 0.000000)
Shields.SetPosition2D(67.000000, 47.000000)
Shields.SetRepairComplexity(1.000000)
Shields.SetDisabledPercentage(0.500000)
Shields.SetRadius(0.002000)
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
Shields.SetShieldChargePerSecond(Shields.FRONT_SHIELDS, 0.000000)
Shields.SetShieldChargePerSecond(Shields.REAR_SHIELDS, 0.000000)
Shields.SetShieldChargePerSecond(Shields.TOP_SHIELDS, 0.000000)
Shields.SetShieldChargePerSecond(Shields.BOTTOM_SHIELDS, 0.000000)
Shields.SetShieldChargePerSecond(Shields.LEFT_SHIELDS, 0.000000)
Shields.SetShieldChargePerSecond(Shields.RIGHT_SHIELDS, 0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Shields)
#################################################
MainHull = App.HullProperty_Create("Main Hull")

MainHull.SetMaxCondition(1000.000000)
MainHull.SetCritical(1)
MainHull.SetTargetable(0)
MainHull.SetPrimary(1)
MainHull.SetPosition(0.000000, 0.000000, 0.000000)
MainHull.SetPosition2D(67.000000, 47.000000)
MainHull.SetRepairComplexity(3.000000)
MainHull.SetDisabledPercentage(0.000000)
MainHull.SetRadius(0.030000)
App.g_kModelPropertyManager.RegisterLocalTemplate(MainHull)
#################################################
Engines = App.ImpulseEngineProperty_Create("Engines")

Engines.SetMaxCondition(1500.000000)
Engines.SetCritical(0)
Engines.SetTargetable(0)
Engines.SetPrimary(1)
Engines.SetPosition(0.000000, 0.000000, 0.000000)
Engines.SetPosition2D(51.000000, 48.000000)
Engines.SetRepairComplexity(1.000000)
Engines.SetDisabledPercentage(0.500000)
Engines.SetRadius(0.003000)
Engines.SetNormalPowerPerSecond(75.000000)
Engines.SetMaxAccel(5.000000)
Engines.SetMaxAngularAccel(4.500000)
Engines.SetMaxAngularVelocity(1.100000)
Engines.SetMaxSpeed(7.200000)
Engines.SetEngineSound("Federation Engines")
App.g_kModelPropertyManager.RegisterLocalTemplate(Engines)
#################################################
FuelReserves = App.PowerProperty_Create("Fuel Reserves")

FuelReserves.SetMaxCondition(1200.000000)
FuelReserves.SetCritical(1)
FuelReserves.SetTargetable(1)
FuelReserves.SetPrimary(1)
FuelReserves.SetPosition(0.000000, -0.015720, 0.001500)
FuelReserves.SetPosition2D(65.000000, 60.000000)
FuelReserves.SetRepairComplexity(2.000000)
FuelReserves.SetDisabledPercentage(0.500000)
FuelReserves.SetRadius(0.010000)
FuelReserves.SetMainBatteryLimit(50000.000000)
FuelReserves.SetBackupBatteryLimit(20000.000000)
FuelReserves.SetMainConduitCapacity(200.000000)
FuelReserves.SetBackupConduitCapacity(100.000000)
FuelReserves.SetPowerOutput(100.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(FuelReserves)
#################################################
Radar = App.SensorProperty_Create("Radar")

Radar.SetMaxCondition(1800.000000)
Radar.SetCritical(0)
Radar.SetTargetable(1)
Radar.SetPrimary(1)
Radar.SetPosition(0.000000, 0.035000, 0.001500)
Radar.SetPosition2D(65.000000, 22.000000)
Radar.SetRepairComplexity(1.000000)
Radar.SetDisabledPercentage(0.750000)
Radar.SetRadius(0.500000)
Radar.SetNormalPowerPerSecond(30.000000)
Radar.SetBaseSensorRange(1500.000000)
Radar.SetMaxProbes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Radar)
#################################################
F3022 = App.ShipProperty_Create("F3022")

F3022.SetGenus(1)
F3022.SetSpecies(714)
F3022.SetMass(30.000000)
F3022.SetRotationalInertia(2000.000000)
F3022.SetShipName("F3022")
F3022.SetModelFilename("data/Models/Ships/F302/F3022.NIF")
F3022.SetDamageResolution(0.000100)
F3022.SetAffiliation(0)
F3022.SetStationary(0)
F3022.SetAIString("RomulanAttack")
F3022.SetDeathExplosionSound("g_lsDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(F3022)
#################################################
JetEngine1 = App.EngineProperty_Create("Jet Engine 1")

JetEngine1.SetMaxCondition(1400.000000)
JetEngine1.SetCritical(0)
JetEngine1.SetTargetable(1)
JetEngine1.SetPrimary(1)
JetEngine1.SetPosition(-0.020000, -0.040000, 0.001000)
JetEngine1.SetPosition2D(52.000000, 70.000000)
JetEngine1.SetRepairComplexity(2.000000)
JetEngine1.SetDisabledPercentage(0.500000)
JetEngine1.SetRadius(0.004000)
JetEngine1.SetEngineType(JetEngine1.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(JetEngine1)
#################################################
JetEngine2 = App.EngineProperty_Create("Jet Engine 2")

JetEngine2.SetMaxCondition(1400.000000)
JetEngine2.SetCritical(0)
JetEngine2.SetTargetable(1)
JetEngine2.SetPrimary(1)
JetEngine2.SetPosition(0.020000, -0.040000, 0.001000)
JetEngine2.SetPosition2D(78.000000, 70.000000)
JetEngine2.SetRepairComplexity(2.000000)
JetEngine2.SetDisabledPercentage(0.500000)
JetEngine2.SetRadius(0.004000)
JetEngine2.SetEngineType(JetEngine2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(JetEngine2)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 0.030000, 0.008000)
ViewscreenForward.SetPosition(ViewscreenForwardPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenForward)
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
ViewscreenLeftPosition.SetXYZ(0.000000, 0.030000, 0.008000)
ViewscreenLeft.SetPosition(ViewscreenLeftPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenLeft)
#################################################
ViewscreenRight = App.PositionOrientationProperty_Create("ViewscreenRight")

ViewscreenRightForward = App.TGPoint3()
ViewscreenRightForward.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenRightUp = App.TGPoint3()
ViewscreenRightUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenRightRight = App.TGPoint3()
ViewscreenRightRight.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenRight.SetOrientation(ViewscreenRightForward, ViewscreenRightUp, ViewscreenRightRight)
ViewscreenRightPosition = App.TGPoint3()
ViewscreenRightPosition.SetXYZ(0.000000, 0.030000, 0.008000)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.015000, 0.010000)
ViewscreenBack.SetPosition(ViewscreenBackPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenBack)
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
ViewscreenUpPosition.SetXYZ(0.000000, 0.030000, 0.008000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.030000, -0.005000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 0.030000, 0.008000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
Repair = App.RepairSubsystemProperty_Create("Repair")

Repair.SetMaxCondition(1200.000000)
Repair.SetCritical(0)
Repair.SetTargetable(0)
Repair.SetPrimary(1)
Repair.SetPosition(0.000000, 0.000000, 0.000000)
Repair.SetPosition2D(0.000000, 0.000000)
Repair.SetRepairComplexity(1.000000)
Repair.SetDisabledPercentage(0.500000)
Repair.SetRadius(0.010000)
Repair.SetNormalPowerPerSecond(1.000000)
Repair.SetMaxRepairPoints(2.000000)
Repair.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Repair)
#################################################
PortMissiles = App.TorpedoTubeProperty_Create("Port Missiles")

PortMissiles.SetMaxCondition(1200.000000)
PortMissiles.SetCritical(0)
PortMissiles.SetTargetable(1)
PortMissiles.SetPrimary(1)
PortMissiles.SetPosition(-0.027500, 0.020000, -0.004500)
PortMissiles.SetPosition2D(52.000000, 35.000000)
PortMissiles.SetRepairComplexity(1.000000)
PortMissiles.SetDisabledPercentage(0.250000)
PortMissiles.SetRadius(0.003000)
PortMissiles.SetDumbfire(1)
PortMissiles.SetWeaponID(0)
PortMissiles.SetGroups(24)
PortMissiles.SetDamageRadiusFactor(0.200000)
PortMissiles.SetIconNum(370)
PortMissiles.SetIconPositionX(67.000000)
PortMissiles.SetIconPositionY(65.000000)
PortMissiles.SetIconAboveShip(1)
PortMissiles.SetImmediateDelay(0.000000)
PortMissiles.SetReloadDelay(20.000000)
PortMissiles.SetMaxReady(1)
PortMissilesDirection = App.TGPoint3()
PortMissilesDirection.SetXYZ(0.000000, 1.000000, 0.000000)
PortMissiles.SetDirection(PortMissilesDirection)
PortMissilesRight = App.TGPoint3()
PortMissilesRight.SetXYZ(1.000000, 0.000000, 0.000000)
PortMissiles.SetRight(PortMissilesRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(PortMissiles)
#################################################
StarMissiles = App.TorpedoTubeProperty_Create("Star Missiles")

StarMissiles.SetMaxCondition(1200.000000)
StarMissiles.SetCritical(0)
StarMissiles.SetTargetable(1)
StarMissiles.SetPrimary(1)
StarMissiles.SetPosition(0.027500, 0.020000, -0.004500)
StarMissiles.SetPosition2D(78.000000, 35.000000)
StarMissiles.SetRepairComplexity(1.000000)
StarMissiles.SetDisabledPercentage(0.250000)
StarMissiles.SetRadius(0.003000)
StarMissiles.SetDumbfire(1)
StarMissiles.SetWeaponID(0)
StarMissiles.SetGroups(24)
StarMissiles.SetDamageRadiusFactor(0.200000)
StarMissiles.SetIconNum(370)
StarMissiles.SetIconPositionX(86.000000)
StarMissiles.SetIconPositionY(65.000000)
StarMissiles.SetIconAboveShip(1)
StarMissiles.SetImmediateDelay(0.000000)
StarMissiles.SetReloadDelay(20.000000)
StarMissiles.SetMaxReady(1)
StarMissilesDirection = App.TGPoint3()
StarMissilesDirection.SetXYZ(0.000000, 1.000000, 0.000000)
StarMissiles.SetDirection(StarMissilesDirection)
StarMissilesRight = App.TGPoint3()
StarMissilesRight.SetXYZ(1.000000, 0.000000, 0.000000)
StarMissiles.SetRight(StarMissilesRight)
App.g_kModelPropertyManager.RegisterLocalTemplate(StarMissiles)
#################################################
Missiles = App.TorpedoSystemProperty_Create("Missiles")

Missiles.SetMaxCondition(2200.000000)
Missiles.SetCritical(0)
Missiles.SetTargetable(0)
Missiles.SetPrimary(1)
Missiles.SetPosition(0.000000, 5.200000, 0.600000)
Missiles.SetPosition2D(64.000000, 10.000000)
Missiles.SetRepairComplexity(1.000000)
Missiles.SetDisabledPercentage(0.250000)
Missiles.SetRadius(0.090000)
Missiles.SetNormalPowerPerSecond(100.000000)
Missiles.SetWeaponSystemType(Missiles.WST_TORPEDO)
Missiles.SetSingleFire(0)
Missiles.SetAimedWeapon(1)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
Missiles.SetFiringChainString(kFiringChainString)
Missiles.SetMaxTorpedoes(0, 4)
Missiles.SetTorpedoScript(0, "Tactical.Projectiles.F302Missile")
Missiles.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(Missiles)
#################################################
Cockpit = App.HullProperty_Create("Cockpit")

Cockpit.SetMaxCondition(1000.000000)
Cockpit.SetCritical(1)
Cockpit.SetTargetable(1)
Cockpit.SetPrimary(0)
Cockpit.SetPosition(0.000000, 0.020000, 0.007000)
Cockpit.SetPosition2D(65.000000, 38.000000)
Cockpit.SetRepairComplexity(1.000000)
Cockpit.SetDisabledPercentage(0.500000)
Cockpit.SetRadius(0.008000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Cockpit)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("F3022", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shields", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Main Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Cockpit", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Radar", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Repair", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Fuel Reserves", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Engines", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Jet Engine 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Jet Engine 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Missiles", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Port Missiles", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Star Missiles", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
