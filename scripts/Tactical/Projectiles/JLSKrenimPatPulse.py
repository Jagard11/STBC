###############################################################################
#	Filename:	JLSKrenimPulse.py
#	
#	Modified:	8/18/02 -	
###############################################################################

import App
import string
pWeaponLock = {}

###############################################################################
#	Create(pTorp)
#	
#	Creates a Krenim disruptor blast which goes through shields.
#	
#	Args:	pTorp - the "torpedo", ready to be filled-in
#	
#	Return:	zero
###############################################################################
def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.500000, 0.000000, 1.000000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(0.800000, 0.800000, 1.000000, 1.000000)
	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 1.8, 0.30) 	

	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.1)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(65.0)

def GetLaunchSound():
	return("JLSKrenimP")

def GetPowerCost():
	return(10.0)

def GetName():
	return("Plasmatic Torpedo")

def GetDamage():
	return 390.0

def GetGuidanceLifetime():
	return 1.0

def GetMaxAngularAccel():
	return 0.055

def GetLifetime():
	return 8.0

