#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
if not 'Informer2020' in sys.path:
    sys.path += ['Informer2020']


# In[ ]:


import random
import math
from utils.tools import dotdict
from exp.exp_informer import Exp_Informer
from data.data_loader import Dataset_Custom
from torch.utils.data import DataLoader
import torch


# In[ ]:


expertTestSize = 2
noviceTestSize = 4
expertValSize = 2
noviceValSize = 4
noviceSize = 40
expertSize = 5
expertTrialsSize= 7


# In[ ]:


random.seed(27)


# In[ ]:


IPexpertTest = []
IPnoviceTest = []

IPnoviceVal = []
IPexpertVal = []

# In[ ]:


while(len(IPexpertTest)<expertTestSize):
    ran = random.randint(1,expertTrialsSize)
    if(ran in IPexpertTest):
        continue
    else:
        IPexpertTest.append(ran)

while(len(IPexpertVal)<expertValSize):
    ran = random.randint(1,expertTrialsSize)
    if(ran in IPexpertTest or ran in IPexpertVal):
        continue
    else:
        IPexpertVal.append(ran)

# In[ ]:


while(len(IPnoviceTest)<noviceTestSize):
    randomNovice = random.randint(1, noviceSize)
    if(randomNovice%2==0):
        continue
    if(randomNovice!=23 and randomNovice not in IPnoviceTest):
        IPnoviceTest.append(randomNovice)

while(len(IPnoviceVal)<noviceValSize):
    randomNovice = random.randint(1, noviceSize)
    if(randomNovice%2==0):
        continue
    if(randomNovice!=23 and randomNovice not in IPnoviceTest and randomNovice not in IPnoviceVal):
        IPnoviceVal.append(randomNovice)


# In[ ]:


random.seed(10)


# In[ ]:


OOPexpertTest = []
OOPnoviceTest = []
OOPexpertVal = []
OOPnoviceVal = []


# In[ ]:

while(len(OOPexpertTest)<expertTestSize):
    ran = random.randint(1,expertTrialsSize)
    if(ran in OOPexpertTest):
        continue
    else:
        OOPexpertTest.append(ran)

while(len(OOPexpertVal)<expertValSize):
    ran = random.randint(1,expertTrialsSize)
    if(ran in OOPexpertTest or ran in OOPexpertVal):
        continue
    else:

        OOPexpertVal.append(ran)


# In[ ]:



while(len(OOPnoviceTest)<noviceTestSize):
    randomNovice = random.randint(1, noviceSize)
    if(randomNovice%2==1):
        continue
    if(randomNovice!=28  and randomNovice not in OOPnoviceTest):
        OOPnoviceTest.append(randomNovice)

while(len(OOPnoviceVal)<noviceValSize):
    randomNovice = random.randint(1, noviceSize)
    if(randomNovice%2==1):
        continue
    if(randomNovice!=28 and randomNovice not in OOPnoviceTest and randomNovice not in OOPnoviceVal):
        OOPnoviceVal.append(randomNovice)


# In[ ]:


print("IP Novices T: " + str(IPnoviceTest))
print("IP Experts T: " + str(IPexpertTest))
print("IP Novices V: " + str(IPnoviceVal))
print("IP Experts V: " + str(IPexpertVal))



# In[ ]:


print("OOP Novices T: " + str(OOPnoviceTest))
print("OOP Experts T: " + str(OOPexpertTest))
print("OOP Novices V: " + str(OOPnoviceVal))
print("OOP Experts V: " + str(OOPexpertVal))


# In[ ]:

IPexpertValFiles = []
IPnoviceValFiles = []
OOPnoviceValFiles = []
OOPexpertValFiles = []

IPexpertTestFiles = []
IPnoviceTestFiles = []
OOPnoviceTestFiles = []
OOPexpertTestFiles = []

IPexpertTrainFiles = []
IPnoviceTrainFiles = []
OOPnoviceTrainFiles = []
OOPexpertTrainFiles = []


# In[ ]:


