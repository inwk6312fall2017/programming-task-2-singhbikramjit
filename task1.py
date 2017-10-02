def crime():
 # myfile=open("Crime.cvs",'r')
  with open("Crime.csv", 'r') as myfile:
   myfile.read()
   print(myfile)
  
  
  for r in myfile:
    crime_type =r[8]
    crime_id = r[7]
    dict={crime_id: crime_type}
    print(dict)
   #for words in line:
    #  print(word)

crime()
