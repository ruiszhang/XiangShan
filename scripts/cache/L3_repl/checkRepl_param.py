# 用于检查单个db文件的l3_replDB中的替换算法相关参数是否正确
#!/bin/python3
import sqlite3
import sys
import matplotlib.pyplot as plt
import numpy as np

args = sys.argv
filename = args[1]
dbtype = args[2]

fileName = filename.replace(':', '-').replace('.db', '')

# read xs_repl_db
if(dbtype == 'r'):
    conn1 = sqlite3.connect(filename)
    cursor1 = conn1.cursor()

    cursor1.execute('SELECT ID, STAMP, HIT, HITWAY, SELECTEDWAY, CHANNEL, TRIPCOUNT, USECOUNT, \
                    L_SUM, L_0, L_1, L_2, L_3, L_4, L_5, L_6, L_7, \
                    D_L_0, D_L_1, D_L_2, D_L_3, D_L_4, D_L_5, D_L_6, D_L_7, SITE FROM l3_repl_readDir')
    data1 = cursor1.fetchall()

    conn1.close()
elif(dbtype == 'w'):
    conn1 = sqlite3.connect(filename)
    cursor1 = conn1.cursor()

    cursor1.execute('SELECT ID, STAMP, HIT, ISSAMPLE, OPCODE, CHANNEL, TRIPCOUNT, USECOUNT, \
                    WL_0, WL_1, WL_2, WL_3, WL_4, WL_5, WL_6, WL_7, \
                    WD_L_0, WD_L_1, WD_L_2, WD_L_3, WD_L_4, WD_L_5, WD_L_6, WD_L_7, \
                    RL_0, RL_1, RL_2, RL_3, RL_4, RL_5, RL_6, RL_7, \
                    RD_L_0, RD_L_1, RD_L_2, RD_L_3, RD_L_4, RD_L_5, RD_L_6, RD_L_7, SITE FROM l3_repl_writeDir')
    data1 = cursor1.fetchall()

    conn1.close()
else:
    print('wrong dbtype! "r" for readDB and "w" for writeDB!')

# -----------------------------------------------------------data processing--------------------------------------------------------- #
def str_to_int(x):
    return int(x)

data1_np = np.array(data1)
data1_str = np.array(data1_np)



