#defining the dictionary of molecular weights
molecular_weights = {
    'NaCl': 58.44,
    'H2SO4': 98.079,
    'NaOH': 40.00,
    'KMnO4': 158.034,
    'CH3COOH': 60.052}

solutions_needed = ['NaCl-0.5M', 'H2SO4-0.25M', 'NaOH-1M', 'KCl-0.1M', 'CH3COOH-0.3M'] #defining the inputs

def calculate_solution_weights(molecular_weights,solutions_needed): #defining the function 
    result = []  #empty list initialization
    for solution in solutions_needed:
        #specifying the chemical_formula and concentration in the inputs for each chemical
        chemical_formula , concentration = solution.split('-') 
        if chemical_formula in molecular_weights: #if chemical formula was available in molecular weight datasets
            
            #calculation of weight using the molecular_weights and concentration, also converting concentration to a float and removing it's unit
           weight= np.multiply(molecular_weights[chemical_formula],float(concentration[:-1]))
            
          #defining expected format for the outcome also adding the unit for weight and removing excess decimal places 
           result.append(f'{chemical_formula}-{concentration}-{weight:.2f}g')
        else:
           result.append("unknown") #if chemical formula was not available in molecular weight datasets 
    return result
        
results =calculate_solution_weights(molecular_weights,solutions_needed)   
print(results) #displays the result