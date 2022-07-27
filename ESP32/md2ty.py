import re
import os
import time



g = os.walk(".")
i=3
for path,dir_list,file_list in g:  
    for file_name in file_list:
    	if os.path.splitext(file_name)[1] == ".md":
    		f = open(file_name,'r', encoding='utf-8')
    		#print(file_name)    		
    		for s in f.readlines():
    			if "title:" in s:
    				title=s.lstrip("title:").strip()
    				#print(title)
    			if "date:" in s:
    				t=s.lstrip("date:").strip()
    				try:
    					timeArray = time.strptime(t, "%Y-%m-%d")
    				except:
    					timeArray = time.strptime(t, "%Y/%m/%d")
    				timestamp = int(time.mktime(timeArray))
    			else:
    				timestamp=1550563724
    			#s.replace("\'", "\\\'")
    		f.close()
    		f = open(file_name,'r', encoding='utf-8')
    		content = f.read().replace("\'", "\\\'")
    		sql="("+str(i)+", '"+title+"', '"+file_name.rstrip(".md")+"', "+str(timestamp)+", "+str(timestamp)+", '<!--markdown-->"+content+"', 0, 1, NULL, 'post', 'publish', NULL, 0, '1', '1', '1', 0),"
    		i=i+1
    		print(sql)
