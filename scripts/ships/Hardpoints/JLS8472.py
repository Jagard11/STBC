# C:\Users\Admin\FOR TIQUD\Species 8472\Data\Models\Ships\DQP\JLS8472\JLS8472.py
# This file was automatically generated - modify at your own risk.
# 

import App
import GlobalPropertyTemplates
# Setting up local templates.
#################################################
Warp = App.EngineProperty_Create("Warp")

Warp.SetMaxCondition(40000.000000)
Warp.SetCritical(0)
Warp.SetTargetable(0)
Warp.SetPrimary(1)
Warp.SetPosition(0.001013, -0.195095, -0.000641)
Warp.SetPosition2D(63.000000, 38.000000)
Warp.SetRepairComplexity(1.000000)
Warp.SetDisabledPercentage(0.250000)
Warp.SetRadius(0.010000)
Warp.SetEngineType(Warp.EP_WARP)
App.g_kModelPropertyManager.RegisterLocalTemplate(Warp)
#################################################
Pod1 = App.EngineProperty_Create("Pod 1")

Pod1.SetMaxCondition(900000.000000)
Pod1.SetCritical(0)
Pod1.SetTargetable(0)
Pod1.SetPrimary(1)
Pod1.SetPosition(-0.031816, -0.249748, -0.018606)
Pod1.SetPosition2D(45.000000, 93.000000)
Pod1.SetRepairComplexity(1.000000)
Pod1.SetDisabledPercentage(0.250000)
Pod1.SetRadius(0.100000)
Pod1.SetEngineType(Pod1.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Pod1)
#################################################
Pod2 = App.EngineProperty_Create("Pod 2")

Pod2.SetMaxCondition(900000.000000)
Pod2.SetCritical(0)
Pod2.SetTargetable(0)
Pod2.SetPrimary(1)
Pod2.SetPosition(0.000145, -0.248851, 0.037617)
Pod2.SetPosition2D(63.000000, 93.000000)
Pod2.SetRepairComplexity(1.000000)
Pod2.SetDisabledPercentage(0.250000)
Pod2.SetRadius(0.100000)
Pod2.SetEngineType(Pod2.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Pod2)
#################################################
Pod3 = App.EngineProperty_Create("Pod 3")

Pod3.SetMaxCondition(900000.000000)
Pod3.SetCritical(0)
Pod3.SetTargetable(0)
Pod3.SetPrimary(1)
Pod3.SetPosition(0.034738, -0.244175, -0.020402)
Pod3.SetPosition2D(78.000000, 93.000000)
Pod3.SetRepairComplexity(1.000000)
Pod3.SetDisabledPercentage(0.250000)
Pod3.SetRadius(0.100000)
Pod3.SetEngineType(Pod3.EP_IMPULSE)
App.g_kModelPropertyManager.RegisterLocalTemplate(Pod3)
#################################################
ProbeLauncher = App.ObjectEmitterProperty_Create("Probe Launcher")

ProbeLauncherForward = App.TGPoint3()
ProbeLauncherForward.SetXYZ(0.000000, 1.000000, 0.000000)
ProbeLauncherUp = App.TGPoint3()
ProbeLauncherUp.SetXYZ(0.000000, 0.000000, 1.000000)
ProbeLauncherRight = App.TGPoint3()
ProbeLauncherRight.SetXYZ(1.000000, 0.000000, 0.000000)
ProbeLauncher.SetOrientation(ProbeLauncherForward, ProbeLauncherUp, ProbeLauncherRight)
ProbeLauncherPosition = App.TGPoint3()
ProbeLauncherPosition.SetXYZ(0.000000, 0.640000, 0.000000)
ProbeLauncher.SetPosition(ProbeLauncherPosition)
ProbeLauncher.SetEmittedObjectType(ProbeLauncher.OEP_PROBE)
App.g_kModelPropertyManager.RegisterLocalTemplate(ProbeLauncher)
#################################################
ImpulsePods = App.ImpulseEngineProperty_Create("Impulse Pods")

