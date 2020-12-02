class SillyString: 
    def __init__(self): 
        self.string = None 

    def getString(self, inputString): 
        self.string = inputString 

    def printString(self): 
        if self.string is not None: 
            print(self.string.upper()) 
        if self.string is None: 
            print("No string to print, use getString to add one\n") 

if __name__ == "__main__":  
    mySillyString = SillyString() 
    newString = input("Enter a string:\n") 
    mySillyString.getString(newString) 
    mySillyString.printString() 