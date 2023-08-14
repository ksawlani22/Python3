#Intro to Physics 
#Kabir Sawlani

# Values
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Physics Functions

def get_force(mass, acceleration):
    """Calculate and return the force."""
    return mass * acceleration

def get_energy(mass, c=3*10**8):
    """Calculate and return the energy."""
    return mass * c**2

def get_work(mass, acceleration, distance):
    """Calculate and return the work."""
    force = get_force(mass, acceleration)
    return force * distance

# Temperature Conversion

def f_to_c(f_temp):
    """Convert Fahrenheit to Celsius."""
    c_temp = (f_temp - 32) * 5/9
    return c_temp

def c_to_f(c_temp):
    """Convert Celsius to Fahrenheit."""
    f_temp = (c_temp * (9/5)) + 32
    return f_temp

# Testing and Results 

# Force calculations
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# Energy calculations
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

# Work calculations
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")

# Temperature conversions
f100_in_celsius = round(f_to_c(100), 2)
print("100 degrees Fahrenheit is " + str(f100_in_celsius) + " degrees Celsius.")

c0_in_fahrenheit = c_to_f(0)
print("0 degrees Celsius is " + str(c0_in_fahrenheit) + " degrees Fahrenheit.")
