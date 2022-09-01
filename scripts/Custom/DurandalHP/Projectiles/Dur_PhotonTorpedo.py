###############################################################################
#	Filename:	PhotonTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
###############################################################################

import App

###############################################################################
#	Create(pTorp)
#	
#	Creates a photon torpedo.
#	
#	Args:	pTorp - the torpedo, ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(165.0 / 255.0, 40.0 / 255.0, 0.0, 1.0)	
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(255.0 / 255.0, 225.0 / 255.0, 100.0 / 255.0, 1.0)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(255.0 / 255.0, 65.0 / 255.0, 0.0, 1.0)

	# Params are:

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor, 
					0.05,
					1.2,	 
					"scripts/Custom/DurandalHP/Textures/FTBpoltorp02.tga", 
					kGlowColor,
					2.0,	
					0.6,	 
					0.7,	
					"scripts/Custom/DurandalHP/Textures/Dur_TorpedoFlares.tga",
					kFlareColor,										
					10,		
					0.35,		
					0.3)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.27)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.PHOTON)

	return(0)

def GetLaunchSpeed():
	return(20.0)

def GetLaunchSound():
	return("Photon Torpedo")

def GetPowerCost():
	return(40.0)

def GetName():
	return("Photon")

def GetDamage():
	return 600.0

def GetGuidanceLifetime():
	return 12.0

def GetMaxAngularAccel():
	return 0.15

def GetLifetime():
	return 20.0

def GetFlashColor():
	return (165.0, 40.0, 0.0)