ImpulsePods.SetMaxCondition(6000.000000)
ImpulsePods.SetCritical(0)
ImpulsePods.SetTargetable(0)
ImpulsePods.SetPrimary(1)
ImpulsePods.SetPosition(-0.021173, -0.183116, -0.010936)
ImpulsePods.SetPosition2D(63.000000, 111.000000)
ImpulsePods.SetRepairComplexity(1.000000)
ImpulsePods.SetDisabledPercentage(0.250000)
ImpulsePods.SetRadius(0.010000)
ImpulsePods.SetNormalPowerPerSecond(50.000000)
ImpulsePods.SetMaxAccel(13.699100)
ImpulsePods.SetMaxAngularAccel(1.250000)
ImpulsePods.SetMaxAngularVelocity(1.500000)
ImpulsePods.SetMaxSpeed(16.239000)
ImpulsePods.SetEngineSound("8472 Engine")
App.g_kModelPropertyManager.RegisterLocalTemplate(ImpulsePods)
#################################################
BeamF = App.PhaserProperty_Create("Beam F")

BeamF.SetMaxCondition(500000.000000)
BeamF.SetCritical(0)
BeamF.SetTargetable(0)
BeamF.SetPrimary(1)
BeamF.SetPosition(0.000000, 0.200000, 0.000000)
BeamF.SetPosition2D(20.000000, 25.000000)
BeamF.SetRepairComplexity(1.000000)
BeamF.SetDisabledPercentage(0.000000)
BeamF.SetRadius(1.600000)
BeamF.SetDumbfire(0)
BeamF.SetWeaponID(1)
BeamF.SetGroups(0)
BeamF.SetDamageRadiusFactor(1.250000)
BeamF.SetIconNum(364)
BeamF.SetIconPositionX(64.000000)
BeamF.SetIconPositionY(36.000000)
BeamF.SetIconAboveShip(1)
BeamF.SetFireSound("8472")
BeamF.SetMaxCharge(20.000000)
BeamF.SetMaxDamage(20000.000000)
BeamF.SetMaxDamageDistance(300.000000)
BeamF.SetMinFiringCharge(10.000000)
BeamF.SetNormalDischargeRate(1.000000)
BeamF.SetRechargeRate(1.000000)
BeamF.SetIndicatorIconNum(510)
BeamF.SetIndicatorIconPositionX(57.000000)
BeamF.SetIndicatorIconPositionY(32.000000)
BeamFForward = App.TGPoint3()
BeamFForward.SetXYZ(0.000000, 1.000000, 0.000000)
BeamFUp = App.TGPoint3()
BeamFUp.SetXYZ(1.000000, 0.000000, 0.000000)
BeamF.SetOrientation(BeamFForward, BeamFUp)
BeamF.SetWidth(0.010000)
BeamF.SetLength(0.010000)
BeamF.SetArcWidthAngles(-0.261799, 0.261799)
BeamF.SetArcHeightAngles(-0.261799, 0.261799)
BeamF.SetPhaserTextureStart(24)
BeamF.SetPhaserTextureEnd(31)
BeamF.SetPhaserWidth(0.300000)
kColor = App.TGColorA()
kColor.SetRGBA(0.874510, 0.439216, 0.000000, 1.000000)
BeamF.SetOuterShellColor(kColor)
kColor.SetRGBA(1.000000, 0.647059, 0.286275, 1.000000)
BeamF.SetInnerShellColor(kColor)
kColor.SetRGBA(0.768628, 0.768628, 0.000000, 1.000000)
BeamF.SetOuterCoreColor(kColor)
kColor.SetRGBA(1.000000, 1.000000, 0.501961, 1.000000)
BeamF.SetInnerCoreColor(kColor)
BeamF.SetNumSides(6)
BeamF.SetMainRadius(0.080000)
BeamF.SetTaperRadius(0.040000)
BeamF.SetCoreScale(0.500000)
BeamF.SetTaperRatio(0.250000)
BeamF.SetTaperMinLength(5.000000)
BeamF.SetTaperMaxLength(30.000000)
BeamF.SetLengthTextureTilePerUnit(0.500000)
BeamF.SetPerimeterTile(1.000000)
BeamF.SetTextureSpeed(0.010000)
BeamF.SetTextureName("data/JLS8472.tga")
App.g_kModelPropertyManager.RegisterLocalTemplate(BeamF)
#################################################
ShieldGenerator = App.ShieldProperty_Create("Shield Generator")

