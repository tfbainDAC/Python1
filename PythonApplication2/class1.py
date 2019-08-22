#
# Example file for working with classes
#

# defines a class using the class keyword, in this program myClass is the super class for anotherClass.
class myClass():                                                                    
  def method1(self):                                                                                               
    print ("myClass method1")
    
  def method2(self, someString):
    print ("myClass method2: " + someString)
    
#myClass is the superclass for anotherClass and so methods from the superclass can be inherited.
class anotherClass(myClass):                                         
  def method1(self):
    myClass.method1(self);                                            #using the superclass myClass method1, must use the self keyword
    print ("anotherClass method1")

  def method2(self,someString):                                 # overrides method 2 in the superclass / baseclass
    print ("anotherClass method2")
    
      
def main():                                                                        # main function, not part of myClass      
  c = myClass()                                                                  # creates object c instance of myClass()
  c.method1()                                                                   #do not have to use the self keyword as automatically handled
  c.method2("This is a string")
  c2 = anotherClass()                                                       # creates object c2 instance of anotherClass
  c2.method1()                                                                 # can use the inherited method from the superclass    
  c2.method2("This is a string")                                    #calls the method 2 from anotherClass NOT the inherited method2 

if __name__ == "__main__":
  main()
