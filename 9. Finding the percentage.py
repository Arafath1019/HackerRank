n = int(input())
student_marks = {}
for _ in range(n):
  name, *line = input().split()
  scores = list(map(float, line))
  student_marks[name] = scores
query_name = input()

def result(student_marks, query_name):
  for name in student_marks: 
    if name == query_name:
      total = 0
      for i in range(len(student_marks[name])):
        total = total + student_marks[name][i]

      final = total/len(student_marks[name])
      print("%.2f" % final)

result(student_marks, query_name)