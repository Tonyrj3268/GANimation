import numpy as np
import os
from tqdm import tqdm
import argparse
import glob
import re
import pickle
import csv
parser = argparse.ArgumentParser()
parser.add_argument('-ia', '--input_aus_filesdir', type=str, help='Dir with imgs aus files')
parser.add_argument('-op', '--output_path', type=str, help='Output path')
args = parser.parse_args()

def get_data(filepaths):
    data = dict()
    i=0
    for filepath in tqdm(filepaths):
        label = np.loadtxt(filepath, delimiter=',',  dtype=str)
        content = np.loadtxt('imgs.csv', delimiter=',', skiprows=1, dtype=str)
        #data[os.path.basename(filepath[:-4])] = content.tolist()[2:19]
        #data[os.path.basename(filepath[:-4])] = content
        for e in label.tolist():
            data[e[:-4]] = content[i]
            print(e[:-4])
            print(content[i])
            if i<1000:  
                # 開啟輸出的 CSV 檔案
                with open('train_ids.csv', 'w', newline='') as csvfile:
                    # 建立 CSV 檔寫入器
                    writer = csv.writer(csvfile)
                    # 寫入一列資料
                    writer.writerow([e])
            else:
                with open('test_ids.csv', 'w', newline='') as csvfile:
                    # 建立 CSV 檔寫入器
                    writer = csv.writer(csvfile)
                    # 寫入一列資料
                    writer.writerow([e])
            i+=1

    return data

def save_dict(data, name):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

def main():
    filepaths = glob.glob(os.path.join(args.input_aus_filesdir, '*.csv'))
    filepaths.sort()

    # create aus file
    data = get_data(filepaths)

    if not os.path.isdir(args.output_path):
        os.makedirs(args.output_path)
    save_dict(data, os.path.join(args.output_path, "aus_openface"))


if __name__ == '__main__':
    main()
