path=/Users/baidu/Downloads/PerformaceTest/output/20180620/f1b5ca49/
files=$(ls $path)
mkdir hprof
for filename in $files
do
   hprof-conv filename hprof/
done
