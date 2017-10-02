def crime():
 # myfile=open("Crime.cvs",'r')
  with open("Crime.cvs", 'r') as myfile:
   myfile.read()
  for line in myfile:
    for words in line:
      print(words)


crime()
