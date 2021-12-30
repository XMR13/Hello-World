def membuat_baju(size,message):
    print(f'baju ini berukuran {size}')
    print(f'dibelakangnya tertera {message}')

#fungsi positional argumen
membuat_baju('L','I love Nino nakano')

#menggunakan keyword arguments
membuat_baju(message='I love you Megumi',size='S')
