import rospy
from std_msgs.msg import String
#---------------------------------------# A1234567890123456B
msg="null"

def ceviri(string1):
	if string1[0]!='A' && string1[len(string1)-1]!='B':
		#print("Yanlis input")
		return ""
	
	motor=int((len(string1)-2)/4) #for döngü sayıları belirlenir
	if motor==4:
		string2=['','','','']
	else:
		string2=['','','','','','']
		
	for i in range(motor):
		str_temp=string1[4*i+1:4*i+5] #her turda stringten gerekli 4 haneyi alır
		if str_temp[0]=='0':
			temp=int(str_temp,10)
			if temp>255:
				#print("Deger limiti asiyor,255e esitlendi")
				temp=255
		else:
			temp=0-(int(str_temp,10)%1000)
			if abs(temp)>255:
				#print("Deger limiti asiyor,-255e esitlendi")
				temp= -255
	
		string2[i]=str(temp)+' '
		
	return string2
	
def callback(data):
	msg=ceviri(data.data)
	if len(msg)==4:
		pub=rospy.Publisher('/position/drive',String,queue_size=10)
		
	else:
		pub=rospy.Publisher('/position/robotic_arm',String,queue_size=10)

def main():
	rospy.init_node("node_one")
	rate=rospy.Rate(1)
	sub=rospy.Subscriber("encode_pub_node",String,callback)
	
	"""if len(sub)==18:
		pub=rospy.Publisher('/position/drive',String,queue_size=10)
		
	else:
		pub=rospy.Publisher('/position/robotic_arm',String,queue_size=10)
	"""	
	while not rospy.is_shutdown():
		pub.publish(msg)
		rate.sleep()
		
if __name__=='__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
