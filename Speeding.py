#function for speeding
def caught_speeding(speed, is_birthday):
    
# if it is there birthday, there speed is 5 less than actual    
    if is_birthday:
        speed = speed - 5
    
    else: 
        speed = speed
    
# No ticket for speed less than or equal to 60
    if speed <= 60:
        print("No ticket")

# Small ticket for speed greater than or equal to 61 and less than or equal to 80     
    elif speed >= 61 and speed <= 80:
        print("Small Ticket")
# Big ticket for speed greater than or equal to 81
    elif speed >= 81:
        print("Big Ticket")
    
    pass


#Case one caught speeing doing 81 and it is there birthday
caught_speeding(81,True)
#Case two caught speeing doing 81 and it is not there birthday
caught_speeding(81,False)
