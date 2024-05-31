
import matplotlib.pyplot as plt

hours = [10,9,2,15,10,16,11,16]
score = [95,80,10,50,45,98,38,93]

plt.plot(hours, score, marker='*', color='red', linestyle='-')

plt.xlabel('Number of Hours Studied')
plt.ylabel('Score in Final Exam')
plt.title('Effect of Hours Studied on Exam Score')
plt.grid(True)
plt.show()