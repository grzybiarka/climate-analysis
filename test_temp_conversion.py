from temp_conversion import fahr_to_kelvin
from nose.tools import *

def test_zero_kelvin():
	assert round(fahr_to_kelvin (-459.67),2)==0.00

#def test_zero_kelvin2():
	#assert fahr_to_kelvin (-459.67)==0.00, "text"	

#@raises(TypeError)
def strin_test():
	assert fahr_to_kelvin("some string")