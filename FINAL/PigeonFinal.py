class bird:
  def __init__(self, flaps=15, information='hello'): #Main function
    self.flaps = flaps
    self.information = information #defualt message if there is no user specified message as information
    #self.information = textdata #ignore this, not used


  def delivermessage(self):#Deliver Message

    print(self.information)

  def fly(self):


    import time


    a="""                 
                               .----. 
                              /      \ 
                           .-'  O     \ 
                          '____       | 
                               \ ______\ 
                                )-------\__ 
                               /   /       \__ 
                              /   /       \   \___
                              |   \        \      \________ 
                              |    \        \           ---| 
                               \    \__      \          ---| 
                                \      \__    \ ___     ---| 
                                 \      | \_   \   |_______/ 
                                  --    |   \__| 
                                    \ / / 
                                     / / 
                                    / / 
                           _____,^-( /______
                          |_____ ,^-(/ _____|
    """      
                                 
    b="""                                                __
                               .----.         _/  |
                              /      \     __/    /
                           .-'  O     \ __/      /
                          '____       |/        /
                               \ _____/        /
                                )----/        /        
                               /     \       /          
                              /       \     /___    
                              |                 \_________
                              |                        ---|
                               \                       ---|
                                \        _________     ---|
                                 \      |         \_______/
                                  --    |         
                                    \ / /
                                     / /
                                    / /
                           _____,^-( /______
                          |_____ ,^-(/ _____|          
    """                             

    n=0
    while n <= self.flaps:
      print(a)
      print(self.information)#Prints info near scroll
      time.sleep(.5)#time delay between print outs of pigeon (wings down)
      print(b)
      time.sleep(.5)#time delay between print outs of pigeon (wings up)
      n=n+1

      
#bird = bird(3, "hi there") #ignore all this stuff for now, not used
#bird.askformessage()
#bird.fly()
#bird.delivermessage()

