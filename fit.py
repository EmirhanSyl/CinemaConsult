import numpy as np
from scipy.optimize import curve_fit

def model_func(t, a, b):
    return a * t + b

def fit_curve(speeds, times):
    # Convert lists to numpy arrays for use with curve_fit
    speeds = np.array(speeds)
    times = np.array(times)
    
    # Define initial guess for parameters (slope 'a' and intercept 'b')
    initial_guess = [1.0, 0.0]
    
    # Use curve_fit to fit the model_func to the data
    params, params_covariance = curve_fit(model_func, times, speeds, initial_guess)
    
    # Extract the fitted parameters
    a_fit, b_fit = params
    
    return a_fit, b_fit

# Given speeds and corresponding times
velocities = [0.0,0.0702576112412178,0.49180327868852464,0.49180327868852464,1.0538641686182668,1.2646370023419204,1.8266978922716628,1.6159250585480094,2.1779859484777515,2.459016393442623,2.9508196721311477,3.3021077283372366,3.2318501170960188,3.934426229508197]

times = [0.033 * n for n in range(len(velocities))]

# Fit the curve to the data
a_fit, b_fit = fit_curve(velocities, times)

# Print the fitted parameters
print("Fitted slope (a):", a_fit)
print("Fitted intercept (b):", b_fit)