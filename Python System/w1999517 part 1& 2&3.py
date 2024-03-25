#validations
pas=0
deferr=0
faile=0
star1=0
star2=0
star3=0
star4=0
count1=0
count2=0
count3=0
count4=0
list_u=[]
file=open('DOC.txt','w')

while True:
    while True:
        try:
            pas=int(input('Please enter your credit at pass: '))
        except ValueError:
            print('Integer required.')
            continue
        
        if pas<=120 and pas>=0:
            if pas!=0 and pas%20!=0:
                print('Out of range.')
                continue    
        else:
            print('Out of range.')
            continue    
        
        break


    while True:   
        try:
            deferr=int(input('Please enter your credit at defer: '))
        except ValueError:
            print('Integer required.')
            continue
        
        if deferr<=120 and deferr>=0:
            if deferr!=0 and deferr%20!=0:
                print('Out of range.')
                continue
        else:
            print('Out of range.')
            continue    
        
        break

    while True:
        try:
            faile=int(input('Please enter your credit at fail: '))
        except ValueError:
            print('Integer required.')
            continue
        
        if faile<=120 and faile>=0:
            if faile!=0 and faile%20!=0:
                print('Out of range.')
                continue
        else:
            print('Out of range.')
            continue
        break

    total=pas+deferr+faile        
    while True:
        if total!=120:
            print('Total incorrect')
        break

    total=pas+deferr+faile
    if total==120:
        if pas==120 and deferr==0 and faile==0  :
            print('Progress')
            list_u.append('progress'+' '+'-'+' '+str(pas)+','+' '+str(deferr)+','+' '+str(faile))
            file.write('\n progress'+' '+'-'+' '+str(pas)+','+' '+str(deferr)+','+' '+str(faile))

            count1=count1+1
            star1='*'*count1
        elif pas==100 and (deferr==20 or deferr==0) and (faile==0 or faile==20) :
            print('progress(module trailer)')
            list_u.append('progress (module trailer)'+' '+'-'+' '+str(pas)+','+' '+str(deferr)+','+' '+str(faile))
            file.write('\n progress (module trailer)'+' '+'-'+' '+str(pas)+','+' '+str(deferr)+','+' '+str(faile))
            count2=count2+1
            star2='*'*count2

        elif (pas==40 or pas==20 or pas==0) and (deferr==0 or deferr==20 or deferr==40) and (faile==80 or faile==100 or faile==120):
            print('Exclude')
            list_u.append('exclude'+' '+'-'+' '+str(pas)+','+' '+str(deferr)+','+' '+str(faile))
            file.write('\n exclude'+' '+'-'+' '+str(pas)+','+' '+str(deferr)+','+' '+str(faile))
            count3=count3+1
            star3='*'*count3
        else:
            (pas==80 or pas==60 or pas==40 or pas==20 or pas==0) and (deferr==0 or deferr==20 or deferr==40 or deferr==60 or deferr==80 or deferr==100) and (faile==0 or faile==20 or faile==40 or faile==60)
            print('Do Not Progress-module retriever')
            list_u.append('module retriever'+' '+'-'+' '+str(pas)+','+' '+str(deferr)+','+' '+str(faile))
            file.write('\n module retriever'+' '+'-'+' '+str(pas)+','+' '+str(deferr)+','+' '+str(faile))
            count4=count4+1
            star4='*'*count4
        print('\n')    
        print('Would you like to enter another set of data?')
    yes=input('Enter "y" for yes or "q" to quit and view results:' )
    if yes.lower()=='q':
        break

print('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('Histogram')
print('progress                ',count1,':',star1)
print('progress(module trailer)',count2,':',star2)
print('exclude                 ',count3,':',star3)
print('module retriever        ',count4,':',star4)
total_count=count1+count2+count3+count4
print(total_count,'outcomes in total')
print('-----------------------------------------------------------------')
for item in list_u:
    print(item)
file.close() 
