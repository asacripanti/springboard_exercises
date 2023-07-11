def convert_temp(unit_in, unit_out, temp):
    """Convert farenheit <-> celsius and return results."""
    if unit_in != 'f' and unit_in != 'c' or unit_out != 'f' and unit_out != 'c':
        return 'Invalid'
    elif unit_in == 'f' and unit_out == 'c':
       temp = (temp - 32) / 1.8
       return temp
    elif unit_in == 'c' and unit_out == 'f':
        temp = (temp * 1.8) + 32
        return temp
        
       

  


print("c", "f", 0, convert_temp("c", "f", 0), "should be 32.0")
print("f", "c", 212, convert_temp("f", "c", 212), "should be 100.0")
print("z", "f", 32, convert_temp("z", "f", 32), "should be Invalid unit z")
print("c", "z", 32, convert_temp("c", "z", 32), "should be Invalid unit z")
print("f", "f", 75.5, convert_temp("f", "f", 75.5), "should be 75.5")

