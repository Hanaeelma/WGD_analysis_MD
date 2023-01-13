import argparse
import pandas as pd

def join(Blastpisoforms,seqlen,output):
 blast=pd.read_table(Blastpisoforms,sep='\t',header=None)
 columns={
         0:"query",1:"subject",2:"%ident",3:"Allength",4:"gapquery",5:"gapsubject",6:"qstart",7:"qend",
         8:"substart",9:"subend",10:"evalue",11:"bitscore"
        }
        
        
 blast.rename(columns=columns,inplace=True)

 lengths=pd.read_csv(seqlen,header=None)

 columns_len={0:"query",1:"qlen"}
 lengths.rename(columns=columns_len,inplace=True)
 df1=pd.merge(blast,lengths,on="query")
 columns_len={"query":"subject","qlen":"slen"}
 lengths.rename(columns=columns_len,inplace=True)
 df2=pd.merge(df1,lengths,on="subject")
 lengths.rename(columns=columns_len,inplace=True)
 df2.to_csv(output,index=False)
 
if __name__=='__main__':
    parser=argparse.ArgumentParser(description="join")
    parser.add_argument("-i1","--blastpisoforms",type=str,required=True)
    parser.add_argument("-i2","--seqlen",type=str,required=True)
    parser.add_argument("-o","--merged",type=str,required=True)
    args=parser.parse_args()
    join(args.blastpisoforms,args.seqlen,args.merged)

