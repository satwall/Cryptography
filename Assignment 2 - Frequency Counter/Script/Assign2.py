import pandas as pd


Book1 = input('Enter the .txt file location: ')
#Book2 = input('Enter the second .txt file location: ')

freqs = {}
with open(Book1, encoding="utf8") as f:
    for line in f:
        for char in line:
            if char in freqs:
                freqs[char] += 1
            else:
                freqs[char] = 1

#print(freqs)

#freqs2 = {}
#with open(Book2, encoding="utf8") as f2:
 #   for line2 in f2:
  #      for char2 in line2:
   #         if char2 in freqs2:
    #            freqs2[char2] += 1
     #       else:
      #          freqs2[char2] = 1

#print(freqs2)




#test = {'Book 1 Output':[freqs], 'Book 2 Output':[freqs2] }

#df = pd.DataFrame(test, columns=['Letter','Book 1 Output','Letter','Book 2 Output'])

#df.to_csv(r'book_export.csv', sep=',', index=False)

df1=(pd.DataFrame.from_dict(freqs, orient='index',columns=['Book 1 Frequency']).rename_axis('Letter'))

#df2=(pd.DataFrame.from_dict(freqs2, orient='index',columns=['Book 2 Output']).rename_axis('Letter'))


#print(df)

#print(dd)

df1.to_csv(r'BookOutput.csv',sep=',')

#df2.to_csv(r'SecondBookOutput.csv',sep=',')
