import matplotlib.pyplot as plt
import numpy as np

beta, gamma = 0.95, 1.2
x_grid = np.linspace(0.1,5,100) #This is like the kgrid from Adams lectures

#CRRA utility
def u(c, gamma):
    return c**(1 - gamma) / (1 - gamma)

#BE solution, our value function
def v_star(x,beta,gamma):
    return (1-beta**(1/gamma)**(-gamma)*u(x,gamma))

#Policy function, pen paper derivation
def c_star(x,beta,gamma):
    return (1-beta**(1/gamma))*x

fig, ax = plt.subplots()

ax.plot(x_grid, v_star(x_grid,beta,gamma),label="$v^*(x)$")
ax.set_xlabel("$x$", fontsize=12)
ax.set_ylabel("$v^*(x)$", fontsize=12)
ax.legend(fontsize=12)

plt.show()

fig, ax = plt.subplots()
ax.plot(x_grid, c_star(x_grid, beta, gamma), label='default parameters')
ax.plot(x_grid, c_star(x_grid, beta + 0.02, gamma), label=r'higher $\beta$')
ax.plot(x_grid, c_star(x_grid, beta, gamma + 0.2), label=r'higher $\gamma$')
ax.set_ylabel(r'$\sigma(x)$')
ax.set_xlabel('$x$')
ax.legend()

plt.show()