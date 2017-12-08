import os
import SO_CALC
import hello
from pycorenlp import StanfordCoreNLP


class SOCAL:
	def so_cal_run(self, sentence):
		rows = self.pos_tagging(sentence)
		out = SO_CALC.run(str(rows[0]))
		return out


	def pos_tagging(self, text_string):
	    nlp = StanfordCoreNLP('http://localhost:9000')
	    standford_annotators = 'tokenize,ssplit,pos'

	    processed_json = nlp.annotate(text_string, properties={
	                   'annotators': standford_annotators,
	                   'outputFormat': 'json'
	               })


	    rows = []
	    for sent in processed_json['sentences']:
	        parsed_sent = " ".join([t['originalText'] + "/" + t['pos'] for t in sent['tokens']])
	        rows.append(parsed_sent)

	    return rows

	'''
    def main():
	    config_file = 'config_files/en_SO_Calc.ini'
	    cutoff = 0.0
	    
	    if os.path.isfile(input_path):  # 1 single file
	        print("Processing " + os.path.basename(input_path) + "...")
	        cmd = "python SO_Calc.py -i \"" + input_path + "\" -bo \"" + basicout_path + "\" -ro \"" + richout_path + "\" -c \"" + config_file + "\""
	        os.system(cmd)
	    elif os.path.isdir(input_path):   # an input folder, only reads files
	        for f_name in os.listdir(input_path):
	            print("Processing " + f_name + "...")
	            file_path = os.path.abspath(input_path) + "/" + f_name
	            if os.path.isfile(file_path) == False: continue
	            cmd = "python SO_Calc.py -i \"" + file_path + "\" -bo \"" + basicout_path + "\" -ro \"" + richout_path + "\" -c \"" + config_file + "\""
	            os.system(cmd)

'''
	    