for i in range(1,noviceSize+1):
    if(i==23 or i==28):
        continue
    if(i%2==1):
        if(i in IPnoviceTest):
            IPnoviceTestFiles.append("N" + str(i))
        elif(i in IPnoviceVal):
            IPnoviceValFiles.append("N" + str(i))
        else:
            IPnoviceTrainFiles.append("N" + str(i))
    else:
        if(i in OOPnoviceTest):
            OOPnoviceTestFiles.append("N" + str(i))
        elif(i in OOPnoviceVal):
            OOPnoviceValFiles.append("N" + str(i))
        else:
            OOPnoviceTrainFiles.append("N" + str(i))


# In[ ]:


for i in range(1,expertTrialsSize+1):
    if(i>4):
        fileName = "E" + str(i-2) + "_" + str(1)
    else:
        fileName = "E" + str(math.ceil(i/2)) + "_" + str(i%2+1)

    if(i in IPexpertTest):
        IPexpertTestFiles.append(fileName)
    elif(i in IPexpertVal):
        IPexpertValFiles.append(fileName)
    else:
        IPexpertTrainFiles.append(fileName)

    if(i in OOPexpertTest):
        OOPexpertTestFiles.append(fileName)
    elif(i in OOPexpertVal):
        OOPexpertValFiles.append(fileName)
    else:
        OOPexpertTrainFiles.append(fileName)


# In[ ]:


#print(IPnoviceTest)


# In[ ]:


print("IP Novice Train" + str(IPnoviceTrainFiles))
print("IP Novice Test" + str(IPnoviceTestFiles))
print("IP Novice Val" + str(IPnoviceValFiles))


# In[ ]:


#print(IPexpertTest)


# In[ ]:


print("IP Expert Train" + str(IPexpertTrainFiles))
print("IP Expert Test" + str(IPexpertTestFiles))
print("IP Expert Val" + str(IPexpertValFiles))



# In[ ]:


#print(OOPnoviceTest)


# In[ ]:


print("OOP Novice Train" + str(OOPnoviceTrainFiles))
print("OOP Novice Test" + str(OOPnoviceTestFiles))
print("OOP Novice Val" + str(OOPnoviceValFiles))


# In[ ]:


#print(OOPexpertTest)


# In[ ]:


print("OOP Expert Train" + str(OOPexpertTrainFiles))
print("OOP Expert Test" + str(OOPexpertTestFiles))
print("OOP Expert Val" + str(OOPexpertValFiles))


# In[ ]:




args = dotdict()

args.model = 'informer' # model of experiment, options: [informer, informerstack, informerlight(TBD)]

args.data = 'IPusneedle_data' # data
args.root_path = './allData' # root path of data file
args.data_path = 'IPusneedle_data.csv' # data file
args.features = 'MS' # forecasting task, options:[M, S, MS]; M:multivariate predict multivariate, S:univariate predict univariate, MS:multivariate predict univariate
args.target = 'Skill' # target feature in S or MS task
args.freq = 'h' # freq for time features encoding, options:[s:secondly, t:minutely, h:hourly, d:daily, b:business days, w:weekly, m:monthly], you can also use more detailed freq like 15min or 3h
args.checkpoints = './informer_checkpoints' # location of model checkpoints

args.seq_len = 96 # input sequence length of Informer encoder
args.label_len = 48 # start token length of Informer decoder
args.pred_len = 24
# Informer decoder input: concat[start token series(label_len), zero padding series(pred_len)]

args.enc_in = 7 # encoder input size
args.dec_in = 7 # decoder input size
args.c_out = 7 # output size
args.factor = 5 # probsparse attn factor
args.d_model = 512 # dimension of model
args.n_heads = 8 # num of heads
args.e_layers = 2 # num of encoder layers
args.d_layers = 1 # num of decoder layers
args.d_ff = 2048 # dimension of fcn in model
args.dropout = 0.05 # dropout
args.attn = 'prob' # attention used in encoder, options:[prob, full]
args.embed = 'timeF' # time features encoding, options:[timeF, fixed, learned]
args.activation = 'gelu' # activation
args.distil = True # whether to use distilling in encoder
args.output_attention = False # whether to output attention in ecoder
args.mix = True
args.padding = 0
args.freq = 'h'