if(dbtype == 'r'):
    
    bool0 = np.array([x[25] == 'L3_repl_Directory_4.sliceId: Wire[UInt]' for x in data1_str])
    bool1 = np.array([x[25] == 'L3_repl_Directory_5.sliceId: Wire[UInt]' for x in data1_str])
    bool2 = np.array([x[25] == 'L3_repl_Directory_6.sliceId: Wire[UInt]' for x in data1_str])
    bool3 = np.array([x[25] == 'L3_repl_Directory_7.sliceId: Wire[UInt]' for x in data1_str])

    data1_0_str = np.array(data1_str[bool0])
    data1_1_str = np.array(data1_str[bool1])
    data1_2_str = np.array(data1_str[bool2])
    data1_3_str = np.array(data1_str[bool3])
    
    data1_0_ = data1_0_str[:, :-1]
    data1_1_ = data1_1_str[:, :-1]
    data1_2_ = data1_2_str[:, :-1]
    data1_3_ = data1_3_str[:, :-1]

    data1_0_int = np.vectorize(str_to_int)(data1_0_)
    data1_1_int = np.vectorize(str_to_int)(data1_1_)
    data1_2_int = np.vectorize(str_to_int)(data1_2_)
    data1_3_int = np.vectorize(str_to_int)(data1_3_)

    data1_0 = np.array(data1_0_int[0:]) # to exclude warm-up
    data1_1 = np.array(data1_1_int[0:]) 
    data1_2 = np.array(data1_2_int[0:]) 
    data1_3 = np.array(data1_3_int[0:]) 
   
    L_sum_bank0_row = np.array([row[8] for row in data1_0])

    L_0_bank0_row = np.array([row[9] for row in data1_0])
    L_1_bank0_row = np.array([row[10] for row in data1_0])
    L_2_bank0_row = np.array([row[11] for row in data1_0])
    L_3_bank0_row = np.array([row[12] for row in data1_0])
    L_4_bank0_row = np.array([row[13] for row in data1_0])
    L_5_bank0_row = np.array([row[14] for row in data1_0])
    L_6_bank0_row = np.array([row[15] for row in data1_0])
    L_7_bank0_row = np.array([row[16] for row in data1_0])

    L_SUM = np.array(L_1_bank0_row + L_2_bank0_row + L_3_bank0_row)

    L_sumCorrect = np.array_equal(L_SUM, L_sum_bank0_row)

    print('L_sumCorrect = ', L_sumCorrect)

    # bool_L_0 = ((L_row >= 1) & (L_row <= 2)).astype(int)
    # bool_L_100_200 = ((L_row >= 100) & (L_row <200)).astype(int)
    # bool_L_200_300 = (L_row >= 200) & (L_row <300)
    # bool_L_300_400 = (L_row >= 300) & (L_row <400)
    # bool_L_400_ = (L_row >= 400)
    # L_1_2 = np.sum(bool_L_1_2)
    # L_100_200 = np.sum(bool_L_100_200)
    # L_200_300 = np.sum(bool_L_200_300)
    # L_300_400 = np.sum(bool_L_300_400)
    # L_400_ = np.sum(bool_L_400_)

    D_L_0_bank0_row = np.array([row[17] for row in data1_0])
    D_L_1_bank0_row = np.array([row[18] for row in data1_0])
    D_L_2_bank0_row = np.array([row[19] for row in data1_0])
    D_L_3_bank0_row = np.array([row[20] for row in data1_0])
    D_L_4_bank0_row = np.array([row[21] for row in data1_0])
    D_L_5_bank0_row = np.array([row[22] for row in data1_0])
    D_L_6_bank0_row = np.array([row[23] for row in data1_0])
    D_L_7_bank0_row = np.array([row[24] for row in data1_0])

    TC_bank0_row = np.array([row[6] for row in data1_0])
    bool_TC_0 = (TC_bank0_row == 0)
    bool_TC_1 = (TC_bank0_row == 1)
    TC_0 = np.sum(bool_TC_0)
    TC_1 = np.sum(bool_TC_1)

    UC_bank0_row = np.array([row[7] for row in data1_0])
    bool_UC_1 = (UC_bank0_row == 1)
    bool_UC_2 = (UC_bank0_row == 2)
    bool_UC_3 = (UC_bank0_row == 3)
    UC_1 = np.sum(bool_UC_1)
    UC_2 = np.sum(bool_UC_2)
    UC_3 = np.sum(bool_UC_3)


    HIT_bank0_row = np.array([row[2] for row in data1_0])
    hit_bank0_row = (HIT_bank0_row == 1).astype(int)
    hit = np.sum(hit_bank0_row)

    #----------------------------------------------- draw ----------------------------------------------#
    x_values = np.arange(len(L_0_bank0_row))

    fig1, axs1 = plt.subplots(8, 1, figsize=(40, 30))

    axs1[0].plot(x_values, L_0_bank0_row, label='L_0_bank0_row')
    axs1[1].plot(x_values, L_1_bank0_row, label='L_1_bank0_row')
    axs1[2].plot(x_values, L_2_bank0_row, label='L_2_bank0_row')
    axs1[3].plot(x_values, L_3_bank0_row, label='L_3_bank0_row')
    axs1[4].plot(x_values, L_4_bank0_row, label='L_4_bank0_row')
    axs1[5].plot(x_values, L_5_bank0_row, label='L_5_bank0_row')
    axs1[6].plot(x_values, L_6_bank0_row, label='L_6_bank0_row')
    axs1[7].plot(x_values, L_7_bank0_row, label='L_7_bank0_row')
    axs1[0].legend(loc='upper right')
    axs1[1].legend(loc='upper right')
    axs1[2].legend(loc='upper right')
    axs1[3].legend(loc='upper right')
    axs1[4].legend(loc='upper right')
    axs1[5].legend(loc='upper right')
    axs1[6].legend(loc='upper right')
    axs1[7].legend(loc='upper right')


    fig2, axs2 = plt.subplots(8, 1, figsize=(40, 30))

    axs2[0].plot(x_values, D_L_0_bank0_row, label='D_L_0_bank0_row')
    axs2[1].plot(x_values, D_L_1_bank0_row, label='D_L_1_bank0_row')
    axs2[2].plot(x_values, D_L_2_bank0_row, label='D_L_2_bank0_row')
    axs2[3].plot(x_values, D_L_3_bank0_row, label='D_L_3_bank0_row')
    axs2[4].plot(x_values, D_L_4_bank0_row, label='D_L_4_bank0_row')
    axs2[5].plot(x_values, D_L_5_bank0_row, label='D_L_5_bank0_row')
    axs2[6].plot(x_values, D_L_6_bank0_row, label='D_L_6_bank0_row')
    axs2[7].plot(x_values, D_L_7_bank0_row, label='D_L_7_bank0_row')
    axs2[0].legend(loc='upper right')
    axs2[1].legend(loc='upper right')
    axs2[2].legend(loc='upper right')
    axs2[3].legend(loc='upper right')
    axs2[4].legend(loc='upper right')
    axs2[5].legend(loc='upper right')
    axs2[6].legend(loc='upper right')
    axs2[7].legend(loc='upper right')

    plt.tight_layout()

    fig1.savefig(f'{fileName}_Lr.svg')
    fig2.savefig(f'{fileName}_DLr.svg')



