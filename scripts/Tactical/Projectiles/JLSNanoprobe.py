########################################################################
#	Filename:	JLSNanoprobe.py				       #
#								       #
#								       #
#	Designer:	Jb06			  		       #
#								       #
########################################################################

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(149.0 / 255.0, 198.0 / 255.0, 76.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.2,
					1.0,	 
					"data/Textures/Tactical/JTorpedoGlow.tga", 
					kGlowColor,
					8.0,	
					0.5,	 
					0.9,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					15,		
					0.05,		
					0.27)

	pTorp.SetDamage(800.0)
	pTorp.SetDamageRadiusFactor(0.2)
	pTorp.SetGuidanceLifetime(60.0)
	pTorp.SetMaxAngularAccel(0.3)

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("Nanoprobe")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Enhanced Nanoprobes")

try:
	import FoundationTech
	import ftb.Tech.NanoprobeProjectile
	oFire = ftb.Tech.NanoprobeProjectile.NanoprobeProjectileDef('Nanoprobe Projectile')
	FoundationTech.dYields[__name__] = oFire
except:
	pass