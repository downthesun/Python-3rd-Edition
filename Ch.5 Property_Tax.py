def askFor_Property_Value():
    actual_Property_Value = float(input("Enter the actual value: "))
    return actual_Property_Value

def calculate_Assessment_Value( actual_Property_Value ):
    ASSESS_PERCENT = 0.6
    property_Assessment_Value = (ASSESS_PERCENT * actual_Property_Value)
    return property_Assessment_Value

def calculate_Property_Tax( property_Assessment_Value ):
    PROPERTY_TAX_PERCENT = 0.72
    property_Tax = ( property_Assessment_Value / 100 ) * PROPERTY_TAX_PERCENT
    return property_Tax

def print_Details( property_Assessment_Value, property_Tax ):
    print( "Assessed Value: $", format( property_Assessment_Value, ",.2f" ) + \
           "\nProperty Tax: $", format( property_Tax, ",.2f" ) )

def main():
    user_Property_Value = askFor_Property_Value()
    property_Assessment_Value = calculate_Assessment_Value( user_Property_Value)
    property_Tax = calculate_Property_Tax( property_Assessment_Value )
    print_Details( property_Assessment_Value,  property_Tax)

main()

