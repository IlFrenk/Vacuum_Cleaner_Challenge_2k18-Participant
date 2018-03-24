from . agents import *
from random import *


class GesenuBotVACClass(Agent):

	def __init__(self, x=2, y=2):
		Agent.__init__(self)
		self.name = 'GesenuBotVAC'
		self.img = 'GesenuBotVAC'
		self.lastAction = "none"
		self.backCount = 6
		self.nextAction = "none"
		self.posizioneX = 0
		self.posizioneY = 0
		self.actions = ['GoEast', 'GoSouth', 'GoWest', 'GoNorth']


		def program(status, bump, neighbors, view):

			self.posizioneX, self.posizioneY = LaMiaPosizione(view)
			if (status == "Dirty"):
				return "Suck"
			else:
				return Move(view)
		self.program = program


		def LaMiaPosizione(view):
			for x, row in enumerate(view):
				for y, item in enumerate(row):
					if(item == "Y"):
						return (x, y)


		def Move(view):
			posizioneX = self.posizioneX
			posizioneY = self.posizioneY
			FirstStepNoDirt(view)
			if(self.nextAction != "none"):
				tempVar = self.nextAction
				self.lastAction = tempVar
				self.nextAction = "none"
				return tempVar
			elif(view[posizioneX][posizioneY+1] == '*'):
				return Peek(1, 1, 1, 0, view)
			elif(view[posizioneX+1][posizioneY] == '*'):
				return Peek(1, -1, 2, 1, view)
			elif(view[posizioneX][posizioneY-1] == '*'):
				return Peek(-1, -1, 3, 2, view)
			elif(view[posizioneX-1][posizioneY] == '*'):
				return Peek(-1, 1, 0, 3, view)
			else:
				if(view[posizioneX][posizioneY+2] == '*'):
					return NeverLoseHope(0)
				elif(view[posizioneX-2][posizioneY] == '*'):
					return NeverLoseHope(3)
				elif(view[posizioneX][posizioneY-2] == '*'):
					return NeverLoseHope(2)
				elif(view[posizioneX+2][posizioneY] == '*'):
					return NeverLoseHope(1)
				else:
					if(view[posizioneX][posizioneY+3] == '*'):
						return NeverLoseHope(0)
					elif(view[posizioneX-3][posizioneY] == '*'):
						return NeverLoseHope(3)
					elif(view[posizioneX][posizioneY-3] == '*'):
						return NeverLoseHope(2)
					elif(view[posizioneX+3][posizioneY] == '*'):
						return NeverLoseHope(1)
					else:
						if(view[posizioneX][posizioneY+4] == '*'):
							return NeverLoseHope(0)
						elif(view[posizioneX-4][posizioneY] == '*'):
							return NeverLoseHope(3)
						elif(view[posizioneX][posizioneY-4] == '*'):
							return NeverLoseHope(2)
						elif(view[posizioneX+4][posizioneY] == '*'):
							return NeverLoseHope(1)
						else:
							if(view[posizioneX][posizioneY+5] == '*'):
								return NeverLoseHope(0)
							elif(view[posizioneX-5][posizioneY] == '*'):
								return NeverLoseHope(3)
							elif(view[posizioneX][posizioneY-5] == '*'):
								return NeverLoseHope(2)
							elif(view[posizioneX+4][posizioneY] == '*'):
								return NeverLoseHope(1)
							else:
								if(view[posizioneX][posizioneY+6] == '*'):
									return NeverLoseHope(0)
								elif(view[posizioneX-6][posizioneY] == '*'):
									return NeverLoseHope(3)
								elif(view[posizioneX][posizioneY-6] == '*'):
									return NeverLoseHope(2)
								elif(view[posizioneX+6][posizioneY] == '*'):
									return NeverLoseHope(1)
								else:
									if(view[posizioneX][posizioneY+7] == '*'):
										return NeverLoseHope(0)
									elif(view[posizioneX-7][posizioneY] == '*'):
										return NeverLoseHope(3)
									elif(view[posizioneX][posizioneY-7] == '*'):
										return NeverLoseHope(2)
									elif(view[posizioneX+7][posizioneY] == '*'):
										return NeverLoseHope(1)
									else:
										if(view[posizioneX][posizioneY+8] == '*'):
											return NeverLoseHope(0)
										elif(view[posizioneX-8][posizioneY] == '*'):
											return NeverLoseHope(3)
										elif(view[posizioneX][posizioneY-8] == '*'):
											return NeverLoseHope(2)
										elif(view[posizioneX+8][posizioneY] == '*'):
											return NeverLoseHope(1)
										else:
											if(view[posizioneX][posizioneY+9] == '*'):
												return NeverLoseHope(0)
											elif(view[posizioneX-9][posizioneY] == '*'):
												return NeverLoseHope(3)
											elif(view[posizioneX][posizioneY-9] == '*'):
												return NeverLoseHope(2)
											elif(view[posizioneX+9][posizioneY] == '*'):
												return NeverLoseHope(1)
											else:
												if(view[posizioneX][posizioneY+10] == '*'):
													return NeverLoseHope(0)
												elif(view[posizioneX-10][posizioneY] == '*'):
													return NeverLoseHope(3)
												elif(view[posizioneX][posizioneY-10] == '*'):
													return NeverLoseHope(2)
												elif(view[posizioneX+10][posizioneY] == '*'):
													return NeverLoseHope(1)
												else:
													if(self.backCount != 0):
														if(self.lastAction == self.actions[0]):
																return BackRuler(0, -1, 1, 3, 2, view)
														elif(self.lastAction == self.actions[1]):
																return BackRuler(-1, 0, 0, 2, 3, view)
														elif(self.lastAction == self.actions[2]):
																return BackRuler(0, 1, 3, 1, 0, view)
														elif(self.lastAction == self.actions[3]):
																return BackRuler(1, 0, 2, 0, 1, view)
														else:
															return 'NoOp'
													else:
														return 'NoOp'

		def ModifyCounter(index):
			if(index == 0):
				self.backCount = 6
			else:
				self.backCount -= 1

		def Peek(xPeek, yPeek, nextA, lastA, view):
			if(view[self.posizioneX + xPeek][self.posizioneY + yPeek] == '*'):
				self.nextAction = self.actions[nextA]
			self.lastAction = self.actions[lastA]
			ModifyCounter(0)
			return self.actions[lastA]

		def NeverLoseHope(lastA):
			self.lastAction = self.actions[lastA]
			if(self.backCount != 6):
				ModifyCounter(0)
			return self.actions[lastA]

		def BackRuler(xPeek, yPeek, act1, act2, backA, view):
			actions2 = [act1, act2]
			randN = choice(actions2)
			ModifyCounter(1)
			if(view[self.posizioneX + xPeek][self.posizioneY + yPeek] == '#'):
				return self.actions[randN]
			else:
				return self.actions[backA]

		def FirstStepNoDirt(view):
			posizioneX = self.posizioneX
			posizioneY = self.posizioneY
			if(self.lastAction == 'none'):
				if(view[posizioneX][posizioneY-1] == '#' and view[posizioneX+1][posizioneY] == '#' and view[posizioneX-1][posizioneY] == '#'):
					self.lastAction = self.actions[2]
				elif(view[posizioneX][posizioneY-1] == '#' and view[posizioneX][posizioneY+1] == '#' and view[posizioneX-1][posizioneY] == '#'):
					self.lastAction = self.actions[3]
				elif(view[posizioneX+1][posizioneY] == '#' and view[posizioneX-1][posizioneY] == '#' and view[posizioneX][posizioneY+1] == '#'):
					self.lastAction = self.actions[0]
				elif(view[posizioneX][posizioneY+1] == '#' and view[posizioneX][posizioneY-1] == '#' and view[posizioneX+1][posizioneY] == '#'):
					self.lastAction = self.actions[1]
