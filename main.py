print('welcome to data analyzer and transformer program')

print('1. input data')
print('2. display data summary (built in function)')
print('3. calculate factorial')
print('4. filter data (using lambda )')
print('5. sort data')
print('6. display statistics (return multiple values)')
print('7. exit')

def get_1d():
        return list(map(int,input('enter 1D data separated by commas: ').split(',')))
def get_2d():
    matrix=[]
    rows=int(input('enter number of rows: '))
    for i in range(rows):
        matrix.append(list(map(int,input(f'enter {i+1} row data separated by commas: ').split(','))))

    return matrix

def flatten(number):
    if len(number)>0 and isinstance(number[0], list):
        m=[x for row in number for x in row]
    else:
        m=number
    print('total elements: ', len(m))
    print('minimum: ', min(m))
    print('maximum: ', max(m))
    print('sum: ', sum(m))
    print('average: ', sum(m)/len(m))


def fact(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return n*fact(n-1)
    


def filt(number,threshold):
    if len(number)>0 and isinstance(number[0], list):
        m=[x for row in number for x in row]
    else:
        m=number

    return list(filter(lambda x:x>threshold,m))
    
    
            
        


def srt(number):
    if len(number)>0 and isinstance(number[0], list):
        m=[x for row in number for x in row]
    else:
        m=number

    choice=int(input('enter 1 for ascending order, 2 for descending order: '))
    if choice==1:
        return sorted(m)
    else:
        return sorted(m, reverse=True)
    


def stats(number):
    if len(number)>0 and isinstance(number[0], list):
        m=[x for row in number for x in row]
    else:
        m=number
    return min(m), max(m), sum(m), sum(m)/len(m)   

while True:
    choice=int(input('enter your choice: '))

    if choice == 1:
        print('press 1 for 1D data, 2 for 2D data')
        choice=int(input('enter your choice: '))
        if choice==1:
            number=get_1d()
        elif choice==2:
            number=get_2d()
            for i in number:
                for element in i:
                    print(element, end=' ')
                print()
        
    elif choice == 2:

        flatten(number)
    elif choice==3:
        num=int(input('enter a number to calculate its factorial: '))
        res=fact(num)
        print('factorial of', num, 'is', res)
    elif choice == 4:
        while True:
        
            threshold=int(input('enter the threshold value: '))
            if len(number)>0 and isinstance(number[0], list):
                m=[x for row in number for x in row]
            else:
                m=number
            if threshold in m:
                filtered_data=filt(number,threshold)
                print('filtered data: ', filtered_data)
                break
            else:
                print('invalid threshold')
    elif choice == 5:
        print(srt(number))
    elif choice == 6:
        min,max,sum,avg=stats(number)
        print('minimum: ', min)
        print('maximum: ', max)
        print('sum: ', sum)
        print('average: ', avg)
    elif choice==7:
        print('exiting...')
        break
    else:
        print('invalid choice , try again and input choice between 1-7')




    

    
    