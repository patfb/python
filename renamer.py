import os

targetDir = input(
    "Enter full path of target directory that contains files to be renamed:")

print("Target directory:", targetDir)

originalFiles = os.listdir(targetDir)

print("Files in target directory:", originalFiles)

baseName = input("Enter base TV show name:")
seasonNumber = int(input("Enter season number:"))
episodeNumber = int(input("Enter starting episode number:"))

files = {}
for originalFile in originalFiles:
    extension = os.path.splitext(originalFile)[1]
    files[originalFile] = f"{baseName} S{seasonNumber:02d}E{episodeNumber:02d}{extension}"
    episodeNumber += 1

print("Files will be renamed like this")
for key in files:
    print(f"{key} -> {files[key]}")


shouldProceed = input("Proceed with rename Y/N?:")

if shouldProceed == "y" or shouldProceed == "Y":
    print("Renaming!")
    for key in files:
        original = f"{targetDir}\\{key}"
        renamed = f"{targetDir}\\{files[key]}"
        print(original, "->", renamed)
        os.rename(original, renamed)
else:
    print("Closing")
