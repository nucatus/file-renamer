import os
import time
import sys
import getopt
import time
import datetime

files_with_dates = dict()

def build_dictionary(path):
        for root, dirs, files in os.walk(path):
                for f in files:
                        fName = f.split('.')[0]
                        files_with_dates[fName] = os.path.getmtime(root + f)

def rename_files(path):
        for f in os.listdir(path):
                if f.find('.') == -1:
                        continue
                fName = f.split('.')[0]
                fExt = f.split('.')[1]
                try:
                        fDate = files_with_dates[fName]
                except KeyError:
                        continue
                deserlzdDate = datetime.datetime.utcfromtimestamp(fDate)
                newFileName = deserlzdDate.strftime('%Y%m%d') + '_' + fName + '.' + fExt
                os.rename(path + f, path + newFileName)

def main(argv):
        sourcePath = ''
        targetPath = ''
        try:
                opts, args = getopt.getopt(argv,"hs:t:",["spath=","tpath="])
        except getopt.GetopetError:
                print 'file.py -s <sourcePath> -t <taretPath>'
                sys.exit(2)
        for opt, arg in opts:
                if opt in ("-s", "--source"):
                        sourcePath = arg
                elif opt in ("-t", "--target"):
                        targetPath = arg
        build_dictionary(sourcePath)
        rename_files(targetPath)

if __name__ == "__main__":
        main(sys.argv[1:])
