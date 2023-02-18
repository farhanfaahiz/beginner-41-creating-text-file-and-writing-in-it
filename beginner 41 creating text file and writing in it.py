from re import I


fh = open('demo.txt', 'a')

for i in range(10):
    fh.write('God is great\nThere is none like unto him\n')
fh.close()

#new example

fh = open('C:\\New folder\\demo.txt', 'a')

try:
    for i in range(10):
        fh.write('This is line no %d\n' %i)
finally:
    fh.close()
    
#with open('demo.txt', 'a') as fh:
#    for i in range(10):
#        fh.write('my name if farhan-faahiz\n')