if [[ ! -d glove ]]; then
	mkdir glove
fi

cd glove
wget "https://nlp.stanford.edu/data/wordvecs/glove.42B.300d.zip"
unzip "glove.42B.300d.zip"
