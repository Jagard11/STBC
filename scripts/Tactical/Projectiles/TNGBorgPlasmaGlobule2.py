########################################################################
#	Filename:	TNGBorgPlasmaGlobule2.py		       #
#								       #
#	Description:	Creates a TNG Borg Plasma Cannon projectile    #
#								       #
#	Designer:	Bryan Cook				       #
#								       #
#	Date:		4/14/2006				       #
########################################################################

import App

def Create(pTorp):

	kOuterShellColor = App.TGColorA()
	kOuterShellColor.SetRGBA(0.950000, 1.000000, 0.600000, 1.000000)	
	kOuterCoreColor = App.TGColorA()
	kOuterCoreColor.SetRGBA(1.000000, 1.000000, 0.800000, 1.000000)

	pTorp.CreateDisruptorModel(kOuterShellColor,kOuterCoreColor, 0.3, 0.175) 	
	pTorp.SetDamage( GetDamage() )
	pTorp.SetDamageRadiusFactor(0.15)
	pTorp.SetGuidanceLifetime( GetGuidanceLifetime() )
	pTorp.SetMaxAngularAccel( GetMaxAngularAccel() )
	pTorp.SetLifetime( GetLifetime() )

	# Multiplayer specific stuff.  Please, if you create a new torp
	# type. modify the SpeciesToTorp.py file to add the new type.
	import Multiplayer.SpeciesToTorp
	pTorp.SetNetType (Multiplayer.SpeciesToTorp.DISRUPTOR)

	return(0)

def GetLaunchSpeed():
	return(50.0)

def GetLaunchSound():
	return("Borg Disruptor")

def GetPowerCost():
	return(10.0)

def GetName():
	return("BorgDisruptor")

def GetDamage():
	return 750.0

def GetGuidanceLifetime():
	return 0.0

def GetMaxAngularAccel():
	return 0.005

def GetLifetime():
	return 10.0
