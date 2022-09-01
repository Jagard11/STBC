from Custom.Autoload.LoadNanoFX import *
import Foundation

class PlayerShipCreated(Foundation.TriggerDef):
        def __init__(self, name, eventKey, dict = {}):
                Foundation.TriggerDef.__init__(self, name, eventKey, dict)

        def __call__(self, pObject, pEvent, dict = {}):            
                CreateMenus()
                if pObject and pEvent:
                        pObject.CallNextHandler(pEvent)

PlayerShipCreated('Player Ship Created', Foundation.TriggerDef.ET_FND_CREATE_PLAYER_SHIP, dict = { 'modes': [ mode ] } )

def CreateMenus():
	import MissionLib
	pMission = MissionLib.GetMission()
	if pMission != None:
		if pMission.GetScript() == "QuickBattle.QuickBattle":
	                try:
                                # sample comment it out
				import Systems.Starbase12.Starbase
				Systems.Starbase12.Starbase.CreateMenus()

				# place systems here
				import Systems.AveryIII.AveryIII
				Systems.AveryIII.AveryIII.CreateMenus()

				import Systems.BorgPrime.BorgPrime
				Systems.BorgPrime.BorgPrime.CreateMenus()
	
				import Systems.CaretakerArray.CaretakerArray
				Systems.CaretakerArray.CaretakerArray.CreateMenus()

				import Systems.Tarok.Tarok
				Systems.Tarok.Tarok.CreateMenus()

				import Systems.SuspiriaArray.SuspiriaArray
				Systems.SuspiriaArray.SuspiriaArray.CreateMenus()

				import Systems.FluidicSpace.FluidicSpace
				Systems.FluidicSpace.FluidicSpace.CreateMenus()

				import Systems.IcePlanet.IcePlanet
				Systems.IcePlanet.IcePlanet.CreateMenus()

				import Systems.GravitonCatapult.GravitonCatapult
				Systems.GravitonCatapult.GravitonCatapult.CreateMenus()

				import Systems.KrenimHomeworld.KrenimHomeworld
				Systems.KrenimHomeworld.KrenimHomeworld.CreateMenus()

				import Systems.MalonHomeworld.MalonHomeworld
				Systems.MalonHomeworld.MalonHomeworld.CreateMenus()

				import Systems.DemonPlanet.DemonPlanet
				Systems.DemonPlanet.DemonPlanet.CreateMenus()

				import Systems.OcampaV.OcampaV
				Systems.OcampaV.OcampaV.CreateMenus()

				import Systems.Sikaris.Sikaris
				Systems.Sikaris.Sikaris.CreateMenus()

				import Systems.Talax.Talax
				Systems.Talax.Talax.CreateMenus()
	
				import Systems.TheVoid.TheVoid
				Systems.TheVoid.TheVoid.CreateMenus()

				import Systems.TranswarpHub.TranswarpHub
				Systems.TranswarpHub.TranswarpHub.CreateMenus()

				import Systems.VaadwaurHomeworld.VaadwaurHomeworld
				Systems.VaadwaurHomeworld.VaadwaurHomeworld.CreateMenus()

				import Systems.WaterPlanet.WaterPlanet
				Systems.WaterPlanet.WaterPlanet.CreateMenus()

				import Systems.VhnoriHomeworld.VhnoriHomeworld
				Systems.VhnoriHomeworld.VhnoriHomeworld.CreateMenus()

				import Systems.Unicomplex.Unicomplex
				Systems.Unicomplex.Unicomplex.CreateMenus()
				
	                except:
        	                pass   