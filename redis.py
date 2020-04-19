from sortedcontainers import SortedList, SortedDict, SortedSet
import time

class Redis_implementation:

	redis=dict() 
	ttl=dict()

	def GET(self,key):
		# delete keys whose ttl has expired
		for key in self.ttl:
			curr_time=int(time.time())
			if(curr_time<=ttl[key]):
				continue
			else:
				del self.ttl[key]

		if key in self.redis:
			if key in self.ttl:
				curr_time=int(time.time())
				# check if curr_time in epochs is less than the time to live for the desired key
				if(curr_time<=self.ttl[key]):
					return self.redis[key]
				else:
					# delete the key if the  expiry time has been reached
					del self.redis[key]
					del self.ttl[key]
			else:
				return self.redis[key]
		else:
			return None


	def SET(self,key, value):
		try:
			self.redis[key]=value
			return "OK"
		except:
			print("ERROR")


	def ZADD(self,key,mem,score):
		if key in self.redis:
			# check if the sorted list exists for the existing key
			if(type(self.redis[key])==str):
				return -1
			else:
				# add new member and score to the sorted list
				self.redis[key].add((mem,score))
		else:
			# if the key does not exist already, add the first elements to the sorted list
			self.redis[key]=SortedList()
			self.redis[key].add((mem,score))


	def ZRANGE(self,key,start,endi,withscore):
		length=len(self.redis[key])
		# find the correct index for negative indexes
		if(start<0):
			start=length-start
		if(endi<0):
			endi=length+endi

		for item in range(start,endi+1):
			print(self.redis[key][item][1])
			if(withscore==1):
				print(self.redis[key][item][0])


	def ZRANK(self,key,mem):
		length=len(self.redis[key])
		for item in range(0,length):
			if(self.redis[key][item][1]==mem):
				return item
		return None

	def EXPIRE(self,key,timesec):
		try:
			# calculate the expiry time in epochs
			curr_time = int(time.time())
			self.ttl[key]=curr_time+timesec
			return 1
		except:
			return None

	def TTL(self,key):
		# calculate the leftover time to live in epochs
		curr_time=int(time.time())
		return self.ttl[key]-curr_time

	def INCR(self,key):
		if key in self.redis:
			self.redis[key]=str(int(self.redis[key])+1)
			print(self.redis[key])


obj=Redis_implementation()
print(obj.SET("myval","10"))
print(obj.GET("myval"))
print(obj.GET("nonexist"))
obj.ZADD("myval","1","One")
obj.ZADD("newval","1","Uno")
obj.ZADD("newval","2","Two")
obj.ZADD("newval","1","Une")
obj.ZADD("newval","3","Three")
obj.ZRANGE("newval",0,-1,1)
print(obj.ZRANK("newval","Three"))
obj.EXPIRE("myval",10)
print(obj.TTL("myval"))
obj.INCR("myval")

