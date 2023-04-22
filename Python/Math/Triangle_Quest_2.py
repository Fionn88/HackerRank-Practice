"""
1 => 1^2 => 1
121 => 11^2 => 121
12321 => 111^2 => 12321
1234321 => 1111^2 => 1234321

(10**i)//(9)
i = 1 => 10^1//9 => 1
i = 2 => 10^2/9 => 11
i = 3 => 10^3/9 => 111
i = 4 => 10^4/9 => 1111
"""

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ((((10**i)-1)//(9))**2);