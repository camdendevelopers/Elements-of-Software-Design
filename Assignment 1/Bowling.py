#  File: Bowling.py
#  Description: Program that reads a file with bowling scores and prints a scoreboard for each game 
#  Student's Name: Marcos J. Ortiz
#  Student's UT EID: mjo579
#  Course Name: CS 313E 
#  Unique Number: 51320
#
#  Date Created: September 4, 2016
#  Date Last Modified: September 8, 2016

def isstrike(val):
	return val == 10

def isspare(val):
	return val == "/"

def iszero(val):
	return val == 0

def main():

	#Open file for reading
	in_file = open("./scores.txt", "r")

	#Read line by line
	for line in in_file:

		#Declare variables
		score = 0
		frame_scores = []
		frames = 1
		toss = 0
		frame = 1

		#Remove new line values and make a list of numbers
		line = line.strip()
		line = line.split(" ")

		toss_scores = line[:]

		#Convert char to int
		for element in range(len(line)):
			if line[element] == "-":
				line[element] = 0
			elif line[element] == "X":
				line[element] = 10
			elif line[element] == "/":
				continue
			else:
				line[element] = int(line[element])

		#Iterate through each line
		for x in range(len(line)):
			ball = line[x]
			if (len(line) - 3 <= x) and (frame >= 10):
				toss += 1
				if isspare(ball):
					score += (10 - line[x-1])
				else:
					score += ball
				continue
			elif isstrike(ball):
				toss += 2
				score += ball
				score += line[x+1]
				if isspare(line[x+2]):
					score += (10 - line[x+1])
				else:
					score += line[x+2]

			elif isspare(ball):
				toss += 1
				score += (10 - line[x-1])
				score += line[x+1]
			else:
				toss += 1
				score += ball

			#Toss represents balls "tossed"
			#Usually for each element, toss increases by 1
			#With strikes it increases by 2

			#This snippet will create a new frame everytime there is two tosses
			if toss % 2 == 0:
				frame += 1
				frame_scores.append(score)
		#This snippet will append the final score to the frame_score list 
		if toss <= 21:
			frame += 1
			frame_scores.append(score)

			#Print scoreboard for each game
			print("  1   2   3   4   5   6   7   8   9    10  ")
			print("+---+---+---+---+---+---+---+---+---+-----+")

			final_frame = 0
			j = 0
			while j <= (len(toss_scores) - 2):
				ball1 = toss_scores[j]

				if final_frame >= 9:
					ball2 = toss_scores[j + 1]
					last_ball = toss_scores[len(toss_scores) - 1]
					if last_ball is not None and (last_ball != ball2 or last_ball == "X"):
						print("|{:} {:} {:}|".format(ball1, ball2, last_ball), end = "")
					else:
						print("|{:} {:}  |".format(ball1, ball2), end = "")
					j+=1
					break
				elif ball1 == "X":
					
					print("|{:}  ".format(ball1), end = "")

					final_frame += 1
					j += 1

				else:
					ball2 = toss_scores[j + 1]
					

					print("|{:} {:}".format(ball1, ball2), end = "")
					j+=2
					final_frame += 1
				
			print()
			for i in range(len(frame_scores)):
				if i == 9:
					print("|{:5d}|".format(frame_scores[i]), end = "")
				else:
					print("|{:3d}".format(frame_scores[i]), end = "")
			print()
			print("+---+---+---+---+---+---+---+---+---+-----+")

		print("\n")
	
main()