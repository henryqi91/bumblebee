# from ple.games.utils.udp_comm_sender_new import CommSender
# import signal_center
import pygame

class Algorithms(object):

    def __init__(self,screen_width,comm_sender,clock):
        self.screen_width = screen_width
        self.left_light_speed = 40
        self.right_light_speed = 40
        self.bound = 20
        self._sender = comm_sender
        self.clock = clock
        pass

    def run(self,algo_num,pad_x,obj_x,obj_y):
        while 1:
            if algo_num == 1:
                self.run_algo_1(pad_x,obj_x,obj_y)
            if algo_num == 2:
                self.run_algo_2(pad_x,obj_x,obj_y)
            if algo_num == 3:
                self.run_algo_3(pad_x,obj_x,obj_y)
            if algo_num == "Qlearning":
                self.run_Q_learning(pad_x,obj_x,obj_y)
            if algo_num == "pilco":
                self.run_pilco(pad_x,obj_x,obj_y)
            if algo_num == "pilco_bayesian":
                self.run_pilco_bayesian(pad_x,obj_x,obj_y)

    def run_algo_1(self,pad_x,obj_x,obj_y):
        obj_left_bound = obj_x - self.bound
        obj_right_bound = obj_x + self.bound
        if pad_x < obj_left_bound:
            self._sender._action_single_screen("right",self.right_light_speed)
            self._sender._action_single_screen("right", self.right_light_speed)
        if pad_x > obj_right_bound:
            self._sender._action_single_screen("left",self.left_light_speed)
            self._sender._action_single_screen("left", self.left_light_speed)

    def run_algo_2(self,pad_x,obj_x,obj_y):
        obj_left_bound = self.screen_width/2 - self.bound
        obj_right_bound = self.screen_width/2 + self.bound
        if obj_x > obj_right_bound:
            self._sender._action_single_screen("right",self.right_light_speed)
            self._sender._action_single_screen("right", self.right_light_speed)
        if obj_x < obj_left_bound:
            self._sender._action_single_screen("left",self.left_light_speed)
            self._sender._action_single_screen("left", self.left_light_speed)

    def run_algo_3(self,pad_x,obj_x,obj_y,acce):
        if pad_x - obj_x > 300:
            self._sender._action_single_screen(self.left_light_speed + acce,"left")
        if pad_x - obj_x > 150:
            self._sender._action_single_screen(self.left_light_speed,"left")
        if obj_x - pad_x > 300:
            self._sender._action_single_screen(self.right_light_speed + acce,"right")
        if obj_x - pad_x > 150:
            self._sender._action_single_screen(self.left_light_speed,"right")

    def run_Q_learning(self,pad_x,obj_x,obj_y):
        pass

    def run_pilco(self,pad_x,obj_x,obj_y):
        pass

    def run_pilco_bayesian(self,pad_x,obj_x,obj_y):
        pass
