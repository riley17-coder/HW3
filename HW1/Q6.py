People_Sum=1000
Number_FD=700
Number_Water=1.1*Number_FD
Number_Nachos=(1/4)*Number_Water
Number_Hotdogs=2*Number_Nachos
Revenue_Sum=Number_Hotdogs*10.99+Number_Nachos*9.99+Number_FD*2.99+Number_Water*3
Revenue_B=Revenue_Sum/1+(1+0.3)
print(Revenue_B)