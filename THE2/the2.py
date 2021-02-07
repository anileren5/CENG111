

import math
import random
from evaluator import *    # get_data() will come from this import


initialstate=get_data()[6] #This is the universel state before new moves is done.

def new_move():
	global initialstate
	M=get_data()[0] #Number of rows.
	N=get_data()[1] #Number of columns.
	D=get_data()[2] #Threshold distance value for infection.
	k=get_data()[3]	#Probability constant(kappa) for mutual infection.
	y=get_data()[4]	#The constant(lambda) that the maske reduced the probablity of infection by factor of that constant.
	u=get_data()[5] #The probability constant(mu) for next move.
	P=len(initialstate) #The number of individuals

	green=(1/2)*(u)
	yellow=(1/8)*(u)
	blue=(1/2)*(1-u-(u**2))
	purple=(2/5)*(u**2)
	gray=(1/5)*(u**2)

	filledpositions=[]

	for individual in initialstate:
		filledpositions.append(individual[0])
	i=0
	for individual in initialstate:

		x=individual[0][0] #The column(x) where the individual is on before move.
		y=individual[0][1] #The row(y) where the individual is on before move.
		lastmove=individual[1] #The direction of lastmove.

		if lastmove==0:
			#possible next positions and updatedlastmoves
			p0=[(x,y-1),4]  #position with possibility 1/5 u^2 updatedlastmove=4
			p1=[(x+1,y-1),5]#position with possibility 2/5 u^2 updatedlastmove=5
			p2=[(x+1,y),6]  #position with possibility 1/2(1-u-u^2) updatedlastmove=6
			p3=[(x+1,y+1),7]#position with possibility 1/8 u updatedlastmove=7
			p4=[(x,y+1),0]  #position with possibility 1/2 u updatedlastmove=0
			p5=[(x-1,y+1),1]#position with possibility 1/8 u updatedlastmove=1
			p6=[(x-1,y),2]  #position with possibility 1/2 (1-u-u^2) updatedlastmove=2
			p7=[(x-1,y-1),3]#position with possibility 2/5 (u^2) updatedlastmove=3

			#let's choose where he will go
			next=random.choices([p0,p1,p2,p3,p4,p5,p6,p7],weights=[gray,purple,blue,yellow,green,yellow,blue,purple])
			#We have chosen a point but we do not know this position is preoccupied or is out of arena.Let's check.
			nextposition=next[0][0]
			nextlastmove=next[0][1]
			if (nextposition[0] in range(0,N)) and (nextposition[1] in range(0,M)) and (nextposition not in filledpositions):
				individual[0]=nextposition
				individual[1]=nextlastmove
				filledpositions[i]=nextposition

		if lastmove==2:
			#possible next positions and updatedlastmoves
			p0=[(x,y-1),4]   #blue
			p1=[(x+1,y-1),5] #purple
			p2=[(x+1,y),6]   #gray
			p3=[(x+1,y+1),7] #purple
			p4=[(x,y+1),0]   #blue
			p5=[(x-1,y+1),1] #yellow
			p6=[(x-1,y),2]   #green
			p7=[(x-1,y-1),3] #yellow

			#let's choose where he will go
			next=random.choices([p0,p1,p2,p3,p4,p5,p6,p7],weights=[blue,purple,gray,purple,blue,yellow,green,yellow])
			#We have chosen a point but we do not know this position is preoccupied or is out of arena.Let's check.
			nextposition=next[0][0]
			nextlastmove=next[0][1]
			if (nextposition[0] in range(0,N)) and (nextposition[1] in range(0,M)) and (nextposition not in filledpositions):
				individual[0]=nextposition
				individual[1]=nextlastmove
				filledpositions[i]=nextposition

		if lastmove==4:
			#possible next positions and updatedlastmoves
			p0=[(x,y-1),4]  #green
			p1=[(x+1,y-1),5]#yellow
			p2=[(x+1,y),6]  #blue
			p3=[(x+1,y+1),7]#purple
			p4=[(x,y+1),0]  #gray
			p5=[(x-1,y+1),1]#purple
			p6=[(x-1,y),2]  #blue
			p7=[(x-1,y-1),3]#yellow

			#let's choose where he will go
			next=random.choices([p0,p1,p2,p3,p4,p5,p6,p7],weights=[green,yellow,blue,purple,gray,purple,blue,yellow])
			# We have chosen a point but we do not know this position is preoccupied or is out of arena.Let's check.
			nextposition=next[0][0]
			nextlastmove=next[0][1]
			if (nextposition[0] in range(0,N)) and (nextposition[1] in range(0,M)) and (nextposition not in filledpositions):
				individual[0]=nextposition
				individual[1]=nextlastmove
				filledpositions[i]=nextposition



		if lastmove==6:
			#possible next positions and updatedlastmoves
			p0=[(x,y-1),4]   #blue
			p1=[(x+1,y-1),5] #yellow
			p2=[(x+1,y),6]   #green
			p3=[(x+1,y+1),7] #yellow
			p4=[(x,y+1),0]   #blue
			p5=[(x-1,y+1),1] #purple
			p6=[(x-1,y),2]   #gray
			p7=[(x-1,y-1),3] #purple

			#let's choose where he will go
			next=random.choices([p0,p1,p2,p3,p4,p5,p6,p7],weights=[blue,yellow,green,yellow,blue,purple,gray,purple])
			nextposition=next[0][0]
			nextlastmove=next[0][1]
			if (nextposition[0] in range(0, N)) and (nextposition[1] in range(0, M)) and (nextposition not in filledpositions):
				individual[0]=nextposition
				individual[1]=nextlastmove
				filledpositions[i]=nextposition

		if lastmove==7:
			#possible next positions and updatedlastmoves
			p0=[(x,y-1),4]   #purple
			p1=[(x+1,y-1),5] #blue
			p2=[(x+1,y),6]   #yellow
			p3=[(x+1,y+1),7] #green
			p4=[(x,y+1),0]   #yellow
			p5=[(x-1,y+1),1] #blue
			p6=[(x-1,y),2]   #purple
			p7=[(x-1,y-1),3] #gray

			#let's choose where he will go
			next=random.choices([p0,p1,p2,p3,p4,p5,p6,p7],weights=[purple,blue,yellow,green,yellow,blue,purple,gray])
			nextposition = next[0][0]
			nextlastmove = next[0][1]
			if (nextposition[0] in range(0, N)) and (nextposition[1] in range(0, M)) and (nextposition not in filledpositions):
				individual[0] = nextposition
				individual[1] = nextlastmove
				filledpositions[i] = nextposition

		if lastmove==1:
			#possible next positions and updatedlastmoves
			p0 = [(x, y - 1), 4]     #purple
			p1 = [(x + 1, y - 1), 5] #gray
			p2 = [(x + 1, y), 6]     #purple
			p3 = [(x + 1, y + 1), 7] #blue
			p4 = [(x, y + 1), 0]     #yellow
			p5 = [(x - 1, y + 1), 1] #green
			p6 = [(x - 1, y), 2]     #yellow
			p7 = [(x - 1, y - 1), 3] #blue

			#let's choose where he will go
			next=random.choices([p0,p1,p2,p3,p4,p5,p6,p7],weights=[purple,gray,purple,blue,yellow,green,yellow,blue])
			nextposition = next[0][0]
			nextlastmove = next[0][1]
			if (nextposition[0] in range(0, N)) and (nextposition[1] in range(0, M)) and (nextposition not in filledpositions):
				individual[0] = nextposition
				individual[1] = nextlastmove
				filledpositions[i] = nextposition

		if lastmove==3:
			#possible next positions and updatedlastmoves
			p0 = [(x, y - 1), 4]     #yellow
			p1 = [(x + 1, y - 1), 5] #blue
			p2 = [(x + 1, y), 6]     #purple
			p3 = [(x + 1, y + 1), 7] #gray
			p4 = [(x, y + 1), 0]     #purple
			p5 = [(x - 1, y + 1), 1] #blue
			p6 = [(x - 1, y), 2]     #yellow
			p7 = [(x - 1, y - 1), 3] #green

			#let's choose where he will go
			next=random.choices([p0,p1,p2,p3,p4,p5,p6,p7],weights=[yellow,blue,purple,gray,purple,blue,yellow,green])
			nextposition = next[0][0]
			nextlastmove = next[0][1]
			if (nextposition[0] in range(0, N)) and (nextposition[1] in range(0, M)) and (nextposition not in filledpositions):
				individual[0] = nextposition
				individual[1] = nextlastmove
				filledpositions[i] = nextposition
		if lastmove==5:
			#possible next positions and updatedlastmoves
			p0 = [(x, y - 1), 4]     #yellow
			p1 = [(x + 1, y - 1), 5] #green
			p2 = [(x + 1, y), 6]     #yellow
			p3 = [(x + 1, y + 1), 7] #blue
			p4 = [(x, y + 1), 0]     #purple
			p5 = [(x - 1, y + 1), 1] #gray
			p6 = [(x - 1, y), 2]     #purple
			p7 = [(x - 1, y - 1), 3] #blue

			#let's choose where he will go
			next=random.choices([p0,p1,p2,p3,p4,p5,p6,p7],weights=[yellow,green,yellow,blue,purple,gray,purple,blue])
			nextposition = next[0][0]
			nextlastmove = next[0][1]
			if (nextposition[0] in range(0, N)) and (nextposition[1] in range(0, M)) and (nextposition not in filledpositions):
				individual[0] = nextposition
				individual[1] = nextlastmove
				filledpositions[i] = nextposition

		i+=1

	#ALL MOVES ARE DONE.NOW IT IS INFECTION TIME.

	for i in range(0,P-1):
		individual1=initialstate[i]
		for j in range(i+1,P-1):
			individual2=initialstate[j]
			distance=(((individual1[0][0]-individual2[0][0])**2)+((individual1[0][1]-individual2[0][1])**2))**(1/2)
			if individual1[3]!=individual2[3]:
				if individual1[3]=="infected" and individual2[3]=="notinfected":
					if distance<=D:
						if individual1[2]=="masked" and individual2[2]=="masked":
							a=(k/(distance**2))
							infectionprobability=min(1,a)/(y**2)


						if individual1[2]=="masked" and individual2[2]=="notmasked":
							a=(k/(distance**2))
							infectionprobability=min(1,a)/y


						if individual1[2]=="notmasked" and individual2[2]=="masked":
							a=(k/(distance**2))
							infectionprobability=min(1,a)/y

						if individual1[2]=="notmasked" and individual2[2]=="notmasked":
							a=(k/(distance**2))
							infectionprobability=min(1,a)

						r=random.choices(["infected","notinfected"],weights=[(infectionprobability),(1-infectionprobability)])[0]
						individual2[3]=r

				if individual1[3]=="notinfected" and individual2[3]=="infected":
					if distance<=D:
						if individual1[2]=="masked" and individual2[2]=="masked":
							a=k/(distance**2)
							infectionprobability=min(1,a)/(y**2)
						if individual1[2]=="masked" and individual2[2]=="notmasked":
							a=k/(distance**2)
							infectionprobability=min(1,a)/y
						if individual1[2]=="notmasked" and individual2[2]=="masked":
							a=k/(distance**2)
							infectionprobability=min(1,a)/y
						if individual1[2]=="notmasked" and individual2[2]=="notmasked":
							a=k/(distance**2)
							infectionprobability=min(1,a)

						r=random.choices(["infected","notinfected"],weights=[(infectionprobability),(1-infectionprobability)])[0]
						individual1[3]=r

	return initialstate

















































































