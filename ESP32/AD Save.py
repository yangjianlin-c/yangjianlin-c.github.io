import xlwt
import time
import serial
#设置表格样式
def set_style(name,height,bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style

#写Excel
def write_excel():
    if serial.isOpen():
        print ('Serial is Open')
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('arduino_data',cell_overwrite_ok=True)
    row0 = ["temp","pres","hum"]
    time1=time.localtime(time.time())
    #写第一行
    for i in range(len(row0)):
        sheet1.write(0,i,row0[i],set_style('Times New Roman',220,True))
    i=1
    time.sleep(5)
    serial.flushInput()
    while True:
        try:
            size = serial.inWaiting()
            if size != 0:
                response = serial.read(size)        # 读取内容并显示
                s=response.decode('utf-8').rstrip('rn').split('t')
                if len(s)!=3:
                    serial.flushInput()
                    continue
                else:
                    try:
                        for j in range(len(s)):
                            sheet1.write(i,j,int(s[j]),set_style('Times New Roman',220,False))
                        print(s)
                        serial.flushInput()                 # 清空接收缓存区
                        i = i+1
                        time.sleep(0.5)
                    except ValueError:
                        serial.flushInput()
                        continue
        except KeyboardInterrupt:
            time2=time.localtime(time.time())
            f.save(r'C:\\a.xls'.format
                   (time1[1],time1[2],time1[3],time1[4],time1[5],
                    time2[1],time2[2],time2[3],time2[4],time2[5]))
            serial.close()
            print(time1)
            print(time2)
            quit()

if __name__ == '__main__':
    serial = serial.Serial('COM4',115200,timeout=2)
    write_excel()