import math,sys
from point2d import Point2D

f=open('day10Input.txt','r')
line_num=0
points=[]
for line in f:
	line=list(line.strip('\n'))
	for i in range(len(line)):
		if line[i]=='#':
			points.append((i,line_num))
	line_num+=1


ans={}
for point in points:
	data=points[:]
	lup=set()
	data.remove(point)
	for point2 in data:
		p1=Point2D(point)
		p2=Point2D(point2)
		x=math.degrees((p2 - p1).a)
		lup.add(x)
	ans[point]=len(lup)

real_ans=0
lanswer=0
for answer in ans:
	if ans[answer]>real_ans:
		real_ans=ans[answer]
		lanswer=answer
print(real_ans,lanswer)#part1
answer=lanswer


love={}
few=points[:]
few.remove(answer)
for point in few :
	p1=Point2D(answer)
	p2=Point2D(point)
	a=round((math.degrees((p1 - p2).a)+270)%360,5)
	if a in love:
		love[a].append(point)
	else:
		love[a]=[point]
love_values = sorted(love)

for jo in love:
	love[jo]=sorted(love[jo],reverse=True,key=lambda x:(Point2D(x)-Point2D(answer)).r)
count=0
while True:
	for angle in love_values:
		if len(love[angle])>0:
			haha=love[angle].pop()
			count+=1
			if count==200:
				print(haha[0]*100+haha[1])#part2
				sys.exit(0)