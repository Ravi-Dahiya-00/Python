# Python program to build an archery game
from builtins import len, range
import pygame
import random

pygame.init()

# Dimensions of the game window
WIDTH, HEIGHT = 600, 500

# Standard Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Paths
balloonPath = "balloon.png"
archerPath = "archer.png"
arrowPath = "arrow.png"

font = pygame.font.Font('freesansbold.ttf', 20)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Archer")

# To control the frame rate
clock = pygame.time.Clock()
FPS = 30
# Spawn the balloons
def populateBalloons(bWidth, bHeight, bSpeed, bCount):
	listOfBalloons = []

	# For the given count, spawn balloons at random
	# positions in the right half of the screen with
	# the given dimensions and speed
	for _ in range(bCount):
		listOfBalloons.append(Balloon(random.randint(
			WIDTH//2, WIDTH-bWidth), random.randint(0, HEIGHT), 
									bWidth, bHeight, bSpeed))

	return listOfBalloons


# Game Over Screen. Waits for the user to replay or quit
def gameOver():
	gameOver = True

	while gameOver:
		gameOverText = font.render("GAME OVER", True, WHITE)
		retryText = font.render("R - Replay Q - Quit", True, WHITE)

		# render the text on the screen using the pygame blit function
		screen.blit(gameOverText, (WIDTH//2-200, HEIGHT//2-100))
		screen.blit(retryText, (WIDTH//2-200, HEIGHT//2-80))

		# Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False
			if event.type == pygame.KEYDOWN:
				# replay
				if event.key == pygame.K_r: 
					return True
				# quit
				if event.key == pygame.K_q: 
					return False

		pygame.display.update()
class Archer:
	# init function to set the object variables and load the image
	def __init__(self, width, height, speed):
		self.width = width
		self.height = height
		self.speed = speed

		self.archer = pygame.transform.scale(
			pygame.image.load(archerPath), (self.width, self.height))
		self.archerRect = self.archer.get_rect()

		# Default position
		self.archerRect.x, self.archerRect.y = 100, HEIGHT//2

	# Method to render the archer on the screen
	def display(self):
		screen.blit(self.archer, self.archerRect)

	# Method to update the archer position
	def update(self, xFac, yFac):
		self.archerRect.x += xFac*self.speed
		self.archerRect.y += yFac*self.speed

		# Constraints to maintain the archer in the left half of the screen
		if self.archerRect.x <= 0:
			self.archerRect.x = 0
		elif self.archerRect.x >= WIDTH//2 - self.archerRect.w:
			self.archerRect.x = WIDTH//2 - self.archerRect.w
		if self.archerRect.y <= 0:
			self.archerRect.y = 0
		elif self.archerRect.y >= HEIGHT-self.archerRect.h:
			self.archerRect.y = HEIGHT - self.archerRect.h
# Balloon class consists of all the 
# functionalities related to the balloons
class Balloon:
	# init function to set the object variables and load the image
	def __init__(self, posx, posy, width, height, speed):
		self.width, self.height = width, height
		self.speed = speed

		self.balloonImg = pygame.image.load(balloonPath)
		self.balloon = pygame.transform.scale(
			self.balloonImg, (self.width, self.height))
		self.balloonRect = self.balloon.get_rect()

		self.balloonRect.x, self.balloonRect.y = posx, posy

	# Method to render the balloon on the screen
	def display(self):
		screen.blit(self.balloon, self.balloonRect)

	# Method to update the position of the balloon
	def update(self):
		self.balloonRect.y -= self.speed

		# If the balloon crosses the upper edge of the screen, 
		# we put it back at the lower edge
		if self.balloonRect.y < 0:
			self.balloonRect.y = HEIGHT+10
# Arrow class consists of all the functions related to the arrows
class Arrow:
	# init function to set the object variables and load the image
	def __init__(self, posx, posy, width, height, speed):
		self.width, self.height = width, height
		self.speed = speed
		self.hit = 0 # Used to track if the arrow has hit any balloon

		self.arrow = pygame.transform.scale(
			pygame.image.load(arrowPath), (width, height))
		self.arrowRect = self.arrow.get_rect()

		# arrow coordinates
		self.arrowRect.x, self.arrowRect.y = posx, posy

	# Method to render the arrow on the screen
	def display(self):
		screen.blit(self.arrow, self.arrowRect)

	# Method to update the position of the arrow
	def update(self):
		self.arrowRect.x += self.speed

	# Method to update the hit variable
	def updateHit(self):
		self.hit = 1

	def getHit(self):
		return self.hit
# Game Manager
def main():
	score = 0
	lives = 5
	running = True

	archer = Archer(60, 60, 7)
	xFac, yFac = 0, 0 # Used to control the archer

	numBalloons = 10

	listOfBalloons = populateBalloons(30, 40, 5, numBalloons)
	listOfArrows = []

	while running:
		screen.fill(GREEN) # Background

		# Representing each life with an arrow tilted by 45 degrees
		for i in range(lives):
			screen.blit(pygame.transform.rotate(pygame.transform.scale(
				pygame.image.load(arrowPath), (20, 30)), 45), (i*30, 10))

		# Rendering the score
		scoreText = font.render(f"Score: {score}", True, WHITE)
		screen.blit(scoreText, (10, HEIGHT-50))

		if len(listOfBalloons) == 0:
			listOfBalloons = populateBalloons(30, 40, 5, numBalloons)

		# When all the lives are over
		if lives <= 0:
			running = gameOver()

			# Clearing the lists
			listOfBalloons.clear()
			listOfArrows.clear()

			# Resetting the variables
			lives = 5
			score = 0
			listOfBalloons = populateBalloons(30, 40, 5, numBalloons)

		# Display and update all the balloons
		for balloon in listOfBalloons:
			balloon.update()
			balloon.display()

		# Display and update all the arrows
		for arrow in listOfArrows:
			arrow.update()
			arrow.display()

		# Display and update the archer
		archer.display()
		archer.update(xFac, yFac)

		# Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			# Key press event
			if event.type == pygame.KEYDOWN:
				# Replay button
				if event.key == pygame.K_r:	 
					listOfBalloons = populateBalloons(30, 40, 5, numBalloons)
					score = 0
				# Right arrow key => move rightwards => xFac = 1
				if event.key == pygame.K_RIGHT: 
					xFac = 1
				# Left arrow key => move leftwards => xFac = -1
				if event.key == pygame.K_LEFT: 
					xFac = -1
				# Down arrow key => move downwards => yFac = 1
				if event.key == pygame.K_DOWN: 
					yFac = 1
				# Up arrow key => move upwards => yFac = -1
				if event.key == pygame.K_UP: 
					yFac = -1
				# Fire button
				if event.key == pygame.K_SPACE: 
					listOfArrows.append(Arrow(
						archer.archerRect.x, 
						archer.archerRect.y+archer.archerRect.h/2-15, 60, 30, 10))

			# Key release event
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
					xFac = 0
				if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
					yFac = 0

		# Check for any collision between the arrows and the balloons
		for arrow in listOfArrows:
			for balloon in listOfBalloons:
				if pygame.Rect.colliderect(arrow.arrowRect, balloon.balloonRect):
					# Changes the arrow's 'hit' from 0 to 1
					arrow.updateHit() 
					# Remove the balloon form the list
					listOfBalloons.pop(listOfBalloons.index(balloon))
					# Increase the score
					score += 1	

		# Delete the arrows that crossed end of the screen
		for arrow in listOfArrows:
			if arrow.arrowRect.x > WIDTH:
				if not arrow.getHit():
					# If the arrow's state is 0, then a life is deducted
					lives -= 1
				listOfArrows.pop(listOfArrows.index(arrow))

		pygame.display.update()
		clock.tick(FPS)
# Python program to build an archery game
import pygame
import random

pygame.init()

# Dimensions of the game window
WIDTH, HEIGHT = 600, 500

# Standard Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Paths
balloonPath = "balloon.png"
archerPath = "archer.png"
arrowPath = "arrow.png"

font = pygame.font.Font('freesansbold.ttf', 20)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Archer")

# To control the frame rate
clock = pygame.time.Clock()
FPS = 30


class Archer:
	# init function to set the object variables and load the image
	def __init__(self, width, height, speed):
		self.width = width
		self.height = height
		self.speed = speed

		self.archer = pygame.transform.scale(
			pygame.image.load(archerPath), (self.width, self.height))
		self.archerRect = self.archer.get_rect()

		# Default position
		self.archerRect.x, self.archerRect.y = 100, HEIGHT//2

	# Method to render the archer on the screen
	def display(self):
		screen.blit(self.archer, self.archerRect)

	# Method to update the archer position
	def update(self, xFac, yFac):
		self.archerRect.x += xFac*self.speed
		self.archerRect.y += yFac*self.speed

		# Constraints to maintain the archer in the left half of the screen
		if self.archerRect.x <= 0:
			self.archerRect.x = 0
		elif self.archerRect.x >= WIDTH//2 - self.archerRect.w:
			self.archerRect.x = WIDTH//2 - self.archerRect.w
		if self.archerRect.y <= 0:
			self.archerRect.y = 0
		elif self.archerRect.y >= HEIGHT-self.archerRect.h:
			self.archerRect.y = HEIGHT - self.archerRect.h


# Balloon class consists of all the
# functionalities related to the balloons
class Balloon:
	# init function to set the object variables and load the image
	def __init__(self, posx, posy, width, height, speed):
		self.width, self.height = width, height
		self.speed = speed

		self.balloonImg = pygame.image.load(balloonPath)
		self.balloon = pygame.transform.scale(
			self.balloonImg, (self.width, self.height))
		self.balloonRect = self.balloon.get_rect()

		self.balloonRect.x, self.balloonRect.y = posx, posy

	# Method to render the balloon on the screen
	def display(self):
		screen.blit(self.balloon, self.balloonRect)

	# Method to update the position of the balloon
	def update(self):
		self.balloonRect.y -= self.speed

		# If the balloon crosses the upper edge of the screen,
		# we put it back at the lower edge
		if self.balloonRect.y < 0:
			self.balloonRect.y = HEIGHT+10


# Arrow class consists of all the functions related to the arrows
class Arrow:
	# init function to set the object variables and load the image
	def __init__(self, posx, posy, width, height, speed):
		self.width, self.height = width, height
		self.speed = speed
		# Used to track if the arrow has hit any balloon
		self.hit = 0

		self.arrow = pygame.transform.scale(
			pygame.image.load(arrowPath), (width, height))
		self.arrowRect = self.arrow.get_rect()

		# arrow coordinates
		self.arrowRect.x, self.arrowRect.y = posx, posy

	# Method to render the arrow on the screen
	def display(self):
		screen.blit(self.arrow, self.arrowRect)

	# Method to update the position of the arrow
	def update(self):
		self.arrowRect.x += self.speed

	# Method to update the hit variable
	def updateHit(self):
		self.hit = 1

	def getHit(self):
		return self.hit


# Spawn the balloons
def populateBalloons(bWidth, bHeight, bSpeed, bCount):
	listOfBalloons = []

	# For the given count, spawn balloons at random
	# positions in the right half of the screen with
	# the given dimensions and speed
	for _ in range(bCount):
		listOfBalloons.append(Balloon(random.randint(
			WIDTH//2, WIDTH-bWidth), random.randint(0, HEIGHT),
			bWidth, bHeight, bSpeed))

	return listOfBalloons


# Game Over Screen. Waits for the user to replay or quit
def gameOver():
	gameOver = True

	while gameOver:
		gameOverText = font.render("GAME OVER", True, WHITE)
		retryText = font.render("R - Replay Q - Quit", True, WHITE)

		# render the text on the screen using the pygame blit function
		screen.blit(gameOverText, (WIDTH//2-200, HEIGHT//2-100))
		screen.blit(retryText, (WIDTH//2-200, HEIGHT//2-80))

		# Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False
			if event.type == pygame.KEYDOWN:
				# replay
				if event.key == pygame.K_r: 
					return True
				# quit
				if event.key == pygame.K_q: 
					return False

		pygame.display.update()


# Game Manager
def main():
	score = 0
	lives = 5
	running = True

	archer = Archer(60, 60, 7)
	# Used to control the archer
	xFac, yFac = 0, 0

	numBalloons = 10

	listOfBalloons = populateBalloons(30, 40, 5, numBalloons)
	listOfArrows = []

	while running:
	# Background
		screen.fill(GREEN) 

		# Representing each life with an arrow tilted by 45 degrees
		for i in range(lives):
			screen.blit(pygame.transform.rotate(pygame.transform.scale(
				pygame.image.load(arrowPath), (20, 30)), 45), (i*30, 10))

		# Rendering the score
		scoreText = font.render(f"Score: {score}", True, WHITE)
		screen.blit(scoreText, (10, HEIGHT-50))

		if len(listOfBalloons) == 0:
			listOfBalloons = populateBalloons(30, 40, 5, numBalloons)

		# When all the lives are over
		if lives <= 0:
			running = gameOver()

			# Clearing the lists
			listOfBalloons.clear()
			listOfArrows.clear()

			# Resetting the variables
			lives = 5
			score = 0
			listOfBalloons = populateBalloons(30, 40, 5, numBalloons)

		# Display and update all the balloons
		for balloon in listOfBalloons:
			balloon.update()
			balloon.display()

		# Display and update all the arrows
		for arrow in listOfArrows:
			arrow.update()
			arrow.display()

		# Display and update the archer
		archer.display()
		archer.update(xFac, yFac)

		# Event handling
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

			# Key press event
			if event.type == pygame.KEYDOWN:
				# Replay button
				if event.key == pygame.K_r:	 
					listOfBalloons = populateBalloons(30, 40, 5, numBalloons)
					score = 0
				# Right arrow key => move rightwards => xFac = 1
				if event.key == pygame.K_RIGHT: 
					xFac = 1
				# Left arrow key => move leftwards => xFac = -1
				if event.key == pygame.K_LEFT: 
					xFac = -1
				# Down arrow key => move downwards => yFac = 1
				if event.key == pygame.K_DOWN: 
					yFac = 1
				# Up arrow key => move upwards => yFac = -1
				if event.key == pygame.K_UP: 
					yFac = -1
					# Fire button
				if event.key == pygame.K_SPACE: 
					listOfArrows.append(Arrow(
						archer.archerRect.x, 
						archer.archerRect.y+archer.archerRect.h/2-15, 60, 30, 10))

			# Key release event
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
					xFac = 0
				if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
					yFac = 0

		# Check for any collision between the arrows and the balloons
		for arrow in listOfArrows:
			for balloon in listOfBalloons:
				if pygame.Rect.colliderect(arrow.arrowRect, balloon.balloonRect):
					# Changes the arrow's 'hit' from 0 to 1
					arrow.updateHit() 
					# Remove the balloon form the list
					listOfBalloons.pop(listOfBalloons.index(balloon))
					# Increase the score
					score += 1	

		# Delete the arrows that crossed end of the screen
		for arrow in listOfArrows:
			if arrow.arrowRect.x > WIDTH:
				if not arrow.getHit():
					# If the arrow's state is 0, then a life is deducted
					lives -= 1
				listOfArrows.pop(listOfArrows.index(arrow))

		pygame.display.update()
		clock.tick(FPS)


if __name__ == "__main__":
	main()
	pygame.quit()
