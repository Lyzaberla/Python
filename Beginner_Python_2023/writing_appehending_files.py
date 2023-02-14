sampleFile = open("sampleFile.txt", "r")
print(sampleFile.read())
sampleFile.close()

#apphend 
sampleFile = open("sampleFile.txt", "a")
sampleFile.write("\nthis report is from my previous job")
sampleFile.close()

#write  - overwrite and creaates new files
sampleFile = open("sampleFile1.txt", "w")
sampleFile.write("this report is from my previous job")
sampleFile.close()