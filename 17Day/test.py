
file_list = []

execel_file1 = []
sheet1 = [1,1,1,1,1]
sheet2 = [1,1,1,1,1]
sheet3 = [1,1,1,1,1]
execel_file1.append(sheet1, sheet2, sheet3)

execel_file2 = []
sheet1 = [2,2,2,2,2]
sheet2 = [2,2,2,2,2]
sheet3 = [2,2,2,2,2]
execel_file2.append(sheet1, sheet2, sheet3)

execel_file3 = []
sheet1 = [3,3,3,3,3]
sheet2 = [3,3,3,3,3]
sheet3 = [3,3,3,3,3]
execel_file3.append(sheet1, sheet2, sheet3)

file_list.append(execel_file1, execel_file2, execel_file3)


for execel in file_list:
    list_sum = []
    list_count = []
    for sheet in execel:
        sheet_sum = 0
        sheet_avg = 0.0
        count = 0
        for data in sheet:
            sheet_sum += data
            count += 1
        sheet_avg = sheet_sum / count
        list_sum.append(sheet_sum)
        list_count.append(count)
    file_sum = sum(list_sum)                    # 파일 합계
    file_avg = file_sum / sum(list_count)       # 파일 평균


