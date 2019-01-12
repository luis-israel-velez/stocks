#The following repository is to play around with ML and Stocks

#Let's have some fun!

#The following is NOT my code but compilation from different sites/videos to start trainning.
#Learning how model works, and what we can do. 

sudo docker build -t python-stock .


sudo docker run python-stock python ./train.py GSPC 10 1000
