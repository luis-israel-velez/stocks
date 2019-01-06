#!/usr/bin/python3
#The following is code from "Reinforcement_Learning_for_Stock_Prediction"

from agent.agent import Agent 
from functions import *
import sys

if len(sys.argv) != 4:
	print("Ups!! Correct usage: [stock] [window] [episodes]")
	exit()

stock_name, window_size, episode_count = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])

print("Good so far!")

#We can ask this in the future
ftype = 'csv'

#agent = Agent(window_size)
data = getStockDataVec(stock_name, ftype)
l = len(data) - 1
batch_size = 32


for e in range(episode_count + 1):
	print("Episode " + str(e) + "/" + str(episode_count))
	state = getState(data, 0, window_size + 1)