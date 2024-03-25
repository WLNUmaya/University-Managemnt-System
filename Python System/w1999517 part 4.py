#validations
pas=0
deferr=0
faile=0


my_dic1={}
my_dic2={}

#student id =k


      

while True:
    try:
        k=(input('enter student id:'))
        s=(k[0]+','+k[1]+','+k[2]+','+k[3]+','+k[4]+','+k[5]+','+k[6]+','+k[7])
        if len(s)!=15:
            print('enter correct student id')
        
            break
        pas=int(input('please enter your credits at pass:'))
        if pas not in range (0,121,20):
            print('out of range')
        else:
            deferr=int(input('please enter your credits at defer:'))
            if deferr not in range (0,121,20):
                print('out of range')
            else:
                faile=int(input('please enter your credits at fail:'))
                if faile not in range (0,121,20):
                    print('out of range')
    
        if (pas+deferr+faile)!=120:
           print('total is incorrect')
        else:
            if pas==120:
                
                my_dic2[k]=('progress'+' '+'-'+' '+str(pas)+','+' '+str(deferr)+','+' '+str(faile))
                
            elif pas==100:
                
                my_dic2[k]=('progress (module trailer)'+' '+'-'+' '+str(pas)+','+' '+str(deferr)+','+' '+str(faile))
            elif (faile==120 or faile==100 or faile==80):
                
                my_dic2[k]=('exclude'+' '+'-'+' '+str(pas)+','+' '+str(deferr)+','+' '+str(faile)) 
            else:
               
                
                my_dic2[k]=('do not progress (module retriever)'+' '+'-'+' '+str(pas)+','+' '+str(deferr)+','+' '+str(faile))
    
    except ValueError:
        print('ingeger required')
    
                            
    yes=input('''would you like to enter another set of data?.
enter y for yes or q to quit and view results:''')
    if yes=='y':
        continue
    elif yes=='q':
       break
    else:
        print('please enter y or q')
for u,total_count in my_dic2.items():
    print( u,':',total_count)



