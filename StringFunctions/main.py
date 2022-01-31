# Input file
inputFile = open("config.xml", "rt")

# Output file to write the results to
outputFile = open("config_out.xml", "wt")

# For each line in the input file
for line in inputFile:
    # Read and replace the string and write to output file
    outputFile.write(line.replace('<stringToReplace>','<stringToReplaceWith>'))

# Close input and output file
inputFile.close()
outputFile.close()