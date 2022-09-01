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
                               		0.15,
                               		1.2,	 
					"data/textures/tactical/JTorpedoGlow.tga", 
					kGlowColor,
                               		2.0,
                              		0.5,
                              		0.6,	
					"data/textures/tactical/TorpedoFlares.tga",
					kGlowColor,										
                        	        40,
                                	0.12,
                                	0.27)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.30)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("JLSQuantum")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Quantum Torpedo")

def GetDamage():
	return 2350.0

def GetGuidanceLifetime():
	return 0.2

def GetMaxAngularAccel():
	return 20.3
