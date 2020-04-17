def closest_power(base,target):
    '''
    This function  takes in a ​base number and a target number as input parameters​ then
    ​returns the smallest number that the base number has to be raised to,
    that brings it closest to the target number.
    '''

    if base == int(base) and target==int(target):#checks if both are integers
        power = 0
        while power>= 0:
            raised_to_power = base **power
        
            if (raised_to_power)>target:
                return(power-1)

            power = power + 1
    else:#checks if they are non integer
        return 'Error'

print(closest_power('3',18))
