# List of Ideas for different Models for epidemiological predictions

# For new ideas, please create a new entry below and describe them briefly (add link to source)

## Heatmap 

### Description

Anlalyzing and visualizing correlations between the evolution of the pandemic in different countries   

## Kernel density estimation 

### Link 

https://en.wikipedia.org/wiki/Kernel_density_estimation

### Description 

A spatial model that describes each infected individual with a normalized gaussian distribution. 
In total this gives a spatial probability distribution for the number of infected people. 
This could be used to determine the likelihood of spatial spread of infections in every timestep.
Open questions are: 
-What could be the model parameters to optimize by fitting to the data?
-How to even fit this model to data?
-Can this be used to model time evolution as well?  
-How accurate is the description with gaussians? Maybe other distributions can be tested as well  

 

## Agent based simulation from Washington post 

### Link 

https://www.washingtonpost.com/graphics/2020/world/corona-simulator/

### Despcription

An agent based model that simulates the particle movement of an ideal gas in a finite volume. 
Infection spreads through particle collisions with a certain probability.    

## SIR model

### Link 

https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology

### Description

A simple epidemiological model to simulate the time evolution of disease spreading.
At the core is the division of the whole population N in three subsets S ("Susceptible"), 
R ("Recovered") and I ("Infected"). Therefor at all times, I + S + R = N holds. 
The model then consists of three ordinary non-linear differential equations. One for each subset. 
The two model parameters $`\beta`$ (average number of people getting infected by one infected) and $`\gamma`$ 
(average recoveries per time step). The ratio of these two numbers $`R_0:=\frac{\beta}{\gamma}`$ is called the 
"basic reproduction number" and is a key variable that determines the trajectory of the epidemic. 

The logistic regression can be seen as the integrated result of this set of differential equations. In this sense both models 
should be equally powerful to model the datasets at hand. However, if we want to look into the future (especially considering changes of 
political policies and measures) the logistic regression will always be a simple extrapolation from the existing data. In contrast, with a 
differential model as the SIR, we can evolve a single time step and even consider model parameters to be time dependent ($`\beta = \beta(t)`$). 
In this sense the SIR can be used to fit every timestep of the evolution to existing data and therefor provide a model parameter for every timestep.

There is extensions of this model to spacial models (spatial SIR models) which also attempt to model the spatial evolution of the disease. 
 
## Logistic regression

### Link 

https://en.wikipedia.org/wiki/Logistic_regression

### Description 

The logistic regression model fits existing data to a given trajectory with time independent model parameters. 
This can be a simple entry point to model the time evolution for given data sets and in the same way as the SIR model can 
be extended to spatial spreading models. However it does not include the mechanics that drive the epidemic. It hence can only 
extrapolate from a given dataset by a best parameter estimation on the given data. 

The logistic model is given as $`I(t) = \frac{c}{1+ae^{-(b_0 + b_1t)}} + d `$. 

#### example:  https://towardsdatascience.com/covid-19-infection-in-italy-mathematical-models-and-predictions-7784b4d7dd8d


