import App

def Create(pTorp):
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 255.0 / 255.0, 128.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(255.0 / 255.0, 128.0 / 255.0, 0.0 / 255.0, 1.000000)	

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/ZZ_VoyPhotonCore.tga",
					kCoreColor, 
                               		0.005,
                               		10.0,	 
					"data/textures/tactical/ZZ_VoyPhotonGlow3.tga", 
					kGlowColor,
                               		4.0,
                              		0.1,
                              		0.04,	
					"data/textures/tactical/TorpedoFlares.tga",
					kGlowColor,										
                        	        20,
                                	0.07,
                                	0.07)



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
	return(38.0)

def GetLaunchSound():
	return("VoyPhoton")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Mirco Photon Torpedo")

def GetDamage():
	return 1150.0

def GetGuidanceLifetime():
	return 0.2

def GetMaxAngularAccel():
	return 20.3
