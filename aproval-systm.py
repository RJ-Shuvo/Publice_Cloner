def main_apv():
    os.system('clear')
    #Wasi ke jaga apna name likhlo 
    ak="RJ"
    logo()
    
    os.system('xdg-open https://www.facebook.com/profile.php?id=100007016558237')
    try:
    	
        key1=open('/data/data/com.termux/files/usr/bin/.SHUVO-cov', 'r').read()
    except IOError:
        os.system("clear")
        logo()
        print ("[*]--------------------------------------------------------------")
        print ("  Your Token Is Not Approved Already")
        print ("[*]--------------------------------------------------------------")
        print ("           THIS TOOL IS PAID ")
        print ("           THIS IS YOUR KEY BRO")
        print ("[*]--------------------------------------------------------------")
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("          YOUR KEY : "+ak+myid)
        print ("[*]--------------------------------------------------------------")
        
        kok=open('/data/data/com.termux/files/usr/bin/.RJ-cov', 'w')
        kok.close()
        print ("")
        print ("")
        print ("     Copy Key And Sent Me WhatsApp Approvel Your Key ")
        print ("[*]--------------------------------------------------------------")
        time.sleep(6)
        
        os.system("xdg-open https://wa.me/+8801950808973")
        
    r1=requests.get("https://github.com/RJ-Shuvo/Publice_Cloner/blob/main/approved.txt").text
    if key1 in r1:
    	#R ke jaga apne main jahan sy script started krna chahty wo lagao 
        R()
    else:
        os.system("clear")
        os.system('xdg-open https://www.facebook.com/profile.php?id=100007016558237')
        logo()
        print ("[*]--------------------------------------------------------------")
        print ("  Your Token Is Not Approved Already")
        print ("[*]--------------------------------------------------------------")
        print ("          THIS IS YOUR KEY BRO")
        print ("[*]--------------------------------------------------------------")
        print ("")
        print ("          YOUR KEY : "+ak+key1)
        print ("[*]--------------------------------------------------------------")
        print ("     Copy Key And Sent Me WP Approvel Your Key ")
        print ("[*]--------------------------------------------------------------")
        time.sleep(3.5)
        #Numbr chnge krlyna
        os.system("xdg-open https://wa.me/+8801950908973")