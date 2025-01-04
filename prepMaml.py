import time
import pandas as pd
import os
from nltk.tokenize import sent_tokenize

curr_dir=os.getcwd()+"\\Downloads"
project_root=os.path.dirname(curr_dir)

art_dir=os.path.join(project_root,'bbc-data','News Articles')
sum_dir=os.path.join(project_root,'bbc-data','Summaries')

art_sub_dir=os.listdir(art_dir)
sum_sub_dir=os.listdir(sum_dir)

train_percent=0.79
test_percent=0.21

TOTAL=2225

def prepare():
 headers={'headline':[],
          'article':[],
          'summary':[]}
 
 for topic in art_sub_dir:
  df_train_ind=0
  df_test_ind=0

  train=pd.DataFrame(headers)
  test=pd.DataFrame(headers)

  out_train_file=os.path.join(project_root,'generated-data2','bbc_'+topic+'_train.csv')
  out_test_file=os.path.join(project_root,'generated-data2','bbc_'+topic+'_test.csv')

  art_file_dir=os.path.join(art_dir,topic)
  sum_file_dir=os.path.join(sum_dir,topic)

  art_files=os.listdir(art_file_dir)
  sum_files=os.listdir(sum_file_dir)

  train_num=int(train_percent*len(art_files))
  
  for i in range(len(art_files)):
   try:
    art_contents=open(art_file_dir+'\\'+art_files[i],"r",encoding='utf-8').read().split('\n')
    sum_contents=open(sum_file_dir+'\\'+sum_files[i],"r",encoding='utf-8').readlines()
    head_content=art_contents[0]
    art_content=" ".join(sent_tokenize(" ".join(art_contents[2:])))
    sum_content=" ".join(sum_contents)

    if i<train_num:
     train.at[df_train_ind,'headline']=head_content
     train.at[df_train_ind,'article']=art_content
     train.at[df_train_ind,'summary']=sum_content
     df_train_ind+=1
    else: 
     test.at[df_test_ind,'headline']=head_content
     test.at[df_test_ind,'article']=art_content
     test.at[df_test_ind,'summary']=sum_content
     df_test_ind+=1

   except UnicodeDecodeError:
    continue

  train.to_csv(out_train_file,index=False)
  test.to_csv(out_test_file,index=False)

if __name__ == '__main__':
 start=time.time()
 prepare()
 end=time.time()
 print("Time taken: "+str(end-start))