args.batch_size = 1024
args.learning_rate = 0.00001
args.loss = 'mse'
args.lradj = 'type1'
args.use_amp = False # whether to use automatic mixed precision training

args.num_workers = 0
args.itr = 1
args.train_epochs = 1
args.patience = 3
args.des = 'exp'

args.use_gpu = True if torch.cuda.is_available() else False
args.gpu = 0

args.use_multi_gpu = False
args.devices = '0,1,2,3'


# In[ ]:


# Set augments by using data name
data__parser = {
    'ETTh1':{'data':'ETTh1.csv','T':'OT','M':[7,7,7],'S':[1,1,1],'MS':[7,7,1]},
    'ETTh2':{'data':'ETTh2.csv','T':'OT','M':[7,7,7],'S':[1,1,1],'MS':[7,7,1]},
    'ETTm1':{'data':'ETTm1.csv','T':'OT','M':[7,7,7],'S':[1,1,1],'MS':[7,7,1]},
    'ETTm2':{'data':'ETTm2.csv','T':'OT','M':[7,7,7],'S':[1,1,1],'MS':[7,7,1]},
}
IPdata_train_parser = {}
IPdata_test_parser = {}
IPdata_val_parser = {}
OOPdata_train_parser = {}
OOPdata_test_parser = {}
OOPdata_val_parser = {}

for novice in IPnoviceTrainFiles:
    files = []
    for i in range(0,6):
        if(i==0):
            files.append(novice + "_" + "B.csv")
        elif(i==5):
            files.append(novice + "_" + "F.csv")
        else:
            files.append(novice + "_" + "T" + str(i)+ ".csv")
    IPdata_train_parser[novice] = {}
    IPdata_train_parser[novice]["data"]=files
    IPdata_train_parser[novice]["T"] = "Skill"
    IPdata_train_parser[novice]["M"] = [7,7,7]
    IPdata_train_parser[novice]["S"] = [1,1,1]
    IPdata_train_parser[novice]["MS"] = [13,13,1]
for novice in OOPnoviceTrainFiles:
    files = []
    for i in range(0,6):
        if(i==0):
            files.append(novice + "_" + "B.csv")
        elif(i==5):
            files.append(novice + "_" + "F.csv")
        else:
            files.append(novice + "_" + "T" + str(i)+ ".csv")
    OOPdata_train_parser[novice] = {}
    OOPdata_train_parser[novice]["data"]=files
    OOPdata_train_parser[novice]["T"] = "Skill"
    OOPdata_train_parser[novice]["M"] = [7,7,7]
    OOPdata_train_parser[novice]["S"] = [1,1,1]
    OOPdata_train_parser[novice]["MS"] = [13,13,1]

for novice in IPnoviceTestFiles:
    files = []
    for i in range(0,6):
        if(i==0):
            files.append(novice + "_" + "B.csv")
        elif(i==5):
            files.append(novice + "_" + "F.csv")
        else:
            files.append(novice + "_" + "T" + str(i)+ ".csv")
    IPdata_test_parser[novice] = {}
    IPdata_test_parser[novice]["data"]=files
    IPdata_test_parser[novice]["T"] = "Skill"
    IPdata_test_parser[novice]["M"] = [7,7,7]
    IPdata_test_parser[novice]["S"] = [1,1,1]
    IPdata_test_parser[novice]["MS"] = [13,13,1]

for novice in OOPnoviceTestFiles:
    files = []
    for i in range(0,6):
        if(i==0):
            files.append(novice + "_" + "B.csv")
        elif(i==5):
            files.append(novice + "_" + "F.csv")
        else:
            files.append(novice + "_" + "T" + str(i)+ ".csv")
    OOPdata_test_parser[novice] = {}
    OOPdata_test_parser[novice]["data"]=files
    OOPdata_test_parser[novice]["T"] = "Skill"
    OOPdata_test_parser[novice]["M"] = [7,7,7]
    OOPdata_test_parser[novice]["S"] = [1,1,1]
    OOPdata_test_parser[novice]["MS"] = [13,13,1]

