# vim:set et sts=4 sw=4:
#-*- coding:utf-8 -*-
import sys,os
sys.path.append("../lib")
import Image,ImageOps
class IAC:
	
	def __init__(self,filename):
		self.laser_pic_path=filename
		self.pic=Image.open(self.laser_pic_path)
		self.pic=self.pic.convert("RGB")
		self.pic=ImageOps.invert(self.pic)
		self.pic.save("temp/image_inverted.png")
		self.pic_tmp=self.pic.convert("1")
		self.pic_tmp.save("temp/image_binarized.png")

	def create_array(self):
		self.im=Image.open("temp/image_binarized.png")
		self.width,self.height=self.im.size
		self.array=[]

#	normal
		for y in range(self.height):
			self.array.append([self.im.getpixel((x,y)) for x in range(self.width)])
                #print "array size:"
                #print len(self.array[0])
                #print len(self.array)

        # calcutate zero data counts for calc. working time
        def calculate_steps(self):

                # how many N steps
                self.stepN_counts = 0
                # total N step counts
                self.stepN_total = 0
                # how many steps over 10
                self.step10N_counts = 0
                # total over10 step counts
                self.step10N_total = 0
                # data counts
                self.have_data_counts = 0
                n=0
                for x in range(self.width):
                        for y in range(self.height):
                                if (self.array[y][x]):
                                        self.have_data_counts += 1
                                        if (n>10):
                                                self.step10N_counts+=1
                                                self.step10N_total+=n
                                        else:
                                                self.stepN_counts+=1
                                                self.stepN_total+=n
                                        n=0
                                else:
                                        n+=1

                #print info
                #print "stepN counts: %d" %self.stepN_counts,
                #print "total: %d" %self.stepN_total
                #print ">10 stepN counts: %d" %self.step10N_counts,
                #print "total: %d" %self.step10N_total
                                    
                                    
		

#       A better human readable style for create the normal array.(append list)		
#		for y in range(self.height):
#		        a_line = []
#                       for x in range(self.width):
#		                  a_line.append( self.im.getpixel((x,y)) )
#		        self.array.append(a_line)
	
#	mirror array
#      WHAT is MIRROR ? the x ---> y and y -----> x.
#		for y in range(self.width):
#			 self.array.append([self.im.getpixel((y,x)) for x in range(self.height-1,-1,-1)])
			

		


