divisions = ["Div-A", "Div-B", "Div-C", "Div-D", "Div-E"] 
division_average_marks = [70, 82, 73, 65, 68]

plt.bar(divisions, division_average_marks, color='green')
plt.title("Ban Graph")
plt.xlabel("Divisions")
plt.ylabel("Marks")
plt.show()
