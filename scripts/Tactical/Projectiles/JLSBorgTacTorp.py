import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(10.0 / 255.0, 255.0 / 255.0, 180.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(10.0 / 255.0, 255.0 / 255.0, 150.0 / 255.0, 1.000000)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/JLSBorgDiamond.tga",
					kCoreColor, 
					0.6,
					1.0,	 
					"data/Textures/Tactical/JTorpedoGlow.tga", 
					kGlowColor,
					4.0,	
					1.8,	 
					3.3,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					12,		
					1.7,		
					0.04)

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
	return(120.0)

def GetLaunchSound():
	return("JLSBT1")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Gravimetric Torpedo")

def GetDamage():
	return 1200.0

def GetGuidanceLifetime():
	return 12.0

def GetMaxAngularAccel():
	return 0.5