for novice in IPnoviceValFiles:
    files = []
    for i in range(0,6):
        if(i==0):
            files.append(novice + "_" + "B.csv")
        elif(i==5):
            files.append(novice + "_" + "F.csv")
        else:
            files.append(novice + "_" + "T" + str(i)+ ".csv")
    IPdata_val_parser[novice] = {}
    IPdata_val_parser[novice]["data"]=files
    IPdata_val_parser[novice]["T"] = "Skill"
    IPdata_val_parser[novice]["M"] = [7,7,7]
    IPdata_val_parser[novice]["S"] = [1,1,1]
    IPdata_val_parser[novice]["MS"] = [13,13,1]

for novice in OOPnoviceValFiles:
    files = []
    for i in range(0,6):
        if(i==0):
            files.append(novice + "_" + "B.csv")
        elif(i==5):
            files.append(novice + "_" + "F.csv")
        else:
            files.append(novice + "_" + "T" + str(i)+ ".csv")
    OOPdata_val_parser[novice] = {}
    OOPdata_val_parser[novice]["data"]=files
    OOPdata_val_parser[novice]["T"] = "Skill"
    OOPdata_val_parser[novice]["M"] = [7,7,7]
    OOPdata_val_parser[novice]["S"] = [1,1,1]
    OOPdata_val_parser[novice]["MS"] = [13,13,1]


# In[ ]:


for expert in IPexpertTrainFiles:
    IPdata_train_parser[expert] = {}
    IPdata_train_parser[expert]["data"]=[expert + ".csv"]
    IPdata_train_parser[expert]["T"] = "Skill"
    IPdata_train_parser[expert]["M"] = [7,7,7]
    IPdata_train_parser[expert]["S"] = [1,1,1]
    IPdata_train_parser[expert]["MS"] = [13,13,1]

for expert in IPexpertTestFiles:
    IPdata_test_parser[expert] = {}
    IPdata_test_parser[expert]["data"]=[expert + ".csv"]
    IPdata_test_parser[expert]["T"] = "Skill"
    IPdata_test_parser[expert]["M"] = [7,7,7]
    IPdata_test_parser[expert]["S"] = [1,1,1]
    IPdata_test_parser[expert]["MS"] = [13,13,1]

for expert in IPexpertValFiles:
    IPdata_val_parser[expert] = {}
    IPdata_val_parser[expert]["data"]=[expert + ".csv"]
    IPdata_val_parser[expert]["T"] = "Skill"
    IPdata_val_parser[expert]["M"] = [7,7,7]
    IPdata_val_parser[expert]["S"] = [1,1,1]
    IPdata_val_parser[expert]["MS"] = [13,13,1]


for expert in OOPexpertTrainFiles:
    OOPdata_train_parser[expert] = {}
    OOPdata_train_parser[expert]["data"]=[expert + ".csv"]
    OOPdata_train_parser[expert]["T"] = "Skill"
    OOPdata_train_parser[expert]["M"] = [7,7,7]
    OOPdata_train_parser[expert]["S"] = [1,1,1]
    OOPdata_train_parser[expert]["MS"] = [13,13,1]
for expert in OOPexpertTestFiles:
    OOPdata_test_parser[expert] = {}
    OOPdata_test_parser[expert]["data"]=[expert + ".csv"]
    OOPdata_test_parser[expert]["T"] = "Skill"
    OOPdata_test_parser[expert]["M"] = [7,7,7]
    OOPdata_test_parser[expert]["S"] = [1,1,1]
    OOPdata_test_parser[expert]["MS"] = [13,13,1]
for expert in OOPexpertValFiles:
    OOPdata_val_parser[expert] = {}
    OOPdata_val_parser[expert]["data"]=[expert + ".csv"]
    OOPdata_val_parser[expert]["T"] = "Skill"
    OOPdata_val_parser[expert]["M"] = [7,7,7]
    OOPdata_val_parser[expert]["S"] = [1,1,1]
    OOPdata_val_parser[expert]["MS"] = [13,13,1]


