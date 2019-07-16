import argparse
import numpy as np
import torch
import pickle
import os

import LSTM11r_datagen as datagen ## CHANGE with VERSION ##
import LSTM11r_functions as functions ## CHANGE with VERSION ##
import LSTM11r_models as models ## CHANGE with VERSION ##

'''Settings'''
parser=argparse.ArgumentParser()

parser.add_argument('--runname',type=str,required=True,help='identifier used to name all output files') 
parser.add_argument('--model',type=str,required=True,help='model name')

parser.add_argument('--genrunname',type=str,default='DEFAULT') ## CHANGE with VERSION ##
parser.add_argument('--cuda',type=int,default=0)

parser.add_argument('--budget',type=int,default=10) #HP search budget
parser.add_argument('--epochs',type=int,default=10)
parser.add_argument('--T',type=int,default=48)
parser.add_argument('--d',type=int,default=76)
parser.add_argument('--num_classes',type=int,default=2)
parser.add_argument('--N',type=int,default=0)
parser.add_argument('--share_num',type=int,default=2,help="share number for moo and mow")

parser.add_argument('--hidden_size',type=int,default=20)
parser.add_argument('--hyp_hidden_size',type=int,default=20)
parser.add_argument('--batch_size',type=int,default=8)
parser.add_argument('--shiftLSTMk',type=int,default=0)
parser.add_argument('--realstart',type=bool,default=False)
parser.add_argument('--te_size',type=int,default=24) #must be even
parser.add_argument('--te_base',type=float,default=10000.0)

parser.add_argument('--savedir',type=str,default='/save')
parser.add_argument('--datadir',type=str,default='/data1/jeeheh/mimic/mimic3models/in_hospital_mortality/joh data extraction/')


args=parser.parse_args()
args=vars(args)
if args['genrunname']=='DEFAULT': args['genrunname']=args['runname']

'''Cuda'''
args['use_cuda'] = torch.cuda.is_available()
if args['use_cuda']:
    torch.cuda.set_device(args['cuda'])
    print('Run on cuda: {}'.format(torch.cuda.current_device()))

    
'''Test Models on Datasets'''
if args['model']=='LSTM':
    functions.real_data_search3(args, datagen.IHM_data,models.LSTM)
if 'shiftLSTM' in args['model']: 
    functions.real_data_search3(args, datagen.IHM_data,models.nidLSTM)
if args['model']=='LSTMT': 
    functions.real_data_search3(args, datagen.IHM_data,models.LSTMT)
if args['model']=='HyperLSTM': 
    functions.real_data_search3(args, datagen.IHM_data,models.HyperLSTM)
if args['model']=='LSTMTE': 
    functions.real_data_search3(args, datagen.IHM_data,models.LSTMTE)
if args['model']=='mow': 
    functions.real_data_search3(args, datagen.IHM_data,models.mixLSTM)

    
