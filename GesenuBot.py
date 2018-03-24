from . agents import *


class GesenuBotClass(Agent):

    def __init__(self, x=2, y=2):
        Agent.__init__(self)

        ##
        # Personalize the identifier of this class.
        # Will be used instead of the class name
        # in neighbours info
        self.name = 'GesenuBot'
        self.img = 'GesenuBot'

        def program(status, bump, neighbors, view):


            print(status, bump, neighbors)
            self.print_map(view)

            actions = ['GoEast', 'GoWest', 'GoNorth', 'GoSouth']
            posizioneX, posizioneY = LaMiaPosizione(view)

            if(status == 'Dirty'):
                return 'Suck'
            else:
                if(view[posizioneX][posizioneY+1]=='*'):
                    #print(view[posizioneX][posizioneY+1])
                    #print('x: '+str(posizioneX)+' y: '+str(posizioneY+1))
                    #print("vado a destra")
                    return actions[0]
                elif(view[posizioneX-1][posizioneY]=='*'):
                    #print(view[posizioneX-1][posizioneY])
                    #print('x: '+str(posizioneX-1)+' y: '+str(posizioneY))
                    #print("vado in alto")
                    return actions[2]
                elif(view[posizioneX][posizioneY-1]=='*'):
                    #print(view[posizioneX][posizioneY-1])
                    #print('x: '+str(posizioneX)+' y: '+str(posizioneY-1))
                    #print("vado a sinistra")
                    return actions[1]
                elif(view[posizioneX+1][posizioneY]=='*'):
                    #print(view[posizioneX+1][posizioneY])
                    #print('x: '+str(posizioneX+1)+' y: '+str(posizioneY))
                    #print("vado in basso")
                    return actions[3]
                else:
                    if(view[posizioneX][posizioneY+2]=='*'):
                        #print("vado a destra x2")
                        return actions[0]
                    elif(view[posizioneX-2][posizioneY]=='*'):
                        #print("vado in alto x2")
                        return actions[2]
                    elif(view[posizioneX][posizioneY-2]=='*'):
                        #print("vado a sinistra x2")
                        return actions[1]
                    elif(view[posizioneX+2][posizioneY]=='*'):
                        #print("vado in basso x2")
                        return actions[3]
                    else:
                        if(view[posizioneX][posizioneY+3]=='*'):
                            #print("vado a destra x3")
                            return actions[0]
                        elif(view[posizioneX-3][posizioneY]=='*'):
                            #print("vado in alto x3")
                            return actions[2]
                        elif(view[posizioneX][posizioneY-3]=='*'):
                            #print("vado a sinistra x3")
                            return actions[1]
                        elif(view[posizioneX+3][posizioneY]=='*'):
                            #print("vado in basso x3")
                            return actions[3]
                        else:
                            if(view[posizioneX][posizioneY+4]=='*'):
                                #print("vado a destra x4")
                                return actions[0]
                            elif(view[posizioneX-4][posizioneY]=='*'):
                                #print("vado in alto x4")
                                return actions[2]
                            elif(view[posizioneX][posizioneY-4]=='*'):
                                #print("vado a sinistra x4")
                                return actions[1]
                            elif(view[posizioneX+4][posizioneY]=='*'):
                                #print("vado in basso x4")
                                return actions[3]
                            else:
                                if(view[posizioneX][posizioneY+5]=='*'):
                                    #print("vado a destra x5")
                                    return actions[0]
                                elif(view[posizioneX-5][posizioneY]=='*'):
                                    #print("vado in alto x5")
                                    return actions[2]
                                elif(view[posizioneX][posizioneY-5]=='*'):
                                    #print("vado a sinistra x5")
                                    return actions[1]
                                elif(view[posizioneX+5][posizioneY]=='*'):
                                    #print("vado in basso x5")
                                    return actions[3]
                                else:
                                    if(view[posizioneX][posizioneY+6]=='*'):
                                        #print("vado a destra x6")
                                        return actions[0]
                                    elif(view[posizioneX-6][posizioneY]=='*'):
                                        #print("vado in alto x6")
                                        return actions[2]
                                    elif(view[posizioneX][posizioneY-6]=='*'):
                                        #print("vado a sinistra x6")
                                        return actions[1]
                                    elif(view[posizioneX+6][posizioneY]=='*'):
                                        #print("vado in basso x6")
                                        return actions[3]
                                    else:
                                        if(view[posizioneX][posizioneY+7]=='*'):
                                            #print("vado a destra x7")
                                            return actions[0]
                                        elif(view[posizioneX-7][posizioneY]=='*'):
                                            #print("vado in alto x7")
                                            return actions[2]
                                        elif(view[posizioneX][posizioneY-7]=='*'):
                                            #print("vado a sinistra x7")
                                            return actions[1]
                                        elif(view[posizioneX+7][posizioneY]=='*'):
                                            #print("vado in basso x7")
                                            return actions[3]
                                        else:
                                            #print("vado a nanna")
                                            return 'NoOp'
        self.program = program


        #funzione per determinare dove sei
        def LaMiaPosizione(view):
            for x, row in enumerate(view):
                for y, item in enumerate(row):
                    if(item == 'Y'):
                        return (x,y)
