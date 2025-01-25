### Logistic Map and Lyapunov Exponent

The **logistic map** is a mathematical model used to describe the dynamic behavior of nonlinear systems. It is expressed by the equation:

$x_{n+1} = r x_n (1 - x_n)$

where \( x_n \) represents the system's state at time \( n \), and \( r \) is the control parameter. The logistic map was introduced by Pierre François Verhulst in 1838 to model population growth, but it later became important in the study of chaotic systems. As the value of \( r \) changes, the system's behavior can shift from stability to chaos. Specifically:

- For \( r \) small (less than 1), the population tends to zero.
- For \( r \) between 1 and 3, the system reaches a stable equilibrium.
- For \( r \) between 3 and 3.57, periodic oscillations (bifurcations) occur.
- For \( r \) values greater than 3.57, the system becomes chaotic, exhibiting unpredictable behavior highly sensitive to initial conditions.

The **Lyapunov exponent** is a measure of the rate of divergence or convergence of nearby trajectories in a dynamical system. It is used to quantify the system's sensitivity to initial conditions, which is a hallmark of chaos. 

When the Lyapunov exponent is positive, the system's trajectories diverge exponentially, indicating chaotic behavior. If it is negative, the system is stable and the trajectories converge, while a zero exponent suggests the system is periodic or non-chaotic but not necessarily stable.

For the logistic map, the Lyapunov exponent can be used to determine in which intervals of \( r \) the system behaves chaotically. In regions where the system is chaotic, the Lyapunov exponent will be positive.
