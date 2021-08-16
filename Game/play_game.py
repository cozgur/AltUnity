import math

from altunityrunner import By

from base_page import BasePage

class GameplayPage(BasePage):
    def __init__(self, altdriver):
        BasePage.__init__(self, altdriver)
        self.previous_x = 0
        self.previous_y = 0

    @staticmethod
    def get_distance(player, enemy):
        x = float(player.worldX)-float(enemy.worldX)
        y = float(player.worldZ)-float(enemy.worldZ)
        distance = [x, y]
        return distance

    def find_player(self):
        return self.altdriver.find_object(By.NAME, "Player")

    def find_enemy(self):
        return self.altdriver.find_object(By.NAME, "Enemy")

    def find_obstacle(self):   
        return self.altdriver.find_object(By.NAME, "Obstacle")

    def move(self, x, y):

        pad = self.altdriver.find_object(By.NAME, "Movement_Pad")
        if x > 0 and y > 0:
            self.altdriver.swipe_and_wait(int(pad.x), int(pad.y), int(pad.x), int(pad.y)+150, 1)

        elif x == 0 and y > 0:
            self.altdriver.swipe_and_wait(int(pad.x), int(pad.y), int(pad.x), int(pad.y)+75, 1) 

        elif x < 0 and y < 0:
            self.altdriver.swipe_and_wait(int(pad.x), int( pad.y), int(pad.x), int(pad.y)-150, 1)

        elif x == 0 and y == 0:
            self.altdriver.swipe_and_wait(int(pad.x), int(pad.y), int(pad.x), int(pad.y), 1)     

        elif x > 0 > y:
                self.altdriver.swipe_and_wait(int(pad.x), int(pad.y), int(pad.x)+150, int(pad.y), 1)

        elif x < 0 < y:
                self.altdriver.swipe_and_wait(int(pad.x), int(pad.y), int(pad.x)-150, int(pad.y), 1)

    def shoot(self, a, b):
        shoot_pad = self.altdriver.find_object(By.NAME, "attackButton")
        if a > 0 and b > 0:
                self.altdriver.swipe_and_wait(int(shoot_pad.a), int(
                    shoot_pad.b), int(shoot_pad.a), int(shoot_pad.b)+90, 1)
        elif a < 0 and b < 0:
                self.altdriver.swipe_and_wait(int(shoot_pad.a), int(
                    shoot_pad.b), int(shoot_pad.a), int(shoot_pad.b) - 90, 1)
        elif a > 0 > b:
                self.altdriver.swipe_and_wait(int(shoot_pad.a), int(
                    shoot_pad.b), int(shoot_pad.a) + 90, int(shoot_pad.b), 1)
        elif a < 0 < b:
                self.altdriver.swipe_and_wait(int(shoot_pad.a), int(
                    shoot_pad.b), int(shoot_pad.a) - 90, int(shoot_pad.b), 1)

    def stay_away_obstacles(self, dict):

        player = self.find_player

        for str1 in dict:

            for tag, str2 in str1:

                if tag == True:

                    if str1 == "Enemy":
                        enemies = self.find_enemy    
                        distance = self.get_distance(player, enemies[0])
                        self.shoot(-distance[str2], distance[str2])

                    elif str1 == "Obstacle":

                        self.move(-distance[str2], -distance[str2])    

                else:   

                    self.move(distance[str2], -distance[str2])








    