# In[ ]:


print("IP val")
print(IPdata_val_parser)


# In[ ]:


print("IP test")
print(IPdata_test_parser)


# In[ ]:



print("OOP val")
print(OOPdata_val_parser)


# In[ ]:




print("OOP test")
print(OOPdata_test_parser)


# In[ ]:





# In[ ]:


Exp = Exp_Informer
args.detail_freq = args.freq
args.freq = args.freq[-1:]
#i=0
#print(args.root_path)
#args.root_path = args.root_path + "/IP/"
#print(args.root_path)
originPath = args.root_path
origin_checkpoint_path = args.checkpoints



for participant in IPdata_val_parser:
    args.checkpoints = origin_checkpoint_path + "/" + "IP"
    args.root_path = originPath + "/IP/"
    #print(args.root_path)
    args.data = "custom"
    data_info = IPdata_val_parser[participant]
    args.target = data_info['T']
    args.enc_in, args.dec_in, args.c_out = data_info[args.features]
    for i in range(len(data_info['data'])):
        args.data_path = data_info['data'][i]
        print(args.data_path)
        print(args.root_path)
    #args.data_path = data_info['data']

        setting = '{}_{}_ft{}_sl{}_ll{}_pl{}_dm{}_nh{}_el{}_dl{}_df{}_at{}_fc{}_eb{}_dt{}_mx{}_{}_{}'.format(args.model, args.data, args.features,
                    args.seq_len, args.label_len, args.pred_len,
                    args.d_model, args.n_heads, args.e_layers, args.d_layers, args.d_ff, args.attn, args.factor, args.embed, args.distil, args.mix, args.des, 1)

        # set experiments

        exp = Exp(args)
        # train
        print('>>>>>>>start validating IP: {}>>>>>>>>>>>>>>>>>>>>>>>>>>'.format(setting))
        print(exp.validate(setting))
        print("done validating")

       # args.root_path = originPath

Exp = Exp_Informer
args.detail_freq = args.freq
args.freq = args.freq[-1:]
#i=0
#print(args.root_path)
#args.root_path = args.root_path + "/IP/"
#print(args.root_path)
args.root_path = originPath
origin_checkpoint_path = args.checkpoints


for participant in OOPdata_val_parser:
    args.root_path = originPath + "/OOP/"
    args.checkpoints = origin_checkpoint_path + "/" + "OOP"
    #print(args.root_path)
    args.data = "custom"
    data_info = OOPdata_val_parser[participant]
    args.target = data_info['T']
    args.enc_in, args.dec_in, args.c_out = data_info[args.features]
    for i in range(len(data_info['data'])):
        args.data_path = data_info['data'][i]
        print(args.data_path)
        print(args.root_path)
    #args.data_path = data_info['data']

        setting = '{}_{}_ft{}_sl{}_ll{}_pl{}_dm{}_nh{}_el{}_dl{}_df{}_at{}_fc{}_eb{}_dt{}_mx{}_{}_{}'.format(args.model, args.data, args.features,
                    args.seq_len, args.label_len, args.pred_len,
                    args.d_model, args.n_heads, args.e_layers, args.d_layers, args.d_ff, args.attn, args.factor, args.embed, args.distil, args.mix, args.des, 1)

        # set experiments
        #xprint(setting)
        exp = Exp(args)
        #print("hi")
        # train
        print('>>>>>>>start validating : {}>>>>>>>>>>>>>>>>>>>>>>>>>>'.format(setting))
        print(exp.validate(setting))
        print("done validating")

       # args.root_path = originPath




"""
for i in range
if args.data in data_parser.keys():
    data_info = data_parser[args.data]
    args.data_path = data_info['data']
    args.target = data_info['T']
    args.enc_in, args.dec_in, args.c_out = data_info[args.features]
"""


# In[ ]:


"""
args.detail_freq = args.freq
args.freq = args.freq[-1:]
"""
