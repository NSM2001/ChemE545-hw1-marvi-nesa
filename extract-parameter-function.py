#defining unit_operation_data dictionary
unit_operations_data = {
    "distillation_column": {"temperature": [150, 160, 170], "pressure": [2, 2.5, 3], "flow_rate": [100, 110, 120]},
    "reactor": {"temperature": [250, 260, 270], "pressure": [5, 5.5, 6], "residence_time": [10, 12, 14]},
    "heat_exchanger": {"temperature_in": [80, 90, 100], "temperature_out": [50, 60, 70], "flow_rate": [200, 210, 220]}}

def extract_parameter(unit_name,parameter_name,value): #defining the function
        
        #using if loops to check if the input exists in categories above
        if unit_name in unit_operations_data:
           if parameter_name in unit_operations_data[unit_name]:
               #checks the existence of inputted {value} in the parameter_name index range
               if 0 <= value < len(unit_operations_data[unit_name][parameter_name]):

                 #defining expected format for the outcome
                 return f"{unit_name}_{parameter_name}_{unit_operations_data[unit_name][parameter_name][value]}"
                
               else:
                return "invalid input" #if index was not in range of parameter_name index
           else:
              return "invalid input" #if parameter_name was not available in unit_operations_data
        else:
          return "invalid input" #if unit_name was existing in the unit_operations_data
        return result

results = extract_parameter("distillation_column", "temperature",1)  #Inserting inputs inside the function
print(results) #displays the result