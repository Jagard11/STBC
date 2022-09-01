import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
    	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 255.0 / 255.0, 1.0)
    	kGlowColor = App.TGColorA()
    	kGlowColor.SetRGBA(25.0 / 255.0, 25.0 / 255.0, 50.0 / 255.0, 1.0)
    	kFlareColor = App.TGColorA()
    	kFlareColor.SetRGBA(50.0 / 255.0, 50.0 / 255.0, 100.0 / 255.0, 1.0)

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.1,
					0.0,	 
					"data/Textures/Tactical/JTorpedoGlow.tga", 
					kGlowColor,
					0.5,	
					0.6,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kGlowColor,										
					42,		
					0.1,		
					0.5)

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
	return(40.0)

def GetLaunchSound():
	return("JLSTTorp")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Photonic Torpedo")

def GetDamage():
	return 450.0

def GetGuidanceLifetime():
	return 12.0

def GetMaxAngularAccel():
	return 2.1
