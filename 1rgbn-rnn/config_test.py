
## Setting
Setting = {}
K = [100, 80, 50]
H = [100, 80, 50]
DPGDS_Layer  = 3
sent_J = 8
Batch_Size = 8
tao0 = 1
gamma0  = 100
eta0    = 0.1
epilson0= 0.1
c       = 1
real_min = 2.2e-20
tm_epoch_size = 2
epoch_size=3 #n_epoch

#  online parameter
Setting['Iterall'] = epoch_size * 110000/Batch_Size
Setting['tao0FR'] = 0;
Setting['kappa0FR'] = 0.9
Setting['tao0'] = 20;
Setting['kappa0'] = 0.7
Setting['epsi0'] = 1;
Setting['FurCollapse'] = 1  # 1 or 0
Setting['flag'] = 0

## Supara
Supara = {}
Supara['tao0'] = 1
Supara['gamma0'] = 100
Supara['eta0'] = 0.1
Supara['epilson0'] = 0.1
Supara['c'] = 1


#preprocessing options
vocab_minfreq=10 #minimum vocab frequency to filter
vocab_maxfreq=0.001 #proportion of most-frequent vocab to filter
stopwords="D:/PGBN_LSTM/Data/stoplists/en.txt"
tm_sent_len=3
lm_sent_len=30
doc_len=300
num_fiter1 = 100
num_fiter2 = 100
num_fiter3 = 100
#training options
seed=1
rnn_layer_size=2 #n_layer
rnn_hidden_size1=600 #n_hidden
rnn_hidden_size2=512 #n_hidden
rnn_hidden_size3=256 #n_hidden

topic_number=100 #k
word_embedding_size=300 #e; setting ignored if word_embeding_model is provided
word_embedding_model="D:/PGBN_LSTM/Data/word-embedding/GoogleNews-vectors-negative300.bin" #pre-trained word embedding (gensim format); None is no pre-trained model
word_embedding_update=True #update word embedding for topic model
theta_size1=K[0]
theta_size2=K[1]
theta_size3=K[2]
learning_rate=0.001 #l
learning_rate_tm=0.0005 #l

lm_keep_prob= 0.6 #p_2
max_grad_norm = 5
rnn_bias = 1
#misc
save_model=True #save model to output_dir/output_prefix
verbose=True #print progress

#input/output
dataname = "apnews" #  imdb apnews bnc

data_path = 'D:/PGBN_LSTM/Data/'
train_corpus=data_path + dataname + "/train.txt"
valid_corpus=data_path + dataname + "/valid.txt"
test_corpus=data_path + dataname + "/test.txt"
output_dir="output-DPGDS-LSTM-100-80-50"

output_prefix=dataname+"-3-model"
output_path = dataname+"-3-res"