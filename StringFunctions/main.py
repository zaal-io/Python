# String to replace
srcStrings = ['6443d736deaae25ef80d2a8d5e40f883c170ef90','026257f2d8404910336c8de067520360065de417','f0d6c69d4a3d86d9ae2caa292831521a69a5abea','aad4086d9543306953a24c2b3d6ce49e6e17b41e','5dcecac63c3f34f6f88af217834a6603453fb31f']
# srcString1 = '6443d736deaae25ef80d2a8d5e40f883c170ef90'
# srcString2 = '026257f2d8404910336c8de067520360065de417'
# srcString3 = 'f0d6c69d4a3d86d9ae2caa292831521a69a5abea'
# srcString4 = 'aad4086d9543306953a24c2b3d6ce49e6e17b41e'
# srcString5 = '5dcecac63c3f34f6f88af217834a6603453fb31f'

# String to replace with
dstString = 'ea9100d4159a98538dbbd24fa27b51bf229bea6c'

# certificateThumbTranslation = {srcString1: dstString, srcString2: dstString, srcString3: dstString, srcString4: dstString, srcString5: dstString}

# Input file
inputFile = open(".\StringFunctions\exportNPS.xml", "rt")

# Output file to write the results to
outputFile = open(".\StringFunctions\exportNPS_out.xml", "wt")

# For each line in the input file
for line in inputFile:
 
 for srcString in srcStrings:
  line = line.replace(srcString,dstString)
 
 outputFile.write(line)
 # Read and replace the string and write to output file
 # outputFile.write(line.replace(str(srcStrings),dstString))
 # outputFile.write(line.replace(srcString1,dstString).replace(srcString2,dstString).replace(srcString3,dstString).replace(srcString4,dstString).replace(srcString5,dstString))
 # outputFile.write(line.translate(str.maketrans(certificateThumbTranslation)))

# Close input and output file
inputFile.close()
outputFile.close()


