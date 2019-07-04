
import time
import webbrowser

total_breaks =5#take a break 5 times
break_count =0
print ("this program started on "+time.ctime())
while(break_count < total_breaks):
        time.sleep(2*60*60) #wait 2 hours to open the url in browser
        webbrowser.open('https://www.youtube.com/watch?v=_7Irvqnn5QE')#open the url
        break_count = break_count+1

