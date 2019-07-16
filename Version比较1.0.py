#把txt文件转换成字典
def generate_dic(file_path):
    with open(file_path,'r',encoding ='utf-8' ) as f:
        dic = {}
        for i in f:
            line = i.strip('\n').split(' ')
            while '' in line:
                line.remove('')
            (key,value) = line
            dic[key] = value
    return(dic)

#比较两个字典中key相同value不同得值，并打印出来
def compare_two_dict(dict1, dict2, key_list):
    keys1 = dict1.keys()
    keys2 = dict2.keys()
    for key in key_list:
        if key in keys1 and key in keys2:
           if dict1[key] != dict2[key]:
                result = dict2[key]
                print('{key}:{result}'.format(key = key, result = result))
        elif key in keys2 and key not in keys1:
            print('{key}:{result}'.format(key=key, result=result))

if __name__== '__main__':
  s= generate_dic('d:/Version.txt')
  t= generate_dic('d:/fabu/Version.txt')
  new_list = []
  for k in t:
      new_list.append(k)
  compare_two_dict(s,t,new_list)









