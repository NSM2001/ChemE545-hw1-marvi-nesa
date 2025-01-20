# ChemE545-hw1-marvi-nesa
**Here are some descriptions on uploaded Python files and a guide on how to run them:**

•**calculate-solution-weights-function**:
-The Python function` calculate_solution_weights` takes the inputs which are the` solutions_needed` and gives the name of` chemical_formula` ,` concentration` and `weight` of that chemical substance in the format of 'chemical_formula-concentration-weight' by using the` molecular_weights dictionary` .
-In order to check for the existence of specific chemical in the` molecular_weights` dictionary I used 1 if loop, if the chemical doesn't exist in the dataset outcome from that input gets replaced with ** 'unknown'** .
-In order to edit this file and replace it with your own inputs or dictionary you can use a text editor like Nano by simply saving the file and typing nano` calculate-solution-weights-function.py` in the terminal of your computer  and edit the `molecular_weights` dictionary or the `solutions_needed` input, the you can save the file and run it through the terminal of your computer by typing ` Python3 calculate-solution-weights-function.py` and you'll be able to see the outcome.  
 
•**Data-Extraction-and-Modification-function**:
-The Python function `extract_parameter` takes the input and gives the name of unit, parameter and the index related to the parameter by using the `unit_operations_data` dictionary.
-In order to check for the existence of specific input in `unit_operations_data`, I used 3 loops to check this input in the `unit_name`, `parameter_name` and also `value`, if the input is not found in any of the categories above, the function returns **"Invalid input"**.
-In order to edit this file and replace it with your own inputs or dictionary you can use a text editor like Nano by simply saving the file and typing`nano Data-Extraction-and-Modification-function.py` in the terminal of your computer  and edit the `unit_operations_data` or the `extract_parameter` inputs, then you can save the file and run it through the terminal of your computer by typing ` Python3 Data-Extraction-and-Modification-function.py` and you'll be able to see the outcome.
 

