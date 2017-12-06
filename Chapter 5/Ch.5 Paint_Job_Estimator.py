FEET_PER_GALLON = 112
LABOR_HOURS = 8
LABOR_CHARGE = 35

def ask_For_Wall_Space():
    wall_Space = float( input( "Enter wall space in square feet: " ) )
    return wall_Space

def ask_For_Price_Of_Paint():
    paint_Price = float( input( "Enter paint price per gallon: " ) )
    return paint_Price

def calculate_Paint_Required( wall_Space ):
    paint_Required = int( wall_Space / FEET_PER_GALLON ) + 1
    return paint_Required

def calculate_Hours_Of_Labor( wall_Space ):
    labor_Hours_Total = ( wall_Space / FEET_PER_GALLON ) * LABOR_HOURS
    return labor_Hours_Total

def calculate_Cost_Of_Paint( paint_Price, paint_Required ):
    cost_Of_Paint = ( paint_Required * paint_Price )
    return cost_Of_Paint

def calculate_Labor_Cost( labor_Hours_Total ):
    labor_Cost = (labor_Hours_Total * LABOR_CHARGE)
    return labor_Cost

def calculate_Total_Cost( labor_Cost, cost_Of_Paint ):
    total_Cost = (labor_Cost + cost_Of_Paint)
    return total_Cost

def print_Results( paint_Required, labor_Hours_Total, cost_Of_Paint, \
                  labor_Cost, total_Cost ):
    print( "Gallons of paint: " + format( paint_Required, "" ) )
    print( "Hours of labor: " + format(labor_Hours_Total, ".2f"))
    print( "Paint charges: $" + format(cost_Of_Paint, ",.2f"))
    print( "Labor charges: $" + format(labor_Cost, ",.2f"))
    print( "Total cost: $" + format(total_Cost, ",.2f"))

def main():
    wall_Space = ask_For_Wall_Space()
    paint_Price = ask_For_Price_Of_Paint()
    paint_Required = calculate_Paint_Required( wall_Space )
    labor_Hours = calculate_Hours_Of_Labor( wall_Space )
    cost_Of_Paint = calculate_Cost_Of_Paint( paint_Price, paint_Required )
    labor_Cost = calculate_Labor_Cost( labor_Hours )
    total_Cost = calculate_Total_Cost( labor_Cost, cost_Of_Paint )
    print_Results( paint_Required, labor_Hours, cost_Of_Paint, \
                  labor_Cost, total_Cost)

main()
    
    
