import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(173.0 / 255.0, 171.0 / 255.0, 249.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(47.0 / 255.0, 43.0 / 255.0, 209.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/JLSBorgDiamond.tga",
					kCoreColor, 
					0.3,
					6.0,	 
					"data/Textures/Tactical/JTorpedoGlow.tga", 
					kGlowColor,
					1.5,	
					0.6,	 
					0.8,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					43,		
					0.2,		
					0.2)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(60.0)

def GetLaunchSound():
	return("JLSVaadwaur")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Partical Cannon")

def GetDamage():
	return 150.0

def GetGuidanceLifetime():
	return 12.0

def GetMaxAngularAccel():
	return 1.5
