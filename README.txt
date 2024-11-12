从PDB数据库到酶反应方程式：
1.在PDB数据库搜索得到若干结果后在“Tabular Report（表格报告）”栏选择“Custom Report（自定义报告）”，勾选“Entity ID”、“EC Number
”、“EC Provenance Source”后点击右上“Run Report”运行筛选器。
2.得到若干结果，都包含 EC number。点击右上角“CSV”，若结果>2500个，则分批输出，后再整合为一个文件即可。
3.根据EC number升序排序，删除冗余的number，WPS内查找“^p”，替换为“^phttps://www.brenda-enzymes.org/enzyme.php?ecno=”，得到若干网址，将网址复制粘贴到urls.txt文件，cmd中运行python3 getweborigincode.py，脚本开始在Google chrome（指定）中自动搜索酶催化反应编号，输入到numbers.txt。
4.运行python3 remove_consecutive_duplicates.py，去除冗余的反应编号。将非冗余的反应编号copy到WPS中，在前后添加“https://www.brenda-enzymes.org/structure.php?show=reaction&id=”、“&type=I&displayType=marvin”，转变为若干网址，将其覆盖到urls.txt。（运行python3 openweb.py可以批量打开这些上千百条网站以观看酶催化反应式。*可能有风险导致内存不足，系统卡死，谨慎运行)
5.运行python3 screenshot.py将上述若干网站截图保存为若干酶催化反应式.png