elif(dbtype == 'w'):

    bool0 = np.array([x[40] == 'L3_repl_Directory_4.sliceId: Wire[UInt]' for x in data1_str])
    bool1 = np.array([x[40] == 'L3_repl_Directory_5.sliceId: Wire[UInt]' for x in data1_str])
    bool2 = np.array([x[40] == 'L3_repl_Directory_6.sliceId: Wire[UInt]' for x in data1_str])
    bool3 = np.array([x[40] == 'L3_repl_Directory_7.sliceId: Wire[UInt]' for x in data1_str])

    data1_0_str = np.array(data1_str[bool0])
    data1_1_str = np.array(data1_str[bool1])
    data1_2_str = np.array(data1_str[bool2])
    data1_3_str = np.array(data1_str[bool3])
    
    data1_0_ = data1_0_str[:, :-1]
    data1_1_ = data1_1_str[:, :-1]
    data1_2_ = data1_2_str[:, :-1]
    data1_3_ = data1_3_str[:, :-1]

    data1_0_int = np.vectorize(str_to_int)(data1_0_)
    data1_1_int = np.vectorize(str_to_int)(data1_1_)
    data1_2_int = np.vectorize(str_to_int)(data1_2_)
    data1_3_int = np.vectorize(str_to_int)(data1_3_)

    data1_0 = np.array(data1_0_int[0:]) # to exclude warm-up
    data1_1 = np.array(data1_1_int[0:]) 
    data1_2 = np.array(data1_2_int[0:]) 
    data1_3 = np.array(data1_3_int[0:]) 

    WL_0_bank0_row = np.array([row[8] for row in data1_0])
    WL_1_bank0_row = np.array([row[9] for row in data1_0])
    WL_2_bank0_row = np.array([row[10] for row in data1_0])
    WL_3_bank0_row = np.array([row[11] for row in data1_0])
    WL_4_bank0_row = np.array([row[12] for row in data1_0])
    WL_5_bank0_row = np.array([row[13] for row in data1_0])
    WL_6_bank0_row = np.array([row[14] for row in data1_0])
    WL_7_bank0_row = np.array([row[15] for row in data1_0])

    WD_L_0_bank0_row = np.array([row[16] for row in data1_0])
    WD_L_1_bank0_row = np.array([row[17] for row in data1_0])
    WD_L_2_bank0_row = np.array([row[18] for row in data1_0])
    WD_L_3_bank0_row = np.array([row[19] for row in data1_0])
    WD_L_4_bank0_row = np.array([row[20] for row in data1_0])
    WD_L_5_bank0_row = np.array([row[21] for row in data1_0])
    WD_L_6_bank0_row = np.array([row[22] for row in data1_0])
    WD_L_7_bank0_row = np.array([row[23] for row in data1_0])

    RL_0_bank0_row = np.array([row[24] for row in data1_0])
    RL_1_bank0_row = np.array([row[25] for row in data1_0])
    RL_2_bank0_row = np.array([row[26] for row in data1_0])
    RL_3_bank0_row = np.array([row[27] for row in data1_0])
    RL_4_bank0_row = np.array([row[28] for row in data1_0])
    RL_5_bank0_row = np.array([row[29] for row in data1_0])
    RL_6_bank0_row = np.array([row[30] for row in data1_0])
    RL_7_bank0_row = np.array([row[31] for row in data1_0])

    RD_L_0_bank0_row = np.array([row[32] for row in data1_0])
    RD_L_1_bank0_row = np.array([row[33] for row in data1_0])
    RD_L_2_bank0_row = np.array([row[34] for row in data1_0])
    RD_L_3_bank0_row = np.array([row[35] for row in data1_0])
    RD_L_4_bank0_row = np.array([row[36] for row in data1_0])
    RD_L_5_bank0_row = np.array([row[37] for row in data1_0])
    RD_L_6_bank0_row = np.array([row[38] for row in data1_0])
    RD_L_7_bank0_row = np.array([row[39] for row in data1_0])

    TC_bank0_row = np.array([row[6] for row in data1_0])
    UC_bank0_row = np.array([row[7] for row in data1_0])
    HIT_bank0_row = np.array([row[2] for row in data1_0])

    L_check_list = np.column_stack((RL_1_bank0_row, WL_1_bank0_row))
    compare_L = L_check_list[:, 0] > L_check_list[:, 1]     # check: writeL must not be smaller than readL 

    TCUC_bank0_row = np.column_stack((TC_bank0_row, UC_bank0_row))
    binNumber_0_bank0_row = (TCUC_bank0_row[:, 0] == 0) & (TCUC_bank0_row[:, 1] == 0)
    binNumber_1_bank0_row = (TCUC_bank0_row[:, 0] == 0) & (TCUC_bank0_row[:, 1] == 1)
    binNumber_2_bank0_row = (TCUC_bank0_row[:, 0] == 0) & (TCUC_bank0_row[:, 1] == 2)
    binNumber_3_bank0_row = (TCUC_bank0_row[:, 0] == 0) & (TCUC_bank0_row[:, 1] == 3)
    binNumber_4_bank0_row = (TCUC_bank0_row[:, 0] == 1) & (TCUC_bank0_row[:, 1] == 0)
    binNumber_5_bank0_row = (TCUC_bank0_row[:, 0] == 1) & (TCUC_bank0_row[:, 1] == 1)
    binNumber_6_bank0_row = (TCUC_bank0_row[:, 0] == 1) & (TCUC_bank0_row[:, 1] == 2)
    binNumber_7_bank0_row = (TCUC_bank0_row[:, 0] == 1) & (TCUC_bank0_row[:, 1] == 3)

    cum0 = 0
    Sum0 = []
    for num in compare_L:
        cum0 += num
        Sum0.append(cum0)
    print('number of (readL > writeL) is ', Sum0[-1])

    #----------------------------------------------- draw ----------------------------------------------#
    x_values = np.arange(len(WL_0_bank0_row))

    fig1, axs1 = plt.subplots(16, 1, figsize=(40, 30))

    axs1[0].plot(x_values, WL_0_bank0_row,  label='WL_0_bank0_row' )
    axs1[1].plot(x_values, binNumber_0_bank0_row,  label='binNumber_0_bank0_row' )
    axs1[2].plot(x_values, WL_1_bank0_row,  label='WL_1_bank0_row' )
    axs1[3].plot(x_values, binNumber_1_bank0_row,  label='binNumber_1_bank0_row' )
    axs1[4].plot(x_values, WL_2_bank0_row,  label='WL_2_bank0_row' )
    axs1[5].plot(x_values, binNumber_2_bank0_row,  label='binNumber_2_bank0_row' )
    axs1[6].plot(x_values, WL_3_bank0_row,  label='WL_3_bank0_row' )
    axs1[7].plot(x_values, binNumber_3_bank0_row,  label='binNumber_3_bank0_row' )
    axs1[8].plot(x_values, WL_4_bank0_row,  label='WL_4_bank0_row' )
    axs1[9].plot(x_values, binNumber_4_bank0_row,  label='binNumber_4_bank0_row' )
    axs1[10].plot(x_values, WL_5_bank0_row,  label='WL_5_bank0_row' )
    axs1[11].plot(x_values, binNumber_5_bank0_row,  label='binNumber_5_bank0_row' )
    axs1[12].plot(x_values, WL_6_bank0_row,  label='WL_6_bank0_row' )
    axs1[13].plot(x_values, binNumber_6_bank0_row,  label='binNumber_6_bank0_row' )
    axs1[14].plot(x_values, WL_7_bank0_row,  label='WL_7_bank0_row' )
    axs1[15].plot(x_values, binNumber_7_bank0_row,  label='binNumber_7_bank0_row' )
    axs1[0].legend(loc='upper right')
    axs1[1].legend(loc='upper right')
    axs1[2].legend(loc='upper right')
    axs1[3].legend(loc='upper right')
    axs1[4].legend(loc='upper right')
    axs1[5].legend(loc='upper right')
    axs1[6].legend(loc='upper right')
    axs1[7].legend(loc='upper right')
    axs1[8].legend(loc='upper right')
    axs1[9].legend(loc='upper right')
    axs1[10].legend(loc='upper right')
    axs1[11].legend(loc='upper right')
    axs1[12].legend(loc='upper right')
    axs1[13].legend(loc='upper right')
    axs1[14].legend(loc='upper right')
    axs1[15].legend(loc='upper right')

    fig2, axs2 = plt.subplots(16, 1, figsize=(40, 30))

    axs2[0].plot(x_values, WD_L_0_bank0_row,  label='WD_L_0_bank0_row' )
    axs2[2].plot(x_values, WD_L_1_bank0_row,  label='WD_L_1_bank0_row' )
    axs2[4].plot(x_values, WD_L_2_bank0_row,  label='WD_L_2_bank0_row' )
    axs2[6].plot(x_values, WD_L_3_bank0_row,  label='WD_L_3_bank0_row' )
    axs2[8].plot(x_values, WD_L_4_bank0_row,  label='WD_L_4_bank0_row' )
    axs2[10].plot(x_values, WD_L_5_bank0_row,  label='WD_L_5_bank0_row' )
    axs2[12].plot(x_values, WD_L_6_bank0_row,  label='WD_L_6_bank0_row' )
    axs2[14].plot(x_values, WD_L_7_bank0_row,  label='WD_L_7_bank0_row' )
    axs2[1].plot(x_values, binNumber_0_bank0_row,  label='binNumber_0_bank0_row' ) 
    axs2[3].plot(x_values, binNumber_1_bank0_row,  label='binNumber_1_bank0_row' )
    axs2[5].plot(x_values, binNumber_2_bank0_row,  label='binNumber_2_bank0_row' )
    axs2[7].plot(x_values, binNumber_3_bank0_row,  label='binNumber_3_bank0_row' )
    axs2[9].plot(x_values, binNumber_4_bank0_row,  label='binNumber_4_bank0_row' )
    axs2[11].plot(x_values, binNumber_5_bank0_row,  label='binNumber_5_bank0_row' )
    axs2[13].plot(x_values, binNumber_6_bank0_row,  label='binNumber_6_bank0_row' )
    axs2[15].plot(x_values, binNumber_7_bank0_row,  label='binNumber_7_bank0_row' )
    axs2[0].legend(loc='upper right')
    axs2[1].legend(loc='upper right')
    axs2[2].legend(loc='upper right')
    axs2[3].legend(loc='upper right')
    axs2[4].legend(loc='upper right')
    axs2[5].legend(loc='upper right')
    axs2[6].legend(loc='upper right')
    axs2[7].legend(loc='upper right')
    axs2[8].legend(loc='upper right')
    axs2[9].legend(loc='upper right')
    axs2[10].legend(loc='upper right')
    axs2[11].legend(loc='upper right')
    axs2[12].legend(loc='upper right')
    axs2[13].legend(loc='upper right')
    axs2[14].legend(loc='upper right')
    axs2[15].legend(loc='upper right')



    fig3, axs3 = plt.subplots(16, 1, figsize=(40, 30))

    axs3[0].plot(x_values, RL_0_bank0_row,  label='RL_0_bank0_row' )
    axs3[2].plot(x_values, RL_1_bank0_row,  label='RL_1_bank0_row' )
    axs3[4].plot(x_values, RL_2_bank0_row,  label='RL_2_bank0_row' )
    axs3[6].plot(x_values, RL_3_bank0_row,  label='RL_3_bank0_row' )
    axs3[8].plot(x_values, RL_4_bank0_row,  label='RL_4_bank0_row' )
    axs3[10].plot(x_values, RL_5_bank0_row,  label='RL_5_bank0_row' )
    axs3[12].plot(x_values, RL_6_bank0_row,  label='RL_6_bank0_row' )
    axs3[14].plot(x_values, RL_7_bank0_row,  label='RL_7_bank0_row' )
    axs3[1].plot(x_values, binNumber_0_bank0_row,  label='binNumber_0_bank0_row' )    
    axs3[3].plot(x_values, binNumber_1_bank0_row,  label='binNumber_1_bank0_row' )
    axs3[5].plot(x_values, binNumber_2_bank0_row,  label='binNumber_2_bank0_row' )
    axs3[7].plot(x_values, binNumber_3_bank0_row,  label='binNumber_3_bank0_row' )
    axs3[9].plot(x_values, binNumber_4_bank0_row,  label='binNumber_4_bank0_row' )
    axs3[11].plot(x_values, binNumber_5_bank0_row,  label='binNumber_5_bank0_row' )
    axs3[13].plot(x_values, binNumber_6_bank0_row,  label='binNumber_6_bank0_row' )
    axs3[15].plot(x_values, binNumber_7_bank0_row,  label='binNumber_7_bank0_row' )
    axs3[0].legend(loc='upper right')
    axs3[1].legend(loc='upper right')
    axs3[2].legend(loc='upper right')
    axs3[3].legend(loc='upper right')
    axs3[4].legend(loc='upper right')
    axs3[5].legend(loc='upper right')
    axs3[6].legend(loc='upper right')
    axs3[7].legend(loc='upper right')
    axs3[8].legend(loc='upper right')
    axs3[9].legend(loc='upper right')
    axs3[10].legend(loc='upper right')
    axs3[11].legend(loc='upper right')
    axs3[12].legend(loc='upper right')
    axs3[13].legend(loc='upper right')
    axs3[14].legend(loc='upper right')
    axs3[15].legend(loc='upper right')

    fig4, axs4 = plt.subplots(16, 1, figsize=(40, 30))

    axs4[0].plot(x_values, RD_L_0_bank0_row,  label='RD_L_0_bank0_row' )
    axs4[2].plot(x_values, RD_L_1_bank0_row,  label='RD_L_1_bank0_row' )
    axs4[4].plot(x_values, RD_L_2_bank0_row,  label='RD_L_2_bank0_row' )
    axs4[6].plot(x_values, RD_L_3_bank0_row,  label='RD_L_3_bank0_row' )
    axs4[8].plot(x_values, RD_L_4_bank0_row,  label='RD_L_4_bank0_row' )
    axs4[10].plot(x_values, RD_L_5_bank0_row,  label='RD_L_5_bank0_row' )
    axs4[12].plot(x_values, RD_L_6_bank0_row,  label='RD_L_6_bank0_row' )
    axs4[14].plot(x_values, RD_L_7_bank0_row,  label='RD_L_7_bank0_row' )
    axs4[1].plot(x_values, binNumber_0_bank0_row,  label='binNumber_0_bank0_row' )    
    axs4[3].plot(x_values, binNumber_1_bank0_row,  label='binNumber_1_bank0_row' )
    axs4[5].plot(x_values, binNumber_2_bank0_row,  label='binNumber_2_bank0_row' )
    axs4[7].plot(x_values, binNumber_3_bank0_row,  label='binNumber_3_bank0_row' )
    axs4[9].plot(x_values, binNumber_4_bank0_row,  label='binNumber_4_bank0_row' )
    axs4[11].plot(x_values, binNumber_5_bank0_row,  label='binNumber_5_bank0_row' )
    axs4[13].plot(x_values, binNumber_6_bank0_row,  label='binNumber_6_bank0_row' )
    axs4[15].plot(x_values, binNumber_7_bank0_row,  label='binNumber_7_bank0_row' )
    axs4[0].legend(loc='upper right')
    axs4[1].legend(loc='upper right')
    axs4[2].legend(loc='upper right')
    axs4[3].legend(loc='upper right')
    axs4[4].legend(loc='upper right')
    axs4[5].legend(loc='upper right')
    axs4[6].legend(loc='upper right')
    axs4[7].legend(loc='upper right')
    axs4[8].legend(loc='upper right')
    axs4[9].legend(loc='upper right')
    axs4[10].legend(loc='upper right')
    axs4[11].legend(loc='upper right')
    axs4[12].legend(loc='upper right')
    axs4[13].legend(loc='upper right')
    axs4[14].legend(loc='upper right')
    axs4[15].legend(loc='upper right')



    plt.tight_layout()

    fig1.savefig(f'{fileName}_bank0_wL_w.svg')
    fig2.savefig(f'{fileName}_bank0_wDL_w.svg')
    fig3.savefig(f'{fileName}_bank0_wL_r.svg')
    fig4.savefig(f'{fileName}_bank0_wDL_r.svg')
    
else:
    print('wrong')