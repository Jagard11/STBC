from bcdebug import debug
import App
import QuickBattle
import MissionLib

def CreateAI(pShip, pFriendlies=MissionLib.GetFriendlyGroup()):
        debug(__name__ + ", CreateAI")
        if not pFriendlies .GetNameTuple():
            pFriendlies .AddName("This ship probably wont exist")
	#########################################
	# Creating CompoundAI Attack at (108, 133)
	import AI.Compound.DomRamAI
	pAttack = AI.Compound.DomRamAI.CreateAI(pShip, pFriendlies)
	# Done creating CompoundAI Attack
	#########################################
	#########################################
	# Creating PreprocessingAI AvoidObstacles at (126, 263)
	## Setup:
	import AI.CustomPreprocessors
	pScript = AI.CustomPreprocessors.AvoidObstaclesRam()
	## The PreprocessingAI:
	pAvoidObstacles = App.PreprocessingAI_Create(pShip, "AvoidObstacles")
	pAvoidObstacles.SetInterruptable(1)
	pAvoidObstacles.SetPreprocessingMethod(pScript, "Update")
	pAvoidObstacles.SetContainedAI(pAttack)
	# Done creating PreprocessingAI AvoidObstacles
	#########################################
	#########################################
	# Creating ConditionalAI Wait at (29, 332)
	## Conditions:
	#### Condition TimePassed
	pTimePassed = App.ConditionScript_Create("Conditions.ConditionTimer", "ConditionTimer", 7, 0)
	## Evaluation function:
	def EvalFunc(bTimePassed):
		ACTIVE = App.ArtificialIntelligence.US_ACTIVE
		DORMANT = App.ArtificialIntelligence.US_DORMANT
		DONE = App.ArtificialIntelligence.US_DONE
		if bTimePassed:
			return ACTIVE
		return DORMANT
	## The ConditionalAI:
	pWait = App.ConditionalAI_Create(pShip, "Wait")
	pWait.SetInterruptable(1)
	pWait.SetContainedAI(pAvoidObstacles)
	pWait.AddCondition(pTimePassed)
	pWait.SetEvaluationFunction(EvalFunc)
	# Done creating ConditionalAI Wait
	#########################################


	return pWait
