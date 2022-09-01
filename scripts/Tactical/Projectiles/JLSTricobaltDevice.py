#script modified by Lint

import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(104.0 / 255.0, 200.0 / 255.0, 255.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/JLSTorpedoCore.tga",
					kCoreColor, 
					0.6,
					3.5,	 
					"data/Textures/Tactical/JLSTorpedoGlow.tga", 
					kGlowColor,
					7,	
					7.10,	 
					7.75,	
					"data/Textures/Tactical/JLSTorpedoFlares.tga",
					kGlowColor,										
					0,		
					0.1,		
					0.14)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.25)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.QUANTUM)

	return(0)

def GetLaunchSpeed():
	return(45.0)

def GetLaunchSound():
	return("JLSTricobaltDevice")

def GetPowerCost():
	return(30.0)

def GetName():
	return("Tricobalt Device")

def GetDamage():
	return 58500.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.15

def GetLifetime():
	return 20.0

