import re
import glob

patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y'
}

def utf8_to_ascii(text):
	if text is None:
		return ''
	output = text
	for regex, replace in patterns.items():
		output = re.sub(regex, replace, output)
		# deal with upper case
		output = re.sub(regex.upper(), replace.upper(), output)
	return output

folders = glob.glob('data/*.txt')

for f in folders:
	data = open(str(f), encoding="utf8").read()
	data = utf8_to_ascii(data)
	write_path = f.replace("data\\", "")
	file = open('processed/' + str(write_path), 'w',encoding="utf8")
	file.write(data)
	file.close()