import numpy as np
colors = ["red", "blue", "green"]
print(np.random.choice(colors))


import numpy as np
colors = ["red", "blue", "green"]
print(np.random.choice(colors, size=5))


import numpy as np
names = ["Anu", "Rahul", "Asha", "John"]
print(np.random.choice(names, size=3))

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)

import numpy as np
student_ids = np.array([101, 102, 103, 104, 105])
np.random.shuffle(student_ids)
print(student_ids)


import numpy as np
marks = np.random.randint(40, 100, size=(5, 3))
print(marks)

import numpy as np
attendance = np.random.randint(75, 100, size=5)
print(attendance)


import numpy as np
image = np.random.randint(0, 256, size=(3, 3))
print(image)