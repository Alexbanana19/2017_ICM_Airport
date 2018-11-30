# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 23:40:55 2017

@author: Alex
"""
import numpy as np
import random
import math

class Passenger:
    def __init__(self):
        rand = np.random.randint(2, 9)
        #self_attribute
        self.No = 0
        self.ispre = False 
        self.delay = rand
        #waiting time at each buffer
        self.id_time = 0
        self.bag_time = 0
        self.per_time = 0
        self.addb_time = 0
        self.addp_time = 0
        self.exit_time = 17 #17.4082 
        #waiting time at each service
        self.idser_time = 0
        self.bagser_time = 0
        self.perser_time = 0
        self.addbser_time = 0
        self.addpser_time = 0
        
    def getWaitTime(self):
        return self.id_time + max(self.bag_time, self.per_time) \
        + max(self.addb_time, self.addp_time) + self.exit_time

class Lane:
    def __init__(self):
        #service check time
        self.id_checktime = 11
        self.bag_checktime = 2
        self.per_checktime = 30
        self.addb_checktime = 90
        self.addp_checktime = 60
        #additional check odds
        self.bag_eps = 0.0714
        self.per_eps = 0.05
        #service buffer Q
        self.id_buffer = []
        self.bag_buffer = []
        self.per_buffer = []
        self.addb_buffer = []
        self.addp_buffer = []
        self.passenger_list = []
        #passenger at each service
        self.id = []
        self.bag = []
        self.per = []
        self.addb = []
        self.addp = []
        
        

    def renew(self):
         #renew buffer
        for i in range(0, len(self.id_buffer)):
            self.id_buffer[i].id_time += 1
        for i in range(0, len(self.bag_buffer)):
            self.bag_buffer[i].bag_time += 1
        for i in range(0, len(self.per_buffer)):
            self.per_buffer[i].per_time += 1
        for i in range(0, len(self.addb_buffer)):
            self.addb_buffer[i].addb_time += 1
        for i in range(0, len(self.addp_buffer)):
            self.addp_buffer[i].addp_time += 1
        #renew service
        #ID checking
        if self.id == []:
            if len(self.id_buffer):
                self.id_buffer[0].idser_time += 1
                self.id.append(self.id_buffer[0])
                del self.id_buffer[0]
        else:
            self.id[0].idser_time += 1
            if self.id[0].idser_time >= self.id_checktime + self.id[0].delay:
                self.id[0].id_time += self.id[0].idser_time 
                self.bag_buffer.append(self.id[0])
                self.per_buffer.append(self.id[0])
                self.id = [] #need to confirm dist
                #self.id_checktime += math.ceil(np.random.randn())#need to fix
        #Bag checking        
        if self.bag == []:
            if len(self.bag_buffer):
                self.bag_buffer[0].bagser_time += 1
                self.bag.append(self.bag_buffer[0])
                del self.bag_buffer[0]
        else:
            self.bag[0].bagser_time += 1
            if self.bag[0].bagser_time >= self.bag_checktime + self.bag[0].delay:
                self.bag[0].bag_time += self.bag[0].bagser_time #need to confirm dist
                self.bag_checktime += math.ceil(np.random.randn())#need to fix
                
                rand = np.random.random()
                if rand <= self.bag_eps :
                    self.addb_buffer.append(self.bag[0])
                    self.bag = []
                else:
                    flag = 0
                    for i in range(0,len(self.passenger_list)):
                        if self.passenger_list[i].No == self.bag[0].No:
                            self.passenger_list[i].bag_time = self.bag[0].bag_time 
                            flag = 1
                            break
                    if flag == 0:
                        self.passenger_list.append(self.bag[0])
                    self.bag = []
        #Per checking
        if self.per == []:
            if len(self.per_buffer):
                self.per_buffer[0].perser_time += 1
                self.per.append(self.per_buffer[0])
                del self.per_buffer[0]
        else:
            self.per[0].perser_time += 1
            if self.per[0].perser_time >= self.per_checktime + self.per[0].delay:
                self.per[0].per_time += self.per[0].perser_time
                #self.per_checktime += math.ceil(np.random.randn())#need to fix
                
                rand = np.random.random()
                if rand <= self.per_eps :
                    self.addp_buffer.append(self.per[0])
                    self.per = []
                else:
                    flag = 0
                    for i in range(0,len(self.passenger_list)):
                        if self.passenger_list[i].No == self.per[0].No:
                            self.passenger_list[i].per_time = self.per[0].per_time 
                            flag = 1
                            break
                    if flag == 0:
                        self.passenger_list.append(self.per[0])
                    self.per = []
        #addb checking
        if self.addb == []:
            if len(self.addb_buffer):
                self.addb_buffer[0].addbser_time += 1
                self.addb.append(self.addb_buffer[0])
                del self.addb_buffer[0]
        else:
            self.addb[0].addbser_time += 1
            if self.addb[0].addbser_time >= self.addb_checktime + self.addb[0].delay:
                self.addb[0].addb_time += self.addb[0].addbser_time
                #self.addb_checktime += math.ceil(np.random.randn())#need to fix
                
                flag = 0
                for i in range(0,len(self.passenger_list)):
                    if(self.passenger_list[i].No == self.addb[0].No):
                        self.passenger_list[i].addb_time = self.addb[0].addb_time
                        self.passenger_list[i].bag_time= self.addb[0].bag_time
                        flag = 1
                        break
                if flag == 0:
                    self.passenger_list.append(self.addb[0])
                self.addb = []           
        #addp checking
        if self.addp == []:
            if len(self.addp_buffer):
                self.addp_buffer[0].addpser_time += 1
                self.addp.append(self.addp_buffer[0])
                del self.addp_buffer[0]
        else:
            self.addp[0].addpser_time += 1
            if self.addp[0].addpser_time >= self.addp_checktime + self.addp[0].delay:
                self.addp[0].addp_time += self.addp[0].addpser_time
                #self.addp_checktime += math.ceil(np.random.randn())#need to fix
                
                flag = 0
                for i in range(0,len(self.passenger_list)):
                    if(self.passenger_list[i].No == self.addp[0].No):
                        self.passenger_list[i].addp_time = self.addp[0].addp_time 
                        self.passenger_list[i].per_time = self.addp[0].per_time 
                        flag = 1
                        break
                if flag == 0:
                    self.passenger_list.append(self.addp[0])
                self.addp = []   
        return         
    
    def isClear(self):
        if len(self.id) != 0 or len(self.bag) != 0  or len(self.per) != 0 \
            or len(self.addb) != 0 or len(self.addp) != 0 or len(self.id_buffer) != 0\
            or len(self.bag_buffer) != 0 or len(self.per_buffer) != 0 or \
            len(self.addb_buffer) != 0 or len(self.addp_buffer) != 0:
            return False
        else:
            return True
    
    def getQLen(self):
        return len(self.id_buffer) + len(self.bag_buffer) + len(self.per_buffer)

def firePassenger(fire_eps1, fire_eps2, fire_eps3, fire_eps4):
    b = 1 / 5
    fire_rand = np.random.random()
    
    if fire_rand < fire_eps4:
        return 4, math.ceil(random.expovariate(b))
    elif fire_eps4 < fire_rand < fire_eps3:
        return 3, math.ceil(random.expovariate(b))
    elif fire_eps3 < fire_rand < fire_eps2:
        return 2, math.ceil(random.expovariate(b))
    else:
        return 1, math.ceil(random.expovariate(b))

def main():
    N = 500
    j = 0
    delta = 0
    cur_state = 0
    next_state = 0
    counter = 0
    fire_eps1 = 1
    fire_eps2 = 0.6
    fire_eps3 = 0.3
    fire_eps4 = 0.1
    passenger_eps = 0.45
    
    lane1 = Lane()
    lane2 = Lane()
    lane3 = Lane()
    lanep = Lane()
    
    lanep.id_checktime = 11#9.1895 
    lanep.bag_checktime = 5 #4.862
    lanep.per_checktime = 10 #10.463
    lanep.addb_checktime = 90 
    lanep.addp_checktime = 60
    
    while True:
        if counter == N:
            while not lane1.isClear(): 
                lane1.renew()
            while not lane2.isClear():  
                lane2.renew()
            while not lane3.isClear(): 
                lane3.renew()
            while not lanep.isClear():  
                lanep.renew()
            break
    
        if next_state == cur_state and counter <= N:
            passenger = []
            passenger_num, delta = firePassenger(fire_eps1, fire_eps2, fire_eps3, fire_eps4)
            rand = np.random.random()
            if rand < passenger_eps:
                for k in range(0, passenger_num):
                    temp = Passenger()
                    temp.No = counter
                    temp.ispre = True
                    passenger.append(temp)
                    counter += 1
                    if counter == N:
                        break
            else:
                for k in range(0, passenger_num):
                    temp = Passenger()
                    temp.No = counter
                    passenger.append(temp)
                    counter += 1
                    if counter == N:
                        break
            
            cur_state = j
            next_state = j + delta
            
            if passenger[0].ispre:
                lanep.id_buffer += passenger
            else:
                if lane1.getQLen() <= min(lane2.getQLen(), lane3.getQLen()):
                    lane1.id_buffer += passenger
                elif lane2.getQLen() <= min(lane1.getQLen(), lane3.getQLen()):
                    lane2.id_buffer += passenger
                elif lane3.getQLen() <= min(lane1.getQLen(), lane2.getQLen()):
                    lane3.id_buffer += passenger
            lane1.renew()
            lane2.renew()
            lane3.renew()
            lanep.renew()
            #print("Enter %d passenger" %counter)
            
        else:
            lane1.renew()
            lane2.renew()
            lane3.renew()
            lanep.renew()
        
        j += 1
        cur_state += 1
    
    passenger_list = lane1.passenger_list + lane2.passenger_list + lane3.passenger_list + lanep.passenger_list    
    final_time_list = []
    
    for k in range(0, N):
        final_time_list.append(passenger_list[k].getWaitTime())

    mean = np.mean(final_time_list)
    a = np.array(final_time_list)
    var = np.var(a)
    return mean, var

   
        
        
        
        
        

