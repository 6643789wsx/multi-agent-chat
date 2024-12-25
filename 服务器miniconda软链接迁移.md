之前在/home/zxl目录下安装了miniconda，随着配的虚拟环境越来越多，空间占用也多了起来。

根目录空间有限，现在将miniconda移到/data/zxl（这是我以前自己建的目录，也可以移到/data/data_public/zxl）。

1. 复制文件夹

   ```
   cp -r /home/zxl/miniconda3 /data/zxl/miniconda3
   cp -r /home/dtw/.conda /data/data_public/dtw_data/.conda
   ```


2. 备份

   ```
   mv /home/zxl/miniconda3 /data/zxl/miniconda3_bk
   mv /home/dtw/.conda /home/dtw/.conda_bk
   ```

3. 创建软链接

   ```
   ln -s /data/zxl/miniconda3 /home/zxl/miniconda3
   ln -s /data/data_public/dtw_data/.conda /home/dtw/.conda
   ```

4. 确认conda环境正常后，删除备份

   ```
   rm -rf /data/zxl/miniconda3_bk
   rm -rf /home/dtw/.conda_bk
   ```



参考csdn博客：https://blog.csdn.net/lan3_5/article/details/133773222

