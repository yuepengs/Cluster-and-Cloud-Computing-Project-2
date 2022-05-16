#Zizhao Li (1267416) zizhaol2@student.unimelb.edu.au (Suzhou, China)
#Fu Zhu (1166186) fuzhu@student.unimelb.edu.au (Melbourne, Australia)
#Chuting Wang (1074511) chutingw@student.unimelb.edu.au (Xi’an, China)
#Xuezhu Wu (938808) xuezhuw@student.unimelb.edu.au (Hangzhou, China)
#Yuepeng Sheng (1048382) yuepengs@student.unimelb.edu.au (Shanghai, China)

FROM python:3.8.10
COPY package_version.txt package_version.txt
COPY real_view.py real_view.py
COPY api.json api.json
RUN pip3 install --upgrade pip
RUN pip3 install -r package_version.txt
COPY . .
CMD [ "python3", "real_view.py"]

