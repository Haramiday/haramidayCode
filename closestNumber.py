def closest_power(base,target):
    '''
    This function  takes in a ​base number and a target number as input parameters​ then
    ​returns the smallest number that the base number has to be raised to,
    that brings it closest to the target number.
    '''

    if base == int(base) and target==int(target):#checks if both are integers
        power = 0 #starting point for the power
        while power>= 0:
            raised_to_power = base **power
        
            if raised_to_power < target and base**(power+1)>target \
               and (target - raised_to_power > base**(power+1) - target): 
                return(power+1)
                
            elif raised_to_power > target and base**(power-1)<target \
                 and (raised_to_power - target < target - base**(power-1)):
                return(power-1)
                
            elif (raised_to_power < target and base**(power+1)>target and (target - raised_to_power == base**(power+1) - target))\
                 or (raised_to_power > target and base**(power-1)<target and (raised_to_power - target == target - base**(power-1))):
                return(power)

            power = power + 1
    else:#checks if they are non integer
        return 'Error'

print(closest_power(3,18))
print(closest_power(4,45))

