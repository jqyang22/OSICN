# -*- coding: utf-8 -*-

import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
# import os
# os.environ['KERAS_BACKEND']='theano'

# os.environ['THEANO_FLAGS'] = "device=gpu1"
# import theano
# theano.config.floatX = 'float32'

import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt


def featureNormalize(X,type):
    #type==1 x = (x-mean)/std(x)
    #type==2 x = (x-max(x))/(max(x)-min(x))
    if type==1:
        mu = np.mean(X,0)
        X_norm = X-mu
        sigma = np.std(X_norm,0)
        X_norm = X_norm/sigma
        return X_norm
    elif type==2:
        minX = np.min(X,0)
        maxX = np.max(X,0)
        X_norm = X-minX
        # X_norm = int(X_norm/(maxX-minX))
        X_norm = X_norm/(maxX-minX)
        return X_norm
    
def PCANorm(X,num_PC):
    mu = np.mean(X,0)
    X_norm = X-mu
    
    Sigma = np.cov(X_norm.T)
    [U, S, V] = np.linalg.svd(Sigma)   
    XPCANorm = np.dot(X_norm,U[:,0:num_PC])
    return XPCANorm
    
def MirrowCut(X,hw):
    #X  size: row * column * num_feature

    [row,col,nb_feature] = X.shape

    X_extension = np.zeros((3*row,3*col,nb_feature))
    
    for i in range(0,nb_feature):
        lr = np.fliplr(X[:,:,i])
        ud = np.flipud(X[:,:,i])
        lrud = np.fliplr(ud)
        
        l1 = np.concatenate((lrud,ud,lrud),axis=1)
        l2 = np.concatenate((lr,X[:,:,i],lr),axis=1)
        l3 = np.concatenate((lrud,ud,lrud),axis=1)
        
        X_extension[:,:,i] = np.concatenate((l1,l2,l3),axis=0)
    
    X_extension = X_extension[row-hw:2*row+hw,col-hw:2*col+hw,:]
    
    return X_extension
    
def DrawResult(labels,imageID):  # ######################增加新数据要改该函数和后面HyperspectralSamples函数
    #ID=1:Pavia University
    #ID=2:Indian Pines
    #ID=6:KSC
    num_class = labels.max()+1
    if imageID == 1:
        row = 610
        col = 340
        palette = np.array([[216,191,216],
                            [0,255,0],
                            [0,255,255],
                            [45,138,86],
                            [255,0,255],
                            [255,165,0],
                            [159,31,239],
                            [255,0,0],
                            [255,255,0]])
        palette = palette*1.0/255
    elif imageID == 2:
        row = 145
        col = 145
        palette = np.array([[255,0,0],
                            [0,255,0],
                            [0,0,255],
                            [255,255,0],
                            [0,255,255],
                            [255,0,255],
                            [176,48,96],
                            [46,139,87],
                            [160,32,240],
                            [255,127,80],
                            [127,255,212],
                            [218,112,214],
                            [160,82,45],
                            [127,255,0],
                            [216,191,216],
                            [238,0,0]])
        palette = palette*1.0/255
    elif imageID == 3:  # Botswana
        row = 1476
        col = 256
        palette = np.array([[255,0,0],
                            [0,255,0],
                            [0,0,255],
                            [255,255,0],
                            [0,255,255],
                            [255,0,255],
                            [176,48,96],
                            [46,139,87],
                            [160,32,240],
                            [255,127,80],
                            [127,255,212],
                            [218,112,214],
                            [160,82,45],
                            [127,255,0]])
        palette = palette*1.0/255
    elif imageID == 4:  # Salinas
        row = 512
        col = 217
        palette = np.array([[37, 58, 150],
                            [47, 78, 161],
                            [56, 87, 166],
                            [56,116, 186],
                            [51, 181, 232],
                            [112, 204, 216],
                            [119, 201, 168],
                            [148, 204, 120],
                            [188, 215, 78],
                            [238, 234, 63],
                            [246, 187, 31],
                            [244, 127, 33],
                            [239, 71, 34],
                            [238, 33, 35],
                            [180, 31, 35],
                            [123,18, 20]])
        palette = palette*1.0/255
    elif imageID == 5:  # Pavia
        row = 1096
        col = 715
        palette = np.array([[37, 97, 163],
                            [44, 153, 60],
                            [122, 182, 41],
                            [219, 36, 22],
                            [227, 156, 47],
                            [227, 221, 223],
                            [108, 35, 127],
                            [130, 67, 142],
                            [229, 225, 74]])
        palette = palette*1.0/255
    elif imageID == 6:
        row = 512
        col = 614
        palette = np.array([[94, 203, 55],
                            [255, 0, 255],
                            [217, 115, 0],
                            [179, 30, 0],
                            [0, 52, 0],
                            [72, 0, 0],
                            [255, 255, 255],
                            [145, 132, 135],
                            [255, 255, 172],
                            [255, 197, 80],
                            [60, 201, 255],
                            [11, 63, 124],
                            [0, 0, 255]])
        palette = palette*1.0/255
    elif imageID == 7:
        row = 349
        col = 1905
        palette = np.array([[0, 205, 0],
                            [127, 255, 0],
                            [46, 139, 87],
                            [0, 139, 0],
                            [160, 82, 45],
                            [0, 255, 255],
                            [255, 255, 255],
                            [216, 191, 216],
                            [255, 0, 0],
                            [139, 0, 0],
                            [0, 0, 0],
                            [255, 255, 0],
                            [238, 154, 0],
                            [85, 26, 139],
                            [255, 127, 80]])
        palette = palette * 1.0 / 255
    
    X_result = np.zeros((labels.shape[0],3))
    for i in range(0,num_class):
        X_result[np.where(labels==i),0] = palette[i,0]
        X_result[np.where(labels==i),1] = palette[i,1]
        X_result[np.where(labels==i),2] = palette[i,2]
    
    X_result = np.reshape(X_result,(row,col,3))
    plt.axis( "off" )
    plt.imshow(X_result)
    return X_result
    
