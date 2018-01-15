#!/usr/bin/env python

# Software License Agreement (BSD)
#
#  file      @navigation.py
#  authors   Ben Fogarty <ben.fogarty@live.com>
#            Better Robotics <ben.fogarty@live.com>
#  copyright Copyright (c) 2017, Better Robotics, Inc., All rights reserved.
#            
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that
# the following conditions are met:
#  * Redistributions of source code must retain the above copyright notice, this list of conditions and the
#    following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
#    following disclaimer in the documentation and/or other materials provided with the distribution.
#  * Neither the name of Better Robotics nor the names of its contributors may be used to endorse or promote
#    products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WAR-
# RANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, IN-
# DIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
# OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



#import numpy as np
import math

class vectorFields:
    def __init__(self, att_field_radius=1, att_field_area=1,  att_field_strength=1,
                      rep_field_radius=20, rep_field_area=50, rep_field_strength=3,
                                               max_vector=30, max_theta=0.87       ):
        
        # initialise variable used to indicate
        self.x_att = self.x_rep = self.y_att = self.y_rep = self.dt_x = self.dt_y = 0.0
        self.att_field_radius = att_field_radius
        self.att_field_area = att_field_area
        self.att_field_strength = att_field_strength
        self.rep_field_radius = rep_field_radius
        self.rep_field_area = rep_field_area
        self.rep_field_strength = rep_field_strength
        self.max_vector = max_vector
        self.max_theta = max_theta

    def attractor(self, att_range, att_angle):
        if(att_range < self.att_field_radius):
            self.x_att = 0
            self.y_att = 0
        elif(att_range <= (self.att_field_radius + self.att_field_area)):
            self.x_att = self.att_field_strength * att_range * math.sin( (att_angle) )
            self.y_att = self.att_field_strength * att_range * math.cos( (att_angle) )
        elif(att_range > (self.att_field_radius + self.att_field_area )):
            self.x_att = att_range * math.sin( (att_angle) )
            self.y_att = att_range * math.cos( (att_angle) )
        return [self.x_att, self.y_att]

    def repulsor(self, rep_range, rep_angle):
        if(rep_range == 0):
            self.x_rep += 0
            self.y_rep += 0
        elif( rep_range <= ( self.rep_field_area + self.rep_field_radius ) ):
            self.x_rep += -self.rep_field_strength * ( ( self.rep_field_area + self.rep_field_radius ) - rep_range ) * math.sin( (rep_angle) )
            self.y_rep += -self.rep_field_strength * ( ( self.rep_field_area + self.rep_field_radius ) - rep_range ) * math.cos( (rep_angle) )
        else:
            self.x_rep += 0
            self.y_rep += 0
        return [self.x_rep, self.y_rep]

    def get_heading(self):
        self.dt_x = self.x_att + self.x_rep
        self.dt_y = self.y_att + self.y_rep
        vector = math.hypot(self.dt_x, self.dt_y)
        theta = math.atan2(self.dt_x, self.dt_y)  # I swapped X<->Y to make left: -deg, forward: 0deg, right: +deg 

        # reset att/rep values 
        self.x_rep = 0
        self.y_rep = 0
        self.x_att = 0
        self.y_att = 0

        vector = min(vector, self.max_vector)
        if theta > self.max_theta:
            theta = self.max_theta
        elif theta < -self.max_theta:
            theta = -self.max_theta
        return vector, theta, [self.dt_x, self.dt_y]


        
