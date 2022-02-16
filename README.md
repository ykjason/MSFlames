# MSFlames
Tier identifier for stats (currently only the four main stats)

To simplify what the tool achieves, letters and numbers (not representative of the actual values worked with) will be used in the following explanation.

There are 7 possible values that are considered 'whole' which is denoted by W following the value  
1W 2W 3W 4W 5W 6W 7W

There is another set of 7 values that are considered 'dual' which is denoted by D following the value  
1D 2D 3D 4D 5D 6D 7D

There are 4 slots of which the previous values will belong to denoted by separate letters  
S D I L

Each slot may only hold one whole value (values can belong to multiple other slots)  
Ex. S may have 3W and D may have 3W but S cannot have 3W and 5W at the same time

If a dual value is chosen, another dual value must be placed in another slot of the remaining three  
Ex. L may have 3D, another slot (S D I) must then be chosen for the second value of 3D  
L may have 3D and S will have 3D

A slot may have both whole and dual values  
Ex. S may have 3W and 3D  (note that 3D is here so any another slot (D I L) must also have a corresponding 3D so L will be chosen) L will have 3D

Choosing one whole value counts as 1 choice  
Choosing a pair of dual values (Ex. S 5D and I 5D) will also count as 1 choice  
A **MAXIMUM** of 4 choices can be made (1-3 is possible)  
  
Ex. (max 4 choices)  
  
S 3W 4D 7D  
D 4D 1W  
I   
L 7D  

The values are then summed up with no clear indication of what values (either whole or dual) were used to make up the sum. This issue worsens when the values appear on a larger scale and with the condition that dual values inherently have half as much as the index of their whole counterpart.
The program seeks to solve this problem using a recursive algorithm to explore a possible solution set
