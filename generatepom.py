from pathlib import Path



def createNewPom(filename):
	split = str(filename).split("/")
	group = split[0]
	artifact = split[1]
	version = split[2]
	with open(filename, "w") as pomFile:
		pomFile.write('<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">\n')
		pomFile.write("<modelVersion>4.0.0</modelVersion>\n")
		pomFile.write("<groupId>my.{}</groupId>\n".format(group))
		pomFile.write("<artifactId>my.{}</artifactId>\n".format(artifact))
		pomFile.write("<version>my.{}</version>\n".format(version))
		pomFile.write("\n")
		pomFile.write("<dependencies>\n")
		pomFile.write("<dependency>\n")
		pomFile.write("<groupId>{}</groupId>\n".format(group))
		pomFile.write("<artifactId>{}</artifactId>\n".format(artifact))
		pomFile.write("<version>{}</version>\n".format(version))	
		pomFile.write("</dependency>\n")
		pomFile.write("</dependencies>\n")
		pomFile.write("</project>\n")




if __name__== "__main__":
	for file in Path('.').rglob('pom.xml'):
		print(file)
		createNewPom(file)