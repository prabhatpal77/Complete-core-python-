# the concept of storing python object into a file by converting python object into the form of file supported
# format is known as pickling..
import pickle
data=[["scott",7788,3000.00],
["blake", 7902, 2500.00],
["smith", 7369, 4000.00]]
x=open("pickle.txt","wb")
pickle.dump(data, x)
x.close()