def CalAccuracy(predict,label):
    n = label.shape[0]
    OA = np.sum(predict==label)*1.0/n
    correct_sum = np.zeros((max(label)+1))
    reali = np.zeros((max(label)+1))
    predicti = np.zeros((max(label)+1))
    producerA = np.zeros((max(label)+1))
    
    for i in range(0,max(label)+1):
        correct_sum[i] = np.sum(label[np.where(predict==i)]==i)
        reali[i] = np.sum(label==i)
        predicti[i] = np.sum(predict==i)
        producerA[i] = correct_sum[i] / reali[i]
   
    Kappa = (n*np.sum(correct_sum) - np.sum(reali * predicti)) *1.0/ (n*n - np.sum(reali * predicti))
    return OA,Kappa,producerA
   
def HyperspectralSamples(dataID=1, timestep=4, w=24, num_PC=3, israndom=False, s1s2=2):   
    #dataID=1:Pavia University
    #dataID=2:Indian
    #dataID=6:KSC

    if dataID==1:
        data = sio.loadmat('/data/jiaqi.yang/Dataset/HSI/PaviaU.mat')  # Dataset/PaviaU.mat
        X = data['paviaU']
    
        data = sio.loadmat('/data/jiaqi.yang/Dataset/HSI/PaviaU_gt.mat')  # Dataset/PaviaU_gt.mat
        Y = data['paviaU_gt']
        
        # train_num_array = [548, 540, 392, 542, 256, 532, 375, 514, 231]
        # train_num_array = [100, 100, 100, 100, 100, 100, 100, 100, 100]
        # train_num_array = [150, 150, 150, 150, 150, 150, 150, 150, 150]
        train_num_array = [50, 50, 50, 50, 50, 50, 50, 50, 50]
        # train_num_array = [20, 20, 20, 20, 20, 20, 20, 20, 20]
    elif dataID==2:
        data = sio.loadmat('/data/jiaqi.yang/Dataset/HSI/Indian_pines_corrected.mat')
        X = data['indian_pines_corrected']

        data = sio.loadmat('/data/jiaqi.yang/Dataset/HSI/Indian_pines_gt.mat')
        Y = data['indian_pines_gt']

        # train_num_array = [30, 150, 150, 100, 150, 150, 20, 150, 15, 150, 150, 150, 150, 150, 50, 50]
        # train_num_array = [30, 100, 100, 100, 100, 100, 20, 100, 15, 100, 100, 100, 100, 100, 50, 50]
        train_num_array = [20, 90, 90, 90, 90, 90, 10, 90, 5, 90, 90, 90, 90, 90, 40, 40]
        # train_num_array = [10, 50, 50, 50, 50, 50, 10, 50, 5, 50, 50, 50, 50, 50, 30, 30]
    elif dataID==3:
        data = sio.loadmat('/data/jiaqi.yang/Dataset/HSI/Botswana.mat')
        X = data['Botswana']

        data = sio.loadmat('/data/jiaqi.yang/Dataset/HSI/Botswana_gt.mat')
        Y = data['Botswana_gt']

        train_num_array = [27, 10, 25, 22, 27, 27, 26, 20, 31, 25, 30, 18, 27, 15]
    elif dataID==4:
        data = sio.loadmat('/data/jiaqi.yang/Dataset/HSI/Salinas_corrected.mat')
        X = data['salinas_corrected']

        data = sio.loadmat('/data/jiaqi.yang/Dataset/HSI/Salinas_gt.mat')
        Y = data['salinas_gt']

        # train_num_array = [150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150, 150]
        train_num_array = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
        # train_num_array = [201, 373, 198, 139, 268, 396, 358, 1127, 620, 328, 107, 193, 92, 107, 726, 180]
    elif dataID==5:
        data = sio.loadmat('/data/jiaqi.yang/Dataset/HSI/Pavia.mat')
        X = data['pavia']

        data = sio.loadmat('/data/jiaqi.yang/Dataset/HSI/Pavia_gt.mat')
        Y = data['pavia_gt']

        train_num_array = [100, 100, 100, 100, 100, 100, 100, 100, 100]
        # train_num_array = [6597, 759, 309, 268, 658, 925, 728, 4283, 286]
    elif dataID==6:
        data = sio.loadmat('/data/jiaqi.yang/Dataset/HSI/KSC.mat')
        X = data['KSC']
        X[np.where(X>700)] = 0
        data = sio.loadmat('/data/jiaqi.yang/Dataset/HSI/KSC_gt.mat')
        Y = data['KSC_gt']
        
        # train_num_array = [33, 23, 24, 24, 15, 22, 9, 38, 51, 39, 41, 49, 91]
        train_num_array = [23, 13, 14, 14, 5, 12, 9, 28, 41, 29, 31, 39, 81]
    elif dataID==7:
        data = sio.loadmat('/data/jiaqi.yang/Dataset/HSI/Houston.mat')
        X = data['Houston']

        data = sio.loadmat('/data/jiaqi.yang/Dataset/HSI/Houston_GT.mat')
        Y = data['Houston_GT']

        train_num_array = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
   
    [row,col,nb_feature] = X.shape
    K = row*col
    X = X.reshape(row*col, nb_feature)    
    Y = Y.reshape(row*col, 1)
    
    n_class = Y.max()
    
  
    nb_feature_perTime = int(nb_feature/timestep)
    

    train_num_all = sum(train_num_array)    
    

    X_PCA = featureNormalize(PCANorm(X,num_PC),2)    

    X = featureNormalize(X,1)

    
    hw = int(w/2)
    
    X_PCAMirrow = MirrowCut(X_PCA.reshape(row,col,num_PC),hw)

    XP = np.zeros((K,w,w,num_PC), dtype='float32')


    if (w % 2 == 0):  # 偶数patch size
        for i in range(1,K+1):
            index_row = int(np.ceil(i*1.0/col))
            index_col = i - (index_row-1)*col + hw -1
            index_row += hw -1
            patch = X_PCAMirrow[index_row-hw:index_row+hw,index_col-hw:index_col+hw,:]
            XP[i-1,:,:,:] = patch

            # import gc  # 不写，否则错
            # for x in list(locals().keys()):
            #     del locals()[x]
            # gc.collect()
    else:  # 奇数patch size
        for i in range(1, K + 1):
            index_row = int(np.ceil(i * 1.0 / col))
            index_col = i - (index_row - 1) * col + hw - 1
            index_row += hw - 1
            patch = X_PCAMirrow[index_row - hw:index_row + hw + 1, index_col - hw:index_col + hw + 1, :]
            XP[i - 1, :, :, :] = patch

            # import gc
            # for x in list(locals().keys()):
            #     del locals()[x]
            # gc.collect()


    # for i in range(1,K+1):  # w = 28原始方式
    #     index_row = int(np.ceil(i*1.0/col))
    #     index_col = i - (index_row-1)*col + hw -1
    #     index_row += hw -1
    #     patch = X_PCAMirrow[index_row-hw:index_row+hw,index_col-hw:index_col+hw,:]
    #     XP[i-1,:,:,:] = patch
    
    # XP = np.moveaxis(XP, 3, 1)   # 'th'数据格式


    if israndom==True:
        randomArray = list()
        for i in range(1,n_class+1):
            index = np.where(Y==i)[0]
            n_data = index.shape[0]
            randomArray.append(np.random.permutation(n_data))
  

    flag1=0
    flag2=0
    
    X_train = np.zeros((train_num_all,timestep,nb_feature_perTime))
    XP_train = np.zeros((train_num_all,w,w,num_PC))
    Y_train = np.zeros((train_num_all,1))
    
    X_test = np.zeros((sum(Y>0)[0]-train_num_all,timestep,nb_feature_perTime))  # 总数-train = test
    XP_test = np.zeros((sum(Y>0)[0]-train_num_all,w,w,num_PC))
    Y_test = np.zeros((sum(Y>0)[0]-train_num_all,1))







    # X_train1 = np.zeros((train_num_all, 1, 35))
    # X_train2 = np.zeros((train_num_all, 1, 77-36+1))
    # X_train3 = np.zeros((train_num_all, 1, 102-78+1))
    # X_train4 = np.zeros((train_num_all, 1, 98))
    #
    #
    # X_test1 = np.zeros((sum(Y>0)[0]-train_num_all, 1, 35))
    # X_test2 = np.zeros((sum(Y>0)[0]-train_num_all, 1, 77-36+1))
    # X_test3 = np.zeros((sum(Y>0)[0]-train_num_all, 1, 102-78+1))
    # X_test4 = np.zeros((sum(Y>0)[0]-train_num_all, 1, 98))
    # X_train1 = np.zeros((train_num_all, nb_feature))
    # X_test1 = np.zeros((sum(Y>0)[0]-train_num_all, nb_feature))





    
    for i in range(1,n_class+1):
        index = np.where(Y==i)[0]  # an array of a category[n_data, 1]
        n_data = index.shape[0]  # num of every category
        train_num = train_num_array[i-1]  # num of every training category
        randomX = randomArray[i-1]  # randomArray of every category
        

        XP_train[flag1:flag1+train_num,:,:,:] = XP[index[randomX[0:train_num]],:,:,:]
        Y_train[flag1:flag1+train_num,0] = Y[index[randomX[0:train_num]],0]
            
        XP_test[flag2:flag2+n_data-train_num,:,:,:] = XP[index[randomX[train_num:n_data]],:,:,:]
        Y_test[flag2:flag2+n_data-train_num,0] = Y[index[randomX[train_num:n_data]],0]


        if s1s2==2:
            for j in range(0,timestep):
                X_train[flag1:flag1+train_num,j,:] = X[index[randomX[0:train_num]],j:j+(nb_feature_perTime-1)*timestep+1:timestep]  # list[start:end:step]，取每个像素的这些波段作为光谱维的训练集（每个像素在所有波段都有值）
                X_test[flag2:flag2+n_data-train_num,j,:] = X[index[randomX[train_num:n_data]],j:j+(nb_feature_perTime-1)*timestep+1:timestep]
                
        elif s1s2==1:
            for j in range(0,timestep):
                X_train[flag1:flag1+train_num,j,:] = X[index[randomX[0:train_num]],j*nb_feature_perTime:(j+1)*nb_feature_perTime]
                X_test[flag2:flag2+n_data-train_num,j,:] = X[index[randomX[train_num:n_data]],j*nb_feature_perTime:(j+1)*nb_feature_perTime]
                # 每一个timestep都包含波段内所有类的总test data

        # import gc
        # for x in list(locals().keys()):
        #     del locals()[x]
        # gc.collect()


        # elif s1s2==3:
        #     j = 0
        #     X_train1[flag1:flag1 + train_num, j, :] = X[index[randomX[0:train_num]], 0:35]
        #     X_test1[flag2:flag2 + n_data - train_num, j, :] = X[index[randomX[train_num:n_data]], 0:35]
        #
        #     X_train2[flag1:flag1 + train_num, j, :] = X[index[randomX[0:train_num]], 35:77]
        #     X_test2[flag2:flag2 + n_data - train_num, j, :] = X[index[randomX[train_num:n_data]], 35:77]
        #
        #     X_train3[flag1:flag1 + train_num, j, :] = X[index[randomX[0:train_num]], 77:102]
        #     X_test3[flag2:flag2 + n_data - train_num, j, :] = X[index[randomX[train_num:n_data]], 77:102]
        #
        #     X_train4[flag1:flag1 + train_num, j, :] = X[index[randomX[0:train_num]], 102:201]
        #     X_test4[flag2:flag2 + n_data - train_num, j, :] = X[index[randomX[train_num:n_data]], 102:201]






        flag1 = flag1+train_num
        flag2 = flag2+n_data-train_num
        
        
    X_reshape = np.zeros((X.shape[0],timestep,nb_feature_perTime))  # nb_feature_perTime: band num of every timestep





    # X_reshape1 = np.zeros((X.shape[0],1,35))  # nb_feature_perTime: band num of every timestep
    # X_reshape2 = np.zeros((X.shape[0],1,77-36+1))  # nb_feature_perTime: band num of every timestep
    # X_reshape3 = np.zeros((X.shape[0],1,102-78+1))  # nb_feature_perTime: band num of every timestep
    # X_reshape4 = np.zeros((X.shape[0],1,98))  # nb_feature_perTime: band num of every timestep

    if s1s2==2:
        for j in range(0,timestep):
            X_reshape[:,j,:] = X[:,j:j+(nb_feature_perTime-1)*timestep+1:timestep]
    elif s1s2==1:
        for j in range(0,timestep):
            X_reshape[:,j,:] = X[:,j*nb_feature_perTime:(j+1)*nb_feature_perTime]



    # elif s1s2==3:
    #     X_reshape1[:,0,:] = X[:,0:35]
    #     X_reshape2[:,0,:] = X[:,35:77]
    #     X_reshape3[:,0,:] = X[:,77:102]
    #     X_reshape4[:,0,:] = X[:,102:201]

            

    X = X_reshape  # 每一个timestep由该timestep内包含波段平面的所有像素组成，X有timestep个这样的组成



    # X1 = X_reshape1
    # X2 = X_reshape2
    # X3 = X_reshape3
    # X4 = X_reshape4



    # scio.savemat(X_train.astype('float32'), {'X_train': data['X_train']})

    # import gc
    # for x in list(locals().keys()):
    #     del locals()[x]
    # gc.collect()

    return X.astype('float32'),X_train.astype('float32'),X_test.astype('float32'),XP.astype('float32'),XP_train.astype('float32'),XP_test.astype('float32'),Y.astype(int),Y_train.astype(int),Y_test.astype(int)
    # return X.astype('float32'),X_train.astype('float32'),X_test.astype('float32'),XP.astype('float32'),XP_train.astype('float32'),XP_test.astype('float32'),Y.astype(int),Y_train.astype(int),Y_test.astype(int),X_train1.astype('float32'), X_train2.astype('float32'),\
    #        X_train3.astype('float32'), X_train4.astype('float32'), X_test1.astype('float32'), X_test2.astype('float32'), X_test3.astype('float32'), X_test4.astype('float32'), X1, X2, X3, X4

