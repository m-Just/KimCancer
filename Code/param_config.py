import os
import numpy as np

############
## Config ##
############
class ParamConfig:
	def __init__(self,
				feat_folder,
				pattern_folder,
				basic_tfidf_ngram_range=(1,3),
				basic_tfidf_vocabulary_type="common",
				cooccurrence_tfidf_ngram_range=(1,1),
				cooccurrence_word_exclude_stopword=False,
				stemmer_type="snowball",
				count_feat_transform=np.sqrt):

		self.n_classes = 9

		## CV params
		self.n_runs = 3
		self.n_folds = 3
		self.stratified_label = "Gene"

		## path
		self.data_folder = "../../Data"
		self.feat_folder = feat_folder # directory to store processed feature data
		self.pattern_folder = pattern_folder # directory to store extracted subtext from text using specific patterns
		self.original_train_text_path = "%s/training_text" % self.data_folder
		self.original_train_variant_path = "%s/training_variants" % self.data_folder
		self.original_test_text_path = "%s/test_text" % self.data_folder
		self.original_test_variant_path = "%s/test_variants" % self.data_folder
		self.processed_train_data_path = "%s/train.processed.p" % self.feat_folder
		self.processed_test_data_path = "%s/test.processed.p" % self.feat_folder

		## nlp related
		self.basic_tfidf_ngram_range = basic_tfidf_ngram_range
		self.basic_tfidf_vocabulary_type = basic_tfidf_vocabulary_type
		self.cooccurrence_tfidf_ngram_range = cooccurrence_tfidf_ngram_range
		self.cooccurrence_word_exclude_stopword = cooccurrence_word_exclude_stopword
		self.stemmer_type = stemmer_type

		## transform for count features
		self.count_feat_transform = count_feat_transform

		## create feat folder
		if not os.path.exists(self.feat_folder):
			os.makedirs(self.feat_folder)

		## create folder for the training and testing feat
		if not os.path.exists("%s/All" % self.feat_folder):
			os.makedirs("%s/All" % self.feat_folder)

		## create pattern folder
		if not os.path.exists(self.pattern_folder):
			os.makedirs(self.pattern_folder)

		## create folder for each run and fold
		for run in range(1, self.n_runs+1):
			for fold in range(1, self.n_folds+1):
				path = "%s/Run%d/Fold%d" % (self.feat_folder, run, fold)
				if not os.path.exists(path):
					os.makedirs(path)

## initialize a param config
config = ParamConfig(feat_folder="../../Feat/dev",
					pattern_folder="../../Pattern/dev",
					stemmer_type="porter",
					cooccurrence_word_exclude_stopword=False)