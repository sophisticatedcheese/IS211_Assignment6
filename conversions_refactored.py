__author__ = 'T Jeremiah - Ocotber 2015'


import unittest

class ConversionNotPossible(Exception):
    pass

distance = {'met': {'yar':(0,1.09361,0),'mil':(0,0.000621371,0)},'yar': {'mil':(0,0.000568182,0),'met':(0,0.9144,0)},'mil': {'met':(0,1609.34,0),'yar':(0,1760,0)}}
temp = {'kel':{'cel':(0,1,-273.15),'fah':(-273.15,9/5,32)},'cel':{'kel':(0,1,273.15),'fah':(0,9/5,32)},'fah':{'kel':(-32,5.0/9.0,273.15),'cel':(-32,5.0/9.0,0)}}

def convert(fromUnit,toUnit,value):

    fromUnit = fromUnit[0:3].lower()
    toUnit = toUnit[0:3].lower()
    if not ((fromUnit in distance.keys() and toUnit in distance.keys()
             ) or (fromUnit in temp.keys() and toUnit in temp.keys())):
        raise ConversionNotPossible
    else:
        if fromUnit == toUnit:
            retval = value
        elif fromUnit in distance.keys():
            retval = (value + distance[fromUnit][toUnit][0]) * distance[fromUnit][toUnit][1] + distance[fromUnit][toUnit][2]
        else:
            retval = (value + temp[fromUnit][toUnit][0]) * temp[fromUnit][toUnit][1] + temp[fromUnit][toUnit][2]
    return float("%0.2f" %retval)


class ConvertTest(unittest.TestCase):

    def testTemp(self):
        self.assertEqual(convert('celsius','fahrenheit',0),32.0)
        self.assertEqual(convert('kelvin','fahrenheit',0),-241.15)
        self.assertEqual(convert('celcius','kelvin',0),273.15)
        self.assertEqual(convert('kelvin','celcius',273.15),0.0)
        self.assertEqual(convert('fahrenheit','celcius',32),0.0)
        self.assertEqual(convert('fahrenheit','kelvin',0),255.37)

    def testDist(self):
        self.assertEqual(convert('meter','mile',100),0.06)
        self.assertEqual(convert('meter','yard',10),10.94)
        self.assertEqual(convert('mile','meter',10),16093.4)
        self.assertEqual(convert('mile','yard',10),17600.00)
        self.assertEqual(convert('yard','meter',3),2.74)
        self.assertEqual(convert('yard','mile',300),0.17)

    def testSanity(self):
        for i in distance.keys():
            self.assertEqual(convert(i,i,10),10)
        for i in temp.keys():
            self.assertEqual(convert(i,i,10),10)

    def testError(self):
        self.assertRaises(ConversionNotPossible,convert,'met','cel',0)

if __name__ == '__main__':
    unittest.main()