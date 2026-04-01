from FileReaderWriter import FileReaderWriter

class TextFileReadWriter(FileReaderWriter):
    def read(self,filepath):
        with open(filepath,'r',newline='') as txtfile:
            txt_lines = txtfile.read().split('\n')#list of all the strings
            print(txt_lines)
            txtfile.close()
            return txt_lines 

    def write(self,filepath,data):
        #data needs to be a list of strings
        with open(filepath,'w',newline='') as txtfile:
            txtfile.writelines(data)
            txtfile.close()