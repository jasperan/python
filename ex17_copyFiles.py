from sys import argv
from os.path import exists

script, sourceFile, targetFile = argv

print 'Script name %s ' % script
print 'Source file %s ' % sourceFile
print 'Target file %s ' % targetFile

sourceFileDescriptor = open(sourceFile, 'r')
targetFileDescriptor = open(targetFile, 'w')

print 'Opened both files. Going to copy from %s to %s.' % (sourceFile, targetFile)


print 'Reading contents from file 1: '
sourceFileText = sourceFileDescriptor.read()

print 'Overwriting contents. Press Enter to Continue, ^C to cancel.'
raw_input('')

if(exists(targetFile)):
	targetFileDescriptor.write(sourceFileText)
else:
	print 'File doesn"t" exist'

sourceFileDescriptor.close()
targetFileDescriptor.close()