ShieldGenerator.SetMaxCondition(16520.000000)
ShieldGenerator.SetCritical(0)
ShieldGenerator.SetTargetable(0)
ShieldGenerator.SetPrimary(1)
ShieldGenerator.SetPosition(0.000000, 0.400000, 0.000000)
ShieldGenerator.SetPosition2D(63.000000, 66.000000)
ShieldGenerator.SetRepairComplexity(0.125000)
ShieldGenerator.SetDisabledPercentage(0.250000)
ShieldGenerator.SetRadius(0.220000)
ShieldGenerator.SetNormalPowerPerSecond(300.000000)
ShieldGeneratorShieldGlowColor = App.TGColorA()
ShieldGeneratorShieldGlowColor.SetRGBA(0.000000, 0.776471, 0.721569, 0.294118)
ShieldGenerator.SetShieldGlowColor(ShieldGeneratorShieldGlowColor)
ShieldGenerator.SetShieldGlowDecay(1.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.FRONT_SHIELDS, 300000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.REAR_SHIELDS, 300000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.TOP_SHIELDS, 300000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.BOTTOM_SHIELDS, 300000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.LEFT_SHIELDS, 300000.000000)
ShieldGenerator.SetMaxShields(ShieldGenerator.RIGHT_SHIELDS, 300000.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.FRONT_SHIELDS, 99.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.REAR_SHIELDS, 99.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.TOP_SHIELDS, 99.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.BOTTOM_SHIELDS, 99.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.LEFT_SHIELDS, 99.000000)
ShieldGenerator.SetShieldChargePerSecond(ShieldGenerator.RIGHT_SHIELDS, 99.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(ShieldGenerator)
#################################################
NeuralNode = App.PowerProperty_Create("Neural Node")

NeuralNode.SetMaxCondition(45210.000000)
NeuralNode.SetCritical(1)
NeuralNode.SetTargetable(0)
NeuralNode.SetPrimary(1)
NeuralNode.SetPosition(0.000000, -0.295000, 0.000000)
NeuralNode.SetPosition2D(63.000000, 79.000000)
NeuralNode.SetRepairComplexity(0.125000)
NeuralNode.SetDisabledPercentage(0.250000)
NeuralNode.SetRadius(0.150000)
NeuralNode.SetMainBatteryLimit(95000.000000)
NeuralNode.SetBackupBatteryLimit(5000.000000)
NeuralNode.SetMainConduitCapacity(2900.000000)
NeuralNode.SetBackupConduitCapacity(100.000000)
NeuralNode.SetPowerOutput(1000.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(NeuralNode)
#################################################
Hull = App.HullProperty_Create("Hull")

Hull.SetMaxCondition(994500.000000)
Hull.SetCritical(1)
Hull.SetTargetable(0)
Hull.SetPrimary(1)
Hull.SetPosition(0.000000, 1.000000, 0.000000)
Hull.SetPosition2D(64.000000, 64.000000)
Hull.SetRepairComplexity(0.062500)
Hull.SetDisabledPercentage(0.000000)
Hull.SetRadius(1.900000)
App.g_kModelPropertyManager.RegisterLocalTemplate(Hull)
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
ViewscreenForwardPosition.SetXYZ(0.000000, 1.380000, 0.000000)
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
ViewscreenBackPosition.SetXYZ(0.000000, -0.950000, 0.000000)
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
ViewscreenLeftPosition.SetXYZ(-0.130000, 0.000000, 0.000000)
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
ViewscreenRightPosition.SetXYZ(0.138000, 0.000000, 0.000000)
ViewscreenRight.SetPosition(ViewscreenRightPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(ViewscreenRight)
#################################################
ViewscreenUp = App.PositionOrientationProperty_Create("ViewscreenUp")

ViewscreenUpForward = App.TGPoint3()
ViewscreenUpForward.SetXYZ(0.000000, 1.000000, 0.000000)
ViewscreenUpUp = App.TGPoint3()
ViewscreenUpUp.SetXYZ(0.000000, 0.000000, 1.000000)
ViewscreenUpRight = App.TGPoint3()
ViewscreenUpRight.SetXYZ(1.000000, 0.000000, 0.000000)
ViewscreenUp.SetOrientation(ViewscreenUpForward, ViewscreenUpUp, ViewscreenUpRight)
ViewscreenUpPosition = App.TGPoint3()
ViewscreenUpPosition.SetXYZ(0.000000, 0.000000, 0.230000)
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
ViewscreenDownPosition.SetXYZ(0.000000, 0.000000, -0.130000)
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
FirstPersonCameraPosition.SetXYZ(0.000000, 1.000000, 0.000000)
FirstPersonCamera.SetPosition(FirstPersonCameraPosition)
App.g_kModelPropertyManager.RegisterLocalTemplate(FirstPersonCamera)
#################################################
BioElectricBeam = App.WeaponSystemProperty_Create("BioElectric Beam")

BioElectricBeam.SetMaxCondition(60000.000000)
BioElectricBeam.SetCritical(0)
BioElectricBeam.SetTargetable(0)
BioElectricBeam.SetPrimary(1)
BioElectricBeam.SetPosition(0.008239, 0.021534, 0.023550)
BioElectricBeam.SetPosition2D(-64.000000, -64.000000)
BioElectricBeam.SetRepairComplexity(2.000000)
BioElectricBeam.SetDisabledPercentage(0.250000)
BioElectricBeam.SetRadius(0.010000)
BioElectricBeam.SetNormalPowerPerSecond(200.000000)
BioElectricBeam.SetWeaponSystemType(BioElectricBeam.WST_PHASER)
BioElectricBeam.SetSingleFire(0)
BioElectricBeam.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
BioElectricBeam.SetFiringChainString(kFiringChainString)
App.g_kModelPropertyManager.RegisterLocalTemplate(BioElectricBeam)
#################################################
Bioship = App.ShipProperty_Create("Bioship")

Bioship.SetGenus(1)
Bioship.SetSpecies(103)
Bioship.SetMass(500000000.000000)
Bioship.SetRotationalInertia(7500000204423168.000000)
Bioship.SetShipName("Bioship")
Bioship.SetModelFilename("data/Models/Ships/DQP/JLS8472/8472.nif")
Bioship.SetDamageResolution(8.000000)
Bioship.SetAffiliation(1)
Bioship.SetStationary(0)
Bioship.SetAIString("FedAttack")
Bioship.SetDeathExplosionSound("g_lsBigDeathExplosions")
App.g_kModelPropertyManager.RegisterLocalTemplate(Bioship)
#################################################
ImmuneSystem = App.RepairSubsystemProperty_Create("Immune System")

ImmuneSystem.SetMaxCondition(32000.000000)
ImmuneSystem.SetCritical(0)
ImmuneSystem.SetTargetable(0)
ImmuneSystem.SetPrimary(1)
ImmuneSystem.SetPosition(0.000000, -0.100000, 0.000000)
ImmuneSystem.SetPosition2D(64.000000, 64.000000)
ImmuneSystem.SetRepairComplexity(2.000000)
ImmuneSystem.SetDisabledPercentage(0.100000)
ImmuneSystem.SetRadius(0.150000)
ImmuneSystem.SetNormalPowerPerSecond(0.000000)
ImmuneSystem.SetMaxRepairPoints(31.000000)
ImmuneSystem.SetNumRepairTeams(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(ImmuneSystem)
#################################################
SensorArray = App.SensorProperty_Create("Sensor Array")

SensorArray.SetMaxCondition(50000.000000)
SensorArray.SetCritical(0)
SensorArray.SetTargetable(0)
SensorArray.SetPrimary(1)
SensorArray.SetPosition(0.000000, -0.500000, 0.000000)
SensorArray.SetPosition2D(63.000000, 35.000000)
SensorArray.SetRepairComplexity(1.000000)
SensorArray.SetDisabledPercentage(0.250000)
SensorArray.SetRadius(0.100000)
SensorArray.SetNormalPowerPerSecond(150.000000)
SensorArray.SetBaseSensorRange(200000.000000)
SensorArray.SetMaxProbes(8)
App.g_kModelPropertyManager.RegisterLocalTemplate(SensorArray)
#################################################
TranswarpPod = App.WarpEngineProperty_Create("Transwarp Pod")

TranswarpPod.SetMaxCondition(600000.000000)
TranswarpPod.SetCritical(0)
TranswarpPod.SetTargetable(0)
TranswarpPod.SetPrimary(1)
TranswarpPod.SetPosition(0.001013, -0.195095, -0.000641)
TranswarpPod.SetPosition2D(63.000000, 111.000000)
TranswarpPod.SetRepairComplexity(2.000000)
TranswarpPod.SetDisabledPercentage(0.250000)
TranswarpPod.SetRadius(0.150000)
TranswarpPod.SetNormalPowerPerSecond(0.000000)
App.g_kModelPropertyManager.RegisterLocalTemplate(TranswarpPod)
#################################################
TorpedoSystem = App.TorpedoSystemProperty_Create("Torpedo System")

TorpedoSystem.SetMaxCondition(10000.000000)
TorpedoSystem.SetCritical(0)
TorpedoSystem.SetTargetable(0)
TorpedoSystem.SetPrimary(1)
TorpedoSystem.SetPosition(0.000000, 0.000000, 0.000000)
TorpedoSystem.SetPosition2D(0.000000, 0.000000)
TorpedoSystem.SetRepairComplexity(1.000000)
TorpedoSystem.SetDisabledPercentage(0.500000)
TorpedoSystem.SetRadius(0.020000)
TorpedoSystem.SetNormalPowerPerSecond(5.000000)
TorpedoSystem.SetWeaponSystemType(TorpedoSystem.WST_TORPEDO)
TorpedoSystem.SetSingleFire(1)
TorpedoSystem.SetAimedWeapon(0)
kFiringChainString = App.TGString()
kFiringChainString.SetString("")
TorpedoSystem.SetFiringChainString(kFiringChainString)
TorpedoSystem.SetMaxTorpedoes(0, 20)
TorpedoSystem.SetTorpedoScript(0, "Tactical.Projectiles.ZZ_VoyPhoton")
TorpedoSystem.SetNumAmmoTypes(1)
App.g_kModelPropertyManager.RegisterLocalTemplate(TorpedoSystem)
#################################################
TorpedoTube2 = App.TorpedoTubeProperty_Create("Torpedo Tube 2")

TorpedoTube2.SetMaxCondition(10500.000000)
TorpedoTube2.SetCritical(0)
TorpedoTube2.SetTargetable(1)
TorpedoTube2.SetPrimary(1)
TorpedoTube2.SetPosition(0.000000, 0.000000, 0.000000)
TorpedoTube2.SetPosition2D(65.000000, -2.000000)
TorpedoTube2.SetRepairComplexity(0.800000)
TorpedoTube2.SetDisabledPercentage(0.750000)
TorpedoTube2.SetRadius(0.004700)
TorpedoTube2.SetDumbfire(1)
TorpedoTube2.SetWeaponID(0)
TorpedoTube2.SetGroups(0)
TorpedoTube2.SetDamageRadiusFactor(0.600000)
TorpedoTube2.SetIconNum(370)
TorpedoTube2.SetIconPositionX(78.000000)
TorpedoTube2.SetIconPositionY(25.000000)
TorpedoTube2.SetIconAboveShip(1)
TorpedoTube2.SetImmediateDelay(0.100000)
TorpedoTube2.SetReloadDelay(20.000000)
TorpedoTube2.SetMaxReady(2)
TorpedoTube2Direction = App.TGPoint3()
TorpedoTube2Direction.SetXYZ(0.000000, 1.000000, 0.000000)
TorpedoTube2.SetDirection(TorpedoTube2Direction)
TorpedoTube2Right = App.TGPoint3()
TorpedoTube2Right.SetXYZ(1.000000, 0.000000, 0.000000)
TorpedoTube2.SetRight(TorpedoTube2Right)
App.g_kModelPropertyManager.RegisterLocalTemplate(TorpedoTube2)

# Property load function.
def LoadPropertySet(pObj):
	"Sets up the object's properties."
	prop = App.g_kModelPropertyManager.FindByName("Hull", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Neural Node", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Shield Generator", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Sensor Array", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Impulse Pods", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Pod 1", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Pod 2", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Pod 3", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Transwarp Pod", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Warp", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Immune System", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("BioElectric Beam", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Beam F", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)
	prop = App.g_kModelPropertyManager.FindByName("Bioship", App.TGModelPropertyManager.LOCAL_TEMPLATES)
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
	prop = App.g_kModelPropertyManager.FindByName("Probe Launcher", App.TGModelPropertyManager.LOCAL_TEMPLATES)
	if (prop != None):
		pObj.AddToSet("Scene Root", prop)