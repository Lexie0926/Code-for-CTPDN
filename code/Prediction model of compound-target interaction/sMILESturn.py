import pandas as pd

from molvs import standardize_smiles

from MACCS import *

def main():

    filename = 'data/test1.csv'  # path to your csv file

    df = pd.read_csv(filename)              # read the csv file as pandas data frame

    smiles = [standardize_smiles(i) for i in df['smiles'].values]

    ## Compute MACCS Fingerprints and export file.

    maccs_descriptor = MACCS(smiles)        # create your MACCS object and provide smiles

    maccs_descriptor.compute_MACCS(filename)       # 计算 MACCS 并且给文件命名。 命名可以直接使用初始名称，因为MACCS的类会在其后添加 "_MACCS.csv" 作为输出文件。

if __name__ == '__main__':

    main()