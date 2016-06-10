import re

def aaa():

    a=open('kata_kata.txt','w')
    
    filter_konten = []
    kata = raw_input("Input Jumlah Kata yang akan difilter: ")
    print 'Silahkan Input Kata Yang Akan difilter: '
    for i in range(int(kata)):
        n = raw_input("Kata Filter Ke-"+str(i+1)+" : ")
        aa = filter_konten.append(str(a.write(n+"\n")))
        
    #b = open('kata_kata.txt','r').read()
       
    a.close()
    with open('kata_kata.txt', 'r') as pl:
        p = pl.read()
    
    #return p
    return map(lambda x: x.lower(), p.split('\n')[ :-1])
    
def aa():
    '''
    a=open('kata_kata.txt','w')
    
    filter_konten = []
    kata = raw_input("Input Jumlah Kata yang akan dimatch : ")
    print 'Silahkan Input Kata Yang Akan dimatch: '
    for i in range(int(kata)):
        n = raw_input("Kata Filter Ke-"+str(i+1)+" : ")
        aa = filter_konten.append(str(a.write(n+"\n")))
        
    #b = open('kata_kata.txt','r').read()
       
    a.close()'''
    with open('kata_kata.txt', 'r') as pl:
        p = pl.read()
    
    return p
    
def b():
    with open('kata_kata.txt', 'r') as pl:
        p = pl.read()
    return map(lambda x: x.lower(), p.split('\n')[ :-1])

def predefine():
    with open('predefine_words.txt', 'r') as pl:
        p = pl.read()
    return p.lower()
    
if __name__ == '__main__':
    ###################
    #words = str(aa())
    words = aa()
    #ww = b()
    #print ww
    ###################
    print words.split('\n')
    ###############
    p = predefine()
    print p
    ##############
    
    #line = raw_input("Input Kata yang akan dimatch : ")
    try:
        for val in words.split('\n'):
            #print val
            if re.search(val.lower(), p.lower()):
                print '\nFound '+ val+ ' in : ['+p+']'
            else:
                print '\nNoo'
            #print val  
    except:
        print 'Err'
    
