class bird:
  def __init__(self, flaps=15, information='hello'):
    self.flaps = flaps
    self.information = information #defualt message if there is no textdata
    # self.information = textdata

  #def askformessage():
   # information=input("What message do you want the pigeon to carry?: ")

  def delivermessage(self):
    #print("Oh look, it's a carrirer pigeon! Let's see what is has to say...")
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
      time.sleep(.5)
      print(b)
      time.sleep(.5)
      n=n+1

bird = bird(3, "hi there")
#bird.askformessage()
bird.fly()
bird.delivermessage()

#Source: http://ascii.co.uk/art/pigeon
#https://stackoverflow.com/questions/34980251/how-to-print-multiple-lines-of-text-with-python