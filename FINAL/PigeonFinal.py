class bird:
  def __init__(self, flaps=15, information='hello'): #Main function
    self.flaps = flaps
    self.information = information #defualt message if there is no textdata
    #self.information = textdata


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
      time.sleep(.5)
      print(b)
      time.sleep(.5)#Flapping time
      n=n+1

#bird = bird(3, "hi there")
#bird.askformessage()
#bird.fly()
#bird.delivermessage()

