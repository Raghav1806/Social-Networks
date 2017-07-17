# drawing a straight line in python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4, 5])
plt.show()

# quadratic curve
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4, 5], [1, 4, 5, 9, 25], 'ro-')
plt.show()

# adding labels to given plot
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4, 5], [1, 4, 5, 9, 25], 'ro-')
plt.title('Squares of values')
plt.xlabel('The values')
plt.ylabel('The squares')
plt.axis([1, 10, 1, 30])
plt.grid(True)
plt.show()

# plotting two or more plots
import matplotlib.pyplot as plt
import numpy
x = [i for i in range(100)]
x = numpy.array(x)
plt.plot(x, x*2, 'r-', x, x*3, 'g-')
plt.show()

# plotting random data 
import matplotlib.pyplot as plt
import random
x = [random.randint(1, 100) for i in range(100)]
y = [random.randint(1, 100) for i in range(100)]
plt.scatter(x, y)
plt.axis([0, 100, 0, 100])
plt.show()



