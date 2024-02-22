option=''
progress=0
trailer=0
retriever=0
exclude=0
outcome=0
n=0
progression=''
dict_main={}

def main():
    option='y'
    
def outofrangecheck(credit):
    if credit in range(0,121,20):
        global n
        n+=1
        main()
    else:
        print('Out of range')
        main()
    
while option!='q':
    if n==0:
        student_id=input('Enter your Student ID :')
        if student_id in dict_main:
            print('This ID has alredy entered, try again')
            print('')
            continue
        elif student_id=='':
            print("You have not entered a ID")
            print('')
            continue
        else:
            n+=1
            
    try:
        total=0
        if n==1:
            Pass=int(input('Please enter your credits at pass  :'))
            outofrangecheck(Pass)
        elif n==2:
            defer=int(input('Please enter your credits at defer :'))
            outofrangecheck(defer)
        elif n==3:    
            fail=int(input('Please enter your credits at fail  :'))
            outofrangecheck(fail)
        else:
            total=Pass+defer+fail
            if total!=120:
                print('Total Incorrect')
                n=1
                print('')
                main()
            elif Pass==120:
                print('Progress')
                progression='Progress -'
                progress+=1
            elif Pass==100:
                print('Progress(module Trailer)')
                progression='Progress(module trailer)-'
                trailer+=1
            elif fail in range(80,121,20):
                print('Exclude')
                progression='Exclude-'
                exclude+=1
            else:
                print('Do not progress - module retriever')
                progression='module retriever-'
                retriever+=1
    except ValueError:
        print('Integer required')
        
    while total==120:
        print('')
        print('Would you like to enter another set of data?')
        option=input("Enter "'y'" for yes or "'q'" to quit and view results:")
        option=option.lower()
        if option=='y' or option=='q':
            progress_list=[progression,Pass,defer,fail]
            dict_main[student_id]= progress_list
            outcome+=1
            n=0
            print('')
            break
        else:
            print("Invalid Option")
                
main()

print('------------------------------------------')
print('Histogram')
print('Progress ' ,progress,':','*'*progress)
print('Trailer  ',trailer,':','*'*trailer)
print('Retriever',retriever,':','*'*retriever)
print('Excluded ',exclude,':','*'*exclude)
print('')
print(outcome,"outcomes in total.")
print('-------------------------------------------')
print('')
for (k,v) in dict_main.items():
    print(k,':',v[0],v[1],',',v[2],',',v[3])  





