import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

@t.test(0)
def exactMario0(test):
	test.test = lambda : not assertlib.contains(lib.outputOf(_fileName, [0]), "#")
	test.description = lambda : "prints a pyramid of height 0"

@t.test(1)
def exactMario3(test):
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName, [3]),
""" ##
 ###
####
""")
	test.description = lambda : "prints a pyramid of height 3"

@t.test(2)
def exactMario23(test):
	test.test = lambda : assertlib.contains(lib.outputOf(_fileName, [23]),
"""                      ##
                     ###
                    ####
                   #####
                  ######
                 #######
                ########
               #########
              ##########
             ###########
            ############
           #############
          ##############
         ###############
        ################
       #################
      ##################
     ###################
    ####################
   #####################
  ######################
 #######################
########################""")
	test.description = lambda : "prints a pyramid of height 23"


@t.test(10)
def handlesWrongInput(test):
	test.test = lambda : not assertlib.contains(lib.outputOf(_fileName, [100, -100, 0]), "#")
	test.description = lambda : "Can deal with incorrect input: -100 and 100"