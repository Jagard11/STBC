###############################################################################
#	Filename:	ZahlTorpedo.py
#	
#	Confidential and Proprietary, Copyright 2000 by Totally Games
#	
#	Script for filling in the attributes of photon torpedoes.
#	
#	Created:	11/3/00 -	Erik Novales
#
#	Modified by:	Queball - 10/04/2004
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
	kCoreColor = App.TGColorA()
	kCoreColor.SetRGBA(0.0 / 255.0, 222.0 / 255.0, 253.0 / 255.0, 1.000000)
	kGlowColor = App.TGColorA()
	kGlowColor.SetRGBA(0.0 / 255.0, 98.0 / 255.0, 239.0 / 255.0, 1.000000)
	kFlareColor = App.TGColorA()
	kFlareColor.SetRGBA(0.0 / 255.0, 45.0 / 255.0, 220.0 / 255.0, 1.000000)		

	pTorp.CreateTorpedoModel(
					"data/Textures/Tactical/TorpedoCore.tga",
					kCoreColor,
					0.1,
					0.30,	 
					"data/Textures/Tactical/JTorpedoGlow.tga", 
					kGlowColor,
					3.0,	
					0.1,	 
					0.6,	
					"data/Textures/Tactical/TorpedoFlares.tga",
					kFlareColor,										
					15,		
					0.5,		
					0.3)

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.13)
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
	return("JLSMawasi Torpedo")

def GetPowerCost():
	return(20.0)

def GetName():
	return("Plasma Torpdeo")

def GetDamage():
	return 1250.0

def GetGuidanceLifetime():
	return 6.0

def GetMaxAngularAccel():
	return 0.25
