library('ggplot2')
df <- read.csv('MCS.tsv',sep='\t')
ggplot2::ggplot(df , aes(x=family))+
  geom_histogram()

df2 <- read.csv('combifile',sep='\t')
ggplot2::ggplot(df2 , aes(x=family))+
  geom_histogram()



df3 <- read.csv('KAKs.file.txt',sep='\t',header = FALSE)
colnames(df3) <- c('a','b','ks','ka','kaks')
ggplot2::ggplot(df3 , aes(x=ks))+
  geom_histogram(bins = 50)+
  theme_bw()

ggplot2::ggplot(df3 , aes(x=ks))+
  #geom_histogram(bins = 50)+
  geom_density(lwd = 0.8, )+
 # scale_x_log10()+
  theme_bw()+
  labs(x = 'log10(ks)')

ggplot2::ggplot(df3 , aes(x=ks))+
  #geom_histogram(bins = 50)+
  geom_density(lwd = 0.8, )+
  scale_x_log10()+
  theme_bw()+
  labs(x = 'log10(ks)')

ggplot2::ggplot(df3 , aes(x=kaks))+
  #geom_histogram(bins = 50)+
  geom_density(lwd = 0.8, )+
 # scale_x_log10()+
  #labs(x = 'log10(ks)')+
  theme_bw()


