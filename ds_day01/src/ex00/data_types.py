def data_types():
    int_val = 4
    float_val = 1.2
    bool_val = True
    list_val = [1,2]
    dict_val = {1:12,2:15}
    str_val = 'abcdef'
    tuple_val = (1,2,3)
    set_val = {1,2,3,4,5,6,7}
    types = [type(int_val).__name__,type(str_val).__name__,type(float_val).__name__,
             type(bool_val).__name__,type(list_val).__name__,type(dict_val).__name__,
             type(tuple_val).__name__, type(set_val).__name__]
    res = ', '.join(types)
    print(f"[{res}]")

if __name__=='__main__':
    data_types()

