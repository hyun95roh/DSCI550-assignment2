
import tika.tika
import os
from tika import parser
home = os.getenv('HOME')
#print(home) 

tika.tika.TikaServerClasspath = home + '/git/geotopicparser-utils/mime:'+home+'/git/geotopicparser-utils/models/polar'
parsed = parser.from_file(home + '/git/geotopicparser-utils/geotopics/polar.geot')
print(parsed["metadata"])