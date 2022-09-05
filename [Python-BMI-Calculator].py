from traceback import print_tb

print ('''
                                                                                                                                  
    _/_/_/    _/      _/  _/_/_/        _/_/_/            _/                      _/              _/                          
   _/    _/  _/_/  _/_/    _/        _/          _/_/_/  _/    _/_/_/  _/    _/  _/    _/_/_/  _/_/_/_/    _/_/    _/  _/_/   
  _/_/_/    _/  _/  _/    _/        _/        _/    _/  _/  _/        _/    _/  _/  _/    _/    _/      _/    _/  _/_/        
 _/    _/  _/      _/    _/        _/        _/    _/  _/  _/        _/    _/  _/  _/    _/    _/      _/    _/  _/           
_/_/_/    _/      _/  _/_/_/        _/_/_/    _/_/_/  _/    _/_/_/    _/_/_/  _/    _/_/_/      _/_/    _/_/    _/            

    ''')

print("\n")

print (" ---> Welcome To The BMI Calculator App")

print (" ---> Version : 1.1.1 ")

print (" --------- ")

print ( " ### Application Developer : Mohammad Babaee ")

print ( " --------- ")

weight = input ("Please Enter Your Weight In (KG) = ")

height = input ("Please Enter Your Height In (Meter) = ")

height = float(height) * float(height)

bmi = float(weight) / float(height) 

print (" --------- ")

print ("Your BMI Is : " + str(bmi))