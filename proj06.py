# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:01:06 2020

@author: aesha
"""
###########################################################
    #Computer Project #6
    #   open_file function
    #   read_file function
    #   shoots_left_right function
    #   position function
    #   off_side_shooter function
    #   points_per_game function
    #   games_played function
    #   shots_taken function
    #   printing all data through main function
###########################################################

import csv

def open_file():
    '''Asking for a file name and opening file, otherwise print error'''
    fp = input("Enter filename: ") 
    while True:
        try:
            fp = open(fp, "r")
            return fp    
        except FileNotFoundError:
            print("File not found! Please try again!")


def read_file(fp):
    '''create a list of lists from file'''
    reader = csv.reader(fp) 
    master_list=[]
    fp.readline()
    for line_list in reader: 
        if line_list[0].strip == "":
            continue
        master_list.append(line_list)
    return master_list 
    
def shoots_left_right(master_list):
    '''Count number of left and right shooters'''
    right=0
    left=0
    for line in master_list:
        if line[1]== "L": 
            left += 1
            continue
        if line[1]=="R":
            right += 1
            continue
    return left,right

def position(master_list):
    '''Counting number of players playing each position'''
    right = 0
    left = 0
    center = 0
    defense = 0
    for line in master_list:
        if line[2]=="L":
            left += 1
            continue
        if line[2]== "R": 
            right += 1
            continue
        if line[2]== "C": 
            center += 1
            continue
        if line[2]== "D": 
            defense += 1
            continue
    return left,right,center,defense

def off_side_shooter(master_list):
    '''Counting number of players who are left-winged and right-shooters, vise-versa'''
    scl_shootr = 0
    scr_shootl = 0
    for line in master_list:
        if (line[1] == "L") and (line[2] == "R"):
            scl_shootr += 1
        if (line[1] == "R") and (line[2] == "L"):
            scr_shootl += 1
    return scr_shootl, scl_shootr

def points_per_game(master_list):
    '''Creating top 10 list of tuples with player name, pointers per game, and position'''
    points = []
    for line in master_list:
        pgp = float(line[18])
        pgp_tuple = (pgp, line[0], line[2])
        points.append(pgp_tuple)    
    points.sort(reverse=True)
    points = points[0:10]
    return points

def games_played(master_list):
    '''Creating top 10 list of tuples with player name and games played'''
    gp = []
    for line in master_list:
        games = int(line[3].replace(",", ""))
        games_tuple = (games, line[0])
        gp.append(games_tuple)
    gp.sort(reverse=True)
    gp = gp[0:10]
    return gp

def shots_taken(master_list):
    '''Creating top 10 list of tuples with player name and shots taken'''
    shots_list = []
    for line in master_list:
        if line[9] == '--':
            continue
        shots = line[9].replace(",", "")
        shots = int(shots)
        shots_tuple = (shots, line[0])
        shots_list.append(shots_tuple)
    shots_list.sort(reverse = True)
    shots_list = shots_list[0:10]
    return shots_list
    
def main():
    '''Calling all functions'''
    fp = open_file()
    print("")
    print("")
    master_list = read_file(fp)
    
    left,right = shoots_left_right(master_list)
    print("{:^10s}".format("Shooting"))
    print("left:  {:4d}".format(left))
    print("right: {:4d}".format(right))
    print("")
    
    left,right,center,defense = position(master_list)
    print("{:^12s}".format("Position"))
    print("left:    {:4d}".format(left))
    print("right:   {:4d}".format(right))
    print("center:  {:4d}".format(center))
    print("defense: {:4d}".format(defense))
    print("")
    
    scl_shootr, scr_shootl = off_side_shooter(master_list)
    print("{:^24s}".format("Off-side Shooter"))
    print("left-wing shooting right: {:4d}".format(scl_shootr))
    print("right-wing shooting left: {:4d}".format(scr_shootl))
    print("")
        
    pgp = points_per_game(master_list)
    print("{:^36s}".format("Top Ten Points-Per-Game"))
    print("{:<20s}{:>8s}{:>16s}".format('Player','Position','Points Per Game'))
    for line in pgp:
        print("{:<20s}{:>8s}{:>16.2f}".format(line[1],line[2],float(line[0])))
    print("")
    
    gp = games_played(master_list)
    print("{:^36s}".format("Top Ten Games-Played"))
    print("{:<20s}{:>16s}".format('Player','Games Played'))
    for line in gp:
        print("{:<20s}{:>16,d}".format(line[1],line[0]))
    print("")
    
    
    
    
    shots = shots_taken(master_list)
    print("{:^36s}".format("Top Ten Shots-Taken"))
    print("{:<20s}{:>16s}".format('Player','Shots Taken'))
    for line in shots:
        print("{:<20s}{:>16,d}".format(line[1],line[0]))


if __name__ == "__main__":
    main()