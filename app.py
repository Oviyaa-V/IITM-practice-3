from jinja2 import Template
import sys
import matplotlib.pyplot as plt


name = sys.argv[1]
id = int(sys.argv[2])
data = []

with open("data.csv") as file:
    file.readline()
    
    if name == "-s":
        for row in file:
            row = list(map(int,(row.strip()).split(",")))
            if row[0] == id:
                data.append(row)

    elif name == "-c":
        for row in file:
            row = list(map(int,(row.strip().split(","))))
            if row[1] == id:
                data.append(row)

if len(data) == 0:
    file1 = open("error.html")
    data = file1.read()

    file2 = open("output.html","w")
    file2.write(data)

    file1.close()
    file2.close()

elif name == "-s":
    s = sum(i[2] for i in data)

    file1 = open("studentid.html")
    d = file1.read()

    temp = Template(d)
    
    file2 = open("output.html","w")
    file2.write(temp.render(data = data,sum = s))

    file1.close()
    file2.close()

elif name == "-c":
    marks = [i[2] for i in data if id == i[1]]
    avg = sum(marks)/len(marks)
    max = max(marks)

    plt.hist(marks)
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.title("course vs marks")
    plt.savefig("graph.png")

    file1 = open("course.html")
    d = file1.read()

    temp = Template(d)
    file2 = open("output.html","w")
    file2.write(temp.render(avg = avg, max = max, img = "graph.png"))

    file1.close()
    file2.close()

    




    


