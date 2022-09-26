import os
import csv
path = 'sample_dataset/imgs' #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
files.sort()
'''
for file in files:
    print(file)
    print(len(file))
    if len(file)==7:
        file_oldname = os.path.join("sample_dataset\imgs", file)
        file_newname_newfile = os.path.join("sample_dataset\imgs", "0{}".format(file))
        os.rename(file_oldname, file_newname_newfile)
    elif len(file)==6:
        file_oldname = os.path.join("sample_dataset\imgs", file)
        file_newname_newfile = os.path.join("sample_dataset\imgs", "00{}".format(file))
        os.rename(file_oldname, file_newname_newfile)
    elif len(file)==5:
        file_oldname = os.path.join("sample_dataset\imgs", file)
        file_newname_newfile = os.path.join("sample_dataset\imgs", "000{}".format(file))
        os.rename(file_oldname, file_newname_newfile)
'''
i=0
with open('sample_dataset/train_ids.csv', 'w', newline='') as csvfile_train:
            # 建立 CSV 檔寫入器
        writer_train = csv.writer(csvfile_train)
        
        with open('sample_dataset/test_ids.csv', 'w', newline='') as csvfile_test:
            # 建立 CSV 檔寫入器
            writer_test = csv.writer(csvfile_test)
            for file in files:
                print(file)
            # 開啟輸出的 CSV 檔案
                if i<1000:  
                    # 寫入一列資料
                    writer_test.writerow([file])
                    i+=1
                else:
                        # 寫入一列資料
                    writer_train.writerow([file])
                    i+=1   

